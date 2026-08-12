La sección anterior terminaba con una advertencia: en código sin tests, hasta renombrar da miedo. La historia acaba de mostrar el mecanismo completo del miedo — Júlia arregla un bug real y rompe un informe que no sabía que existía — y también la salida. Este capítulo ordena esa salida en tres partes: qué es de verdad el código legacy y cómo se toca sin morir (tests de caracterización), cómo deben ser las funciones para que mentir sea difícil, y qué papel juegan — y cuál no — los comentarios.

## Legacy: la definición de Feathers

**Código legacy** no significa «código viejo». La definición operativa la dio Michael Feathers en *Working Effectively with Legacy Code* (2004), el libro que Gabriel le presta a Júlia, y es deliberadamente brutal:

> «Para mí, código legacy es simplemente código sin tests.» *(traducción propia del prefacio)*

La definición es útil porque señala el síntoma que importa: **el miedo a cambiarlo**. Un código sin tests solo puede modificarse «editando y rezando» — el método oficial de Meridian durante quince años. Y el miedo tiene una dinámica propia que el cuaderno de faro describe con precisión clínica: *el miedo produce copias, las copias divergen, la divergencia produce más miedo*. El informe de descuentos duplicado no fue un accidente: fue la consecuencia lógica de un sistema donde tocar el original era más peligroso que copiarlo. Cuando veas código duplicado en un sistema viejo, no preguntes «¿quién fue el vago?»; pregunta «¿qué daba tanto miedo?».

## Tests de caracterización: fotografiar al dragón

Un test normal codifica lo que el sistema *debería* hacer. Pero para escribirlo hay que saber qué debería hacer — y en un sistema legacy, muchas veces, nadie lo sabe ya. Feathers propone para estos casos el **test de caracterización** (*characterization test*): un test que codifica lo que el sistema **hace hoy**, sea correcto o no.

El procedimiento, tal como lo aplicaron Júlia y Denís:

1. **Genera entradas variadas** que cubran los caminos del código: casos normales, extremos, raros (las cuarenta y una facturas del tipo 7). No hace falta entender cada camino; hace falta *ejercitarlo*.
2. **Captura las salidas exactas** que produce el sistema actual y guárdalas como referencia. Cuando la salida es voluminosa (una remesa entera de facturas), a esta variante se la llama **golden master**: el fichero de referencia contra el que se comparará todo lo posterior.
3. **Convierte cada par entrada→salida en un test automático.** Desde este momento, cualquier cambio que altere *cualquier* comportamiento enciende una alarma.
4. **Ahora — y solo ahora — cambia el código.** Si tu cambio pretendía alterar 12 comportamientos y se encienden 12 alarmas, perfecto: revísalas y actualiza las referencias. Si se encienden 13, la número 13 acaba de ahorrarte una llamada del cliente.

Un esqueleto en Python del arnés de Júlia, simplificado:

```python
import json
from pathlib import Path
from motor_calculo import calcular_factura  # el código legacy, tal cual está

CASOS = Path("casos")           # entradas generadas: caso_001.json, caso_002.json...
REFERENCIAS = Path("referencias")  # salidas capturadas: caso_001.esperado.json...

def test_caracterizacion():
    for caso in sorted(CASOS.glob("caso_*.json")):
        entrada = json.loads(caso.read_text())
        resultado = calcular_factura(entrada)
        referencia = json.loads(
            (REFERENCIAS / f"{caso.stem}.esperado.json").read_text()
        )
        assert resultado == referencia, f"El comportamiento cambió en {caso.name}"
```

Y la misma idea en JavaScript, con cualquier runner de tests moderno:

```javascript
import { readFileSync, readdirSync } from "node:fs";
import { calcularFactura } from "./motorCalculo.js"; // el legacy, sin tocar

for (const fichero of readdirSync("casos")) {
  test(`caracterización: ${fichero}`, () => {
    const entrada = JSON.parse(readFileSync(`casos/${fichero}`, "utf8"));
    const referencia = JSON.parse(
      readFileSync(`referencias/${fichero.replace(".json", ".esperado.json")}`, "utf8")
    );
    expect(calcularFactura(entrada)).toEqual(referencia);
  });
}
```

