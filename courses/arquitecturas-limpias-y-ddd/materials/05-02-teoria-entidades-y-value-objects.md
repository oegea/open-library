Con la casa dibujada (sección 4), toca fabricar los ladrillos que viven en su centro: los objetos del **dominio**. Este capítulo presenta los dos ladrillos fundamentales del Domain-Driven Design táctico — **value objects** y **entidades** — con las definiciones canónicas de Eric Evans y con la API concreta que usa la arquitectura destino de este curso. Es el capítulo más «de código» hasta ahora, y el que convierte la anécdota del céntimo en un principio general: *que los datos inválidos no puedan nacer*.

## El dominio y su modelo

Dos definiciones previas, directamente del *DDD Reference* de Eric Evans (2015, CC BY 4.0; traducción propia):

- **Dominio**: «una esfera de conocimiento, influencia o actividad; el área a la que el usuario aplica el programa es el dominio del software». Para Meridian: la facturación — clientes, líneas, impuestos, descuentos, remesas.
- **Modelo de dominio**: «un sistema de abstracciones que describe aspectos seleccionados del dominio y puede usarse para resolver problemas relativos a él». No es un diagrama colgado en una wiki: en DDD, el modelo **es el código del dominio**. La clase `Importe` de Júlia es un trozo de modelo.

La capa `domain/` de la sección anterior existe para alojar exactamente esto. Y sus habitantes son de dos especies, que se distinguen con una sola pregunta.

## La pregunta: ¿importa quién, o importa qué?

Toma dos billetes de diez euros. ¿Te importa cuál de los dos te den? No: son intercambiables; solo importa su *valor*. Toma ahora dos clientes que casualmente se llaman igual: ¿son el mismo? No: cada uno tiene su historia, sus facturas, su *identidad*. Esa es toda la distinción:

- Un **value object** se define por **sus atributos**: dos instancias con los mismos valores son la misma cosa. Del *DDD Reference*: «un objeto que describe alguna característica o atributo pero no tiene identidad conceptual».
- Una **entidad** se define por **su identidad**, que persiste aunque sus atributos cambien: «un objeto definido fundamentalmente por su identidad, continuidad y ciclo de vida, no por sus atributos». Una factura sigue siendo *esa* factura cuando pasa de borrador a emitida; tu cuenta bancaria sigue siendo la tuya con otro saldo.

En el dominio de Meridian: `Importe`, `Porcentaje`, `NIF`, `PeriodoDeFacturacion` son value objects. `Factura`, `Cliente` son entidades. La regla de oro del reparto, que sorprende a los recién llegados: **el modelo debe tener muchos más value objects que entidades.** La identidad es cara — hay que gestionarla, persistirla, compararla — y solo la merecen los conceptos con ciclo de vida. Martin Fowler resume el instinto correcto en su bliki (entrada *ValueObject*, gratuita): ante un concepto nuevo, la pregunta no es «¿qué clase hago?» sino «¿esto necesita identidad, o es un valor?». En la duda, valor.

## Anatomía de un value object

Tres propiedades definen a un value object bien hecho, y cada una elimina una categoría entera de bugs:

1. **Autovalidación: lo inválido no nace.** El constructor (o la fábrica que lo sustituye) comprueba las reglas del concepto y rechaza lo ilegal *en la puerta*. A partir de ahí, todo el sistema puede confiar: si tienes un `NIF` entre manos, es válido — no porque alguien lo comprobara en la pantalla, sino porque es *imposible* tener uno inválido. Es la «ley física» del cuaderno de faro: la validación deja de ser una costumbre y pasa a ser una propiedad del tipo.
2. **Inmutabilidad: las operaciones devuelven instancias nuevas.** Un value object no cambia jamás después de nacer; `importe.sumar(otro)` no modifica `importe` — devuelve un tercero. ¿Por qué tanto empeño? Porque un valor compartido y mutable es una bomba: si dos facturas comparten el objeto «21% de IVA» y alguien lo muta al 10%, ambas cambian en silencio. La inmutabilidad hace el objeto seguro de compartir, seguro de usar como clave, seguro entre hilos, y — sobre todo — **razonable**: lo que ves al crearlo es lo que habrá siempre.
3. **Igualdad por valor.** Dos `Importe` de 1.990 céntimos son iguales, vengan de donde vengan. Como JavaScript y Python comparan objetos por referencia, la igualdad se implementa a mano (`equals`) — y hacerlo obliga a decidir qué significa «igual», que es en sí una conversación de dominio.

