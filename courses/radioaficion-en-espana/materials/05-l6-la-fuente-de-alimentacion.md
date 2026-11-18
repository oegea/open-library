El receptor gris del rastro no cantaba porque tenía muerta la fuente de alimentación: las «cuatro aduanas» por las que, según Dani, pasa la alterna del enchufe hasta convertirse en la continua que el aparato necesita.

Es la primera «frase completa» que vas a leer en un circuito: cuatro etapas hechas con componentes que ya conoces, en un orden que es pregunta fija de examen. Al terminar sabrás seguir la electricidad desde el enchufe hasta la emisora, qué forma tiene en cada punto y qué es el *rizado*, el defecto que delata a una fuente cansada.

## El problema que resuelve

Recuerda dos cosas de las secciones anteriores:

- En el enchufe hay **corriente alterna de 230 V**: cambia de sentido cien veces por segundo (50 ciclos completos, 50 Hz).
- Una emisora, por dentro, necesita **corriente continua de unos 13,8 V**: siempre en el mismo sentido y siempre del mismo valor, sin altibajos. (Dani hablaba de «doce» porque así se les llama al hablar, «equipos de doce voltios»; ya viste en la sección 2 que el valor real de trabajo es 13,8 V.)

Hay que bajar la tensión, convertir la alterna en continua y dejarla estable. Son cuatro etapas, porque la conversión a continua necesita dos.

![Las cuatro etapas de una fuente de alimentación, de arriba abajo, con la forma de la tensión a la salida de cada una. Enchufe: alterna grande de 230 voltios. Transformador: alterna más pequeña. Rectificador: pulsos todos hacia el mismo lado, continua pulsante. Filtro: continua con una pequeña ondulación, el rizado. Regulador: continua plana y estable de 13,8 voltios.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s05-fuente-etapas.svg)

## Primera aduana: el transformador

El **transformador** baja los 230 V a una tensión cercana a la que se necesita. Recuerda cómo funciona, de la sección 4: dos bobinas sobre un mismo núcleo, y la relación entre sus números de vueltas decide la relación entre sus tensiones. Con unas quince veces menos vueltas en el secundario que en el primario, los 230 V se quedan en unos 15 V.

A su salida sigue habiendo **corriente alterna**, de la misma frecuencia y con la misma forma. Solo ha cambiado el tamaño.

El transformador hace además un segundo trabajo, tan importante como el primero: **aísla**. Entre el primario y el secundario no hay ningún contacto eléctrico; la energía pasa por el campo magnético. Lo que hay a partir de ahí ya no está unido directamente a la red de 230 V. Es la primera barrera de seguridad del aparato.

## Segunda aduana: el rectificador

Ahora hay que conseguir que la corriente vaya siempre en el mismo sentido. Para eso está el componente que solo deja pasar la corriente en un sentido: el **diodo**. Convertir alterna en continua con diodos se llama **rectificar**.

### Con un diodo: media onda

La forma más simple es poner un solo diodo en el camino. Durante medio ciclo, la corriente intenta pasar en el sentido permitido y pasa. Durante el otro medio ciclo intenta pasar al revés, y el diodo la bloquea.

El resultado es una serie de **pulsos** separados por huecos: un semiciclo sí, otro no. Por eso se llama **rectificador de media onda**. Funciona, pero desperdicia la mitad de cada ciclo.

### Con cuatro diodos: onda completa

La solución que usa prácticamente toda fuente es el **puente rectificador**: cuatro diodos (en los esquemas suelen dibujarse formando un rombo) que hacen de cruce con direcciones obligatorias. Venga la corriente del transformador en un sentido o en el otro, el puente la encamina de modo que por el aparato circule **siempre en el mismo sentido**.

![Un puente rectificador de cuatro diodos dibujado dos veces. En el semiciclo positivo la corriente entra por un diodo, atraviesa el aparato de arriba abajo y vuelve por el diodo opuesto. En el semiciclo negativo entra por los otros dos diodos, pero atraviesa el aparato otra vez de arriba abajo, en el mismo sentido.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s05-puente-rectificador.svg)

