Entre el dominio (las reglas) y las puertas de entrada (el mundo) faltaba una capa, y la historia acaba de mostrar el precio de su ausencia: la operación «emitir una factura» escrita tres veces, divergiendo en silencio. Este capítulo presenta la pieza que ocupa ese hueco — el **caso de uso** — y su compañera de fontanería, la **factoría**. Con ellas queda completa la tríada `domain / application / infrastructure` de la arquitectura destino.

## Qué es un caso de uso

Un **caso de uso** (en la literatura también *interactor* — término de Martin en *The Clean Architecture* — o *application service* — término de la comunidad DDD) es **una operación del negocio, escrita una sola vez, en un fichero que se llama como la operación**. «Emitir una factura», «anular una remesa», «registrar un cliente». Es la capa de la *coreografía*: no contiene reglas de negocio — esas viven en el dominio — sino los **pasos** de la historia: buscar esto, comprobar aquello con la entidad, guardar, devolver.

La distinción reglas/pasos es la línea divisoria entre dominio y aplicación, y merece un ejemplo nítido:

- «Una factura emitida no se modifica» → **regla** → vive en la entidad `Factura` (sección 5).
- «Para emitir una factura: recupera el pedido, comprueba que no esté ya facturado, construye la factura descontando los abonos pendientes, guárdala y devuélvela» → **pasos** → viven en el caso de uso `emitirFactura`.

En la arquitectura destino del curso, el caso de uso tiene una forma concreta y deliberadamente humilde: **una función por fichero, que recibe todo lo que necesita — datos y dependencias — en un único objeto de entrada**:

```javascript
// application/emitirFactura.js
export async function emitirFactura({
  pedidoId,                 // datos de la petición
  repositorioDePedidos,     // dependencias: contratos del dominio,
  repositorioDeFacturas,    // servidos por quien invoca
  repositorioDeAbonos,
}) {
  const pedido = await repositorioDePedidos.buscarPorId(pedidoId);
  if (pedido === null) {
    throw new Error("[emitirFactura] el pedido no existe");
  }
  if (pedido.estaFacturado()) {
    throw new Error("[emitirFactura] el pedido ya fue facturado");
  }

  const abonos = await repositorioDeAbonos.buscarPendientesDe(pedido.getClienteId());
  const factura = Factura.crearDesdePedido(pedido).descontar(abonos);

  await repositorioDeFacturas.guardar(factura);
  return factura;
}
```

En Python, la misma criatura:

```python
# application/emitir_factura.py
async def emitir_factura(
    *, pedido_id: PedidoId,
    repositorio_de_pedidos: RepositorioDePedidos,
    repositorio_de_facturas: RepositorioDeFacturas,
    repositorio_de_abonos: RepositorioDeAbonos,
) -> Factura:
    pedido = await repositorio_de_pedidos.buscar_por_id(pedido_id)
    if pedido is None:
        raise ValueError("[emitir_factura] el pedido no existe")
    ...
```

Los rasgos finos, uno a uno:

- **Un fichero, una operación.** El directorio `application/` se convierte en el índice del sistema: listarlo responde «¿qué se puede hacer aquí?». Es la screaming architecture (sección 4) a escala de capa.
- **Las dependencias entran por la puerta** — el *props object*. Es el seam de Feathers y el DIP, en su forma final: el caso de uso declara qué contratos necesita y no sabe quién los cumple. Consecuencia directa: el test le pasa repositorios en memoria y prueba la operación completa en milisegundos.
- **Los errores se prefijan con el nombre del caso de uso** (`[emitirFactura] ...`), igual que los del dominio con el del tipo. Un log a las tres de la mañana dirá qué operación y qué paso — sin stack trace arqueológico.
- **El caso de uso no valida formatos ni autentica.** Eso es trabajo de la puerta (¿viene el campo?, ¿quién eres?). Tampoco decide reglas — pregunta a las entidades. Su única sabiduría es el orden de los pasos.

La prueba del algodón para saber si la capa está bien cortada: **el caso de uso debe poder invocarse, idéntico, desde la pantalla, el proceso nocturno, la API y un test** — las cuatro puertas de Cockburn. Si alguna puerta «necesita una versión especial de la operación», o la puerta está haciendo trabajo de operación o la operación está haciendo trabajo de puerta.

## Entrypoints finos: las puertas tontas

La otra mitad del contrato, con la formulación del cuaderno de faro: *una puerta debe ser tonta — autentica, traduce lo que llega, llama a la operación, traduce lo que sale*. En la arquitectura destino se enuncia así: los handlers de ruta, páginas y jobs ejecutan guardas básicas (autenticación, forma de la petición) y delegan en **UN** caso de uso. Embutir coreografía de negocio en una puerta es una violación de arquitectura — es esconder pasos de la operación donde las otras puertas no los verán.

```javascript
// infrastructure/http/postEmitirFactura.js — la puerta: 9 líneas, cero decisiones
export async function postEmitirFactura(req, res) {
  if (!req.session.usuario) return res.status(401).end();
  try {
    const factura = await facturacion.emitirFactura(req.body.pedidoId);
    res.status(201).json(factura.toPrimitive());
  } catch (error) {
    res.status(422).json({ error: error.message });
  }
}
```

La señal de alarma en una revisión de código: un `if` de negocio en un controlador. Uno solo. Hoy es «si el cliente es de Vesta, añade el campo X»; en dos años es la pantalla interna de Loli divergiendo de la remesa nocturna. Las puertas se multiplican — HTTP hoy, CLI mañana, un webhook pasado — y cada decisión alojada en una puerta es una decisión que las demás no conocen.

## La factoría: fontanería, y solo fontanería

