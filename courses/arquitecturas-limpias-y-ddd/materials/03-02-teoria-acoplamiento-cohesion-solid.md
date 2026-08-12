Veintitrés ficheros para añadir una línea a una factura. La historia acaba de mostrar la enfermedad estructural más común del software, y este capítulo le pone nombres, causas y remedios. Los nombres tienen medio siglo — **acoplamiento** y **cohesión** — y los remedios más citados llevan cuarenta años decantándose hasta cristalizar en un acrónimo que hoy aparece en cualquier entrevista de trabajo: **SOLID**. El objetivo del capítulo no es que memorices cinco principios para recitarlos, sino que entiendas la única idea que los cinco desarrollan: **controlar quién sabe qué sobre quién**.

## Las dos medidas: acoplamiento y cohesión

Los términos los formalizaron Larry Constantine y Edward Yourdon en *Structured Design* (1979), sobre trabajos de Constantine de los años 60 — es literalmente anterior a casi todo lo que usas:

- **Acoplamiento** (*coupling*): cuánto sabe una pieza sobre el interior de otras; cuántas piezas hay que tocar cuando una cambia. Se mide con la pregunta de Júlia: *¿cuántos sitios toco para cambiar una cosa?*
- **Cohesión** (*cohesion*): cuánto tienen que ver entre sí las cosas que viven dentro de una misma pieza. Se mide con la pregunta inversa: *¿cuántos motivos distintos hay para tocar este sitio?*

El criterio clásico — vigente medio siglo después — es **acoplamiento bajo, cohesión alta**: piezas que saben poco unas de otras y cuyo interior está unido por un propósito común. ATLAS es el contraejemplo perfecto en ambos ejes: el PDF que *recalcula* impuestos está acoplado a la lógica de cálculo (sabe *cómo* se calcula, no solo *qué* resultado usar), y `calc2()` — que calcula, valida, formatea y registra — tiene la cohesión de un cajón de sastre.

Martin Fowler cataloga los dos síntomas con nombres que vale la pena conocer porque aparecen en cualquier revisión de código (los popularizó *Refactoring*, 1999):

- **Shotgun surgery** (cirugía de escopeta): *un* motivo de cambio dispara modificaciones en *muchos* sitios. Los veintitrés ficheros del recargo de equivalencia. Es el precio del conocimiento desparramado.
- **Divergent change** (cambio divergente): el espejo — *un* sitio cambia por *muchos* motivos distintos. `calc2()` se modifica cuando cambia el IVA, cuando cambia el formato del PDF, cuando cambia una validación… Es el precio del cajón de sastre.

Y la regla que lo condensa todo, tal como la escribía el cuaderno de faro: **las cosas que cambian juntas deben vivir juntas; las que cambian por motivos distintos deben vivir separadas.** Esta frase es la brújula; todo lo que sigue son instrumentos para navegarla.

## SOLID: de dónde sale de verdad

Un poco de arqueología que muchos seniors no conocen: los cinco principios los recopiló y formuló **Robert C. Martin** a lo largo de los años 90 (el artículo de síntesis es *Design Principles and Design Patterns*, 2000, disponible gratuitamente; la lista comentada vive en su página abierta *The Principles of OOD*, butunclebob.com). Pero **el acrónimo no es suyo**: la reordenación de los principios para que formaran la palabra SOLID se le ocurrió a **Michael Feathers** — el mismo del libro de legacy — hacia 2004. Y dos de los cinco principios ni siquiera son de Martin: uno es de Bertrand Meyer y otro de Barbara Liskov. Los repasamos con su historia, porque cada uno se entiende mejor desde su origen.

### S — Principio de responsabilidad única (SRP)

> «Una clase debería tener una, y solo una, razón para cambiar.» — R. C. Martin, *The Principles of OOD* (traducción propia)

Es la cohesión con definición operativa. La formulación madura de Martin (en *Clean Architecture*, 2017) lo afina de un modo que casi nadie cita bien: una «razón para cambiar» es **un actor** — un colectivo humano que pide cambios. `calc2()` responde ante contabilidad (reglas de cálculo), ante los comerciales (formatos de factura), ante sistemas (rendimiento del PDF)… Cinco jefes, como decía el cuaderno de faro, cada uno tirando hacia un lado. El SRP no dice «haz clases pequeñas»; dice **«no obligues a públicos distintos a compartir la misma pieza de código»**, porque sus cambios colisionarán.

```python
# Viola SRP: tres actores en una clase
class Factura:
    def calcular_total(self): ...      # reglas de negocio → contabilidad
    def generar_pdf(self): ...         # presentación → comercial/cliente
    def guardar_en_mysql(self): ...    # persistencia → sistemas

# Cumple SRP: cada actor tiene su pieza
class Factura:
    def calcular_total(self): ...      # solo negocio

class GeneradorPdfFactura: ...
class RepositorioFacturas: ...         # este nombre reaparecerá en la sección 6
```