Sigue los dos caminos en el dibujo. En cada semiciclo conducen dos de los cuatro diodos, los que están enfrentados; en el siguiente, los otros dos. Y fíjate en lo que no cambia: el aparato recibe la corriente siempre por el mismo lado.

Dicho de otro modo: el puente no tira los semiciclos negativos, **les da la vuelta**. Es un **rectificador de onda completa**.

Existe otra manera de conseguir onda completa con solo **dos diodos**: usar un transformador con *toma central*, es decir, con una conexión a la mitad de su secundario. Cada mitad del secundario, con su diodo, se ocupa de un semiciclo. Ahorra dos diodos a cambio de un transformador más complicado, y el examen la menciona.

![Arriba, la tensión alterna de entrada. En el centro, la salida de un rectificador de media onda con un diodo: solo quedan los semiciclos positivos, con huecos entre ellos, 50 pulsos por segundo. Abajo, la salida de un rectificador de onda completa con puente de cuatro diodos: los semiciclos negativos se han dado la vuelta y no hay huecos, 100 pulsos por segundo.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s05-rectificacion.svg)

A la salida del rectificador la corriente ya no cambia de sentido. Pero mira la forma: sube desde cero hasta el máximo y vuelve a cero, un pulso tras otro. A eso se le llama **corriente continua pulsante**. Es continua porque va siempre hacia el mismo lado; es pulsante porque su valor no para de subir y bajar. Una emisora alimentada así zumbaría como un transformador viejo.

Un detalle que el examen pregunta: ¿cuántos pulsos hay por segundo?

- En **media onda**, uno por ciclo: **50** por segundo.
- En **onda completa**, dos por ciclo (el semiciclo positivo y el negativo dado la vuelta): **100** por segundo, uno cada centésima de segundo.

## Tercera aduana: el filtro

Hay que rellenar los valles entre pulso y pulso. Lo hace un **condensador electrolítico grande** conectado en paralelo con la salida del rectificador. Es el «condensador gordo» que Dani encontró hinchado como una lata al sol.

Piensa en la membrana de goma de la sección 4, en una tubería a la que el agua llega a golpes:

- Cuando llega un pulso, la tensión sube y el condensador **se carga** hasta arriba (la membrana se tensa).
- Cuando el pulso baja, el condensador **se va descargando** poco a poco sobre el aparato y mantiene la tensión mientras llega el siguiente (la membrana devuelve el agua que había acumulado).

Aquí trabaja la constante de tiempo de la sección 4 (τ = R × C: tras un tiempo τ, a un condensador que se descarga le queda el 37 % de su tensión). El condensador se descarga a través del aparato, y si es lo bastante grande, esa descarga es lenta comparada con la centésima de segundo que tarda en llegar el pulso siguiente. La tensión apenas baja entre uno y otro.

«Apenas» no es «nada». Entre pulso y pulso la tensión cae un poco y luego se recupera. Esa pequeña ondulación que queda montada sobre la continua tiene nombre:

> **Rizado** (en inglés, *ripple*): la ondulación residual que queda en la salida de una fuente después del filtro.

Tres cosas sobre el rizado que conviene saber:

- **Su frecuencia** es la de los pulsos: **100 Hz** con un puente de onda completa (50 Hz si fuera de media onda). «¿Qué frecuencia tiene el rizado de una fuente con rectificador de onda completa conectada a una red de 50 Hz?» es pregunta habitual, y la respuesta es 100 Hz.
- **Es mayor cuanto más corriente pide el aparato**, porque el condensador se vacía más deprisa. Y menor cuanto mayor es el condensador.
- **Se oye.** Un rizado excesivo se cuela en el audio como un zumbido grave, y en un transmisor sale al aire montado en tu voz. Si un compañero te dice que tu señal «zumba», piensa en la fuente.

Y es por donde mueren las fuentes viejas: los electrolíticos se secan con los años, pierden capacidad, el rizado crece y el condensador se calienta hasta hincharse. Eso era la «aduana tres, reventada» del receptor gris.

