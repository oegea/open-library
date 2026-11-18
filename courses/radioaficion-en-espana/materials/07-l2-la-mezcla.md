La lección anterior terminó en un callejón: un filtro muy estrecho no se puede hacer móvil. La salida que propuso Vicente fue no mover el filtro, sino la señal. Suena a truco de ilusionista: ¿cómo se le cambia la frecuencia a una emisora que está a mil kilómetros?

No se le cambia a la emisora, claro. Se le cambia a la copia de su señal que corre por dentro del receptor. La pieza que lo hace se llama **mezclador**, y aquel fue precisamente el bloque que se estropeó en el transceptor de Vicente y que él y Amparo tardaron tres tardes en encontrar. Al terminar esta lección sabrás qué entra en un mezclador, qué sale de él y por qué lo que sale sigue llevando el mensaje intacto.

## Algo que ya has oído: el batido

En la sección 6, al hablar del morse, apareció el **batido**. Recuérdalo con sonido. Si dos instrumentos dan a la vez dos notas casi iguales, una de 440 Hz y otra de 444 Hz, no oyes dos notas: oyes una sola que sube y baja de volumen cuatro veces por segundo, como un vibrato lento. Los músicos afinan así: cuando el vaivén desaparece, las dos notas coinciden.

¿De dónde salen esas cuatro veces por segundo? De la **diferencia**: 444 − 440 = 4. Las dos ondas van casi a la par; a ratos coinciden sus crestas y se refuerzan, a ratos coincide la cresta de una con el valle de la otra y se anulan. Cuanto más distintas son las dos frecuencias, más rápido es ese vaivén.

Quédate con la idea, porque es la semilla de todo lo que sigue: **cuando se juntan dos frecuencias, aparece un ritmo nuevo que vale la diferencia entre ellas.**

## Sumar no es mezclar

Hay que deshacer una confusión antes de continuar, porque la palabra «mezclar» engaña.

En una mesa de mezclas de sonido, mezclar es **sumar**: entra la guitarra, entra la voz, y sale la guitarra más la voz. Cada una sigue siendo lo que era. Si a la salida pones un filtro que solo deje pasar las frecuencias de la voz, recuperas la voz. No se ha creado ninguna frecuencia que no estuviera ya.

Así se comportan los cables, las resistencias, los condensadores, las bobinas y los amplificadores que trabajan sin forzar: por ellos pueden pasar mil señales a la vez sin que ninguna se entere de las demás. A los circuitos que se comportan así se les llama **lineales**: su salida es una copia fiel de la entrada, más grande o más pequeña, pero con la misma forma.

—Un momento —dijo Marina—. Las dos notas de antes, la de 440 y la de 444, solo se suman en el aire. Y aparecía un vaivén de 4 Hz. ¿Eso no es una frecuencia nueva?

—No lo es, y la diferencia importa —dijo Vicente—. En esa suma lo único que hay son las dos notas de siempre. El vaivén es solo la manera en que su tamaño conjunto crece y mengua. Si pusieras un filtro que dejara pasar únicamente 4 Hz, a su salida no habría nada. Para que ese vaivén se convierta en una señal de 4 Hz de verdad hace falta algo que responda al tamaño y no a cada nota por separado. En tu oído lo hay. En un cable, no.

Ese «algo» es el mezclador de radio: un circuito construido a propósito para que las dos señales que le entran **actúen la una sobre la otra**, y de esa interacción salen frecuencias que no estaban en ninguna de las dos. A los circuitos que deforman lo que les entra, y que por eso fabrican frecuencias nuevas, se les llama **no lineales**. Ya conoces dos ejemplos: el diodo, que deja pasar la corriente en un solo sentido, y el amplificador saturado, que recorta las crestas. De hecho, el mezclador más sencillo que existe es un simple diodo.

—¿Y qué hace exactamente con las dos señales? —preguntó Marina.

—Piensa en el diodo como en una puerta —dijo Vicente—. Una de las dos señales, la más fuerte, la abre y la cierra a su ritmo: millones de veces por segundo. La otra señal solo puede pasar cuando la puerta está abierta, así que sale troceada. Trocear una señal es multiplicarla por otra que vale uno, cero, uno, cero… Por eso se dice que un mezclador *multiplica* las dos señales.

Y una onda troceada ya no tiene la forma que tenía. Recuerda de la sección 3 qué le pasa a una onda cuando se deforma: aparecen en ella frecuencias que antes no estaban. Cuando una onda se deforma por sí sola, como en un amplificador saturado, las frecuencias nuevas son sus múltiplos, los armónicos. Cuando lo que la deforma es una **segunda frecuencia**, aparecen además dos muy concretas: la suma y la diferencia de las dos. Es el mismo fenómeno, y volverás a encontrarlo más adelante en esta sección, cuando ocurra sin que nadie lo haya pedido.

## Lo que sale de un mezclador

> **Mezclador:** circuito al que entran dos señales de frecuencias distintas y del que salen dos señales nuevas: una cuya frecuencia es la **suma** de las dos de entrada, y otra cuya frecuencia es su **diferencia**.

