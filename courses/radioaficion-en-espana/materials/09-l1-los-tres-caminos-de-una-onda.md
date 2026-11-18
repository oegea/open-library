La noche de la vigilia, Marina oyó desde un local con goteras de Vallverd a un señor que hablaba desde La Plata, Argentina, a unos once mil kilómetros. Y sin embargo, un walkie como los del club, desde ese mismo local, no llega a un compañero que esté detrás de la sierra, a treinta.

Las dos cosas son radio, y las dos tienen explicación. La explicación se llama **propagación**: el estudio de por dónde va una onda desde que sale de una antena hasta que llega a otra. En esta lección verás que una onda dispone de tres caminos distintos, y que saber cuál usa cada banda es lo que separa a quien hace contactos de quien se pasa la tarde llamando en una banda cerrada.

Esa expresión va a salir mucho, así que conviene fijarla ya. Los aficionados dicen que una banda está **abierta** hacia un sitio cuando las ondas de esa banda están llegando hasta allí, y **cerrada** cuando no llegan, por mucha potencia que se ponga.

Al terminar sabrás nombrar los tres caminos, decir cuál domina en cada tipo de banda y calcular hasta dónde llega una antena de VHF según su altura.

## El problema: la Tierra es redonda y las ondas van rectas

Recuerda de la sección 6 que una onda de radio es de la misma familia que la luz, solo que de frecuencia mucho más baja. Y la luz, si nada la desvía, viaja en línea recta.

Eso crea un problema evidente. La Tierra es curva. Si las ondas de radio fueran siempre rectas, una antena solo podría comunicarse con lo que «ve»: más allá del horizonte, la onda seguiría recta, se separaría del suelo y se perdería en el espacio. No habría radio a larga distancia.

La hay porque existen tres mecanismos distintos que llevan la onda de un sitio a otro. Se llaman **onda de superficie**, **onda directa** y **onda ionosférica**. La primera y la tercera son las que consiguen llegar más allá del horizonte.

![Los tres caminos de una onda de radio. La onda de superficie avanza pegada al suelo y sigue la curva de la Tierra. La onda directa va en línea recta de antena a antena y termina en el horizonte. La onda ionosférica sube hasta la ionosfera, a cientos de kilómetros de altura, y regresa a tierra mucho más lejos.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s09-tres-caminos.svg)

## Primer camino: la onda de superficie

> **Onda de superficie (o de tierra):** la parte de la onda que avanza pegada al suelo y lo va siguiendo, curva incluida.

¿Por qué iba una onda a seguir la curva del suelo en vez de irse recta? Porque el suelo, y sobre todo el mar, conducen algo la electricidad, y la parte baja de la onda va induciendo pequeñas corrientes en él. Esas corrientes la frenan un poco por abajo, y una onda frenada por abajo se inclina hacia el suelo. Imagina una fila de personas que avanza cogida del brazo: si las de un extremo pisan barro y van más despacio, la fila entera gira hacia ese lado. El frente de la onda hace lo mismo, y el resultado es que se queda «agarrada» a la superficie. (Guarda la imagen de la fila: volverá en la lección siguiente.)

Ese agarre tiene un precio: las corrientes que la onda induce en el suelo son energía que pierde. La onda de superficie se va gastando conforme avanza. Y lo importante para ti es **cuánto** se gasta según la frecuencia:

> **Cuanto más baja es la frecuencia, mejor funciona la onda de superficie.** Cuanto más alta, antes se agota.

- En **onda media** (las emisoras de AM de toda la vida, en torno a 1 MHz), la onda de superficie cubre cientos de kilómetros. Es el camino normal de esas emisoras durante el día.
- En la banda de **160 metros** (1,8 MHz), la más baja de las de aficionado, da para distancias medias.
- En las bandas altas de HF (14, 21, 28 MHz), se agota en unas pocas decenas de kilómetros.
- En VHF y UHF, prácticamente no existe.

Sobre el mar llega bastante más lejos que sobre tierra seca, porque el agua salada conduce mucho mejor. Por eso la radio marítima nació en frecuencias bajas.

## Segundo camino: la onda directa

> **Onda directa:** la que viaja en línea recta de una antena a otra, como la luz de un faro. También se la llama propagación «en línea de vista».

Es el camino más simple y es el camino normal de **VHF y UHF**: las bandas de 2 metros (145 MHz) y 70 centímetros (435 MHz), las de los walkies y los repetidores.

Una onda directa llega hasta donde llega la vista desde la antena, es decir, hasta el **horizonte**. Y la distancia al horizonte depende de una sola cosa: la altura.

—Entonces —dijo Lucía, mirando el walkie del club—, ¿si le meto más potencia no llego más lejos?

