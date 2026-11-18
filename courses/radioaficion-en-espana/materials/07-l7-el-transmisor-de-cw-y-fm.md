—El transmisor es el receptor del revés —dijo Vicente, pasando la hoja de la libreta—. El receptor coge una señal de radio diminuta y saca de ella una voz. El transmisor coge una voz y fabrica con ella una señal de radio con fuerza para cruzar un océano. Las cajas te van a sonar casi todas.

Tiene razón: los osciladores, los filtros y los amplificadores ya los conoces, y aquí solo cambian de orden. Empezamos por los dos transmisores más sencillos, el de morse y el de FM, que es el que llevan los walkies. Al terminar esta lección sabrás dibujar el esquema de bloques de los dos, decir para qué sirve cada caja y explicar por qué todo transmisor termina en un filtro paso bajo. El de SSB, que es el de la onda corta y el que más pregunta el examen, tiene lección propia a continuación.

## Las cuatro tareas de todo transmisor

Cualquier transmisor, del más simple al más caro, hace cuatro cosas en este orden:

1. **Generar una portadora.** Una senoide limpia y estable en la frecuencia en la que quieres emitir. La fabrica un oscilador. Recuerda de la sección 6 que la portadora es la onda que hace de vehículo.
2. **Modularla.** Subirle el mensaje: tu voz, o los puntos y rayas del morse.
3. **Amplificarla.** Darle potencia, de las milésimas de vatio con que nace a las decenas o centenas de vatios que salen hacia la antena.
4. **Limpiarla.** Quitarle lo que la amplificación ha añadido y no debe salir al aire.

Los transmisores de esta lección y de la siguiente son tres maneras de hacer esas cuatro cosas.

## El más sencillo: el transmisor de morse

En CW, modular es encender y apagar. El esquema es este:

> **Oscilador → separador → excitador → amplificador de potencia → filtro paso bajo → antena**, con el manipulador (la llave de morse) dando y quitando paso a la señal.

- El **oscilador** genera la portadora. En los equipos antiguos era un oscilador de frecuencia variable (**VFO**, de *Variable Frequency Oscillator*); en los modernos, un sintetizador con la exactitud de un cristal de cuarzo.
- El **separador** (en inglés, *buffer*) es un amplificador pequeño cuyo único trabajo es aislar al oscilador de lo que pasa detrás, para que su frecuencia no se mueva cuando las demás etapas arrancan y paran. La llave de morse actúa sobre las etapas que van después del oscilador, nunca sobre el oscilador mismo, que se deja siempre en marcha.
- El **excitador** es un amplificador intermedio. El oscilador entrega una señal muy pequeña, y la etapa final necesita en su entrada una señal ya considerable para dar toda su potencia. El excitador cubre ese salto: «excita» a la etapa final. (En inglés lo verás como *driver*.)
- El **amplificador de potencia** (**PA**, de *Power Amplifier*) es la etapa final, la que entrega los vatios que van a la antena.
- El **filtro paso bajo** hace la limpieza, y más abajo le dedicamos un apartado.

En este transmisor la señal nace ya en la frecuencia en la que se va a emitir. Se dice que es un transmisor **sin traslación de frecuencia**.

## El de los walkies: el transmisor de FM

En FM, modular es hacer que la frecuencia de la portadora suba y baje al ritmo de la voz. Se consigue actuando directamente sobre el oscilador. Recuerda de la sección 4 el **varicap**, el diodo que se comporta como un condensador cuya capacidad depende de la tensión que se le aplica. Si se pone un varicap en el circuito resonante del oscilador y se le aplica la tensión que viene del micrófono, la voz cambia la capacidad, la capacidad cambia la frecuencia de resonancia, y el oscilador «baila» al son de la voz. Eso ya es FM.

> **Micrófono → amplificador de micrófono → limitador de desviación → oscilador modulado en frecuencia → (multiplicadores) → amplificador de potencia → filtro paso bajo → antena.**

Dos cajas nuevas:

- El **limitador de desviación** recorta el audio que supera cierto nivel antes de que llegue al oscilador, para que la frecuencia no se desplace más de lo permitido por mucho que se grite al micrófono.
- Los **multiplicadores de frecuencia** son amplificadores que deforman la señal a propósito para fabricar armónicos, seguidos de un filtro que se queda con uno de ellos (el doble, el triple). Son un recurso clásico para llegar a frecuencias altas partiendo de un oscilador de frecuencia más baja, que es más fácil de hacer estable.

**Ejemplo.** Un oscilador en 12,125 MHz, seguido de un triplicador y dos duplicadores, multiplica su frecuencia por 3 × 2 × 2 = 12 y entrega 12,125 × 12 = **145,5 MHz**. Todo lo que el oscilador se mueva se multiplica también por doce: si la voz desplaza su frecuencia 417 Hz arriba y abajo, a la salida la desviación es de 417 × 12 ≈ 5.000 Hz, los ±5 kHz habituales.

Los multiplicadores solo valen para CW y FM. Como deforman la onda, destrozarían las variaciones de amplitud de una señal de SSB; por eso la SSB se cambia de frecuencia con mezcladores, como verás en la lección siguiente. En los equipos actuales, a los multiplicadores los sustituye casi siempre un sintetizador.

(Existe una segunda manera de obtener FM, que el examen nombra: dejar el oscilador en paz y actuar con el audio sobre un **modulador de fase** colocado detrás de él. El resultado en el aire es, a efectos prácticos, el mismo.)