Así se ve la clase de Júlia, con la API estándar del documento de arquitectura que este curso usa de destino (la veremos entera en la sección 10):

```javascript
export class Importe {
  #centimos;                      // privado de verdad (campo #)

  constructor(centimos) { this.#centimos = centimos; }

  static create(centimos) {
    Importe.ensureImporteIsValid(centimos);
    return new Importe(centimos);
  }

  static ensureImporteIsValid(centimos) {
    if (!Number.isInteger(centimos)) {
      throw new Error("[Importe] el importe se expresa en céntimos enteros");
    }
    if (centimos < 0) {
      throw new Error("[Importe] no puede ser negativo; usa Abono para importes a favor del cliente");
    }
  }

  static fromPrimitive(centimos) { return Importe.create(centimos); }
  toPrimitive() { return this.#centimos; }

  sumar(otro) { return Importe.create(this.#centimos + otro.toPrimitive()); }

  aplicarPorcentaje(porcentaje) {
    // La política de redondeo vive AQUÍ, una vez, con nombre:
    // redondeo half-up al céntimo, acordado con contabilidad.
    const bruto = this.#centimos * porcentaje.comoFraccion();
    return Importe.create(Math.round(bruto));
  }

  equals(otro) { return otro instanceof Importe && this.#centimos === otro.toPrimitive(); }
}
```

Y su gemela en Python, para ver que el patrón es de ideas, no de sintaxis:

```python
from dataclasses import dataclass

@dataclass(frozen=True)          # inmutable + igualdad por valor, gratis
class Importe:
    centimos: int

    def __post_init__(self):
        if not isinstance(self.centimos, int):
            raise ValueError("[Importe] el importe se expresa en céntimos enteros")
        if self.centimos < 0:
            raise ValueError("[Importe] no puede ser negativo")

    def sumar(self, otro: "Importe") -> "Importe":
        return Importe(self.centimos + otro.centimos)
```

Observa tres decisiones finas del ejemplo JavaScript, porque son las que separan el patrón bien hecho del cargo-cult:

- **`fromPrimitive` / `toPrimitive`**: el value object vive en el dominio, pero sus datos tienen que viajar (a la base de datos, al JSON de una API). Estos dos métodos son la aduana: `toPrimitive()` exporta el valor desnudo, `fromPrimitive()` lo reimporta *revalidando*. El dominio trabaja con objetos ricos; las fronteras, con primitivos. Nada cruza sin pasar la aduana.
- **Los errores llevan el nombre del tipo entre corchetes** (`[Importe] ...`): cuando uno de estos errores llegue a un log a las tres de la mañana, dirá exactamente qué regla de qué concepto se violó.
- **La política de redondeo tiene casa.** El bug de los tres céntimos no se arregló «usando enteros»: se arregló dándole a la decisión «cómo se redondea en Meridian» un domicilio único y con nombre. Si mañana contabilidad cambia el criterio, hay *un* sitio que tocar. Compara con las dos políticas fantasma de `calc2()` que costaron 4.700 €.

### La obsesión por los primitivos

El anti-patrón que los value objects curan tiene nombre en los catálogos de refactoring: **primitive obsession** — modelar conceptos del dominio con tipos primitivos (números, strings) «porque es más simple». El float para el dinero es el ejemplo estrella, pero la plaga es general: el NIF como string (¿validado? ¿dónde? ¿por quién?), el porcentaje como número (¿0.21 o 21? — pregúntale a la sonda de Marte de la sección 1), el email como string, el par `(importe, moneda)` viajando en dos parámetros separados que un día alguien pasará en el orden equivocado. Cada primitivo desnudo es una promesa sin garante. La señal para refactorizar: en cuanto un dato tiene *reglas* (formato, rango, operaciones legales) o *compañeros de viaje inseparables*, quiere ser un value object.

## Anatomía de una entidad

La entidad añade al cóctel una sola cosa — identidad — y una disciplina: **proteger sus invariantes**. Un **invariante** es una regla que debe ser verdad *siempre*, en todo momento observable: «el total de una factura es la suma de sus líneas», «una factura emitida no puede modificarse». La entidad es la guardiana de sus invariantes: ninguna operación pública puede dejarla en un estado que los viole.

