Los tests han cruzado todo el curso como herramienta de cada batalla: caracterización para tocar legacy (sección 2), repositorios en memoria (sección 6), tests de casos de uso como especificación (sección 7), y en la historia, la víspera del despliegue, un test nacido de un pósit salvando la primera remesa. Este capítulo los ordena como sistema: qué se testea en cada capa, con qué dobles, y con qué utillaje — incluidos dos patrones con nombre propio, **Object Mother** y **fixtures**, que forman parte de la arquitectura destino y que mucha gente usa mal o no conoce.

## La estrategia por capas: cada pieza, en su banco de pruebas

La arquitectura limpia no es solo fácil de testear: **dicta** cómo testear. Cada capa tiene su tipo de test natural, y la pirámide sale sola:

**Dominio: tests unitarios puros, a cientos.** Las entidades y value objects no tienen dependencias — esa era la gracia —, así que sus tests son funciones puras comprobando reglas: rapidísimos, sin dobles, sin nada que preparar.

```javascript
test("[Importe] no puede ser negativo", () => {
  expect(() => Importe.create(-100)).toThrow("[Importe]");
});

test("una factura emitida no admite líneas nuevas", () => {
  const factura = FacturaMother.emitida();
  expect(() => factura.anadirLinea(LineaMother.cualquiera())).toThrow("[Factura]");
});
```

**Aplicación: tests de caso de uso con repositorios en memoria, a decenas.** El corazón de la estrategia, y donde este curso pone el énfasis que otros ponen en los unitarios de clase: cada test ejercita una operación completa del negocio — con sus pasos, sus entidades reales y sus contratos servidos por dobles — y se lee como una frase de la especificación. Ya los viste en la sección 7; son el estándar del directorio `test/application/` de la arquitectura destino.

**Infraestructura: tests de contrato contra lo real, a puñados.** Los adaptadores (el `PostgreSQLRepositorioDeFacturas`) sí necesitan probarse contra la tecnología de verdad — una base de datos efímera en local o CI — porque su trabajo es exactamente lo que los dobles fingen. El patrón fino aquí se llama **test de contrato**: la *misma* batería de tests, escrita una vez contra la interfaz (`guarda y recupera una factura idéntica`, `devuelve null si no existe`, `filtra las vencidas correctamente`), se ejecuta contra *todas* las implementaciones — la de PostgreSQL, la de MySQL y la in-memory. Así garantizas la sustituibilidad de Liskov (sección 3) mecánicamente: todas las cajas responden igual a las mismas preguntas, incluida la de mentira que usan los demás tests. Un doble que no pasa el contrato de su original es un test de aplicación mintiendo.

**Extremo a extremo: pocos y valiosos.** Un puñado de recorridos completos (HTTP → caso de uso → base de datos real) que prueban que el cableado — factorías, rutas, configuración — está bien enchufado. Pocos, porque son lentos y frágiles; valiosos, porque son los únicos que pillan el error de fontanería que ninguna capa ve por separado.

La forma resultante — muchos abajo, pocos arriba — es la **pirámide de tests** (el término lo popularizó Mike Cohn; Fowler la matiza en su bliki y en el ensayo *The Practical Test Pyramid* de Ham Vocke, gratuito en martinfowler.com). Pero nota la diferencia con la pirámide ingenua: la base no son «tests de cada clase», sino tests de *reglas* (dominio) y de *operaciones* (aplicación). Testear clase a clase con mocks de las clases vecinas — el estilo que Fowler llama *solitary* llevado al extremo — produce suites enormes que se rompen con cada refactor sin haber pillado un solo bug: acoplan el test a la estructura, no al comportamiento. Los tests del curso son *sociable* por defecto: el caso de uso se prueba con sus entidades de verdad, y solo se finge la frontera (los contratos de infraestructura). Refactoriza por dentro cuanto quieras: mientras el comportamiento se mantenga, el verde se mantiene — exactamente lo que un refactor necesita de su red.

## El vocabulario de los dobles, de una vez por todas

