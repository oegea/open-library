«Cuando lleguemos a los transistores —había prometido Vicente dando un golpecito a la chapa gris—, este señor cantará.» En la lata de Amparo, la cajita correspondiente decía *2N2222 y amigos*: unas piezas diminutas, unas de plástico negro y otras con forma de sombrerito metálico, cada una con tres patas.

El transistor es el componente que hace posible todo lo demás. Los que has visto hasta ahora frenan, almacenan, transforman o dejan pasar en un solo sentido, pero ninguno puede hacer que una señal débil gobierne a una fuerte. El transistor sí. Al terminar la lección sabrás qué significa amplificar, cómo lo consigue un transistor, en qué se diferencian sus dos grandes familias y de qué tres maneras se puede conectar.

## El problema: señales demasiado débiles

La señal que una antena entrega a un receptor es minúscula: millonésimas de voltio. Para mover el cono de un altavoz hacen falta voltios y una corriente apreciable. Entre lo uno y lo otro hay que multiplicar la señal millones de veces. A eso se le llama **amplificar**.

—¿Y de dónde sale la energía de más? —preguntó Marina—. Porque llevas dos meses repitiéndome que la energía no se fabrica.

—Y no se fabrica. Sale de la batería o de la fuente de alimentación. El transistor no engorda la señal: usa la señal para manejar la energía de la fuente.

Esa es la idea central, y con el agua se ve muy bien.

## La imagen del agua: un grifo

Vuelve al circuito de agua de la sección 2, con su bomba y su rueda de paletas, y pon un grifo en la tubería. Con dos dedos giras la manecilla, y con ese gesto pequeño gobiernas todo el caudal que la bomba es capaz de mover. Si mueves la manecilla un poco adelante y atrás, el caudal crece y mengua copiando tu movimiento, y la rueda gira más deprisa o más despacio, con muchísima más fuerza de la que tú has hecho.

Tus dedos no han aportado esa fuerza; solo la han controlado. La fuerza la pone la bomba.

> **Transistor:** componente de tres patas en el que una corriente o una tensión pequeña, aplicada a una de ellas, controla una corriente mucho mayor que circula entre las otras dos.

Las tres patas corresponden a las tres partes del grifo: por una entra el caudal grande, por otra sale, y la tercera es la manecilla. La bomba es la batería o la fuente de alimentación, y la rueda, lo que se quiere mover: un altavoz, por ejemplo.

![A la izquierda, un grifo: una manecilla que se mueve con poco esfuerzo controla el caudal grande de agua que mueve la bomba. A la derecha, un transistor bipolar con sus tres patas: una corriente pequeña que entra por la base controla una corriente grande que circula del colector al emisor y que procede de la fuente de alimentación.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-transistor-y-grifo.svg)

Hay dos grandes familias de transistores. Hacen lo mismo, pero la manecilla funciona de manera distinta.

## El transistor bipolar

Es el que abrió el camino: Bardeen, Brattain y Shockley inventaron el primer transistor en los laboratorios Bell en 1947, y les valió el premio Nobel; la versión «de unión», que es la que se usa hoy, llegó poco después. Su nombre completo es *transistor bipolar de unión*, y verás sus siglas en inglés: **BJT**.

Por dentro es un bocadillo de tres capas de silicio dopado, de los tipos que conociste en la lección anterior. Puede ser N-P-N o P-N-P: dos capas de un tipo con una capa muy fina del otro tipo en medio. Son, por tanto, dos uniones PN espalda con espalda.

Sus tres patas se llaman, y hay que saberlas de memoria:

- **Emisor.**
- **Base:** la capa fina del medio. Es la manecilla.
- **Colector.**

Así funciona un NPN, que es el más común:

1. Entre el colector y el emisor se conecta la fuente de alimentación (en un NPN, el colector hacia el positivo y el emisor hacia el negativo), con algo en medio que aproveche la corriente: un altavoz, una bombilla, el circuito que venga después. Con la base sin conectar, **no circula nada**: la unión entre colector y base está en inversa y bloquea.
2. Ahora se hace entrar una **corriente pequeña por la base**. La unión entre base y emisor queda en directa y, como en cualquier diodo, el emisor empieza a lanzar electrones hacia la base.

   Y aquí está el truco: la base es **finísima** y tiene muy pocos huecos. De cada cien electrones que entran en ella, solo uno, más o menos, encuentra un hueco y sale por la pata de la base. Los otros noventa y nueve la cruzan de largo, llegan al otro lado y allí los atrapa el colector, que está conectado al positivo y tira de ellos. La unión que «bloqueaba» solo bloqueaba porque no tenía electrones que dejar pasar; ahora el emisor se los está sirviendo. Circula una **corriente grande** de colector a emisor.
3. Cuanta más corriente de base, más corriente de colector. Y la proporción entre las dos —ese reparto de uno a noventa y nueve— se mantiene bastante fija.

