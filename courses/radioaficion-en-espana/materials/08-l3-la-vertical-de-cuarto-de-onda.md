En la terraza de Vicente no hay ningún hilo tendido. Hay un tubo blanco de unos diez metros que apunta al cielo: la «vertical» con la que lleva décadas hablando en la banda de 40 metros. Diez metros es la mitad de lo que mide el dipolo de Marina para esa misma banda.

—¿Y con la mitad de antena haces lo mismo que yo? —le preguntó Marina.

—Con la mitad de antena y un espejo —dijo Vicente.

Esta lección explica ese espejo. Al terminar sabrás cómo funciona una antena vertical de cuarto de onda, qué es el plano de tierra y por qué de él depende que la antena rinda o no, y en qué se diferencia de un dipolo a la hora de elegir.

## Medio dipolo

Coge un dipolo y ponlo de pie, con un brazo hacia arriba y el otro hacia abajo. Sigue siendo un dipolo; solo ha cambiado de postura.

Ahora quita el brazo de abajo y, en su lugar, pon justo debajo del brazo que queda una superficie conductora grande y plana: una chapa metálica, por ejemplo.

Ocurre algo que parece un truco. Una superficie conductora refleja las ondas de radio igual que un espejo refleja la luz. Si te pones delante de un espejo ves a otra persona idéntica a ti al otro lado, aunque allí no haya nadie. Del mismo modo, las ondas que la varilla lanza hacia la chapa rebotan en ella y salen como si vinieran de un segundo brazo situado debajo, idéntico al de arriba. Ese brazo no existe, igual que no existe la persona del espejo, pero su efecto es real. Para el espacio de alrededor, el conjunto radia como un dipolo completo del que solo se ha construido la mitad.

> **Monopolo de cuarto de onda** (o **vertical de cuarto de onda**): antena formada por un solo conductor vertical de un cuarto de onda, situado sobre una superficie conductora que hace de espejo y sustituye al brazo que falta.

A esa superficie se le llama **plano de tierra**. Y a la antena, muy a menudo, se le llama por su nombre en inglés: *ground plane*.

![Una varilla vertical de un cuarto de onda sobre el suelo, con varios hilos radiales extendidos desde su base. Bajo el suelo, dibujada con línea discontinua, la imagen reflejada de la varilla: el brazo que falta, que el plano de tierra hace aparecer como en un espejo.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-vertical-espejo.svg)

El cable se conecta en la base: uno de sus dos conductores a la varilla y el otro al plano de tierra.

## Cuánto mide

Un cuarto de onda, que es la mitad de la media onda. Con el mismo acortamiento del 5 % que ya conoces:

**Longitud de la vertical de cuarto de onda (en metros) = 71,25 / f (en MHz)**

(71,25 es simplemente la mitad de 142,5.)

**Ejemplo 1.** *Una vertical para 14,2 MHz:* 71,25 / 14,2 = **5,02 m**.

**Ejemplo 2.** *Una vertical para 145 MHz:* 71,25 / 145 = 0,49 m: **49 centímetros**. Es la varilla de medio metro que llevan en el techo los coches de muchos radioaficionados.

Y la de Vicente: 71,25 / 7,1 = 10 metros. El tubo blanco de su terraza.

## El plano de tierra: la mitad que no se ve

Aquí está el punto delicado de esta antena. El espejo tiene que ser bueno, y conseguir un buen espejo no siempre es fácil.

Para ver por qué, sigue a la corriente. En el dipolo, la corriente que sube por un brazo es la que baja por el otro. En la vertical no hay otro brazo: la corriente que entra en la varilla tiene que salir de algún sitio, y sale del plano de tierra. **Por el plano de tierra circula exactamente la misma corriente que por la varilla.**

La tierra de verdad —el suelo de un campo, de un jardín— conduce la electricidad, pero bastante mal. Es un espejo empañado. Si la corriente de la antena tiene que atravesar ese terreno, que es una resistencia, lo calienta (recuerda P = I² × R) en lugar de radiar. Una parte grande de la energía del transmisor se queda en el suelo.

La solución es ofrecerle a esa corriente un camino de cobre: los **radiales**.

> **Radiales:** hilos conductores que salen de la base de la antena y se extienden en todas las direcciones, como los radios de una rueda. Entre todos forman el plano de tierra.

Hay tres maneras habituales de montarlos:

- **Sobre el suelo o enterrados a poca profundidad**, cuando la antena está a ras de tierra. Aquí vale la regla de cuantos más, mejor: con cuatro radiales la antena funciona; con dieciséis o treinta y dos, rinde de verdad.
- **Elevados**, cuando la antena está en lo alto de un mástil o en un tejado. Entonces bastan tres o cuatro radiales de un cuarto de onda saliendo de la base, porque en el aire ya no hay terreno que robe energía: toda la corriente va por el cobre. Es la antena de varilla con «bigotes» que se ve en muchas azoteas.
- **La chapa de un vehículo.** En un coche, el plano de tierra es el techo o el maletero metálico. Por eso las antenas de coche rinden mejor en el centro del techo que en una esquina del parachoques.

Hay una frase de radioclub que lo resume, y es exacta:

> **Una vertical rinde lo que rinde su plano de tierra.**

—Entonces mi walkie, que solo tiene la antenita de goma, ¿dónde tiene el espejo? —preguntó Lucía.

—En ti —dijo Vicente—. El plano de tierra de un portátil es la carcasa del propio aparato y la mano que lo sujeta. Es un espejo malísimo, y esa es una de las razones por las que un walkie alcanza tan poco con su antena original.