Queda un cabo suelto: si el caso de uso recibe sus repositorios, *alguien* tiene que construirlos y pasárselos. Ese alguien es la **factoría** — en la arquitectura destino, un fichero `application/factory.ts` por módulo — y su descripción cabe en una palabra del documento real: es **wiring only**, solo cableado:

```javascript
// application/factory.js — construye una vez, expone las operaciones
import { PostgreSQLRepositorioDePedidos } from "../infrastructure/PostgreSQLRepositorioDePedidos.js";
import { PostgreSQLRepositorioDeFacturas } from "../infrastructure/PostgreSQLRepositorioDeFacturas.js";
import { PostgreSQLRepositorioDeAbonos } from "../infrastructure/PostgreSQLRepositorioDeAbonos.js";
import { emitirFactura } from "./emitirFactura.js";
import { calcularRemesa } from "./calcularRemesa.js";

const repositorioDePedidos = new PostgreSQLRepositorioDePedidos();
const repositorioDeFacturas = new PostgreSQLRepositorioDeFacturas();
const repositorioDeAbonos = new PostgreSQLRepositorioDeAbonos();

export const facturacion = {
  emitirFactura: (pedidoId) =>
    emitirFactura({ pedidoId, repositorioDePedidos, repositorioDeFacturas, repositorioDeAbonos }),
  calcularRemesa: (fecha) =>
    calcularRemesa({ fecha, repositorioDePedidos, repositorioDeFacturas }),
};
```

Las puertas importan `facturacion` y llaman. Punto. Y las dos prohibiciones del documento de arquitectura destino, que parecen pedantes hasta el día que salvan un diseño:

1. **La factoría no declara interfaces ni tipos.** Los contratos pertenecen al dominio o al caso de uso; una factoría que define contratos se está creyendo una capa.
2. **La factoría no coordina dos casos de uso.** Un método de factoría que llama a `emitirFactura` *y luego* a `enviarNotificacion` está contando una historia — y las historias son casos de uso. La regla del documento real lo dice con precisión quirúrgica: *una cadena de casos de uso en la factoría es un caso de uso que falta*. La solución: crear el caso de uso que posee el flujo (`emitirYNotificarFactura`) e inyectarle el otro caso de uso como una dependencia más — un puerto, igual que un repositorio.

¿Por qué tanta severidad con una pieza tan tonta? Porque la factoría es el único lugar del módulo que conoce *a la vez* la aplicación y la infraestructura concreta, y todo lugar así tiende, por gravedad, a acumular decisiones. Si la fontanería piensa, el edificio tiene dos cerebros.

Nota para quien venga de frameworks con inyección de dependencias automática (Spring, NestJS, los contenedores de Python): la factoría manual es la versión sin magia de lo mismo. Este curso la prefiere por una razón pedagógica y otra práctica: se *lee* (el grafo de dependencias del módulo entero cabe en un fichero, no en anotaciones dispersas), y no impone framework al dominio. Con contenedor o sin él, las reglas no cambian: cableado sí, decisiones no.

## El regalo: los tests como especificación

El descubrimiento de Júlia merece rango de principio, porque es de las mejores razones para toda esta estructura. Cuando las operaciones son funciones con dependencias inyectables, sus tests dejan de ser «tests unitarios» en el sentido burocrático y se convierten en **la especificación ejecutable del sistema**:

```javascript
test("emitirFactura descuenta los abonos pendientes del cliente", async () => {
  const repositorioDePedidos = new InMemoryRepositorioDePedidos([pedidoDe(vesta, 100_00)]);
  const repositorioDeAbonos = new InMemoryRepositorioDeAbonos([abonoDe(vesta, 15_00)]);
  const repositorioDeFacturas = new InMemoryRepositorioDeFacturas();

  const factura = await emitirFactura({
    pedidoId: pedido.getId(), repositorioDePedidos, repositorioDeFacturas, repositorioDeAbonos,
  });

  expect(factura.total().toPrimitive()).toBe(85_00);
});
```

Doce líneas que se leen como una frase de negocio, corren en milisegundos, y no saben qué es HTTP. El directorio de tests de `application/` es la lista completa, siempre al día y con garantía de verdad, de lo que el sistema hace — el documento que ATLAS no tuvo en quince años y Fénix no tuvo jamás. La sección 9 sistematiza esta idea; la sección 8, antes, responderá la pregunta que la historia dejó goteando en la cocina: ¿en qué *idioma* deben estar escritas esas frases de negocio — y qué pasa cuando la misma palabra significa tres cosas?

## Para llevar

- Caso de uso: una operación de negocio, escrita una vez, en un fichero con su nombre. Contiene pasos (coreografía), no reglas (dominio). También llamado interactor o application service.
- Forma destino: función por fichero + props object con datos y dependencias (contratos del dominio). Errores prefijados `[nombreDelCasoDeUso]`.
- La prueba del corte correcto: la misma operación, idéntica, invocable desde pantalla, job, API y test. Puertas tontas: autenticar, traducir, delegar en UN caso de uso; un `if` de negocio en un controlador es una decisión escondida del resto del sistema.
- Factoría = wiring only: construye dependencias y expone operaciones. No declara contratos; no encadena casos de uso — «una cadena de casos de uso en la factoría es un caso de uso que falta» (se crea el que posee el flujo y se le inyecta el otro como puerto).
- Los tests de casos de uso con repositorios en memoria son la especificación ejecutable del sistema: la lista de lo que hace, con garantía de verdad.

## Para profundizar

- Robert C. Martin, *The Clean Architecture* (2012, gratuito) — los «use cases» como anillo propio, distinto de las entidades.
- Eric Evans, *DDD Reference* — entrada *Application Services* dentro de la discusión de capas (CC BY 4.0).
- CodelyTV, *typescript-ddd-example* — casos de uso y su cableado en un proyecto real abierto (AGPL-3.0).