Esa proporción es la **ganancia de corriente** del transistor. Se llama **beta (β)**, o *hFE* en las hojas de datos, y suele valer entre 50 y 300:

**corriente de colector = β × corriente de base**

**Ejemplo.** Un transistor con β = 100 recibe por la base una corriente de 0,2 mA. Por el colector circulan 100 × 0,2 = **20 mA**. Si la corriente de base sube a 0,3 mA, la de colector sube a 30 mA. Una variación de una décima de miliamperio en la base ha producido una variación de diez miliamperios en el colector.

Tres detalles que completan el retrato:

- La entrada del transistor, entre base y emisor, es una unión PN como la de un diodo. Así que para que empiece a conducir hay que superar su umbral: unos **0,7 V** entre base y emisor en un transistor de silicio.
- El transistor **PNP** funciona igual, pero con todas las tensiones y corrientes al revés.
- En el símbolo, la flecha está siempre en la pata del **emisor** e indica el sentido de la corriente: en el NPN apunta hacia fuera; en el PNP, hacia dentro. Es pregunta de examen.

En el agua, el bipolar es un grifo un poco especial: su manecilla no se gira con los dedos, sino con un chorrito que entra por un tubo fino y la empuja, y que acaba saliendo junto con el caudal grande. Cuanto más chorrito, más se abre.

> El transistor bipolar se controla **por corriente**: la corriente de base gobierna la corriente de colector.

## El transistor de efecto de campo

La otra familia es el **transistor de efecto de campo**, o **FET**. Sus tres patas tienen otros nombres, que el examen también pregunta:

- **Fuente** (*source*): por donde entran los portadores. Equivale al emisor.
- **Puerta** (*gate*): la manecilla. Equivale a la base.
- **Drenador** (*drain*): por donde salen. Equivale al colector.

Por dentro, entre fuente y drenador hay un canal de silicio por el que circula la corriente. La puerta está junto a ese canal, pero no deja pasar corriente hacia él. En el tipo más antiguo, el **JFET**, la puerta es una unión PN en inversa (que, como sabes, no conduce). En el **MOSFET**, que es el más extendido, es una capa finísima de óxido aislante. En los dos casos, al aplicar una tensión a la puerta, se crea un campo eléctrico (de ahí el nombre) que estrecha o ensancha el canal, y con ello deja pasar menos o más corriente.

Con el agua: aquí la manecilla se mueve solo con presión, sin que entre ni una gota. Como un tramo de tubería blanda que aprietas desde fuera: basta apretar para estrechar el paso.

> El transistor de efecto de campo se controla **por tensión**: la tensión aplicada a la puerta gobierna la corriente entre fuente y drenador, y por la puerta prácticamente no entra corriente.

Esa es su gran ventaja: controlarlo casi no cuesta energía. Los amplificadores de potencia de las emisoras modernas son MOSFET, y también lo son los miles de millones de transistores de cualquier ordenador o teléfono.

Los MOSFET tienen un punto débil: su capa de óxido es tan fina que una descarga de electricidad estática, como la chispa que salta al tocar algo en un día seco, puede perforarla. Por eso se manejan con cuidado y vienen en bolsas especiales.

| | Transistor bipolar (BJT) | Transistor de efecto de campo (FET) |
|---|---|---|
| Patas | Emisor, **base**, colector | Fuente, **puerta**, drenador |
| Tipos | NPN y PNP | JFET y MOSFET, de canal N o de canal P |
| Se controla con… | la **corriente** de base | la **tensión** de puerta |
| Corriente que pide el control | Pequeña | Prácticamente nula |

## Los dos oficios del transistor

Un grifo se puede usar de dos maneras, y un transistor también.

**Como amplificador.** La manecilla se deja en una posición intermedia, ni cerrada del todo ni abierta del todo. (A fijar ese punto de reposo, con unas resistencias, se le llama **polarizar** el transistor.) La señal débil la mueve un poco hacia un lado y hacia el otro, y la corriente grande copia esos movimientos, ampliados. Si esa corriente grande se hace pasar por una resistencia, en ella aparece una tensión que sube y baja con la señal (U = I × R): así es como una variación diminuta de tensión a la entrada se convierte en una variación grande a la salida. Los detalles están en la sección 5. Así se pasa de las millonésimas de voltio de la antena a los voltios del altavoz: con varios transistores en cadena, cada uno amplificando lo que le entrega el anterior. A cada uno de esos pasos se le llama **etapa**.

**Como interruptor** (o *conmutador*). La manecilla solo se usa en sus dos extremos: cerrada del todo o abierta del todo.

- Sin señal en la base (o en la puerta), el transistor no conduce nada. Se dice que está en **corte**.
- Con señal de sobra, conduce todo lo que el circuito le deja. Se dice que está en **saturación**.

Es un interruptor sin piezas móviles, que una señal eléctrica puede abrir y cerrar millones de veces por segundo. Toda la electrónica digital —ordenadores, móviles, los circuitos que gobiernan una emisora moderna— está hecha de transistores usados así, como interruptores que representan ceros y unos.