### O — Principio abierto/cerrado (OCP)

> «Las entidades de software deberían estar abiertas a la extensión pero cerradas a la modificación.»

Este es de **Bertrand Meyer** (*Object-Oriented Software Construction*, 1988). Suena a acertijo zen y es pura economía: debería ser posible **añadir** comportamiento nuevo sin **editar** el código existente que ya funciona. ¿Cómo? Haciendo que el código existente dependa de *abstracciones* con implementaciones enchufables. El ejemplo eterno son los descuentos:

```javascript
// Cerrado a extensión: cada tipo nuevo de descuento OBLIGA a editar esta función
function aplicarDescuento(importe, tipo) {
  if (tipo === "volumen") return importe * 0.95;
  if (tipo === "temporada") return importe * 0.90;
  if (tipo === "recargo_equivalencia") { /* editar aquí… otra vez */ }
  return importe;
}

// Abierto a extensión: los tipos nuevos se AÑADEN, lo existente no se toca
const politicasDeDescuento = {
  volumen: (importe) => importe * 0.95,
  temporada: (importe) => importe * 0.90,
};
function aplicarDescuento(importe, tipo) {
  const politica = politicasDeDescuento[tipo] ?? ((x) => x);
  return politica(importe);
}
```

El matiz profesional: OCP no ordena predecir el futuro y llenar el código de puntos de extensión especulativos (recuerda la cuarta regla de Beck: mínimos elementos). La práctica sensata es cerrar el código **contra los cambios que ya han dolido**: la primera vez que un `if` en cadena te obligue a editar diez sitios, conviértelo en política enchufable; no antes.

### L — Principio de sustitución de Liskov (LSP)

> Si S es un subtipo de T, los objetos de tipo S deben poder usarse donde se espera un T **sin que el programa lo note**.

Formulado por **Barbara Liskov** (conferencia *Data Abstraction and Hierarchy*, 1987; formalizado con Jeannette Wing en 1994). Liskov ganó el premio Turing en 2008; este principio es un fragmento de por qué. La versión coloquial: **un subtipo no puede romper las promesas de su tipo base** — ni exigir más (precondiciones más duras) ni ofrecer menos (postcondiciones más flojas).

El ejemplo clásico es venenosamente intuitivo: ¿es `Cuadrado` un subtipo de `Rectangulo`? En matemáticas, sí; en código, **no**, si `Rectangulo` promete que puedes cambiar la anchura sin alterar la altura — el cuadrado rompe esa promesa. La herencia válida no sigue al «es un» del diccionario, sino al «se comporta como» de los contratos.

En el mundo sin tipos estáticos de JavaScript y Python, el LSP gobierna el *duck typing*: cualquier objeto que pases «como si fuera» un enviador de correos debe honrar el contrato completo — mismos argumentos, mismos tipos de retorno, mismos errores. La versión práctica que verás cada semana: si una implementación de una interfaz lanza `NotImplementedError` en la mitad de sus métodos, o devuelve `null` donde las demás devuelven listas, tienes una violación de Liskov, y los `if isinstance(...)` que brotan alrededor son sus metástasis.

### I — Principio de segregación de interfaces (ISP)

> «Ningún cliente debería ser forzado a depender de métodos que no usa.» — R. C. Martin

Nació de un caso real: Martin, consultor para Xerox, encontró una clase `Job` gigante de la que dependía todo el software de una impresora — grapar dependía (vía recompilaciones eternas) de imprimir. El remedio: **interfaces pequeñas, por cliente**, en lugar de una interfaz gorda para todos. En lenguajes dinámicos no hay `interface` sintáctica, pero el principio muerde igual: si tu módulo de informes importa el módulo-catedral `facturacion` entero solo para usar `redondearImporteDeLinea`, un cambio en cualquier rincón de la catedral puede arrastrarte. Divide los módulos por *consumidor*: `calculo/redondeo.js` puede importarse sin llevarse la catedral entera.

### D — Principio de inversión de dependencias (DIP)

> «Los módulos de alto nivel no deben depender de los de bajo nivel. Ambos deben depender de abstracciones.» — R. C. Martin

El más importante de los cinco para este curso, porque es el cimiento de la sección 4 entera. Es, exactamente, **el enchufe del cuaderno de faro**: la lámpara (política de alto nivel: «iluminar el salón») no está soldada a la instalación eléctrica (detalle de bajo nivel); en medio hay un contrato — el enchufe — que ambos respetan. Puedes cambiar la lámpara sin electricista y la instalación sin tocar la lámpara.