—Si el otro está detrás del horizonte, no —contestó Dani—. Puedes poner toda la potencia que la ley permite: la onda pasará por encima de su cabeza, recta hacia el espacio. La potencia sirve para que te oigan más fuerte los que ya te veían. Para que te vean más, lo que tienes que hacer es subir.

Esa es la regla práctica más importante de VHF y UHF:

> **En VHF y UHF, la altura de la antena importa más que la potencia.**

Por eso los repetidores se instalan en las cumbres, y por eso con un walkie de 5 vatios desde lo alto de una montaña se habla con media provincia, y con el mismo walkie desde el fondo de un valle, con nadie.

### Cuánto alcanza: la cuenta del horizonte

Hay una fórmula sencilla para estimar el alcance de la onda directa:

**distancia (en km) = 4,12 × √h**

donde **h** es la altura de la antena **en metros**, medida sobre el terreno que la rodea (no sobre el nivel del mar). El símbolo √ es la raíz cuadrada: el número que, multiplicado por sí mismo, da el de dentro (√25 = 5, porque 5 × 5 = 25).

Antes de usarla, dos observaciones sobre lo que dice:

- La raíz cuadrada significa que el alcance **no crece al mismo ritmo que la altura**. Para llegar el doble de lejos no basta con subir el doble: hay que subir cuatro veces más. Las primeras decenas de metros son las que más rinden.
- El 4,12 ya incluye un regalo de la atmósfera. El horizonte que ven los ojos sale de la misma fórmula con un 3,57. Las ondas de radio llegan un 15 % más lejos porque el aire, más denso abajo que arriba, las curva ligeramente hacia el suelo. A ese horizonte ampliado se le llama **horizonte radioeléctrico**.

**Ejemplo.** *Una antena está a 9 metros de altura. ¿Hasta dónde alcanza su onda directa?*

- √9 = 3.
- Distancia = 4,12 × 3 = **12,4 km**, aproximadamente.

Si la otra estación también tiene su antena en alto, **se suman los dos horizontes**: cada antena «ve» hasta su horizonte, y las dos pueden hablarse si sus horizontes se tocan.

**Ejemplo.** *Una antena a 9 m habla con un repetidor situado en una cumbre, 900 m por encima del terreno que la rodea. ¿Qué distancia máxima pueden cubrir?*

- Horizonte de la primera: 4,12 × √9 = 4,12 × 3 = 12,4 km.
- Horizonte del repetidor: 4,12 × √900 = 4,12 × 30 = 123,6 km.
- Suma: 12,4 + 123,6 = **136 km**.

Es una estimación para terreno llano: una montaña en medio corta el camino antes, y hay fenómenos que lo alargan después, como verás al final de la sección. Pero el orden de magnitud es ese, y explica por qué un repetidor bien situado cubre una provincia entera.

Junto a la onda directa suele llegar otra, **reflejada en el suelo** entre las dos antenas. Las dos recorren caminos de distinta longitud, y según lleguen en fase o en oposición de fase (sección 3) se refuerzan o se debilitan. Es una de las razones de que, en VHF, mover el walkie medio metro cambie a veces la señal de mala a buena. Al conjunto de la onda directa y la reflejada en el suelo, el temario del examen lo llama **onda espacial**.

Y la línea de vista no es un muro perfecto. Las ondas se **reflejan** en edificios y laderas, y se **difractan** —se doblan un poco— al rozar una arista, como el sonido que te llega desde detrás de una esquina. Por eso un walkie funciona dentro de una ciudad sin ver al otro, y por eso a veces se oye, débil, a alguien de detrás de un monte. Son ayudas pequeñas: no sustituyen a la altura.

## Tercer camino: la onda ionosférica

> **Onda ionosférica (o de cielo):** la que sube hacia el cielo, es devuelta hacia abajo por una región alta de la atmósfera llamada ionosfera, y cae a tierra a cientos o miles de kilómetros.

Es el camino de la **onda corta (HF)**, y el que explica La Plata. La onda no rodea la Tierra pegada al suelo ni la atraviesa: sube, a unos cientos de kilómetros de altura algo la dobla de vuelta hacia abajo, y aterriza muy lejos, al otro lado del horizonte. Si al caer rebota en el suelo o en el mar y vuelve a subir, el proceso se repite y la onda puede dar así la vuelta a medio planeta.

Qué es esa ionosfera, por qué devuelve unas ondas y otras no, y por qué de noche se comporta distinto que de día es el asunto de las tres lecciones siguientes. De momento quédate con dos cosas:

- Es un fenómeno de **HF** (de 3 a 30 MHz, más o menos). Las ondas de VHF y UHF normalmente atraviesan la ionosfera y se pierden en el espacio. Por eso sirven para hablar con satélites y por eso no sirven, salvo excepciones, para hablar con otro continente.
- No funciona siempre igual. Depende de la hora, de la estación del año y del sol. De ahí que la propagación se parezca más a la meteorología que a la electrónica: hay que aprender a leer el tiempo que hace allá arriba.

## Qué camino usa cada banda

| Bandas | Camino principal | Alcance típico |
|---|---|---|
| Onda media y 160 m (frecuencias bajas) | Onda de superficie; de noche se le suma la ionosférica (verás por qué al llegar a las capas de la ionosfera) | De decenas a cientos de km de día; mucho más de noche |
| HF: de 80 m a 10 m (3 a 30 MHz) | **Onda ionosférica** | De cientos a miles de km, según hora y banda |
| VHF y UHF: 2 m, 70 cm | **Onda directa** | El horizonte radioeléctrico: decenas de km, más desde sitios altos |

Con esta tabla se entiende la paradoja del principio. La Plata se oyó en 40 metros, una banda de HF, por onda ionosférica. Y el compañero de detrás de la sierra no se oye en el walkie porque en VHF manda la onda directa, y la sierra está en medio.

## Donde la gente se lía

- **«Con más potencia se llega más lejos.»** En VHF y UHF, casi nunca: se llega hasta el horizonte, tengas la potencia que tengas. En HF tampoco es la potencia la que decide: decide si la ionosfera está devolviendo esa frecuencia o no. Si la banda está cerrada, un kilovatio no la abre.
- **«Las ondas rodean la Tierra porque son ondas.»** Solo la onda de superficie sigue la curva, y solo sirve en frecuencias bajas. La larga distancia en HF no rodea nada: rebota arriba.
- **«La onda de superficie es la que va por dentro de la tierra.»** No. Va por el aire, pegada al suelo. El suelo solo la sujeta y le cobra energía.
- **«La ionosfera es un espejo.»** Es una imagen útil, y la usaremos, pero no es exacta: no hay ninguna superficie pulida allá arriba. La lección siguiente explica qué hay de verdad.

## Compruébalo tú

1. Una emisora de onda media se oye de día a 150 km. ¿Por qué camino llega la señal?
2. Colocas una antena de VHF en un mástil, a 16 m del suelo. ¿Cuál es, aproximadamente, su horizonte radioeléctrico?
3. Una estación con la antena a 4 m habla en 145 MHz con otra que tiene la antena a 25 m. ¿Qué distancia máxima cabe esperar en terreno llano?
4. Quieres duplicar el alcance en VHF de una antena que está a 10 m. ¿A qué altura tienes que ponerla?
5. Dos amigos intentan hablar en 145 MHz con una sierra entre ambos. Uno propone comprar un amplificador de 100 W. ¿Qué le dirías?
6. Una señal de 14 MHz llega de noche desde 3.000 km. ¿Por qué camino ha venido?

**Soluciones**

1. Por **onda de superficie**: es el camino normal de la onda media durante el día, y a esa frecuencia tan baja cubre cientos de kilómetros.
2. √16 = 4. Distancia = 4,12 × 4 = **16,5 km**, aproximadamente.
3. Horizonte de la primera: 4,12 × √4 = 4,12 × 2 = 8,2 km. Horizonte de la segunda: 4,12 × √25 = 4,12 × 5 = 20,6 km. Suma: **28,8 km**, aproximadamente.
4. A **40 m**: cuatro veces más alta. Compruébalo con la calculadora: a 10 m, √10 ≈ 3,16 y el alcance es de unos 13 km; a 40 m, √40 ≈ 6,32 y el alcance es de unos 26 km.
5. Que no lo compre. En VHF la onda va prácticamente recta y la sierra la corta: con 100 W la sierra sigue en medio. Lo que funciona es ganar altura (subir a un sitio desde el que se vean) o usar un repetidor situado en lo alto, que «ve» a los dos.
6. Por **onda ionosférica**. A 14 MHz la onda de superficie se agota en decenas de kilómetros, y 3.000 km están muy lejos del horizonte: solo ha podido llegar rebotando en la ionosfera.

## En una frase

Una onda puede ir pegada al suelo (onda de superficie, frecuencias bajas, distancias cortas y medias), en línea recta hasta el horizonte (onda directa, VHF y UHF, donde manda la altura) o subir y volver desde el cielo (onda ionosférica, HF, el mundo entero).

Falta saber qué hay allá arriba que devuelve las ondas. Dani lo llamó «un espejo borroso» y «un secante». En la lección siguiente le ponemos nombre y física.
