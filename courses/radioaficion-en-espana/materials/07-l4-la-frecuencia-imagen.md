El superheterodino resuelve el problema de la selectividad con una elegancia que ha durado un siglo. Pero no sale gratis. Tiene un punto débil propio, que no existía en los receptores anteriores, y Vicente no dejó que Marina se fuera a casa sin conocerlo: «Si en el examen te preguntan una sola cosa de receptores, será esta».

Al terminar esta lección sabrás qué es la **frecuencia imagen**, calcularla en diez segundos y explicar las dos maneras de combatirla, incluida la doble conversión.

## El mezclador no distingue por qué lado le llega

Vuelve al receptor de la lección anterior: frecuencia intermedia de 9 MHz, oscilador local por encima de la señal. Para escuchar 7,1 MHz, el oscilador local está en 16,1 MHz, y la diferencia es 16,1 − 7,1 = 9 MHz.

Ahora hazte una pregunta incómoda. El mezclador entrega la diferencia entre el oscilador local y lo que le entre. ¿Hay alguna *otra* frecuencia que, restada con 16,1, dé también 9?

La hay. Una señal que esté 9 MHz **por encima** del oscilador local:

16,1 + 9 = 25,1 MHz → y la diferencia es 25,1 − 16,1 = **9 MHz**

Al mezclador le da igual que la señal esté 9 MHz por debajo del oscilador o 9 MHz por encima. En los dos casos la diferencia vale 9 MHz, y en los dos casos lo que sale entra limpiamente en el taller de frecuencia intermedia. Si en 25,1 MHz hay una emisora fuerte, la oirás encima de la de 7,1 MHz, como una intrusa, y **ningún filtro de frecuencia intermedia podrá separarlas**, porque después del mezclador las dos están exactamente en la misma frecuencia.

> **Frecuencia imagen:** la segunda frecuencia, distinta de la deseada, que al mezclarse con el oscilador local produce también la frecuencia intermedia y por tanto se cuela en el receptor.

## El espejo

El nombre no es casual, y el espejo es la mejor manera de recordarlo. Dibuja las frecuencias sobre una regla:

![Una regla de frecuencias con tres marcas. A la izquierda, la señal deseada en 7,1 megahercios. En el centro, el oscilador local en 16,1 megahercios. A la derecha, la frecuencia imagen en 25,1 megahercios. La deseada y la imagen están las dos a 9 megahercios del oscilador local, una a cada lado, como un objeto y su reflejo en un espejo. Entre la deseada y la imagen hay 18 megahercios, el doble de la frecuencia intermedia.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-frecuencia-imagen.svg)

El oscilador local es el espejo. La señal deseada está a un lado, a una distancia igual a la frecuencia intermedia. La imagen está al otro lado, a la misma distancia. Y como hay una FI de la deseada al espejo y otra FI del espejo a la imagen, entre la deseada y la imagen hay **dos veces la frecuencia intermedia**.

De ahí salen las dos fórmulas que necesitas, según dónde esté el oscilador local:

| Si el oscilador local está… | La imagen está en… |
|---|---|
| **por encima** de la señal deseada | señal deseada **+ 2 × FI** |
| **por debajo** de la señal deseada | señal deseada **− 2 × FI** |

No hace falta memorizarlas como dos reglas. Basta el dibujo: la imagen siempre está **al otro lado del oscilador local, a la misma distancia**.

**Ejemplo 1.** *Un receptor con FI de 9 MHz recibe 21,3 MHz con el oscilador local en 30,3 MHz. ¿Cuál es su frecuencia imagen?*

- El oscilador (30,3) está por encima de la señal (21,3). La imagen está al otro lado del oscilador, 9 MHz más arriba.
- Imagen = 30,3 + 9 = **39,3 MHz**.
- Comprobación con la otra fórmula: 21,3 + 2 × 9 = 21,3 + 18 = 39,3 MHz. Coincide.

**Ejemplo 2.** *Un receptor con FI de 455 kHz recibe 3.650 kHz con el oscilador local en 4.105 kHz. ¿Cuál es su frecuencia imagen?*

- Imagen = 4.105 + 455 = **4.560 kHz**.
- Comprobación: 3.650 + 2 × 455 = 3.650 + 910 = 4.560 kHz.

## Cómo se combate (1): el filtro de entrada

—Si después del mezclador ya no se pueden separar —dijo Marina—, habrá que pararla antes.