Con números. Entran una señal de 7.100 kHz y otra de 16.100 kHz. (7.100 kHz es lo mismo que 7,1 MHz; en esta lección escribimos casi todo en kilohercios para que las sumas y las restas se vean mejor.) Salen:

- la suma: 16.100 + 7.100 = **23.200 kHz**
- la diferencia: 16.100 − 7.100 = **9.000 kHz**

(Para la diferencia se resta siempre la menor de la mayor: una frecuencia no puede ser negativa.)

En un mezclador real se cuelan además, más débiles, las dos señales originales y otras combinaciones. No importa, porque detrás del mezclador se pone siempre un **filtro** que deja pasar solo el producto que interesa y elimina todo lo demás. Mezclador y filtro van siempre juntos: uno fabrica las frecuencias nuevas y el otro elige.

![Esquema de un mezclador. Por la izquierda entra la señal de antena, de 7.100 kilohercios. Por abajo entra la señal del oscilador local, de 16.100 kilohercios. Del mezclador salen la suma, 23.200 kilohercios, y la diferencia, 9.000 kilohercios. Un filtro deja pasar solo la diferencia.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-mezclador.svg)

La diferencia es el batido que ya conocías. Con dos notas de 440 y 444 Hz, tu oído percibe un vaivén de 4 Hz; un mezclador es el circuito que convierte ese vaivén en una señal eléctrica de verdad, que se puede filtrar y amplificar. Y a todo este procedimiento de combinar dos frecuencias para obtener otra se le llama, con una palabra de origen griego, **heterodinar** (*hetero*, distinto; *dyne*, fuerza). De ahí viene el nombre del receptor que veremos en la lección siguiente.

## El oscilador local

De las dos señales que entran en el mezclador de un receptor, una viene de fuera y no la controlas: la de la antena. La otra la fabrica el propio receptor, con un oscilador como los de la sección 5.

> **Oscilador local (OL):** el oscilador del receptor que genera la segunda señal para el mezclador. Su frecuencia se puede variar, y es **lo que de verdad mueves cuando giras el dial**.

Se llama «local» porque está en tu casa, dentro del equipo, por oposición a la señal que llega de lejos. Y es la clave del asunto: como tú decides la frecuencia del oscilador local, tú decides cuánto vale la diferencia. Dicho de otra manera, puedes llevar cualquier señal a la frecuencia que te convenga.

**Ejemplo.** *Quieres llevar una señal de 3.700 kHz a 455 kHz. ¿A qué frecuencia pones el oscilador local?*

Tiene que cumplirse que la diferencia sea 455. Sirven dos valores:

- por encima de la señal: 3.700 + 455 = **4.155 kHz** (comprobación: 4.155 − 3.700 = 455)
- por debajo de la señal: 3.700 − 455 = **3.245 kHz** (comprobación: 3.700 − 3.245 = 455)

Las dos opciones funcionan, y cada diseño elige una. En este curso pondremos el oscilador local por encima de la señal, salvo que se diga otra cosa.

## Lo importante: el mensaje viaja intacto

Aquí está la objeción que Marina tardó diez segundos en hacer.

—Un momento. Me pasé el mes de mayo aprendiendo que la voz va metida en la señal: en la amplitud si es AM, en la frecuencia si es FM, en esa banda lateral de la SSB. Si ahora coges la señal y le cambias la frecuencia, ¿no estás destrozando justo eso?

—No, y es lo que hace que el invento funcione —dijo Vicente—. El mezclador no cambia cada frecuencia a su antojo. Las desplaza todas la misma cantidad. Es como un convoy de camiones que cambia de carril en la autopista: cada camión conserva su distancia con el de delante.

—Pero en mayo aprendí que sumarle 200 Hz a todos los tonos de una voz la convertía en un pato.

—A los tonos del *sonido*, sí. Aquí todavía no hay sonido: hay una señal de radio, y en ella el mensaje no está en la frecuencia de cada pieza, sino en la *distancia* de cada pieza a la portadora, o al sitio donde la portadora estaría. Esas distancias no cambian. El sonido se reconstruye al final del receptor, restando; y solo si esa última resta se hace mal aparece el pato.

Compruébalo con números. En la sección 6 viste que una señal de AM con un tono de 1 kHz son tres frecuencias: la portadora y dos bandas laterales, a 1 kHz por encima y por debajo. Pon la portadora en 7.100 kHz y el oscilador local en 16.100 kHz:

| | En la antena | Cuenta | Tras el mezclador |
|---|---|---|---|
| Banda lateral inferior | 7.099 kHz | 16.100 − 7.099 | 9.001 kHz |
| Portadora | 7.100 kHz | 16.100 − 7.100 | 9.000 kHz |
| Banda lateral superior | 7.101 kHz | 16.100 − 7.101 | 8.999 kHz |

