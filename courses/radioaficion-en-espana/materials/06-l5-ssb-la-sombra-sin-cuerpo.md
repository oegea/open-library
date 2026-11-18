Marina giró el mando hercio a hercio y un graznido de pato se convirtió en un señor de Albacete hablando de la lluvia. Dani le dijo que aquello se llamaba banda lateral única, que la emisora solo enviaba «la sombra de la voz» y que el receptor tenía que poner el resto.

Con lo que aprendiste en la lección anterior, esa explicación deja de ser una imagen bonita y se convierte en algo que puedes calcular. Al terminar esta lección sabrás qué se quita exactamente en SSB y por qué, qué tiene que hacer el receptor para reconstruir la voz, por qué un error de sintonía de 200 Hz produce un pato y qué botón elegir, LSB o USB, en cada banda.

## La dieta: quitar lo que no dice nada

Repasa las cuentas de la AM. Al aire salían tres cosas:

- Una **portadora**, que se lleva dos tercios de la potencia y no contiene información: es igual hables o calles.
- Una **banda lateral superior**, con la voz completa.
- Una **banda lateral inferior**, con la misma voz, reflejada.

Si el mensaje está entero en una sola banda lateral, todo lo demás sobra. La **banda lateral única** hace justamente eso: elimina la portadora, elimina una de las dos bandas laterales y emite solo la otra.

> **SSB** (del inglés *Single Side Band*, banda lateral única; en español también **BLU**): modo de voz en el que se suprimen la portadora y una de las dos bandas laterales, y se transmite únicamente la banda lateral restante.

Esa banda lateral solitaria es «la sombra» de Dani: tiene la forma exacta de la voz, pero le falta el cuerpo al que pertenecía. Y en la imagen del camión de la lección 2: la SSB envía la mercancía sin camión, y por eso el receptor tendrá que poner el suyo para descargarla.

![Arriba, una señal de AM: portadora en el centro y una banda lateral a cada lado, 6 kilohercios en total. Abajo, la misma voz en banda lateral única: la portadora y la banda superior aparecen tachadas y solo queda la banda lateral inferior, que ocupa menos de 3 kilohercios.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s06-ssb-espectro.svg)

(Existe un paso intermedio, por si lo ves nombrado: quitar solo la portadora y dejar las dos bandas se llama *doble banda lateral*, DSB. Ahorra potencia pero no ahorra sitio. Casi no se usa.)

## Lo que se gana

**Se gana sitio.** Una sola banda lateral ocupa lo que ocupa la voz: de 300 a 3.000 Hz, unos 2,7 kHz. En la práctica, entre **2,4 y 2,7 kHz**, según el filtro del equipo. Menos de la mitad que los 6 kHz de la AM: donde cabía una conversación caben dos.

**Se gana potencia útil.** Recupera el ejemplo de la lección anterior: de los 150 W que emitía el transmisor de AM, solo 50 estaban en las bandas laterales, que es donde está el mensaje. (Allí dijimos que bastaría con los 25 W de una; pero el receptor de AM aprovecha las dos copias, y por eso aquí contamos las dos.) Un transmisor de SSB que emita esos mismos 150 W los pone *todos* en el mensaje: el triple. Y lo habitual es comparar dos equipos con el mismo tope de potencia, porque el tope es lo que limita a un transmisor. Ahí la ventaja de la SSB es de unas ocho veces (9 dB), y la cuenta es corta. Con un tope de 400 W, la AM solo puede llevar 100 W de portadora, porque sus crestas llegan a cuatro veces eso, como viste; y con 100 W de portadora, 50 W en las bandas laterales. La SSB pone los 400 W en el mensaje: 400 / 50 = 8.

**Y no se gasta cuando no se habla.** En AM, si te callas, la portadora sigue saliendo a toda potencia. En SSB, si te callas, no hay voz, no hay banda lateral y no sale **nada**. El transmisor solo emite mientras hay sonido en el micrófono, y más cuanto más fuerte hablas.

Sumado todo, una estación de SSB se hace oír como una de AM de bastantes veces más potencia. Por eso la SSB es, como decía Dani, el modo en que se habla en onda corta desde hace unos setenta años: **el modo de voz normal en HF**. Cuando hagas tu primer contacto de voz en HF, será en SSB.

## Lo que se paga: el receptor tiene que poner la portadora

Nada es gratis. Para ver el precio, vuelve al experimento del silbido.

En AM, al modular una portadora de 7.100 kHz con un tono de 1 kHz salían tres ondas: 7.099, 7.100 y 7.101 kHz. En SSB, si nos quedamos con la banda inferior, sale **una sola**: la de 7.099 kHz. Una onda de tamaño constante en 7.099 kHz.

—Pero eso es una portadora —dijo Marina—. Una portadora normal y corriente, en otra frecuencia.