—Eso es. Y ya conoces a quien la para: es la primera caja del plano.

El **filtro de entrada**. En la lección anterior quedó pendiente su segunda misión, y es esta: dejar pasar la banda de la señal deseada y **rechazar la frecuencia imagen antes de que llegue al mezclador**. Si la imagen no entra en el mezclador, no hay intrusa.

En el receptor con el que hemos abierto la lección lo tiene fácil: la deseada está en 7,1 MHz y la imagen en 25,1 MHz, a 18 MHz de distancia. Un filtro paso banda sencillo, centrado en 7 MHz, deja pasar una y aplasta a la otra sin esfuerzo. A esa capacidad del receptor se le llama **rechazo de imagen**, y se mide en decibelios: cuantos más, mejor.

## Cómo se combate (2): una frecuencia intermedia alta

Mira ahora el receptor del ejemplo 2, el de la FI de 455 kHz: su imagen queda a solo 910 kHz de la deseada. En 3.650 kHz todavía se puede separar. Pero lleva ese mismo receptor a la banda de 10 metros: deseada en 28.500 kHz, imagen en 28.500 + 910 = 29.410 kHz. La imagen está a un 3 % de distancia de la deseada, y además cae **dentro de la misma banda de radioaficionados**. El filtro de entrada, que tiene que ser ancho para dejar pasar la banda, no puede hacer nada.

De aquí sale la segunda arma: **elegir una frecuencia intermedia alta.** Como la imagen está a dos veces la FI, cuanto mayor sea la FI, más lejos cae la imagen y más fácil es filtrarla.

| FI | Distancia entre la deseada y su imagen |
|---|---|
| 455 kHz | 910 kHz |
| 9 MHz | 18 MHz |
| 45 MHz | 90 MHz |

Pero una FI alta tiene su contrapartida, y ya la conoces de la primera lección: cuanto más alta es la frecuencia, más difícil es hacer en ella un filtro estrecho. A 9 MHz los cristales de cuarzo todavía dan filtros de 500 Hz; a 45 o a 70 MHz ya no. De modo que el diseñador tira de una manta corta:

- una FI **alta** aleja la imagen, pero complica el filtro estrecho;
- una FI **baja** facilita el filtro estrecho, pero acerca la imagen.

### La doble conversión: las dos cosas a la vez

La solución es no elegir. Se mezcla **dos veces**:

1. Una primera mezcla, con el oscilador local variable, lleva la señal a una **primera FI alta**. Su misión es alejar la imagen.
2. Una segunda mezcla, con un segundo oscilador local de frecuencia **fija**, baja la señal de esa primera FI a una **segunda FI baja**. Allí están los filtros estrechos que dan la selectividad.

Con números. Quieres escuchar 7.100 kHz en un receptor con una primera FI de 45.000 kHz y una segunda de 455 kHz:

| Paso | Cuenta | Resultado |
|---|---|---|
| Primer oscilador local (variable) | 7.100 + 45.000 | 52.100 kHz |
| Primera FI | 52.100 − 7.100 | **45.000 kHz** |
| Imagen de la primera mezcla | 52.100 + 45.000 | 97.100 kHz: lejísimos, la quita un filtro de entrada muy sencillo |
| Segundo oscilador local (fijo) | 45.000 + 455 | 45.455 kHz |
| Segunda FI | 45.455 − 45.000 | **455 kHz** |

—La segunda mezcla tendrá también su imagen, digo yo —apuntó Marina.

—La tiene: al otro lado del segundo oscilador, en 45.910 kHz, a 910 kHz de los 45.000. De ella se encarga un filtro colocado en la primera FI, entre los dos mezcladores. No hace falta que sea estrecho: le basta con dejar pasar los 45.000 y cortar los 45.910.

A esto se le llama receptor de **doble conversión**, y su cadena de bloques también la pide el examen:

> **Antena → filtro de entrada y amplificador de RF → primer mezclador (con el oscilador local variable) → filtro de primera FI → segundo mezclador (con el oscilador local fijo) → filtro de segunda FI → amplificador de FI → demodulador → amplificador de audio → altavoz.**

![Esquema de bloques de un receptor de doble conversión, de arriba abajo: antena; filtro de entrada y amplificador de radiofrecuencia, a 7.100 kilohercios; primer mezclador, al que llega el primer oscilador local, variable, en 52.100 kilohercios; filtro de primera frecuencia intermedia, a 45.000 kilohercios, que aleja la imagen; segundo mezclador, al que llega el segundo oscilador local, fijo, en 45.455 kilohercios; filtro de segunda frecuencia intermedia, a 455 kilohercios, donde está la selectividad; amplificador de frecuencia intermedia, demodulador y audio.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-doble-conversion.svg)