Antes había una portadora con dos acompañantes a 1 kHz de distancia. Después hay una portadora con dos acompañantes a 1 kHz de distancia. El dibujo es el mismo; solo se ha mudado de sitio en el dial. La amplitud de cada pieza se conserva en proporción, así que la voz sigue ahí.

Mira la tabla con atención y verás un detalle curioso: la que estaba arriba ha quedado abajo. Cuando el oscilador local está por encima de la señal, el dibujo sale del mezclador **del revés**, como en un espejo. No es ningún problema: quien diseña el equipo lo sabe y lo tiene en cuenta (y una segunda mezcla hecha de la misma manera lo vuelve a poner del derecho). Pero conviene saberlo para que no te sorprenda.

> **Mezclar es trasladar.** Una señal sale del mezclador en otra frecuencia, pero con su ancho, su forma y su mensaje intactos.

Esta es la herramienta que faltaba. Con ella ya se puede llevar cualquier emisora, esté donde esté, hasta el sitio donde espera el filtro bueno.

## Un viejo conocido

Si repasas la sección 6, verás que ya habías usado un mezclador sin llamarlo así. El BFO que hacía audible el morse era esto mismo: una portadora que dentro del receptor está en 9.000 kHz, mezclada con un oscilador situado 800 Hz más arriba, da una diferencia de 800 Hz: un tono que cae dentro de lo que el oído percibe. Y la «reinserción de portadora» que convertía la SSB en voz es otra mezcla de la misma familia.

En radio, casi todo lo que no es amplificar o filtrar es mezclar.

## Donde la gente se lía

- **«Mezclar es juntar dos señales en un mismo cable.»** Eso es sumar, y no crea nada nuevo. Un mezclador las hace interactuar, y por eso aparecen la suma y la diferencia.
- **«Del mezclador sale solo la diferencia.»** Salen las dos, suma y diferencia. La que no interesa la quita el filtro que va detrás.
- **«Al cambiar la frecuencia se estropea la modulación.»** No: todo se desplaza lo mismo, y las distancias dentro de la señal no cambian.
- **«El dial mueve siempre un filtro.»** En los receptores antiguos de la lección anterior, sí. En los que veremos a continuación, el dial mueve el oscilador local.

## Compruébalo tú

1. En un mezclador entran 10.000 kHz y 10.455 kHz. ¿Qué dos frecuencias nuevas salen?
2. Afinas una cuerda de guitarra comparándola con un diapasón de 440 Hz, y oyes que el sonido sube y baja de volumen dos veces por segundo. ¿En qué frecuencias puede estar vibrando la cuerda?
3. Quieres llevar una señal de 21.300 kHz a una frecuencia de 9.000 kHz, con el oscilador local por encima de la señal. ¿A qué frecuencia lo pones?
4. Con ese mismo oscilador local, una señal de SSB ocupa en la antena de 21.300 a 21.303 kHz. ¿Qué franja ocupa a la salida del mezclador, si te quedas con la diferencia? ¿Ha cambiado su ancho?
5. Un amigo dice que ha «mezclado» dos señales uniendo dos cables con una regleta. ¿Saldrán de ahí la suma y la diferencia?
6. Para oír una señal de morse que dentro del receptor está en 455,0 kHz se usa un BFO. ¿A qué frecuencia hay que ponerlo para que el tono suene a 700 Hz?

**Soluciones**

1. La suma, 10.000 + 10.455 = **20.455 kHz**, y la diferencia, 10.455 − 10.000 = **455 kHz**.
2. El vaivén vale la diferencia entre las dos frecuencias, así que la cuerda está a 2 Hz del diapasón: en **438 Hz** o en **442 Hz**. El batido no dice hacia qué lado; para saberlo hay que tensar un poco la cuerda y ver si el vaivén se hace más lento o más rápido.
3. La diferencia tiene que ser 9.000 y el oscilador va por encima: 21.300 + 9.000 = **30.300 kHz**.
4. 30.300 − 21.300 = 9.000 y 30.300 − 21.303 = 8.997. Ocupa **de 8.997 a 9.000 kHz**. El ancho sigue siendo de **3 kHz**; solo se ha trasladado (y ha quedado del revés, porque el oscilador está por encima).
5. No. Una regleta es un circuito lineal: las dos señales se suman y siguen siendo las mismas dos. Si sus frecuencias son parecidas, la suma tendrá un vaivén de tamaño, pero ningún filtro encontrará ahí una señal en la frecuencia diferencia. Para que aparezcan frecuencias nuevas hace falta un elemento no lineal, como un diodo.
6. 700 Hz son 0,7 kHz. El BFO debe estar a esa distancia de la señal: en **455,7 kHz** (o en 454,3 kHz).

## En una frase

Un mezclador combina la señal de antena con la de un oscilador local y entrega su suma y su diferencia; eligiendo una con un filtro, la señal queda trasladada a otra frecuencia con su mensaje intacto.

Ya tenemos la herramienta. En la lección siguiente la usamos para montar, bloque a bloque, el receptor que lleva un siglo sin rival.