### Un dato que sorprende: la tensión sube

—Una cosa no me cuadra —dijo Marina, con el polímetro en la mano—. El transformador da quince voltios. Y aquí, después del condensador, mido casi veinte. ¿De dónde salen los otros cinco?

—De la sección 3 —dijo Dani—. Los quince voltios del transformador son voltios eficaces. Pero el condensador no se carga hasta el valor eficaz: se carga hasta la cresta, que es el valor de pico.

Recuerda: el valor de pico de una senoide es el eficaz multiplicado por 1,414. Para 15 V eficaces, 15 × 1,414 ≈ 21,2 V. De ahí hay que restar lo que se queda en los diodos: cada diodo de silicio que conduce se queda con unos 0,7 V, y en un puente la corriente atraviesa siempre dos, así que 1,4 V. Quedan 21,2 − 1,4 ≈ **19,8 V**. Es lo que se mide sin apenas consumo; cuando el aparato pide corriente de verdad, la media baja algo, porque el condensador se vacía un poco entre pulso y pulso.

Por eso el transformador de una fuente de 13,8 V no entrega 13,8 V, y por eso sobra tensión a la entrada de la última etapa. Esa tensión sobrante no es un defecto: el regulador la necesita.

## Cuarta aduana: el regulador

Lo que sale del filtro es casi continua, pero no es estable: tiene rizado, baja cuando el aparato pide más corriente y cambia si la tensión de la red sube o baja. El **regulador** (o *estabilizador*) es la etapa que deja la salida clavada en su valor: 13,8 V, pida la emisora un amperio o veinte.

Su principio es fácil de entender. Dentro hay dos cosas:

- Una **referencia** de tensión muy estable, que normalmente es un diodo zéner, el diodo de la sección 4 que mantiene una tensión fija entre sus patas.
- Un **transistor** colocado en serie con la salida, que trabaja como un grifo.

Un pequeño circuito compara continuamente la tensión de salida con la referencia. Si la salida baja, abre un poco más el grifo. Si sube, lo cierra un poco. Lo hace de forma continua y prácticamente instantánea, de modo que el rizado también queda planchado.

Un grifo solo puede *quitar* presión, nunca añadirla. Por eso el regulador necesita siempre que a su entrada haya unos voltios más de los que tiene que entregar: trabaja restando.

Y lo que resta lo convierte en **calor**. Si con el equipo transmitiendo llegan al regulador 18 V y tiene que entregar 13,8 V, el transistor se queda con 4,2 V; con 20 A pasando, son 4,2 × 20 = 84 W de calor. Por eso las fuentes de este tipo llevan grandes radiadores de aluminio con aletas, pesan mucho y se calientan.

En equipos pequeños, todo el regulador viene dentro de un solo circuito integrado de tres patas. Y para consumos mínimos existe la versión más simple posible, que el examen conoce: **una resistencia en serie y un diodo zéner** en paralelo con la salida. El zéner mantiene su tensión y la resistencia se queda con lo que sobra. El principio es siempre el mismo.

## El orden, para el examen

> **Transformador → rectificador → filtro → regulador.**

| Etapa | Componente principal | Qué hace | Qué sale |
|---|---|---|---|
| 1. Transformador | Dos bobinas acopladas | Baja la tensión y aísla de la red | Alterna de baja tensión |
| 2. Rectificador | Diodos (puente de cuatro) | Hace que la corriente vaya en un solo sentido | Continua pulsante |
| 3. Filtro | Condensador electrolítico grande | Rellena los valles | Continua con rizado |
| 4. Regulador | Zéner + transistor (o un integrado) | Fija la tensión exacta, restando lo que sobra | Continua estable |

A este tipo de fuente se le llama **fuente lineal**.

## Las fuentes conmutadas

El transformador de una fuente lineal de 20 A pesa varios kilos. El motivo es la frecuencia: a 50 Hz cada vaivén dura mucho, y el núcleo tiene que ser grande para manejar todo el campo magnético de cada uno. A frecuencias altas los vaivenes son brevísimos, y un transformador diminuto transfiere la misma potencia.

