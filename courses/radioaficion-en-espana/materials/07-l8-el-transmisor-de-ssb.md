En la lección anterior quedaron montados los dos transmisores sencillos. Falta el que Marina va a usar el día que hable por onda corta, y que casualmente es el que más pregunta el examen: el de banda lateral única.

—Te aviso de que este ya lo conoces —dijo Vicente—. Lo viste anteayer, pero andando hacia el otro lado.

Al terminar esta lección sabrás dibujar el esquema de bloques de un transmisor de SSB, decir qué bloque quita la portadora y cuál la banda lateral que sobra, por qué su etapa final tiene que ser de clase AB y qué significa exactamente «100 vatios PEP», que es la medida con la que la normativa española fija los límites de potencia.

## Quitar dos cosas

Recuerda de la sección 6 qué es una señal de banda lateral única: una AM a la que se le ha quitado la **portadora** (que no lleva información) y **una de las dos bandas laterales** (que está repetida). Hay que quitar dos cosas, y cada una la quita un bloque distinto.

Síguelo en el dibujo, de arriba abajo.

![Esquema de bloques de un transmisor de SSB, de arriba abajo: micrófono y amplificador de micrófono; modulador balanceado, al que llega por un lado el oscilador de portadora, y del que salen las dos bandas laterales sin portadora; filtro de cristal, que deja pasar una sola banda lateral; mezclador, al que llega el oscilador variable y que traslada la señal a la frecuencia de emisión; filtro paso banda, que elimina la suma que también sale del mezclador; excitador; amplificador de potencia en clase AB; filtro paso bajo, que elimina los armónicos; antena.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-transmisor-ssb.svg)

**1. Micrófono y amplificador de micrófono.** Convierten la voz en una señal eléctrica de audio y la llevan a un nivel manejable.

**2. Modulador balanceado: fuera la portadora.** Es un mezclador de una clase especial. Le entran el audio y la señal de un oscilador de frecuencia fija, el *oscilador de portadora*. Como todo mezclador, entrega la suma y la diferencia. Pero está construido con dos mitades iguales y enfrentadas, de modo que la portadora que sale por una mitad se anula con la que sale por la otra (de ahí «balanceado», equilibrado). Las bandas laterales no se anulan, porque el audio llega a las dos mitades al revés: lo que una mitad sube, la otra lo baja. Al restar una salida de la otra, la portadora, que es igual en las dos, desaparece; y las bandas laterales, que son opuestas, se suman. A su salida hay bandas laterales, pero no portadora.

Con números. Oscilador de portadora en 9.000 kHz y, para simplificar, en el micrófono un silbido de 1 kHz. Del modulador balanceado salen:

- la diferencia: 9.000 − 1 = **8.999 kHz** (la banda lateral inferior)
- la suma: 9.000 + 1 = **9.001 kHz** (la banda lateral superior)
- y en 9.000 kHz, donde estaría la portadora, **nada**

Con una voz en lugar de un silbido, en vez de dos rayas hay dos franjas de unos 3 kHz de ancho, una a cada lado del hueco. A esto se le llama *doble banda lateral con portadora suprimida*.

**3. Filtro de cristal: fuera una banda lateral.** Un filtro paso banda muy estrecho, de unos 2,4 kHz, hecho con cristales de cuarzo. Se coloca centrado sobre una de las dos bandas laterales, la deja pasar y elimina la otra. A su salida ya hay una señal de SSB completa… pero en 9.000 kHz, que no es donde quieres emitir.

**4. Mezclador, oscilador variable y filtro paso banda: a la frecuencia de emisión.** Ya sabes cómo se cambia de sitio una señal sin estropearla: mezclando. Es el convoy de camiones cambiando de carril otra vez. Si el oscilador variable está en 16.100 kHz, la diferencia con los 9.000 kHz es 7.100 kHz: tu señal queda en la banda de 40 metros. Mueve el oscilador y te mueves por la banda. Como siempre, del mezclador sale también la suma (16.100 + 9.000 = 25.100 kHz), y como siempre, detrás va un filtro: un **paso banda** que deja pasar los 7.100 y elimina la suma y los restos del oscilador.

Como aquí la señal se genera en una frecuencia y se emite en otra, se dice que es un transmisor **con traslación de frecuencia**.

Un detalle para lectores atentos: el oscilador está por encima, así que la señal sale del mezclador del revés, como viste en la lección de la mezcla. Para emitir en banda lateral inferior en 40 metros, el filtro de cristal ha dejado pasar en 9.000 kHz la banda *superior*. El equipo lo sabe y lo hace solo.

—Espera —dijo Marina—. Nueve megahercios, un filtro de cristal de 2,4 kilohercios, un oscilador en dieciséis coma uno. Eso es el receptor del otro día.

