Cuando cerró la tapa de su transceptor, Vicente dijo una frase que parece una exageración de veterano: que aquel receptor, aunque fuera del año noventa y uno, escuchaba mejor que casi cualquier cosa que se fabrique hoy, «si sabes lo que le pides». Esta lección explica qué quería decir.

Al terminar sabrás leer la hoja de características de un receptor, cifra por cifra, y entenderás qué le ocurre a un receptor cuando le entran señales demasiado fuertes: un problema que no tiene que ver con oír lo débil ni con separar lo cercano, y que es justamente el que distingue a los equipos buenos de los que solo lo parecen en el anuncio.

## La hoja de características

Estas son las cifras que encontrarás en el manual de cualquier receptor o transceptor. Las tres primeras ya las conoces; la tabla solo las pone juntas.

| Característica | Qué mide | Cómo se da | Qué es bueno |
|---|---|---|---|
| **Sensibilidad** | La señal más débil utilizable | µV o dBm, para una relación señal/ruido dada | Cifra **baja**. En HF, casi todos van sobrados |
| **Selectividad** | El ancho de los filtros de FI | Hz o kHz | Que haya un filtro adecuado a cada modo: 2,4 kHz para SSB, 500 Hz para CW |
| **Rechazo de imagen** | Cuánto se atenúa la frecuencia imagen | dB | Cifra **alta** |
| **Estabilidad** | Cuánto puede desplazarse la frecuencia | partes por millón (se explican más abajo) | Cifra **baja** |
| **Rango dinámico** | La capacidad de oír lo débil junto a lo muy fuerte | dB | Cifra **alta**. Es la que distingue a los buenos |

Dos aclaraciones antes de ir a lo nuevo.

**Sobre la selectividad.** Un filtro real no corta en seco: sus bordes son rampas, más o menos empinadas. Por eso su ancho se da siempre indicando dónde se ha medido: «2,4 kHz a −6 dB» quiere decir que, entre los dos puntos donde la señal ya sale atenuada 6 dB, hay 2,4 kHz. Las hojas serias dan una segunda medida mucho más abajo («4 kHz a −60 dB»). Cuanto más se parezcan las dos cifras, más empinadas son las rampas y mejor separa el filtro.

**Sobre la estabilidad.** Se da en partes por millón, abreviado **ppm**. «1 ppm» significa que la frecuencia puede desviarse, como mucho, una millonésima de su valor. En 14 MHz, que son 14.000.000 Hz, una millonésima son 14 Hz: inapreciable. Los equipos lo consiguen con un **TCXO**, un oscilador de cristal que mide su propia temperatura y se corrige solo.

Queda la última fila, que es la importante.

## El tercer problema: lo fuerte

En la primera lección de esta sección el problema era oír a un amigo que susurra en un bar. El **rango dinámico** mide algo más difícil: oírle susurrar mientras, a tu lado, alguien toca un bombo.

Un receptor recibe a la vez señales diminutas y señales enormes. Sus primeras etapas, el amplificador de RF y el mezclador, están pensadas para tratar cada señal de antena **por separado**: el amplificador las copia más grandes, y el mezclador combina cada una con el oscilador local, no unas con otras. Eso se cumple mientras las señales son pequeñas. Pero esas etapas, como todo circuito, tienen un tope. Si una señal muy fuerte las lleva cerca de él, empiezan a deformar lo que pasa por ellas.

—Y un circuito que deforma… —empezó Vicente.

—…mezcla —terminó Marina—. Lo dijiste con el diodo: cuando una onda la deforma otra frecuencia, salen sumas y diferencias.

—Pues eso mismo, pero aquí nadie se lo ha pedido. Las señales de antena se ponen a mezclarse entre sí.

> **Rango dinámico:** la diferencia, en decibelios, entre la señal más débil que un receptor puede oír y la más fuerte que soporta sin empezar a deformar. Cuanto mayor, mejor aguanta las señales fuertes.

Lo que ocurre cuando ese margen se supera tiene tres nombres, según el síntoma.

## Intermodulación: señales que no existen

> **Intermodulación:** aparición, dentro del propio receptor, de señales que no existen en el aire, fabricadas al mezclarse entre sí dos o más señales muy fuertes en unas etapas que han empezado a deformar.