Tres matices que separan al que ha leído un tutorial del que lo ha hecho de verdad:

- **Los tests de caracterización consagran bugs, y eso está bien.** Su promesa no es «esto es correcto» sino «esto no cambiará sin que lo sepas». Cuando arreglas un bug conocido, *esperas* que fallen los casos afectados: esa lista de fallos es información valiosísima — es el mapa de todo lo que dependía del comportamiento viejo.
- **El determinismo es un prerrequisito.** Si el código legacy usa la fecha actual, números aleatorios o el orden de un diccionario, las referencias no serán estables. Parte del trabajo del arnés es fijar esas fuentes de variación (inyectar una fecha fija, una semilla). Guarda esta idea: «las dependencias ocultas de la función son el enemigo» reaparecerá en todo el curso.
- **No busques cobertura perfecta; busca cobertura de lo que vas a tocar.** Feathers insiste: el objetivo no es testear el sistema entero (imposible en un legacy grande), sino tender red *bajo la zona de la obra*.

## Funciones: pequeñas, una cosa, un nivel

Con la red puesta, empieza la mejora. La unidad de mejora es la **función**, y el criterio cabe en la frase del cuaderno de faro, que es también la formulación clásica de *Clean Code* (R. C. Martin, 2008, cap. 3):

> Una función debería hacer una cosa, hacerla bien, y no hacer nada más.

«Una cosa» tiene una definición menos vaga de lo que parece: una función hace una cosa cuando **todas sus líneas trabajan en el mismo nivel de abstracción**. Mira la diferencia en JavaScript:

```javascript
// Mezcla niveles: política de negocio y aritmética de céntimos en la misma vista
function emitirFactura(pedido, cliente) {
  let total = 0;
  for (const linea of pedido.lineas) {
    let importe = linea.cantidad * linea.precioUnitario;
    if (cliente.descuento > 0) {
      importe = importe - importe * cliente.descuento;
      importe = Math.round(importe * 100) / 100;
    }
    total += importe;
  }
  // ...30 líneas más de impuestos, numeración y persistencia
}
```

```javascript
// Un nivel por función: cada una se lee como una frase
function emitirFactura(pedido, cliente) {
  const lineas = calcularLineas(pedido.lineas, cliente);
  const totales = calcularTotales(lineas);
  return construirFactura(cliente, lineas, totales);
}

function calcularLineas(lineas, cliente) {
  return lineas.map((linea) => calcularImporteDeLinea(linea, cliente));
}

function calcularImporteDeLinea(linea, cliente) {
  const bruto = linea.cantidad * linea.precioUnitario;
  const conDescuento = aplicarDescuento(bruto, cliente.descuento);
  return redondearImporteDeLinea(conDescuento);
}
```

La versión buena no es más corta — suele ser algo más larga — pero cada función puede leerse, entenderse y **testearse** por separado, y el nivel alto (`emitirFactura`) se lee como el índice de un libro. A esto se le llama a veces la *regla descendente*: el código debería poder leerse de arriba abajo como una narración en la que cada función introduce las del nivel siguiente.

Señales de que una función pide división — todas aparecieron en `calc2()`:

- No puedes nombrarla sin «y» (`validarYCalcularYGuardar`).
- Tiene secciones separadas por comentarios («// ahora los impuestos») — cada sección es una función que quiere nacer, y el comentario es su nombre provisional.
- Sus variables locales cambian de significado por zonas (`$aux3`).
- Tiene muchos parámetros (más de tres es sospechoso; grupos de parámetros que siempre viajan juntos — `importe, moneda` — son un objeto queriendo nacer, como verás en la sección 5).
- **Banderas booleanas**: `calcular(pedido, true)` obliga al lector a memorizar qué diablos significa `true`, y confiesa que la función hace dos cosas (una por rama). Dos funciones con nombre honesto casi siempre lo resuelven.

Y el matiz que los seniors discuten con razón: *pequeña* es consecuencia, no objetivo. El fetichismo de «ninguna función de más de N líneas» produce a veces indirección laberíntica — cuarenta funciones de dos líneas que se llaman en cadena. El criterio rector es el nivel de abstracción único y el nombre honesto; el tamaño baja solo.

## Comentarios: la verdad incómoda

La posición clásica de *Clean Code* escandaliza la primera vez que se oye: **todo comentario es, en cierto sentido, un fracaso** — el fracaso de no haber podido expresarlo en el código. Es deliberadamente provocadora, pero su núcleo es sólido y la historia de Meridian lo ilustra: los comentarios **mienten con el tiempo**. El código se mantiene porque se ejecuta; el comentario no se ejecuta, así que nadie nota cuando queda obsoleto. El bloque de cabecera de `facturacion.php` — «mantenido por: [ver wiki]», con la wiki borrada — es un fósil típico.

La política práctica:

- **Antes de comentar, intenta expresarlo en código.** `// comprueba si puede facturarse` sobre un `if` críptico se convierte en una función `puedeFacturarse()` y el comentario muere de éxito. La mayoría de los comentarios explicativos son nombres que no encontraron su sitio.
- **Los comentarios valiosos explican el *porqué*, nunca el *qué*.** El qué ya lo dice el código. Un buen comentario documenta la decisión invisible: `// Redondeamos al total, no por línea: acta de la reunión con Vesta, 2026-09-14`. Ese comentario no puede sustituirse por código, porque su contenido no está en el código: está en el mundo.
- **Comentarios legítimos**: advertencias de consecuencias («esto tarda 40 minutos con datos reales»), TODO honestos y fechados, aclaración de un algoritmo genuinamente complejo, y documentación de API pública (docstrings/JSDoc) — que es interfaz, no implementación.
- **Comentarios a eliminar sin piedad**: código comentado (para eso está el control de versiones; el código comentado es basura que nadie se atreve a tirar), diarios de cambios en cabecera (para eso está `git log`), y el ruido (`i++; // incrementa i`).

## Las cuatro reglas del diseño simple

Cierra el capítulo la síntesis más compacta que existe de todo lo anterior. Kent Beck las formuló en los 90 (Extreme Programming); Martin Fowler las documenta en su bliki (entrada *BeckDesignRules*, martinfowler.com). Un diseño es simple cuando, **por este orden de prioridad**:

1. **Pasa todos los tests.** Primero funciona — y se sabe que funciona. Sin esto, lo demás es decoración.
2. **Revela la intención.** Cualquier lector entiende qué pretende.
3. **No se repite** (cada pieza de conocimiento vive en un solo lugar — la copia del cálculo de descuentos violaba exactamente esto).
4. **Tiene el mínimo de elementos.** Nada de estructura especulativa «por si acaso».

Fíjate en que el orden zanja el debate de la historia: la red de tests va *antes* que la limpieza, porque es la regla 1; y la duplicación (regla 3) se elimina *después* de tener la red, no antes. Júlia y Denís, sin saberlo, siguieron las cuatro reglas en orden.

## Para llevar

- Legacy = código sin tests (Feathers). El síntoma que importa es el miedo; el miedo produce duplicación y la duplicación, divergencia silenciosa.
- Test de caracterización: codifica lo que el sistema hace hoy, bugs incluidos. No promete corrección; promete que nada cambiará sin que lo sepas. Golden master: la referencia capturada para salidas voluminosas.
- Red primero, cambio después. La lista de tests que fallan tras un cambio es el mapa exacto de sus efectos.
- Una función, una cosa = todas sus líneas al mismo nivel de abstracción. Señales de división: nombres con «y», secciones comentadas, variables camaleónicas, banderas booleanas, parámetros en manada.
- Comentarios: el qué se expresa en código; el porqué (decisiones, contexto del mundo) es el único contenido que justifica un comentario. El código comentado se borra.
- Cuatro reglas del diseño simple (Beck), en orden: pasa los tests, revela intención, no se repite, mínimo de elementos.

## Para profundizar

- Michael Feathers, *Working Effectively with Legacy Code* (2004) — el manual definitivo para tocar sistemas sin red. De pago; su influencia justifica cada euro.
- Martin Fowler, *BeckDesignRules* y *SelfTestingCode* en martinfowler.com (gratuitos).
- *97 Things Every Programmer Should Know* (CC BY-NC-SA 3.0): los capítulos *Comment Only What the Code Cannot Say* (Kevlin Henney) y *The Golden Rule of API Design* complementan este capítulo.