Una advertencia que comparten con las resistencias: un transistor que maneja corrientes grandes se calienta, y tiene una potencia máxima. Los de potencia van atornillados a una pieza metálica con aletas, el **disipador**, que ayuda a soltar el calor.

## Tres maneras de conectarlo

Un transistor tiene tres patas, pero una señal necesita dos hilos para entrar y dos para salir. Las cuentas solo salen si una de las patas la comparten la entrada y la salida. Según cuál sea la pata compartida (la *común*), hay tres montajes. El examen pregunta sus nombres y su rasgo principal; cómo se montan de verdad es asunto de la sección 5.

Para describirlos hacen falta dos expresiones nuevas, que usan la palabra *impedancia* de la lección 5:

- La **impedancia de entrada** de un montaje es lo que estorba a la señal que le llega. Cuanto más alta, menos corriente le pide a quien se la entrega.
- La **impedancia de salida** indica cuánta corriente puede entregar el montaje sin que su señal se hunda. Cuanto más baja, más puede entregar.

| Montaje | Qué amplifica | Rasgo principal |
|---|---|---|
| **Emisor común** | Tensión y corriente | El más usado. La señal sale invertida |
| **Colector común** (o *seguidor de emisor*) | Solo corriente; la tensión sale igual que entra | Impedancia de entrada alta y de salida baja: hace de intermediario entre un circuito débil y otro que pide mucha corriente |
| **Base común** | Solo tensión; la corriente sale igual que entra | Impedancia de entrada baja y de salida alta. Se usa en radiofrecuencia |

Con los FET existen los tres montajes equivalentes: fuente común, drenador común y puerta común.

## Donde la gente se lía

- **«El transistor aumenta la energía de la señal.»** No crea energía. La señal débil controla la energía que aporta la fuente de alimentación.
- **Cruzar los nombres de las patas.** Bipolar: emisor, base, colector. FET: fuente, puerta, drenador. Las manecillas son la **b**ase y la **p**uerta.
- **Cruzar el tipo de control.** El bipolar se controla por corriente; el FET, por tensión.
- **«Saturación es que el transistor se ha estropeado.»** Es simplemente el estado de «abierto del todo». Es lo que se busca cuando se usa como interruptor.
- **«La flecha del símbolo indica por dónde entra la señal.»** La flecha marca el emisor y el sentido de su corriente: hacia fuera en el NPN, hacia dentro en el PNP.

## Compruébalo tú

1. ¿Cómo se llaman las tres patas de un transistor bipolar? ¿Cuál hace de manecilla?
2. Tienes que amplificar la señal de un micrófono que solo puede entregar una corriente minúscula. ¿Qué tipo de transistor le pedirá menos corriente, un bipolar o un FET? ¿Cómo se llaman sus tres patas?
3. Un transistor con β = 150 recibe una corriente de base de 0,1 mA. ¿Qué corriente circula por el colector?
4. Por el colector de un transistor circulan 50 mA cuando por su base entran 0,5 mA. ¿Cuál es su ganancia de corriente?
5. Un transistor NPN tiene el emisor unido al negativo de la batería. Entre su base y su emisor hay 0,2 V. ¿Circula corriente por el colector?
6. Un transistor con β = 100 debe encender una bombilla por la que circulan 200 mA. ¿Qué corriente de base necesita, como mínimo? ¿Cómo se llama el estado del transistor cuando la bombilla está encendida del todo, y cómo cuando está apagada?
7. En el símbolo de un transistor bipolar, la flecha del emisor apunta hacia dentro. ¿Es NPN o PNP?
8. ¿Qué montaje de un transistor bipolar es el más usado y amplifica tanto la tensión como la corriente?

**Soluciones**

1. **Emisor, base y colector.** La manecilla es la base.
2. Un **FET**: se controla por tensión y por su pata de control, la puerta, prácticamente no entra corriente. Sus patas son **fuente, puerta y drenador**.
3. 150 × 0,1 = **15 mA**.
4. β = corriente de colector / corriente de base = 50 / 0,5 = **100**.
5. No. La unión entre base y emisor es como un diodo de silicio y necesita unos 0,7 V para conducir; con 0,2 V no entra corriente por la base y el transistor está en corte.
6. La corriente de base es la de colector dividida entre la ganancia: 200 / 100 = **2 mA**. Encendida del todo, el transistor está en **saturación**; apagada, en **corte**.
7. **PNP.** En el NPN apunta hacia fuera.
8. El de **emisor común**.

## En una frase

Un transistor es un grifo eléctrico: una señal pequeña en su pata de control (la corriente de base en el bipolar, la tensión de puerta en el FET) gobierna una corriente grande que aporta la fuente, y eso permite amplificar señales o conmutar como un interruptor.

Queda la media familia que faltaba, las válvulas, y dos cosas más para cerrar la sección: los circuitos integrados y los símbolos con los que todo esto se dibuja en un esquema.