Esas señales fantasma no aparecen en cualquier sitio. Se puede calcular dónde, con dos cosas que ya sabes. Llama A y B a las frecuencias de las dos señales fuertes.

1. Un circuito que deforma una onda fabrica sus armónicos. De la señal A sale, entre otros, su segundo armónico: **2 × A**. Está lejísimos, al doble de frecuencia, y por sí solo no molesta.
2. Pero ese mismo circuito, como está deformando, también mezcla: combina ese 2 × A con la otra señal, B, y entrega su diferencia: **2 × A − B**. Y esa diferencia cae justo al lado de las señales originales.

Lo mismo ocurre cambiando los papeles: **2 × B − A**.

**Ejemplo.** Dos emisoras muy fuertes en 7.200 y 7.210 kHz. Los fantasmas aparecen en:

- 2 × 7.200 − 7.210 = 14.400 − 7.210 = **7.190 kHz**
- 2 × 7.210 − 7.200 = 14.420 − 7.200 = **7.220 kHz**

![Un eje de frecuencias. En el centro, dos señales muy fuertes en 7.200 y 7.210 kilohercios, separadas 10 kilohercios. A cada lado, a 10 kilohercios de distancia, una señal más pequeña dibujada con trazo discontinuo, en 7.190 y en 7.220 kilohercios: son los productos de intermodulación, que no existen en el aire y se han fabricado dentro del receptor.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-intermodulacion.svg)

Fíjate en la regla que sale del dibujo: los fantasmas aparecen **a los dos lados de la pareja, a la misma distancia que separa a las dos señales fuertes**. Si estabas intentando oír una estación débil en 7.190 kHz, tienes encima una señal que no existe fuera de tu receptor. De noche, en la banda de 40 metros, con las grandes emisoras de radiodifusión al lado, esto es el pan de cada día.

## Bloqueo y modulación cruzada

Los otros dos síntomas no necesitan dos señales fuertes: basta una.

- **Desensibilización**, o **bloqueo.** Mientras la señal fuerte está presente, el receptor «se encoge»: las señales débiles bajan de volumen o desaparecen, y vuelven en cuanto la fuerte calla. Es típico cuando un vecino radioaficionado transmite cerca de tu frecuencia.
- **Modulación cruzada.** La señal fuerte está modulada, y su modulación se oye de fondo encima de la estación que estás escuchando, aunque estén en frecuencias distintas. La modulación de una ha «cruzado» a la otra dentro de tu receptor.

## El remedio va contra la intuición: amplificar menos

Los receptores tienen un **atenuador**: un mando que reduce todo lo que entra por la antena, normalmente 10 o 20 dB. Y muchos tienen un *preamplificador*, un amplificador de RF adicional a la entrada, que se puede apagar.

Parece absurdo debilitar a propósito lo que cuesta tanto recibir, pero funciona por dos razones:

- Al reducir la entrada, las señales fuertes dejan de llevar las primeras etapas a su tope, y los fantasmas desaparecen. Además desaparecen mucho más deprisa de lo que baja todo lo demás: en su fabricación intervienen tres factores (una señal dos veces y la otra una), y cada uno de los tres baja 10 dB; por eso, por cada 10 dB que atenúas la entrada, los productos de intermodulación bajan unos 30 dB.
- La señal que querías oír baja 10 dB, sí, pero el ruido de la banda baja otros 10. En HF, donde manda el ruido que entra por la antena, la relación señal/ruido se queda como estaba.

De ahí sale una prueba muy útil para saber si una señal es real o es un fantasma: pon el atenuador de 10 dB. Si la señal baja lo mismo que las demás, venía del aire. Si baja muchísimo más o desaparece, se estaba fabricando dentro del receptor.

Y esto es lo que quería decir Vicente. Un receptor veterano bien diseñado, con un buen mezclador y buenos filtros, puede tener más rango dinámico que uno moderno y barato que anuncia una sensibilidad espectacular. En una banda vacía, el segundo parece mejor. En una banda llena de señales fuertes, el primero sigue oyendo y el segundo se llena de fantasmas. «Si sabes lo que le pides» significa esto: no le pidas más amplificación de la que la banda necesita.