—Exacto. Si silbas en SSB, emites una portadora. Y ahora dime: el que la recibe, ¿cómo sabe que eso era un silbido de mil hercios, y no de quinientos o de dos mil?

No puede saberlo. Lo que convertía a 7.099 kHz en «un tono de 1 kHz» era su distancia a la portadora de 7.100, y la portadora no se ha enviado. La información está completa, pero falta la referencia para leerla.

La solución es la misma que para el morse. El receptor tiene un oscilador propio, lo coloca en 7.100 kHz —donde *habría estado* la portadora— y lo mezcla con lo que llega. Del mezclador sale la diferencia:

7.100 − 7.099 = **1 kHz**

El silbido original, recuperado. A esta operación se la llama **reinsertar la portadora**, y el oscilador que la hace es el mismo BFO de la lección 3.

Con una voz ocurre lo mismo con todos sus tonos a la vez: cada uno llega convertido en una frecuencia de radio, y el receptor los devuelve a su sitio restándolos de la portadora que él pone.

Eso significa que en SSB **el receptor participa en la reconstrucción de la voz**. Y si no pone la portadora exactamente donde debe, la reconstruye mal.

## El pato, con números

Supón que la estación emite en banda inferior con su portadora (suprimida) en 7.100,0 kHz. Tú, en lugar de sintonizar 7.100,0, te quedas en 7.100,2: te has pasado **200 Hz**. Mira qué les ocurre a tres tonos de la voz:

| Tono original de la voz | Sale al aire en | Tu receptor resta desde 7.100,2 | Oyes |
|---|---|---|---|
| 300 Hz | 7.099,7 kHz | 7.100,2 − 7.099,7 | **500 Hz** |
| 1.000 Hz | 7.099,0 kHz | 7.100,2 − 7.099,0 | **1.200 Hz** |
| 2.000 Hz | 7.098,0 kHz | 7.100,2 − 7.098,0 | **2.200 Hz** |

Todos los tonos de la voz aparecen **desplazados 200 Hz**: a todos se les ha sumado la misma cantidad.

—Bueno, pues la voz sonará un poco más aguda —dijo Marina—. Como cuando aceleras un audio.

—No. Y ahí está la gracia. Cuando aceleras un audio, todos los tonos se *multiplican* por lo mismo: el de 300 pasa a 600 y el de 1.000 a 2.000. Las proporciones entre ellos se conservan, y por eso sigue sonando a voz, aunque de ardilla. Aquí se les *suma* lo mismo: el de 300 pasa a 500, que es casi el doble, y el de 2.000 pasa a 2.200, que es casi igual. Las proporciones se rompen.

Y las proporciones lo son todo. Una voz humana está hecha de tonos que guardan entre sí relaciones exactas: uno base y otros que son su doble, su triple, su cuádruple (los armónicos de la sección 3). Si la cuerda vocal vibra a 150 Hz, la voz contiene 150, 300, 450, 600… Súmales 200 a todos: 350, 500, 650, 800. Ya no son múltiplos de nada. El oído recibe algo que no corresponde a ninguna garganta posible, y lo percibe como una voz metálica, gangosa, de dibujo animado. El pato.

Al girar el mando, vas moviendo tu portadora hacia la posición correcta. El desplazamiento se va reduciendo —200, 100, 50 Hz— y la voz se va «espesando y redondeando», como notó Marina, hasta que las proporciones encajan y aparece la persona. Con menos de unos 50 Hz de error la voz ya suena natural. Con un poco de práctica se hace en dos segundos y de oído.

Un detalle práctico: en SSB, el número que ves en el dial es la frecuencia de esa portadora que no se transmite. Cuando alguien dice «estoy en 7.100», su señal de banda inferior está en realidad entre 7.097 y 7.100.

## LSB o USB: cuál de las dos

Queda decidir con qué banda lateral quedarse. Técnicamente da igual: las dos contienen la voz completa. Pero emisor y receptor tienen que elegir la misma, y para eso existe un convenio mundial que el examen pregunta y que usarás cada día:

> - Por **debajo de 10 MHz** (bandas de 160, 80 y 40 metros): banda lateral **inferior**, **LSB**.
> - Por **encima de 10 MHz** (bandas de 20, 17, 15, 12 y 10 metros, y todo VHF y UHF): banda lateral **superior**, **USB**.

No hay ninguna razón física. Es una costumbre heredada de cómo se fabricaban los primeros equipos de SSB en los años cincuenta, que se convirtió en norma. Los equipos modernos la aplican solos al cambiar de banda, pero conviene sabérsela para cuando no lo hagan. (Hay alguna excepción puntual, como la pequeña banda de 60 metros, donde se usa USB, y los modos digitales, que casi todos usan USB en cualquier banda.)