Es lo que llevan por dentro la mayoría de los transceptores de HF, también el de Vicente. En estas lecciones seguimos dibujándolo con una sola FI de 9 MHz porque el principio es idéntico y las cuentas salen más cortas.

## Donde la gente se lía

- **«La imagen está a una FI de la señal deseada.»** Está a **dos** veces la FI. A una FI de la deseada lo que hay es el oscilador local.
- **«La imagen se quita con el filtro de FI.»** Imposible: después del mezclador, deseada e imagen están en la misma frecuencia. Hay que quitarla **antes** del mezclador, con el filtro de entrada.
- **«La frecuencia imagen es un defecto de un receptor estropeado.»** Es una consecuencia inevitable del propio principio superheterodino. Todos la tienen; los buenos la rechazan mucho.
- **«Una FI alta es siempre mejor.»** Aleja la imagen, pero dificulta el filtrado estrecho. Por eso existe la doble conversión.

## Compruébalo tú

1. Un receptor tiene una FI de 9 MHz y recibe 7,05 MHz con el oscilador local por encima. ¿En qué frecuencia está el oscilador local? ¿Y la imagen?
2. Un receptor de VHF tiene una FI de 10,7 MHz y recibe 145,0 MHz con el oscilador local en 155,7 MHz. ¿Cuál es su frecuencia imagen?
3. Un receptor con FI de 9 MHz recibe 28,5 MHz con el oscilador local **por debajo**, en 19,5 MHz. ¿Cuál es su frecuencia imagen?
4. Dos receptores reciben la misma emisora de 14 MHz. Uno tiene una FI de 455 kHz y el otro de 9 MHz. ¿En cuál será más fácil rechazar la imagen, y por qué?
5. Un receptor capta una emisora de radiodifusión muy fuerte encima de la estación que quiere oír, y resulta ser su frecuencia imagen. Su dueño propone ponerle un filtro de FI más estrecho. ¿Servirá?
6. Un receptor de doble conversión tiene una primera FI de 45.000 kHz y una segunda de 455 kHz, con los dos osciladores por encima. ¿En qué frecuencia están el primer y el segundo oscilador local cuando se escucha 14.200 kHz?
7. ¿Por qué ese receptor usa una primera FI alta y una segunda FI baja, y no al revés?

**Soluciones**

1. Oscilador local: 7,05 + 9 = **16,05 MHz**. Imagen, al otro lado del oscilador: 16,05 + 9 = **25,05 MHz** (o bien 7,05 + 18).
2. Al otro lado del oscilador, a 10,7 MHz: 155,7 + 10,7 = **166,4 MHz** (o bien 145,0 + 2 × 10,7 = 145,0 + 21,4).
3. El oscilador está por debajo, así que la imagen está aún más abajo: 19,5 − 9 = **10,5 MHz** (o bien 28,5 − 18).
4. En el de **9 MHz**: su imagen está a 18 MHz de la deseada (en 32 MHz) y el filtro de entrada la elimina con facilidad. En el de 455 kHz está a solo 910 kHz (en 14,91 MHz), demasiado cerca.
5. No. La imagen llega a la FI exactamente en la misma frecuencia que la señal deseada, y ningún filtro de FI puede distinguirlas. Hay que mejorar el filtro de **entrada**, antes del mezclador.
6. Primero: 14.200 + 45.000 = **59.200 kHz**. El segundo es fijo y no depende de la emisora: 45.000 + 455 = **45.455 kHz**.
7. Porque cada FI hace lo que mejor se le da: la alta, primero, aleja la imagen para que el filtro de entrada pueda con ella; la baja, después, permite los filtros estrechos que dan la selectividad.

## En una frase

En un superheterodino hay siempre una segunda frecuencia, la imagen, situada al otro lado del oscilador local y a dos veces la FI de la señal deseada, que el mezclador no distingue; se elimina antes del mezclador con el filtro de entrada, y se aleja usando una FI alta o una doble conversión.

Ya conoces el plano del superheterodino, con una y con dos conversiones. Antes de aprender a juzgar un receptor, una lección corta para presentarte a sus dos parientes: uno más sencillo y otro más moderno.