## Donde la gente se lía

- **«El mejor receptor es el más sensible.»** En HF casi todos tienen sensibilidad de sobra. Lo que los diferencia es el rango dinámico y la calidad de los filtros.
- **«Si oigo señales raras, necesito más amplificación.»** Al revés: atenúa. La intermodulación nace de que al receptor le entra demasiado.
- **Confundir intermodulación con frecuencia imagen.** La imagen es *una* señal real, lejana en frecuencia, que se cuela por estar al otro lado del oscilador local. La intermodulación son señales *inexistentes*, fabricadas dentro del receptor por dos señales fuertes.
- **Confundir bloqueo con falta de sensibilidad.** Un receptor bloqueado oye perfectamente en cuanto calla la señal fuerte. No es sordo: está deslumbrado.
- **«Un filtro de FI más estrecho arregla la intermodulación.»** No, porque el fantasma se fabrica antes, en las primeras etapas, y llega al filtro de FI justo en la frecuencia que el filtro deja pasar.

## Compruébalo tú

1. Dos estaciones muy fuertes transmiten en 14.250 y 14.270 kHz. ¿En qué dos frecuencias aparecerán los productos de intermodulación más molestos en un receptor que no las soporta?
2. Oyes una señal extraña. Pones el atenuador de 10 dB y la señal desaparece por completo, mientras las demás solo bajan un poco. ¿Qué era?
3. Cada vez que tu vecino radioaficionado pulsa el micrófono, las señales débiles que estabas escuchando, a 20 kHz de su frecuencia, se hunden. Cuando suelta, vuelven. ¿Cómo se llama ese efecto?
4. Mientras escuchas una conversación en 7.150 kHz, se oye de fondo la música de una emisora de radiodifusión potentísima que emite en 7.300 kHz. ¿Qué fenómeno es?
5. Un oscilador tiene una estabilidad de 2 ppm. ¿Cuántos hercios puede desviarse, como mucho, en 28 MHz?
6. Dos filtros de SSB miden los dos 2,4 kHz a −6 dB. A −60 dB, uno mide 3,6 kHz y el otro 7 kHz. ¿Cuál separa mejor a una estación fuerte vecina?
7. En una banda muy ruidosa pones el atenuador de 10 dB. ¿Qué le pasa a la relación señal/ruido de la estación que escuchas?

**Soluciones**

1. 2 × 14.250 − 14.270 = 28.500 − 14.270 = **14.230 kHz**, y 2 × 14.270 − 14.250 = 28.540 − 14.250 = **14.290 kHz**. Están a 20 kHz a cada lado de la pareja, que es justo lo que las separa.
2. Un **producto de intermodulación**: un fantasma fabricado dentro del receptor. Una señal real habría bajado 10 dB como las demás.
3. **Desensibilización** o **bloqueo**: una sola señal muy fuerte lleva las primeras etapas a su tope y el receptor pierde sensibilidad mientras dura.
4. **Modulación cruzada**: la modulación de una señal muy fuerte aparece encima de otra señal, en otra frecuencia.
5. 28 MHz son 28.000.000 Hz. Una millonésima son 28 Hz; dos, **56 Hz**.
6. El de **3,6 kHz**: sus bordes son más empinados, así que a poca distancia de su ventana ya atenúa muchísimo. El otro todavía deja pasar algo de lo que hay a 3 kHz del centro.
7. Prácticamente **nada**: bajan 10 dB la señal y también el ruido de la banda que la acompaña, de modo que la proporción entre los dos no cambia. Solo empeoraría si el ruido de la banda fuese ya tan bajo como el del propio receptor.

## En una frase

De un receptor importan, además de la sensibilidad, la selectividad y la estabilidad, su rango dinámico: lo bien que soporta señales muy fuertes sin fabricar fantasmas (intermodulación), sin ensordecer (bloqueo) y sin pegar una modulación a otra (modulación cruzada); y cuando ocurre, el remedio es atenuar.

Hasta aquí, el camino de la antena al altavoz. Queda recorrerlo en sentido contrario: de tu voz a la antena.