Sin DIP, la lógica de negocio queda soldada a los detalles:

```python
# La política depende del detalle: soldadura
class EmisorDeFacturas:
    def emitir(self, pedido):
        factura = self._calcular(pedido)
        conexion = MySQLConexion("10.0.0.7", "atlas", "...")  # detalle concreto
        conexion.insert("facturas", factura.as_row())          # y su formato de fila
        return factura
```

Con DIP, la dirección del conocimiento **se invierte**: el detalle conoce el contrato que define la política, y no al revés:

```python
# El contrato lo define quien manda: la política
class RepositorioDeFacturas:            # abstracción (en Python, una clase base o Protocol)
    def guardar(self, factura): ...

class EmisorDeFacturas:
    def __init__(self, repositorio: RepositorioDeFacturas):
        self._repositorio = repositorio          # depende del contrato, no del detalle

    def emitir(self, pedido):
        factura = self._calcular(pedido)
        self._repositorio.guardar(factura)
        return factura

# El detalle IMPLEMENTA el contrato: la flecha del conocimiento apunta hacia la política
class RepositorioMySQLDeFacturas(RepositorioDeFacturas):
    def guardar(self, factura): ...     # aquí, y solo aquí, vive MySQL
```

Fíjate en qué se ha invertido exactamente — es el punto que más cuesta ver la primera vez. En tiempo de ejecución, la llamada sigue yendo de la política al detalle (el emisor acaba ejecutando código MySQL). Lo que cambia de dirección es la **dependencia en el código fuente**: antes, el fichero del emisor importaba MySQL; ahora, el fichero de MySQL importa (implementa) el contrato del emisor. El alto nivel ya no sabe que MySQL existe. Y de ese giro se siguen tres regalos: puedes testear el emisor con un repositorio falso en memoria (el *seam* de la sección 2, elevado a principio), puedes cambiar MySQL por otra cosa sin tocar el negocio, y puedes leer la política sin vadear detalles. Cuando en la próxima sección dibujen círculos concéntricos y digan «las dependencias apuntan hacia dentro», estarán diciendo *esto*, a escala de aplicación entera.

## El mapa completo, en una tabla

| Principio | Pregunta que responde | Síntoma de violación |
|---|---|---|
| SRP | ¿Cuántos públicos atiende esta pieza? | Cambio divergente; la clase «hace de todo» |
| OCP | ¿Añadir algo nuevo obliga a editar lo viejo? | El mismo `if`/`switch` crece en cada release |
| LSP | ¿Los sustitutos honran el contrato? | `isinstance`/comprobaciones de tipo; métodos «no aplica» |
| ISP | ¿Dependes de más de lo que usas? | Importas la catedral para usar una vela |
| DIP | ¿Quién define el contrato: la política o el detalle? | El negocio importa drivers, SDKs y formatos de fila |

Los cinco son instrumentos de la misma brújula: acoplamiento bajo (OCP, ISP, DIP gestionan quién sabe qué sobre quién) y cohesión alta (SRP), con contratos honestos (LSP) para que las piezas sean de verdad intercambiables.

## Para llevar

- Acoplamiento: cuántos sitios tocas para cambiar una cosa. Cohesión: cuántos motivos hay para tocar un sitio. Meta eterna: bajo y alta, respectivamente (Constantine & Yourdon, 1979).
- Shotgun surgery y divergent change (Fowler) son los dos síntomas espejo; los veintitrés ficheros y `calc2()` son sus retratos.
- La brújula: lo que cambia junto, vive junto; lo que cambia por motivos distintos, vive separado.
- SOLID (recopilación de R. C. Martin; acrónimo de M. Feathers): SRP = un actor por pieza; OCP (Meyer) = extender sin editar, aplicado donde ya dolió; LSP (Liskov) = los sustitutos honran contratos; ISP = interfaces por cliente; DIP = los contratos los define la política y los detalles los implementan.
- DIP invierte la dependencia *en el código fuente*, no el flujo de llamadas: el negocio deja de saber que la base de datos existe. Es el fundamento de las arquitecturas de la próxima sección.

## Para profundizar

- Robert C. Martin, *The Principles of OOD* (butunclebob.com) y el artículo *Design Principles and Design Patterns* (2000) — gratuitos.
- Barbara Liskov, *Data Abstraction and Hierarchy* (1987) — la keynote original, localizable en abierto; y su charla del premio Turing, en vídeo, muy recomendable.
- Martin Fowler, *Refactoring* — catálogo de los smells citados; las entradas del bliki sobre acoplamiento son gratuitas.
- David Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (1972) — el artículo abuelo de todo este capítulo, breve y sorprendentemente legible; disponible en abierto en la ACM.