Las **fuentes conmutadas** aprovechan eso cambiando el orden de las operaciones. Rectifican y filtran directamente los 230 V de la red; unos transistores, trabajando como interruptores, **trocean** esa continua decenas o cientos de miles de veces por segundo; un transformador pequeño baja esa alterna de alta frecuencia a la tensión deseada (y aísla de la red, igual que antes), y se rectifica y filtra de nuevo. La regulación no se hace quemando el sobrante en calor, sino cambiando la proporción de tiempo que los interruptores pasan cerrados.

| | Fuente lineal | Fuente conmutada |
|---|---|---|
| Peso y tamaño | Grande y pesada | Pequeña y ligera |
| Rendimiento | Alrededor del 50-60 % | 85-90 % |
| Calor | Mucho | Poco |
| Ruido de radiofrecuencia | Ninguno | Puede generarlo |

La última fila es la que importa a un radioaficionado. Trocear corriente a gran velocidad produce armónicos que llegan hasta la onda corta. Una conmutada bien diseñada los filtra y se puede usar sin problema; una mala siembra de ruido la banda entera. El cargador barato de un móvil, que es una fuente conmutada mínima, es uno de los grandes enemigos de la escucha, como verás en la sección 10.

## Donde la gente se lía

- **«El rectificador ya da corriente continua.»** Da continua *pulsante*: va en un solo sentido, pero sube y baja. Falta filtrar y regular.
- **«El rizado tiene 50 Hz, como la red.»** Con rectificador de onda completa, 100 Hz: hay dos pulsos por ciclo.
- **Confundir filtro y regulador.** El filtro (condensador) rellena valles pero no fija ningún valor. El regulador fija el valor exacto.
- **«Desenchufada, una fuente es inofensiva.»** Los condensadores del filtro pueden seguir cargados un buen rato. En las fuentes conmutadas, cargados a más de 300 V.

## Compruébalo tú

1. A una fuente se le quita el regulador y se conecta la emisora directamente al condensador de filtro. ¿Qué notarías al pasar de recibir a transmitir?
2. Una fuente con un solo diodo (media onda) se conecta a una red de 50 Hz. ¿Qué frecuencia tiene su rizado?
3. El secundario de un transformador entrega 12 V eficaces. Tras un puente rectificador y un condensador de filtro, y sin apenas consumo, ¿qué tensión continua habrá aproximadamente?
4. A una fuente lineal se le seca el condensador de filtro. ¿Qué síntoma oirás en un receptor alimentado con ella?
5. El regulador de una fuente lineal recibe 19 V y entrega 13,8 V a un equipo que consume 10 A. ¿Cuánta potencia convierte en calor?

**Soluciones**

1. Al transmitir la emisora pide mucha más corriente: el condensador se vacía más entre pulso y pulso, la tensión media baja y el rizado crece. La tensión ya no sería estable (y en recepción sería demasiado alta, cerca del valor de pico), y la transmisión saldría con zumbido. Mantener la tensión fija es justo el trabajo del regulador.
2. **50 Hz**: en media onda solo hay un pulso por ciclo.
3. Pico: 12 × 1,414 ≈ 17 V. Menos dos diodos (1,4 V): unos **15,6 V**.
4. Un **zumbido grave** de 100 Hz: con menos capacidad, el rizado crece.
5. Sobran 19 − 13,8 = 5,2 V. P = U × I = 5,2 × 10 = **52 W** de calor.

## En una frase

Una fuente de alimentación convierte la alterna de la red en continua estable en cuatro pasos: el transformador baja la tensión y aísla, el rectificador la pone en un solo sentido, el condensador de filtro rellena los valles (lo que queda es el rizado, de 100 Hz) y el regulador la deja clavada.

La emisora ya tiene de qué alimentarse. En la lección siguiente vemos la «palabra» que hace el trabajo más visible de una radio: el amplificador.
