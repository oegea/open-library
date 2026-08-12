Los ladrillos de la teoría parecen sencillos, y por eso mismo sus deformaciones son tan frecuentes: se puede tener carpetas `domain/` llenas de clases con nombres de negocio y no tener modelo de dominio en absoluto. Esta ampliación cataloga las trampas — empezando por la más famosa — y cierra con dos refinamientos que suelen faltar incluso en equipos veteranos: los list classes y el dinero multi-moneda.

## El modelo de dominio anémico

Martin Fowler le dedicó en 2003 una de las entradas más citadas de su bliki (*AnemicDomainModel*, gratuita):

> «Los síntomas básicos de un modelo de dominio anémico: a primera vista parece lo real — hay objetos, muchos con los nombres de los conceptos del dominio [...]. La trampa aparece cuando miras el comportamiento y te das cuenta de que apenas tienen alguno. [...] En su lugar hay un conjunto de objetos de servicio que capturan toda la lógica del dominio y hacen todo el cálculo, usando el modelo de dominio como mero saco de datos. Lo esencialmente terrible es que es lo contrario de la idea básica del diseño orientado a objetos: combinar datos y proceso.» *(traducción propia, abreviada)*

El retrato robot: una clase `Factura` que solo tiene getters y setters, y al lado un `FacturaService` con setecientas líneas donde vive *toda* la lógica — validación, cálculo, transiciones de estado — manipulando la factura desde fuera. Es la versión con carpetas bonitas del «ask» patológico de la sección 3.

¿Por qué es tan común? Porque es el camino de mínima resistencia de varias herramientas y hábitos: los ORMs que generan clases-tabla con setters públicos, los formularios que rellenan objetos campo a campo, los tutoriales de frameworks donde el «modelo» es un espejo de la base de datos. Y ¿por qué es dañino? Porque reparte cada regla entre todos sus llamadores: la regla «una factura emitida no se modifica» acaba comprobada en cuatro controladores (con tres redacciones distintas y un olvido — y el olvido es el bug). El coste no se ve el primer mes; se ve el primer año.

La prueba diagnóstica rápida, útil en cualquier revisión: abre una entidad y busca **setters públicos sin reglas**. `setEstado(estado)` sin lógica es anemia con corbata: cualquiera puede poner cualquier estado en cualquier momento, y los invariantes son una ilusión. Compárese con `emitir()`, que valida, decide y protege. Los nombres de los métodos de una entidad sana son **verbos del negocio**, no operaciones de fontanería sobre campos.

Matiz honesto para no fabricar dogma: el propio Fowler reconoce que hay lógica que legítimamente no cabe en una entidad — la que coordina varios agregados o habla con el exterior. Para eso existen los *domain services* (poca cosa, sin estado, con nombre de operación de negocio) y, sobre todo, los casos de uso de la sección 7. El pecado anémico no es que exista lógica fuera de las entidades: es que *toda* la lógica viva fuera y las entidades no defiendan *nada*.

## Trampas menores del mismo barrio

- **El value object mutable.** Un `Importe` con `setCentimos()` no es un value object: es un primitivo con sombrero. La inmutabilidad no es opcional en el patrón — es lo que hace seguro compartirlo.
- **La validación en la frontera equivocada.** Validar solo en el formulario web deja la puerta trasera abierta: el import masivo, el script de migración y el test crean objetos sin pasar por la pantalla. La validación del *concepto* va en el tipo (`ensureXIsValid`); la de la *petición* (¿viene el campo?, ¿es un JSON bien formado?) va en la frontera. Son validaciones distintas y se necesitan ambas.
- **La entidad-diccionario.** Entidades que exponen su interior crudo (`factura.datos["estado"]`) para que el exterior haga lo que quiera. Toda la protección del constructor se evapora por la escotilla.
- **El id como string mágico por todo el sistema.** Los identificadores también son conceptos con reglas: un `FacturaId` value object evita el clásico «pasé el id del cliente donde iba el de la factura», que con dos strings es invisible y con dos tipos es un error de compilación o una excepción inmediata.
- **Lógica de presentación colándose en el dominio.** `factura.totalFormateadoConEuro()` no es negocio: es pantalla. El dominio calcula (`total(): Importe`); formatear (`"1.990,00 €"`) es un problema del adaptador de salida. La frontera también se viola hacia dentro.