En la arquitectura destino, las entidades son además **inmutables al estilo funcional**: los «modificadores» devuelven una instancia nueva en lugar de mutar la existente:

```javascript
export class Factura {
  #id; #cliente; #lineas; #estado;

  constructor(id, cliente, lineas, estado) { /* asignaciones */ }

  static create(id, cliente, lineas) {
    if (lineas.length === 0) throw new Error("[Factura] debe tener al menos una línea");
    return new Factura(id, cliente, lineas, "borrador");
  }

  anadirLinea(linea) {
    if (this.#estado === "emitida") {
      throw new Error("[Factura] una factura emitida no se modifica; usa una rectificativa");
    }
    return new Factura(this.#id, this.#cliente, [...this.#lineas, linea], this.#estado);
  }

  emitir() { return new Factura(this.#id, this.#cliente, this.#lineas, "emitida"); }

  total() {   // Information Expert (sección 3): quien tiene las líneas, calcula
    return this.#lineas.reduce((suma, l) => suma.sumar(l.importe()), Importe.create(0));
  }

  equals(otra) { return otra instanceof Factura && this.#id === otra.getId(); }  // ¡por identidad!
  getId() { return this.#id; }
}
```

Fíjate en los detalles con carga de profundidad:

- **`equals` compara ids, no atributos.** Es la definición de entidad hecha código: la misma factura con distinto estado sigue siendo igual a sí misma.
- **`anadirLinea` devuelve otra `Factura`.** El estilo inmutable no es obligatorio en DDD clásico, pero paga bien: sin estados intermedios observables, los invariantes se comprueban en un solo sitio (la construcción), el paso del tiempo queda explícito (`factura = factura.anadirLinea(...)`) y los tests no necesitan «deshacer» nada.
- **La regla «emitida no se toca» vive dentro.** No en el controlador, no en la pantalla, no en la buena memoria de Denís: *dentro*. Es Tell, Don't Ask (sección 3) cumplido: el exterior expresa intenciones (`emitir()`, `anadirLinea()`) y la entidad decide si son legales. Los datos y sus reglas, por fin, viven juntos.

Un apunte de vocabulario que te encontrarás en la literatura: cuando varias entidades y valores forman una unidad de consistencia — la factura y sus líneas, que nunca tienen sentido por separado — DDD los agrupa bajo el nombre de **agregado**, con la entidad principal como raíz y guardiana única de la puerta. La ampliación de la sección 6 le dedica espacio; por ahora, la intuición basta: `LineaFactura` no se guarda ni se busca sola — se llega a ella *a través* de su `Factura`.

## Para llevar

- Dominio = el área del problema; modelo de dominio = el sistema de abstracciones que lo describe, encarnado en el código de la capa `domain/` (definiciones del *DDD Reference*, Evans).
- Value object: definido por sus atributos; sin identidad. Autovalidado (lo inválido no nace), inmutable (operar = crear), igual por valor. Debe ser la especie mayoritaria del modelo.
- Entidad: definida por identidad que persiste mientras los atributos cambian; `equals` compara ids; guardiana de sus invariantes; en este curso, inmutable con modificadores que devuelven instancias nuevas.
- `create` valida, `fromPrimitive`/`toPrimitive` son la aduana con las fronteras (BD, JSON), los errores se prefijan `[Tipo]`, y las decisiones delicadas (redondeo) viven una sola vez, con nombre y domicilio.
- Primitive obsession: todo dato con reglas o con compañeros inseparables está pidiendo ser value object. El dinero jamás es un float — es céntimos enteros dentro de un tipo que no sabe mentir.

## Para profundizar

- Eric Evans, *DDD Reference* (CC BY 4.0, domainlanguage.com) — entradas *Entities* y *Value Objects*: dos páginas, canónicas.
- Martin Fowler, *ValueObject* y *EvansClassification* en martinfowler.com — gratuitas.
- El capítulo 5 del «libro azul» (*Domain-Driven Design*, Evans, 2003) desarrolla ambos ladrillos; de pago, y la fuente de todo lo demás.
- Sobre coma flotante: el clásico *What Every Computer Scientist Should Know About Floating-Point Arithmetic* (David Goldberg, 1991) circula en abierto; con leer dos páginas se te quitan las ganas de sumar dinero en float para siempre.