—Es el *mismo taller* —dijo Vicente—. Un transceptor no son un transmisor y un receptor metidos en la misma caja: comparten las piezas. El filtro bueno, que es la pieza cara, y los osciladores se usan en los dos sentidos: al recibir, la señal entra por la antena y acaba en el altavoz; al transmitir, entra por el micrófono y acaba en la antena. Y por eso emites justo en la frecuencia en la que escuchas.

Con otros nombres, son las mismas cajas: el *oscilador variable* del transmisor es el **oscilador local** del receptor, y el *oscilador de portadora* es su **BFO**.

**5. Excitador y amplificador de potencia.** La señal ya está en su frecuencia y limpia de la suma, pero es minúscula. Como en los transmisores de la lección anterior, el excitador la sube y la etapa final le da la potencia de salida.

**6. Filtro paso bajo y antena.** La última caja antes de salir, como en todo transmisor: elimina los armónicos de la etapa final. (Entre la etapa final y la antena tiene que haber, además, un buen acuerdo eléctrico para que la potencia pase de una a otra. Es la *adaptación*, y la sección de antenas le dedica el espacio que merece.)

Para el examen, quédate con la pareja: **el modulador balanceado suprime la portadora; el filtro de cristal suprime la banda lateral que sobra.**

## Qué clase de amplificador, según el modo

En la lección anterior viste por qué los transmisores de morse y de FM pueden usar una etapa final de clase C. Ahora se ve del todo para qué servía distinguir las clases.

- En **CW** y en **FM**, la señal tiene siempre la misma amplitud mientras se emite. Si el amplificador deforma la onda, el mensaje no se entera. Vale la **clase C**.
- En **SSB** (y en AM), el mensaje está precisamente en cómo sube y baja la amplitud. Si el amplificador no respeta esas subidas y bajadas, destroza la voz y, como verás en la lección siguiente, ensucia las frecuencias vecinas. Hace falta un amplificador que entregue una copia fiel, solo que más grande: un amplificador **lineal**. En la práctica, **clase AB** (o clase A, mejor todavía pero muy derrochadora).

> **SSB exige un amplificador lineal: clase AB. La clase C solo sirve para CW y FM, nunca para SSB.**

Por eso a los amplificadores externos de HF se les llama directamente «lineales».

El precio de la fidelidad es el rendimiento, que ya definimos en la sección 2 como lo que se entrega dividido entre lo que se consume. Un transceptor típico que emite 100 W toma de la fuente unos 20 A a 13,8 V:

P = U × I = 13,8 × 20 = 276 W

De 276 W que entran, 100 W salen por la antena: un rendimiento de 100 / 276 ≈ 0,36, el 36 %. El resto, 176 W, es calor. Por eso los transceptores tienen un radiador de aluminio en la parte trasera y un ventilador que se pone en marcha cuando hablas.

(Si recuerdas de la sección 5 que la clase AB rinde bastante más que eso, no hay contradicción: aquella cifra era la de la etapa final sola. Aquí contamos todo lo que el equipo consume: excitador, osciladores, pantalla, ventilador. Y es el consumo a plena potencia sostenida; hablando en SSB, la media es bastante menor.)

## La potencia en SSB: qué es el PEP

En FM, o en CW mientras la llave está pulsada, medir la potencia no tiene misterio: la señal tiene siempre la misma amplitud y la potencia es constante. Cien vatios son cien vatios.

En SSB no hay una cifra fija. Recuerda que en SSB no hay portadora: si te callas, no sale nada. Si hablas bajo, sale poco. En las sílabas fuertes, sale mucho. La potencia sube y baja continuamente con la voz.

Para dibujarlo se usa la **envolvente**, que ya apareció al hablar del detector de AM: la línea que une las crestas de la onda de radiofrecuencia, y que muestra cómo varía su amplitud.

![La envolvente de una señal de SSB mientras alguien habla: una silueta irregular con picos altos en las sílabas fuertes y casi nada en las pausas. Una línea horizontal marca la potencia en los picos más altos, 100 vatios PEP. Otra línea mucho más baja marca la potencia media, unos 25 vatios. Al lado, para comparar, la envolvente de una señal de FM o CW: una banda de altura constante.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-pep.svg)

> **PEP** (*Peak Envelope Power*, **potencia de cresta de envolvente**): la potencia que entrega el transmisor en los picos más altos de la modulación.

Dos consecuencias que conviene tener claras:

- **Es la cifra con la que se anuncian los equipos y con la que se legisla.** La normativa española de radioaficionados fija los máximos de cada banda como *potencia de cresta de envolvente (PEP)*; los verás en la sección de normativa. Cuando un transceptor dice «100 W» en SSB, son 100 W PEP.
- **La potencia media es mucho menor.** Con una voz normal, un transmisor de 100 W PEP entrega de media entre 20 y 30 W. Un vatímetro corriente, que mide valores medios, marcará eso mientras hablas, y no significa que el equipo esté averiado. Para ver los picos hace falta un vatímetro que mida PEP.