## La impedancia: la mitad que el dipolo

El dipolo completo presentaba unos 73 Ω. La vertical de cuarto de onda es medio dipolo, y su impedancia es también la mitad:

> **La impedancia de una vertical de cuarto de onda sobre un plano de tierra perfecto es de unos 36 Ω.**

Tiene su lógica. En el dipolo, la tensión de alimentación se mide entre los dos brazos. Aquí se mide entre la varilla y el plano de tierra, que está justo a medio camino entre la varilla y su imagen: hay la mitad de tensión, con la misma corriente. Y la mitad de tensión con la misma corriente es la mitad de impedancia.

Un detalle práctico que casi nadie cuenta. En las verticales con radiales elevados, los radiales no se ponen horizontales, sino inclinados hacia abajo, a unos 45 grados. No es por estética: al inclinarlos, la impedancia sube desde los 36 Ω hasta acercarse a los 50 Ω, que es justo lo que quieren los cables y los equipos, como verás en la lección 6.

## Hacia dónde radia

Mira una vertical desde arriba: es un punto. No tiene «frente» ni «costado», y por eso radia con la misma fuerza hacia todos los puntos del horizonte. Es una antena **omnidireccional**.

Y como el conductor está en vertical, la onda sale con **polarización vertical**.

Además, una vertical con un buen plano de tierra lanza su energía rasante, cerca del horizonte, sin necesidad de estar a gran altura. En la lección anterior viste que eso es lo que conviene para llegar lejos.

## Dipolo o vertical

Ninguna de las dos es «mejor». Son compromisos distintos:

| | Dipolo horizontal | Vertical de cuarto de onda |
|---|---|---|
| Tamaño | Media onda, tendida en horizontal | Un cuarto de onda, en vertical |
| Espacio que pide | Dos apoyos separados | Un solo punto… más sitio para los radiales |
| Impedancia | Unos 73 Ω | Unos 36 Ω |
| Diagrama visto desde arriba | En ocho | Circular: igual hacia todos los lados |
| Polarización | Horizontal | Vertical |
| Su punto débil | Para llegar lejos necesita altura | Necesita un buen plano de tierra |
| Ruido en recepción | Suele recoger menos | Suele recoger más ruido de aparatos eléctricos |

Sobre la última fila: casi todo el ruido que producen los aparatos eléctricos de una casa tiene polarización vertical, y la antena vertical lo recoge mejor. Es una de las razones por las que mucha gente, en ciudad, prefiere el dipolo.

¿Dónde encontrarás verticales? En casi todas partes: en los coches, en los walkies, en las emisoras de radiodifusión de onda media (esas torres altísimas son la antena, y bajo ellas hay enterrados kilómetros de radiales) y en las terrazas de quienes, como Vicente, no tienen dónde tender veinte metros de hilo.

## Donde la gente se lía

- **«Una vertical es más pequeña, así que se instala en cualquier sitio.»** La varilla ocupa poco. El plano de tierra, no: los radiales necesitan su espacio, y sin ellos la antena no rinde.
- **«Los radiales son un adorno, lo que radia es la varilla.»** Los radiales son media antena: por ellos circula la misma corriente que por la varilla.
- **«Plano de tierra y toma de tierra son lo mismo.»** No. La toma de tierra de una casa es un asunto de seguridad eléctrica. El plano de tierra de una antena es una pieza de la propia antena, que puede estar a veinte metros de altura y no tocar el suelo en ningún punto.
- **«Omnidireccional significa que radia igual en todas las direcciones.»** Igual hacia todos los puntos del horizonte. Hacia arriba, justo en la vertical, una antena así no radia casi nada.

## Compruébalo tú

1. Calcula la longitud de una vertical de cuarto de onda para 28,4 MHz.
2. ¿Y para 433 MHz? Da el resultado en centímetros.
3. Tienes una vertical a ras de suelo con dos radiales y rinde poco. ¿Qué es lo primero que probarías?
4. ¿Qué impedancia aproximada presenta una vertical de cuarto de onda sobre un buen plano de tierra? ¿Qué relación tiene con la del dipolo?
5. Dos estaciones cercanas quieren hablar directamente en VHF. Una usa una antena vertical y la otra un dipolo horizontal. ¿Qué problema tienen? (Recuerda lo que viste en la sección 6.)
6. ¿Por qué una antena de coche rinde mejor en el centro del techo metálico que sujeta a un portaequipajes de plástico?

**Soluciones**

1. 71,25 / 28,4 = **2,51 m**.
2. 71,25 / 433 = 0,165 m: **16,5 cm**.
3. **Añadir radiales.** Con dos, el plano de tierra es muy pobre y buena parte de la potencia se pierde en el suelo.
4. Unos **36 Ω**, la mitad de los 73 Ω del dipolo, porque es medio dipolo.
5. Tienen **polarizaciones cruzadas**: una vertical y otra horizontal. En comunicación directa eso supone una pérdida de señal muy grande. Deberían usar las dos la misma polarización.
6. Porque el techo metálico hace de plano de tierra. Sobre el plástico la antena se queda sin espejo.

## En una frase

La vertical de cuarto de onda es medio dipolo puesto de pie sobre un plano de tierra que hace de espejo: mide 71,25 / f, presenta unos 36 Ω, radia por igual hacia todo el horizonte con polarización vertical, y rinde lo que rinda su plano de tierra.

El dipolo y la vertical reparten la energía con bastante generosidad hacia muchos lados. La lección siguiente trata de lo contrario: antenas que la concentran en una sola dirección, y la palabra con la que se mide esa concentración.