¿Qué pasa si escuchas con la banda equivocada? Dos cosas, las dos malas. La primera, que tu receptor abre su franja hacia el lado contrario de la portadora, y la mayor parte de la señal queda fuera. La segunda, que lo que consigas meter moviendo el dial se reconstruye **invertido**: recuerda que la banda inferior lleva la voz reflejada como en un espejo, y si el receptor la interpreta como si fuera la superior, los tonos graves salen agudos y los agudos, graves. (Invertida en el tono, no en el tiempo: no es una cinta puesta al revés.) No hay forma de entender una palabra, por mucho que afines. Si una señal de voz no se aclara de ninguna manera, lo primero que hay que comprobar es ese botón.

## Cómo se fabrica (en dos líneas)

Dentro del transmisor, la SSB se obtiene en dos pasos: un circuito llamado *modulador balanceado* genera las dos bandas laterales sin portadora, y un filtro muy estrecho deja pasar una y elimina la otra. Lo verás con su diagrama en la sección 7.

## Dónde cojea la imagen de la sombra

La imagen de Dani es buena, pero conviene saber dónde falla. Una sombra pierde información: a partir de la sombra de una persona no puedes saber de qué color lleva la camisa. La banda lateral única **no pierde nada**: contiene la voz completa. Lo único que le falta es la referencia de frecuencia para leerla, y esa la puede poner cualquier receptor. Es menos una sombra que un mueble desmontado al que le falta el plano: las piezas están todas.

## Donde la gente se lía

- **«En SSB se envía la mitad de la voz.»** Se envía la voz entera. Lo que se quita es una copia repetida y una portadora sin información.
- **«La voz de pato es una interferencia o una avería.»** Es una señal perfecta, mal sintonizada. El pato lo fabrica tu receptor al poner la portadora desplazada.
- **«Mal sintonizada, la voz suena solo más aguda o más grave.»** Suena deformada, porque a todos los tonos se les suma la misma cantidad y se rompen las proporciones entre ellos.
- **«LSB y USB son dos calidades distintas.»** Son equivalentes. Es un convenio para que todos usen la misma en cada banda.
- **«En SSB el transmisor emite siempre a toda potencia.»** Solo emite cuando hay voz, y con una potencia que sigue a la voz. En silencio no sale nada.

## Compruébalo tú

1. Una estación transmite en LSB con la portadora suprimida en 3.700 kHz. Su voz contiene un tono de 500 Hz y otro de 2.500 Hz. ¿En qué frecuencias salen al aire?
2. Otra estación transmite en USB con la portadora suprimida en 14.200 kHz y emite un silbido de 1.500 Hz. ¿Qué sale por su antena?
3. Sintonizas la estación del ejercicio 2, pero tu receptor queda en 14.199,9 kHz en lugar de 14.200,0. ¿Con qué frecuencia oyes el silbido?
4. ¿Qué banda lateral eliges para voz en 3.650 kHz? ¿Y en 21.300 kHz? ¿Y en 144.300 kHz?
5. En un tramo de 30 kHz, ¿cuántas señales de AM de 6 kHz caben? ¿Y cuántas de SSB de 2,7 kHz?
6. Un operador de SSB pulsa el micrófono y se queda callado. ¿Qué potencia sale por su antena?
7. Escuchas una voz que no consigues aclarar por más que afinas: suena siempre con los graves y los agudos cambiados. ¿Qué compruebas?

**Soluciones**

1. En banda inferior cada tono sale *por debajo* de la portadora, a una distancia igual a su frecuencia: 3.700 − 0,5 = **3.699,5 kHz** y 3.700 − 2,5 = **3.697,5 kHz**.
2. En banda superior el tono sale por encima: una única onda de tamaño constante en 14.200 + 1,5 = **14.201,5 kHz**. Es, a todos los efectos, una portadora.
3. Tu receptor resta desde 14.199,9: 14.201,5 − 14.199,9 = 1,6 kHz. Lo oyes a **1.600 Hz**, cien hercios más agudo de lo que es.
4. 3.650 kHz está por debajo de 10 MHz: **LSB**. 21.300 kHz y 144.300 kHz están por encima: **USB**.
5. De AM: 30 / 6 = **5**. De SSB: 30 / 2,7 ≈ **11**.
6. **Ninguna**. Sin voz no hay banda lateral, y en SSB no hay portadora.
7. El botón de banda lateral: probablemente estás en USB y la estación emite en LSB, o al revés.

## En una frase

La SSB emite solo una de las dos bandas laterales, sin portadora: ocupa menos de la mitad que la AM y pone toda la potencia en el mensaje, a cambio de que el receptor reinserte la portadora en el punto exacto; si la pone desplazada, todos los tonos de la voz se corren la misma cantidad, se rompen sus proporciones y aparece el pato. LSB por debajo de 10 MHz, USB por encima.

AM y SSB juegan con el tamaño de la onda. Queda la otra gran familia, la que deja el tamaño en paz y mueve la frecuencia: la FM, el modo de tu futuro walkie.