## List classes: la colección con reglas

Refinamiento que usa la arquitectura destino del curso y que casi ningún tutorial cuenta: cuando una colección de objetos de dominio tiene reglas o operaciones propias, merece su propia clase — un **list class** (`FacturaList`, `LineaFacturaList`) — en lugar de un array desnudo paseándose por el sistema.

```javascript
export class LineaFacturaList {
  #lineas;
  constructor(lineas) { this.#lineas = Object.freeze([...lineas]); }  // copia defensiva

  static create(lineas) {
    if (lineas.length === 0) throw new Error("[LineaFacturaList] no puede estar vacía");
    return new LineaFacturaList(lineas);
  }

  anadir(linea) { return LineaFacturaList.create([...this.#lineas, linea]); }
  total() { return this.#lineas.reduce((s, l) => s.sumar(l.importe()), Importe.create(0)); }
  toPrimitive() { return this.#lineas.map((l) => l.toPrimitive()); }
}
```

Qué compra esto frente al array: (1) los invariantes de colección — «no vacía», «sin duplicados», «máximo 500 líneas por factura de Vesta» — tienen dónde vivir; (2) las operaciones de conjunto (`total()`, `filtrarPendientes()`) dejan de repetirse en cada llamador (el `reduce` del total escrito cuatro veces es duplicación de conocimiento, la regla 3 de Beck); y (3) la copia defensiva + `Object.freeze` cierra la escotilla clásica: entregar tu array interno por referencia y que un llamador lo mute por fuera. En Python, el equivalente: una clase con `tuple` interna, o congelar con dataclasses.

## Dinero de verdad: el patrón Money completo

El `Importe` de la historia resuelve el caso de Meridian (una sola moneda). El patrón general — catalogado por Fowler en *Patterns of Enterprise Application Architecture* (2002); el catálogo resumido es gratuito en martinfowler.com — añade dos piezas que conviene conocer antes de necesitarlas:

- **La moneda viaja dentro del tipo**: `Money(1990, "EUR")`. Sumar euros con dólares no devuelve un número raro: lanza un error, porque `sumar` comprueba monedas. La categoría entera de bugs «mezclé monedas» se extingue en el tipo, igual que se extinguió el float.
- **El reparto con resto tiene nombre: `allocate`.** Divide 100 céntimos entre 3 sin perder ni inventar un céntimo: `allocate(3)` → `[34, 33, 33]`. Es la respuesta correcta a «¿cómo reparto un descuento global entre líneas?» — la pregunta cuya respuesta improvisada, duplicada en dos sitios con dos criterios, costó los 4.700,32 € del capítulo 1. El céntimo sobrante no desaparece: se asigna según una política explícita (al primero, al mayor, al azar auditado — lo que el negocio decida, *una vez*).

Detalle de época que un senior agradecerá: los lenguajes van absorbiendo el patrón — Python trae `decimal.Decimal` de serie (correcto para dinero si se fija el contexto de redondeo) y JavaScript ha ido incubando propuestas de decimales exactos —, pero el tipo de dominio sigue mereciendo existir aunque el primitivo mejore: `Decimal` sabe sumar; no sabe que «los importes de Meridian no son negativos» ni qué política de reparto firmó contabilidad. La aritmética es del lenguaje; las *reglas* son tuyas.

## Para llevar

- Modelo anémico (Fowler, 2003): objetos con nombres de dominio y cero comportamiento + servicios que lo hacen todo = lo contrario del diseño orientado a objetos. Diagnóstico rápido: setters públicos sin reglas; los métodos de una entidad sana son verbos de negocio.
- La lógica que coordina o cruza fronteras sí vive fuera (domain services, casos de uso); el pecado es que las entidades no defiendan nada.
- Trampas de barrio: value objects mutables, validación solo en pantalla, entidades-diccionario, ids como strings mágicos, formato de presentación dentro del dominio.
- List classes: colecciones con reglas y operaciones propias, inmutables y con copia defensiva — los invariantes de conjunto también necesitan casa.
- Money completo (PoEAA): la moneda dentro del tipo y `allocate` para repartos sin perder céntimos. Los primitivos mejoran; las reglas del negocio siguen siendo tuyas.
