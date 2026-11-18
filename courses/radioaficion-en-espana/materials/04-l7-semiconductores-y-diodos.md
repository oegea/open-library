La cajita más pequeña de la lata de Amparo tenía la etiqueta más cariñosa: *diodos Ge (quedan 3, tesoro)*. Dentro había tres cilindritos de vidrio del tamaño de un grano de arroz largo, con una raya pintada en un extremo. «Una calle de sentido único para electrones», dijo Vicente. «Parece poca cosa. Sin esto no habría fuentes de alimentación, ni radios, ni una sola pantalla.»

Con el diodo entramos en la familia de los **semiconductores**, la que cambió el mundo en el siglo XX. Al terminar la lección sabrás qué tiene de especial el silicio, cómo se fabrica con él una pieza que solo conduce en un sentido, para qué sirve eso y qué son un LED, un zéner y un varicap.

## Un material que conduce a medias

En la sección 2 repartimos los materiales en conductores (con electrones libres), aislantes (sin ellos) y un tercer grupo que dejamos pendiente: los **semiconductores**. El más usado es el **silicio**, que se obtiene de la arena. Otro, más antiguo, es el **germanio**: el «Ge» de la etiqueta de Amparo.

Los átomos de un sólido se sujetan unos a otros compartiendo sus electrones más exteriores. En un cristal de silicio puro, cada átomo tiene cuatro electrones exteriores y los usa todos para agarrarse a sus cuatro átomos vecinos. No sobra ninguno. Casi no hay electrones libres, así que el silicio puro conduce muy mal: se parece mucho a un aislante.

Lo interesante es que eso se puede cambiar, y en la medida exacta que uno quiera, añadiendo al cristal una cantidad minúscula de átomos de otro tipo. A esa operación se le llama **dopar** el silicio. Hay dos maneras de hacerlo:

**Silicio tipo N.** Se añaden átomos que tienen *cinco* electrones exteriores (fósforo, por ejemplo). Cuatro se usan para agarrarse a los vecinos y el quinto queda suelto. Cada átomo añadido aporta un electrón libre. El cristal ahora conduce, gracias a esos electrones, que tienen carga negativa: de ahí la **N**.

**Silicio tipo P.** Se añaden átomos que solo tienen *tres* electrones exteriores (boro, por ejemplo). Les falta uno para agarrarse a los cuatro vecinos, y en ese sitio queda una vacante. A esa vacante se le llama **hueco**.

Un hueco se comporta de una manera curiosa. Un electrón del átomo de al lado puede saltar a ocuparlo, pero entonces deja un hueco donde él estaba, que a su vez ocupa otro electrón vecino… Piensa en una fila de butacas con una sola vacía: si cada persona se corre un asiento hacia la butaca libre, la gente se mueve hacia un lado y la butaca vacía «viaja» hacia el contrario. El hueco se mueve por el cristal como si fuera una partícula con carga positiva: de ahí la **P**.

> **Tipo N:** silicio con electrones libres de sobra (portadores negativos). **Tipo P:** silicio con huecos, que se comportan como portadores positivos.

Una aclaración que evita un malentendido muy común: ni el trozo N ni el trozo P están cargados eléctricamente. Los dos son neutros, porque los átomos añadidos traen tantos protones como electrones. Lo que cambia es qué tienen disponible para moverse.

## La unión PN

Por separado, un trozo N y un trozo P no son más que conductores mediocres. Lo extraordinario ocurre al fabricar un cristal que es P por un lado y N por el otro. A la frontera entre las dos zonas se le llama **unión PN**.

Justo en la frontera, los electrones libres del lado N que están más cerca saltan al lado P y rellenan los huecos que encuentran. El resultado es una franja finísima, a ambos lados de la frontera, que se ha quedado **sin electrones libres y sin huecos**. Sin nada que pueda moverse, esa franja es aislante. Es una barrera.

¿Por qué saltan solo los más cercanos y no siguen pasando todos? Porque cada electrón que cruza deja atrás, en el borde del lado N, un átomo al que ahora le falta un electrón (queda positivo), y coloca en el borde del lado P un electrón de más (queda negativo). Esas dos franjas cargadas empujan hacia atrás al siguiente electrón que quiera cruzar. Enseguida el rechazo es suficiente y el trasvase se detiene. El cristal entero sigue siendo neutro, pero en la frontera ha quedado un pequeño escalón de tensión: en el silicio, unos 0,7 V. Acuérdate de ese número, porque va a reaparecer.

Todo el comportamiento del diodo depende de qué le ocurre a esa barrera según cómo se le aplique la tensión.

**Con el positivo en el lado P y el negativo en el lado N.** El borne negativo empuja a los electrones del lado N hacia la frontera, y el positivo empuja a los huecos del lado P también hacia la frontera. La barrera se llena de portadores por los dos lados y se estrecha hasta desaparecer. Electrones y huecos se encuentran en la frontera y se van emparejando, mientras la pila repone electrones por el lado N y los retira por el lado P: el movimiento no se interrumpe. **La corriente pasa.** A esta forma de conectarlo se le llama **polarización directa**.