«Mock» se usa coloquialmente para todo, y la imprecisión sale cara. La taxonomía canónica es de Gerard Meszaros (*xUnit Test Patterns*, 2007; Fowler la resume en *TestDouble* y *Mocks Aren't Stubs*, gratuitos):

- **Dummy**: se pasa para rellenar una firma; nadie lo usa.
- **Stub**: responde con valores fijos («cuando te pregunten el tipo de cambio, di 1,08»).
- **Fake**: una implementación *funcional* pero simplificada — el `InMemoryRepositorioDeFacturas` es un fake, y es el doble estrella de este curso.
- **Spy**: registra lo que le hicieron, para preguntárselo después («¿te llamaron una vez, con qué?»).
- **Mock** (en sentido estricto): programado con expectativas *por adelantado* que él mismo verifica.

La preferencia práctica del curso, heredada de la sección 7: **fakes para los contratos, spies para los efectos, mocks estrictos casi nunca.** El fake mantiene los tests legibles y sociables; el spy responde la única pregunta que el fake no responde («¿se notificó?»); el mock estricto acopla el test a la secuencia exacta de llamadas — a la *estructura* — y convierte cada refactor en veinte tests rotos sin bug alguno. Y el recordatorio de la ampliación de la sección 7: en código bien inyectado, un doble es una clase normal de veinte líneas; la sed de frameworks de mocking sofisticados suele delatar inyección pobre.

## Object Mother: ejemplares de fábrica

Primer patrón de utillaje, presente en la arquitectura destino (`test/helpers/EntityMother.ts`): la **Object Mother**. Nombre acuñado en un proyecto de ThoughtWorks (Fowler lo documenta en su bliki, entrada *ObjectMother*, gratuita): una clase compañera que fabrica ejemplares de prueba con nombre expresivo:

```javascript
// test/helpers/FacturaMother.js
export class FacturaMother {
  static cualquiera() { return FacturaMother.borradorCon({}); }

  static emitida() {
    return FacturaMother.borradorCon({}).emitir();
  }

  static conAbonoParcial({ total = 400_00, consumido = 250_00 } = {}) {
    // el caso de la lámina de Marta, listo para cualquier test
    ...
  }

  static borradorCon({ cliente = ClienteMother.deVesta(), lineas = [LineaMother.cualquiera()] }) {
    return Factura.create(FacturaIdMother.siguiente(), cliente, lineas);
  }
}
```

Lo que compra, en orden de importancia real:

1. **Los tests dicen solo lo que importa.** `FacturaMother.emitida()` en un test sobre inmutabilidad de emitidas: una línea, cero ruido. Sin mother, cada test arrastra ocho líneas de construcción irrelevante que entierran la única premisa relevante.
2. **El conocimiento de «cómo se construye un ejemplar válido» vive una vez.** Cuando `Factura.create` gane un parámetro, se toca la mother, no doscientos tests. Es la regla de «una sola vez» de Beck aplicada al utillaje.
3. **Los casos con nombre son cultura de equipo.** `conAbonoParcial()` — el pósit de Marta con nombre de método — queda disponible, documentado y reutilizable para siempre. El catálogo de mothers acaba siendo el bestiario del dominio: leerlo enseña el negocio.

La variante que combina con la mother en equipos modernos: el **builder de datos de test** (`FacturaMother.borradorCon({ lineas: [...] })` ya lo insinúa) para retocar un aspecto sin definir los demás. Mother para los ejemplares canónicos con nombre; overrides para la variación puntual del test. Y una regla de higiene: las mothers construyen **por la puerta oficial** (`create`, los métodos de dominio), jamás esquivando validaciones — un ejemplar de test imposible en producción es una mentira con cobertura.

## Fixtures: los valores compartidos, con domicilio

Segundo utillaje del estándar destino (`test/fixtures/values.ts`): los **fixtures**, valores de prueba constantes y compartidos — ids conocidos, fechas fijas, primitivas de ejemplo:

```typescript
// test/fixtures/values.ts
export const FECHA_FIJA = "2026-03-10T09:00:00Z";
export const VESTA_CLIENTE_ID = "c-000042";
export const NIF_VALIDO = "B12345678";
export const NIF_LETRA_INCORRECTA = "B1234567X";
```

Parecen una tontería hasta que faltan: sin fixtures, cada fichero de tests inventa sus strings mágicos, y el día que el formato de id cambia hay noventa sitios que tocar y tres que se olvidan. Con ellos, además, los tests de frontera (los de `fromPrimitive`, la aduana de la sección 5) declaran su intención por el nombre: `NIF_LETRA_INCORRECTA` se explica solo.

Mención aparte para el fixture más traicionero: **el tiempo**. Un test que usa «ahora» de verdad es un test que falla los años bisiestos, a medianoche o en otra zona horaria. El reloj es una dependencia como la base de datos: entra por la puerta (un `relojFijo(FECHA_FIJA)` como parámetro del caso de uso que lo necesite) — la lección del determinismo de la sección 2, ascendida a norma.

## La red es la manía

El cierre técnico del curso es la frase de Gabriel, porque es la parte del sistema de tests que no es software: la suite solo vale si **se ejecuta siempre y se mantiene verde siempre**. Las reglas de la manía, todas con cicatriz detrás:

- **Rápida o muerta.** El minuto cuarenta de Meridian es un límite de diseño, no una suerte: una suite que tarda veinte minutos se lanza «luego», y «luego» es nunca. Si crece lenta, la grasa está casi siempre en tests que tocan infraestructura sin necesitarla — baja la pirámide.
- **Verde significa verde.** Un solo test «que falla a veces, ignóralo» enseña al equipo a ignorar el rojo, y el día del pósit de Marta nadie mira la pantalla. Los tests intermitentes (*flaky*) se arreglan o se borran ese mismo día: son deuda con el interés más alto que existe, porque devalúan la moneda entera.
- **El rojo de la víspera es el sistema funcionando.** Cultura, no tecnología: un test que falla antes de desplegar es la red *ganando* — merece el veinte-minutos-y-gracias que le dieron Júlia y Denís, no la tentación de «pasarlo luego». Los equipos que celebran el rojo pre-despliegue tienen pocos rojos post-despliegue.

Y la coda del faro, que es de las pocas frases de este curso sin autor famoso detrás y quizá la más importante: los tests son **la diferencia entre creer y saber**. Todo lo demás — pirámides, dobles, mothers — es la técnica; eso es el porqué.

## Para llevar

- Estrategia por capas: dominio = unitarios puros a cientos; aplicación = casos de uso con fakes a decenas (el corazón); infraestructura = tests de contrato contra tecnología real, la misma batería para todas las implementaciones (la in-memory incluida); e2e = pocos, para el cableado.
- Tests sociables sobre solitarios: se finge la frontera, no las clases vecinas; la red debe sobrevivir a los refactores, que es cuando se necesita.
- Dobles con precisión (Meszaros): dummy, stub, fake, spy, mock. Dieta del curso: fakes para contratos, spies para efectos, mocks estrictos casi nunca.
- Object Mother: ejemplares canónicos con nombre (`emitida()`, `conAbonoParcial()`), construcción centralizada, siempre por la puerta oficial. El catálogo de mothers es el bestiario del dominio.
- Fixtures: valores compartidos con domicilio único; el reloj es una dependencia y se inyecta fijo.
- La red es la manía: rápida o muerta, verde significa verde, y el rojo de la víspera es la red ganando.

## Para profundizar

- Ham Vocke, *The Practical Test Pyramid* (martinfowler.com, gratuito) — el mejor recorrido moderno de la pirámide con ejemplos.
- Martin Fowler, *TestDouble*, *Mocks Aren't Stubs*, *ObjectMother*, *UnitTest* (bliki, gratuitos).
- Gerard Meszaros, *xUnit Test Patterns* (2007) — la enciclopedia de referencia; de consulta, no de lectura seguida.
- Kent Beck, *Test-Driven Development: By Example* (2002) — el librito que enseña el ciclo rojo-verde-refactor con el que muchos de estos hábitos nacen; de pago, breve y aún fresco.