**Ejemplo.** *En un osciloscopio, la envolvente de tu señal alcanza en los picos 100 V de pico, medidos sobre una resistencia de 50 Ω (el valor habitual a la salida de un transmisor, como verás en la sección de antenas). ¿Cuál es la PEP?*

- Con lo que aprendiste en la sección 3, el valor eficaz en ese pico es 100 × 0,707 = 70,7 V.
- Con la fórmula de la sección 2, P = U² / R = 70,7² / 50 = 5.000 / 50 = **100 W PEP**.

## Donde la gente se lía

- **«En SSB la portadora la quita el filtro.»** La portadora la quita el **modulador balanceado**. El filtro de cristal quita la banda lateral sobrante.
- **«Clase C, que rinde más, para todo.»** Solo para CW y FM. En SSB hay que respetar la amplitud: clase AB.
- **«Mi equipo es de 100 W y el vatímetro marca 25 al hablar: está roto.»** Está midiendo la media. Los 100 W son de cresta (PEP).
- **«Un transmisor consume lo que emite.»** Consume bastante más. La diferencia es calor.
- **Calcular la PEP con la tensión de pico sin pasarla a eficaz.** Sale el doble de la cifra correcta. Primero × 0,707, después U² / R.

## Compruébalo tú

1. Tu transceptor emite en banda lateral inferior en 7.100 kHz, con el oscilador variable por encima de los 9.000 kHz en los que se genera la señal. ¿Qué banda lateral está dejando pasar el filtro de cristal en 9.000 kHz?
2. En un modulador balanceado entran un tono de audio de 2 kHz y una portadora de 455 kHz. ¿Qué frecuencias aparecen a la salida?
3. Un transmisor genera su señal de SSB en 9.000 kHz y la mezcla con un oscilador variable de 12.650 kHz, quedándose con la diferencia. ¿En qué frecuencia emite? ¿Qué otra frecuencia sale del mezclador y qué la elimina?
4. Un amigo quiere aumentar la potencia de su equipo de SSB con un amplificador de clase C que le sobró de una emisora de FM. ¿Qué le pasará a su señal?
5. Un equipo toma 18 A a 13,8 V y entrega 90 W a la antena. ¿Cuál es su rendimiento? ¿Cuántos vatios se convierten en calor?
6. Un vatímetro normal marca unos 30 W mientras hablas en SSB con un equipo anunciado como de 100 W. ¿Es eso compatible con que el equipo esté bien?
7. La envolvente de una señal de SSB alcanza en los picos 141 V de pico sobre 50 Ω. ¿Cuál es su PEP?

**Soluciones**

1. La **superior**. Con el oscilador por encima, la señal sale del mezclador del revés: lo que en 9.000 kHz era banda superior queda en 7.100 kHz como banda inferior.
2. La diferencia, 455 − 2 = **453 kHz**, y la suma, 455 + 2 = **457 kHz**. En 455 kHz no hay nada: la portadora se ha cancelado.
3. 12.650 − 9.000 = **3.650 kHz**, en la banda de 80 metros. Sale también la suma, 12.650 + 9.000 = 21.650 kHz, y la elimina el **filtro paso banda** que va detrás del mezclador.
4. Que saldrá deformada: la clase C no respeta las subidas y bajadas de amplitud, que en SSB son la voz. Se le entenderá mal y, como verás en la lección siguiente, ensuciará las frecuencias vecinas. Ese amplificador solo sirve para FM y CW.
5. Consume P = 13,8 × 18 = 248,4 W. Rendimiento: 90 / 248,4 ≈ 0,36, un **36 %**. En calor: 248,4 − 90 = **158,4 W**.
6. Sí. Los 100 W son PEP, la potencia en los picos. Un vatímetro normal indica la potencia media, que con la voz ronda la cuarta parte.
7. Valor eficaz en el pico: 141 × 0,707 ≈ 100 V. PEP = U² / R = 100² / 50 = 10.000 / 50 = **200 W**.

## En una frase

En un transmisor de SSB, el modulador balanceado quita la portadora, el filtro de cristal quita una banda lateral y un mezclador con su filtro lleva la señal a la frecuencia de emisión; la etapa final debe ser lineal (clase AB), y la potencia se mide en los picos: potencia de cresta de envolvente, PEP.

Todo esto describe un transmisor que funciona bien. Las dos últimas lecciones de la sección tratan de lo que pasa cuando funciona mal, que es lo que más interesa a tus vecinos de banda.