**Con el positivo en el lado N y el negativo en el lado P.** Ahora el borne positivo tira de los electrones del lado N, alejándolos de la frontera, y el negativo tira de los huecos del lado P, alejándolos también. La barrera vacía se hace más ancha. **La corriente prácticamente no pasa**: solo una corriente minúscula, de millonésimas de amperio o menos, que se llama **corriente de fuga**. Es la **polarización inversa**.

> **Una unión PN conduce en un sentido y bloquea en el contrario.** Conduce en directa (positivo al lado P) y bloquea en inversa.

![Una unión PN en sus dos situaciones. Arriba, polarización directa: el positivo de la pila en el lado P y el negativo en el lado N; la barrera central se estrecha y la corriente pasa. Abajo, polarización inversa: la pila conectada al revés; la barrera se ensancha y la corriente no pasa. Debajo, el símbolo del diodo: una flecha que va del ánodo (lado P) al cátodo (lado N) y choca contra una barrita.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-union-pn.svg)

## El diodo

Un **diodo** es exactamente eso: una unión PN metida en una cápsula con dos patas.

- La pata unida al lado P se llama **ánodo**.
- La pata unida al lado N se llama **cátodo**. En la cápsula está marcada con una **raya**.

En los esquemas se dibuja como una flecha que choca contra una barrita. La flecha señala el sentido en que puede pasar la corriente (el convencional, de positivo a negativo): **de ánodo a cátodo**.

### La imagen del agua: una válvula antirretorno con muelle

En el circuito de agua, un diodo es una **válvula antirretorno**: una compuerta que el agua abre al empujar en un sentido y que se cierra sola si el agua intenta volver.

La comparación es buena incluso en un detalle. La compuerta tiene un muelle que la mantiene cerrada, así que el agua necesita un mínimo de presión para abrirla. Al diodo le pasa lo mismo: aunque esté en directa, no empieza a conducir hasta que la tensión supera un pequeño valor, la **tensión umbral**. El muelle es el escalón de tensión de la barrera, aquellos 0,7 V del silicio: hay que vencerlo para que la corriente pase.

| Tipo de diodo | Tensión umbral aproximada |
|---|---|
| De **silicio** (el normal) | **0,6 a 0,7 V** |
| De germanio | 0,2 a 0,3 V |
| LED | 1,8 a 3 V, según el color |

Por debajo del umbral, el diodo no conduce. Por encima, conduce con mucha facilidad, y mientras conduce se queda siempre con una tensión parecida a la de su umbral: en un diodo de silicio que conduce hay unos 0,7 V entre ánodo y cátodo, pase mucha o poca corriente.

Esto último tiene una consecuencia práctica. El diodo no cumple la ley de Ohm como una resistencia: una vez abierto, no limita la corriente. Si nada más la frena, pasará toda la que la fuente pueda dar y el diodo se quemará. Por eso el LED de la lección 1 necesitaba su resistencia en serie.

Y tampoco bloquea cualquier tensión en inversa. Cada diodo tiene una **tensión inversa máxima**; si se supera, la barrera cede de golpe y el diodo normalmente se destruye.

## Para qué sirve una calle de sentido único

### Rectificar

La corriente alterna va y viene. Si se le pone un diodo en el camino, solo pasan los medios ciclos que van en el sentido permitido; los otros quedan bloqueados. Lo que sale ya no cambia de sentido: son impulsos, todos hacia el mismo lado.

A convertir corriente alterna en corriente de un solo sentido se le llama **rectificar**. Es el primer paso para obtener corriente continua a partir del enchufe, y por tanto el corazón de toda fuente de alimentación. En la sección 5 verás cómo se completa el trabajo.

![Rectificación con un diodo. A la izquierda, la tensión alterna de entrada: una onda que sube por encima de cero y baja por debajo. A la derecha, lo que sale del diodo: solo las mitades positivas de la onda; las mitades negativas han sido bloqueadas y en su lugar la tensión es cero.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-rectificacion.svg)

### Detectar

El mismo truco, aplicado a una señal de radio, permite extraer de ella el sonido que transporta. Así funcionaban los primeros receptores, las *radios de galena*: la galena es un mineral que, tocado con un alambre fino, forma un diodo natural. Los diodos de germanio de Amparo son sus descendientes, y siguen siendo apreciados para esto precisamente por su umbral tan bajo, que les permite trabajar con señales muy débiles. Cómo se extrae exactamente el sonido es asunto de la sección 6; aquí basta con saber que el oficio existe y que lo hace un diodo.

## Diodos con oficio propio

Jugando con el dopado y con la forma de fabricarlos se consiguen diodos especializados. Estos tres entran en el examen:

**LED** (diodo emisor de luz). Un diodo fabricado con materiales que, al conducir en directa, emiten luz. El color depende del material. Como todo diodo, solo luce conectado en el sentido correcto y necesita una resistencia en serie que limite su corriente.

**Diodo zéner.** Un diodo fabricado para trabajar al revés, en inversa, sin romperse. Al llegar a una tensión inversa muy precisa (su *tensión zéner*: 5,1 V, 9,1 V, 12 V…) empieza a conducir, y mantiene esa tensión entre sus patas aunque la corriente varíe. Es como una válvula de seguridad que se abre siempre a la misma presión. Se usa para obtener **tensiones fijas y estables**: como referencia y como regulador de tensión. Como cualquier diodo que conduce, no limita la corriente por sí mismo: siempre lleva una resistencia en serie, que se queda con los voltios que sobran.

**Varicap** (o *varactor*). Mira otra vez la unión PN en inversa: dos zonas conductoras, la P y la N, separadas por una franja aislante. Esa es exactamente la descripción de un condensador. Y como la franja se ensancha al aumentar la tensión inversa, es un condensador cuya capacidad se puede cambiar **variando una tensión**: a más tensión inversa, barrera más ancha, placas más separadas y menos capacidad. Los equipos modernos sintonizan así, sin piezas que giren: el varicap ha sustituido al condensador variable.

| Diodo | Cómo trabaja | Para qué se usa |
|---|---|---|
| Rectificador | En directa conduce, en inversa bloquea | Convertir alterna en continua |
| De señal (germanio, etc.) | Igual, con señales débiles | Detectar señales de radio |
| LED | En directa, emite luz | Indicadores, iluminación |
| Zéner | En inversa, a tensión fija | Estabilizar y regular tensiones |
| Varicap | En inversa, como condensador variable | Sintonía electrónica |

## Donde la gente se lía

- **«El lado P está cargado positivamente y el N negativamente.»** Los dos son neutros. P y N indican qué tipo de portador tienen disponible para moverse.
- **«Los huecos son partículas.»** Son vacantes: sitios donde falta un electrón. Se mueven porque los electrones vecinos van saltando a ocuparlos.
- **Confundir ánodo y cátodo.** El cátodo es el de la raya, y la corriente (convencional) entra por el ánodo y sale por el cátodo. En el símbolo, la flecha apunta hacia el cátodo.
- **«Un diodo en directa conduce desde cero voltios.»** Necesita superar su umbral: unos 0,7 V en silicio.
- **«El zéner es un diodo estropeado que conduce al revés.»** Conduce al revés a propósito, a una tensión exacta y sin dañarse. Es su trabajo.

## Compruébalo tú

1. ¿Qué tipo de silicio se obtiene al añadir átomos con cinco electrones exteriores? ¿Qué portadores tiene?
2. Conectas un diodo de silicio con el positivo de una pila en el cátodo y el negativo en el ánodo. ¿Conduce?
3. A un diodo de silicio en directa le aplicas 0,3 V. ¿Conduce?
4. Una pila de 9 V alimenta, en fila, un diodo de silicio en directa y una resistencia. ¿Qué tensión, aproximadamente, le queda a la resistencia?
5. Quieres obtener una tensión estable de 5,1 V a partir de una batería cuya tensión varía entre 11 y 14 V. ¿Qué tipo de diodo usarías?
6. En un varicap, ¿qué le pasa a la capacidad cuando aumentas la tensión inversa?
7. Aplicas una tensión alterna a un diodo y una resistencia en fila. ¿Cómo es la corriente que pasa por la resistencia?

**Soluciones**

1. **Tipo N**: sus portadores son electrones libres, de carga negativa.
2. No. Está en polarización **inversa** (el positivo está en el lado N): la barrera se ensancha y bloquea.
3. No: 0,3 V está por debajo del umbral del silicio (0,6 a 0,7 V).
4. El diodo se queda con unos 0,7 V; a la resistencia le quedan 9 − 0,7 = **unos 8,3 V**.
5. Un **zéner** de 5,1 V, con una resistencia en serie entre la batería y él. La tensión estable se toma entre las patas del zéner; la resistencia se queda con la diferencia, que irá variando entre 5,9 y 8,9 V.
6. **Disminuye**: la barrera se ensancha, que equivale a separar las placas de un condensador.
7. Una corriente a impulsos, siempre en el mismo sentido: solo pasan los medios ciclos en que el diodo queda en directa. Se ha rectificado.

## En una frase

Dopando el silicio se obtienen dos tipos, N (con electrones libres) y P (con huecos); su frontera, la unión PN, conduce solo en un sentido, y eso es un diodo: sirve para rectificar y detectar, y sus variantes dan luz (LED), tensión estable (zéner) o capacidad ajustable (varicap).

Si con una unión PN se consigue una calle de sentido único, con dos uniones se consigue algo mucho más poderoso: un grifo. Es el transistor, y con él el receptor gris volverá a cantar.