## Qué etapa final llevan: la clase C

En la sección 5 conociste las clases de amplificador. Los dos transmisores de esta lección tienen algo en común: mientras emiten, su señal tiene siempre la misma amplitud. En morse, la portadora está o no está. En FM, lo único que cambia es la frecuencia.

Eso permite usar en la etapa final un amplificador de **clase C**, que deforma mucho la onda pero aprovecha muy bien la energía: como el mensaje no va en la forma ni en el tamaño de la onda, la deformación no lo estropea. En la lección siguiente verás que con la SSB ocurre justo lo contrario.

—Pero si deforma la onda, saldrán armónicos —dijo Marina.

—Muchos. Por eso hay una última caja.

## El filtro paso bajo: la limpieza final

Todo amplificador de potencia deforma algo la señal, y uno de clase C la deforma mucho. Y ya sabes desde la sección 3 lo que ocurre cuando una onda se deforma: aparecen **armónicos**, señales en el doble, el triple, el cuádruple de la frecuencia original. Si emites en 7,1 MHz, del amplificador salen también, más débiles, 14,2, 21,3 y 28,4 MHz.

Tú has elegido ocupar una franja en 7,1 MHz, no aparecer a la vez en otras tres bandas encima de quien las esté usando. Y desde otras bandas es peor: el segundo armónico de una emisión en 10,1 MHz cae en 20,2 MHz, fuera de las bandas de radioaficionado, encima de otros servicios. La solución es un **filtro paso bajo** entre el amplificador y la antena: deja pasar tu frecuencia, que es la más baja de todas, y atenúa todo lo que hay por encima, que es donde están los armónicos. Un transceptor lleva un filtro distinto para cada banda y los cambia automáticamente.

![Dos gráficas con la potencia en vertical y la frecuencia en horizontal. Arriba, a la salida del amplificador: una raya alta en 7,1 megahercios, la señal deseada, y tres rayas más bajas en 14,2, 21,3 y 28,4 megahercios, los armónicos. Abajo, después del filtro paso bajo, cuya curva deja pasar hasta unos 8 megahercios y luego cae: la raya de 7,1 megahercios sigue igual y los armónicos casi han desaparecido.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-filtro-paso-bajo.svg)

## Donde la gente se lía

- **«La llave de morse enciende y apaga el oscilador.»** No debe: el oscilador se deja siempre en marcha, y la llave actúa sobre las etapas siguientes. En la última lección de la sección verás qué pasa cuando no es así.
- **«Los multiplicadores de frecuencia sirven para cualquier modo.»** Solo para CW y FM. La SSB se traslada mezclando.
- **«Un multiplicador multiplica la potencia.»** Multiplica la frecuencia (y la desviación). La potencia la da el amplificador final.
- **«El filtro paso bajo reduce mi potencia.»** Deja pasar tu señal casi íntegra. Lo que atenúa son los armónicos, que están por encima.
- **Confundir el limitador de desviación del transmisor con el limitador del receptor de FM.** El del transmisor recorta el audio antes de modular, para no ocupar más ancho del debido. El del receptor iguala la amplitud de la señal recibida, para quitarle el ruido.

## Compruébalo tú

1. Ordena los bloques de un transmisor de morse: amplificador de potencia, oscilador, filtro paso bajo, separador, excitador.
2. ¿Para qué sirve la etapa separadora que va detrás del oscilador?
3. Un transmisor de FM parte de un oscilador en 18,0 MHz seguido de tres duplicadores. ¿En qué frecuencia emite? Si la voz desplaza el oscilador ±500 Hz, ¿qué desviación hay a la salida?
4. ¿Qué bloque de un transmisor de FM impide que la señal ocupe más ancho del debido cuando se grita al micrófono?
5. Un transmisor emite en 10,12 MHz. ¿En qué frecuencias están su segundo y su tercer armónico? ¿Qué tipo de filtro los atenúa?
6. ¿Por qué se puede usar un amplificador de clase C en un transmisor de FM, aunque deforme la onda?

**Soluciones**

1. Oscilador → separador → excitador → amplificador de potencia → filtro paso bajo.
2. Para aislar al oscilador de las etapas siguientes, de modo que su frecuencia no cambie cuando estas se conectan, se desconectan o cambian de carga.
3. Multiplica por 2 × 2 × 2 = 8: emite en 18,0 × 8 = **144 MHz**, y la desviación es 500 × 8 = 4.000 Hz, es decir, **±4 kHz**.
4. El **limitador de desviación**, que recorta el audio excesivo antes de que llegue al oscilador.
5. Segundo armónico: 2 × 10,12 = **20,24 MHz**. Tercero: 3 × 10,12 = **30,36 MHz**. Los dos caen fuera de las bandas de radioaficionado. Los atenúa un **filtro paso bajo** a la salida del transmisor.
6. Porque en FM el mensaje va en los cambios de frecuencia, no en la amplitud ni en la forma de la onda. La deformación produce armónicos, que el filtro paso bajo elimina, pero no altera el mensaje.

## En una frase

Todo transmisor genera una portadora, la modula, la amplifica y la limpia: el de morse lo hace con oscilador, separador, excitador y etapa final; el de FM añade el limitador de desviación y modula la frecuencia del propio oscilador; y los dos terminan en un filtro paso bajo que elimina los armónicos.

Queda el transmisor que usarás en onda corta, y con él, la manera en que se mide la potencia.
