Cuando Morientes se presentó con el mando de la tele y cara de pocos amigos, Marina no se disculpó ni lo negó: propuso una prueba. Vicente tiene una frase para eso: «jamás niegues de entrada, jamás asumas de entrada. Se mide». Días después, con el asunto ya resuelto, Marina apuntó en su cuaderno que el nombre técnico de lo que habían hecho era «medir antes de opinar».

Esta sección empieza por ahí: por los aparatos con los que un radioaficionado averigua qué está pasando de verdad en su estación. En el examen forman un capítulo propio, y sus preguntas son de las más fáciles de asegurar, porque casi todas se deducen de lo que ya sabes desde la sección 2.

Esta primera lección está dedicada a un solo instrumento, el más básico y el primero que conviene tener. Al terminar sabrás usarlo en sus tres papeles, cómo se conecta en cada uno, qué error típico se comete y por qué ninguna medida es exacta.

## Tres instrumentos en una caja

El **polímetro** (también llamado *multímetro* o *téster*) es el aparato de la pantallita y los dos cables, uno rojo y uno negro, que Vicente sacó el primer día. Girando su selector se convierte en tres instrumentos distintos. Dos ya los conoces.

### Como voltímetro

Mide **tensión**, en voltios. Recuerda de la sección 2 que la tensión es siempre una diferencia entre dos puntos, y que por eso se mide tocando dos puntos, sin cortar nada.

> El voltímetro se conecta **en paralelo** con aquello cuya tensión se quiere medir. Debe tener una **resistencia interna muy alta**.

¿Por qué muy alta? Porque al tocar el circuito con las dos puntas le estás añadiendo un camino nuevo: el propio voltímetro. Si ese camino dejara pasar mucha corriente, el circuito ya no sería el mismo que antes de medir, y la lectura sería falsa. Con una resistencia interna enorme, por el voltímetro pasa una corriente insignificante (ley de Ohm: mucha resistencia, poca corriente) y el circuito ni se entera. Un polímetro digital corriente tiene unos diez millones de ohmios en modo voltímetro.

En el circuito de agua, el voltímetro sería un manómetro que se asoma a dos puntos de la tubería para comparar la presión, a través de un tubito tan fino que casi no deja pasar agua.

### Como amperímetro

Mide **corriente**, en amperios. La corriente es lo que pasa *por* un punto, así que hay que ponerse en su camino.

> El amperímetro se conecta **en serie**: se abre el circuito y se intercala, de modo que toda la corriente lo atraviese. Debe tener una **resistencia interna muy baja**.

¿Por qué muy baja? Por la razón contraria. Al intercalarlo, estás añadiendo algo en fila con el resto del circuito. Si estorbara, la corriente disminuiría y medirías menos de lo que había antes. Con una resistencia casi nula, la corriente pasa como si allí hubiera solo cable.

En el circuito de agua es un contador de caudal: hay que cortar la tubería y ponerlo en medio, y debe ser tan ancho como la propia tubería para no frenar el agua.

De aquí sale el error más clásico de todos, y una pregunta fija de examen. Si conectas el polímetro en modo amperímetro **en paralelo** con una fuente —tocando directamente los dos bornes de una batería, como harías con el voltímetro—, estás uniendo esos dos bornes con algo que casi no tiene resistencia. Eso tiene un nombre que ya conoces: **cortocircuito**. Con suerte se funde el fusible interno del polímetro. Sin suerte, se queman las puntas, el aparato o algo peor.

### Como ohmímetro

Mide **resistencia**, en ohmios. Es el único de los tres que no se limita a observar: para medir, el propio polímetro hace pasar una pequeña corriente por la pieza con su pila interna, mira qué tensión hace falta para ello y calcula la resistencia con la ley de Ohm (R = U / I).

De ese modo de funcionar salen sus dos reglas:

> La resistencia se mide **siempre con el circuito sin tensión**: desenchufado y con las baterías desconectadas. Y, si es posible, con la pieza **desconectada** del resto, al menos por una de sus patas.

- *Sin tensión*, porque si el circuito tiene su propia alimentación, esa tensión se mezcla con la pequeña corriente de prueba del polímetro: la lectura no vale para nada y el aparato puede estropearse.
- *Desconectada*, porque si la pieza sigue unida a otras, la corriente de prueba se reparte por todos los caminos que encuentre y lo que mides es el conjunto, no la pieza.

Una variante muy práctica del ohmímetro es la **prueba de continuidad**: el polímetro pita cuando entre sus dos puntas hay un camino sin apenas resistencia. Sirve para comprobar en un segundo si un cable está entero, si un fusible está fundido o si una soldadura hace contacto.

![Las tres conexiones del polímetro. Como voltímetro, en paralelo: sus dos puntas tocan los extremos de la bombilla sin interrumpir el circuito. Como amperímetro, en serie: el circuito se abre y el aparato se intercala. Como ohmímetro: la pieza se mide suelta, sin pila ni tensión alguna.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s10-polimetro-tres-conexiones.svg)

| El polímetro como… | Mide | Se conecta | Resistencia interna | Error típico |
|---|---|---|---|---|
| **Voltímetro** | Tensión (V) | En paralelo | Muy alta | Medir continua con el selector en alterna, o al revés |
| **Amperímetro** | Corriente (A) | En serie | Muy baja | Conectarlo en paralelo: cortocircuito |
| **Ohmímetro** | Resistencia (Ω) | Sobre la pieza, sin tensión | — | Medir con el circuito alimentado |

## El selector y los agujeros

Con un polímetro de verdad en la mano, lo primero que desconcierta es la rueda llena de símbolos. Se reduce a tres decisiones, que se toman **antes** de tocar nada con las puntas.

**Qué quieres medir.** Tensión (V), corriente (A) o resistencia (Ω).

**De qué tipo.** Tensión y corriente pueden ser continuas o alternas, y el polímetro tiene posiciones distintas para cada una:

- **Continua**: símbolo ⎓ (una raya sobre unos puntos) o las letras DC. Es la de baterías y fuentes de alimentación.
- **Alterna**: símbolo ~ (una onda) o las letras AC. Es la del enchufe.

Si mides los 13,8 V de tu fuente con el selector en alterna, leerás cero o una cifra sin sentido, y creerás que la fuente está averiada.

Una aclaración importante: que el polímetro tenga una posición para la alterna del enchufe no significa que vayas a usarla. **Con este curso no vas a medir un enchufe ni el interior de un aparato enchufado a la red.** Todas las medidas que te proponemos son de pilas, baterías y fuentes de 13,8 V.

**Cuánto esperas medir.** Algunos polímetros eligen la escala solos. En los que tienen varias escalas (2 V, 20 V, 200 V…), se empieza por la más alta y se va bajando.

—¿Y los agujeros? —preguntó Marina, con las dos puntas en la mano—. Hay tres, y yo tengo dos cables.

—El negro va siempre en el que pone COM —dijo Vicente—. El rojo, en el que pone V y Ω, para casi todo. Solo se cambia al tercero, el de los amperios, para medir corriente. Y se vuelve a poner en su sitio al acabar.

Esa última frase evita el accidente más frecuente con un polímetro: medir una tensión con el cable rojo olvidado en el agujero de los amperios. En esa posición el aparato es un amperímetro, es decir, casi un cable, y al tocar los dos bornes de una fuente se produce un cortocircuito.

## Lo que un polímetro no sabe medir

Un polímetro sirve para corriente continua y para la corriente alterna de la red. Con otras alternas se equivoca: en alterna está pensado para una senoide de 50 Hz, y una onda de otra forma o de una frecuencia mucho más alta la mide mal. Para la radiofrecuencia no sirve, y hacen falta otros aparatos, que verás en la lección siguiente.

Tampoco todos los polímetros son iguales. Los antiguos de aguja, llamados **analógicos**, tienen mucha menos resistencia interna en modo voltímetro que los **digitales**, de modo que alteran más el circuito que miden. A cambio, la aguja deja ver de un vistazo si una tensión sube, baja o tiembla, cosa que en una pantalla de números cuesta más.

## Ninguna medida es exacta

Queda una idea que el examen roza y que en la práctica ahorra muchas discusiones. Tiene dos partes.

**Todo instrumento altera lo que mide.** El voltímetro deja pasar un poco de corriente. El amperímetro estorba un poco. Los instrumentos buenos alteran muy poco, pero ninguno altera cero. Por eso se les pide a unos una resistencia interna altísima y a otros una bajísima: para que la alteración sea despreciable.

**Todo instrumento tiene un margen de error.** Si un polímetro marca 12,43 V, la tensión real puede ser 12,40 o 12,46. Cada aparato indica en sus características cuál es su margen. Las últimas cifras de la pantalla dan sensación de precisión, pero no siempre la hay detrás.

De las dos cosas sale una regla de oficio: cuando un resultado importa, se mide dos veces, y si se puede, de dos maneras distintas. Si las dos coinciden, te lo puedes creer.

Y por eso Vicente insiste en que lo más valioso de su cuarto de radio no es ningún aparato, sino la libreta. Una medida que no se apunta, con su fecha y sus condiciones, no sirve para comparar con la siguiente.

## Donde la gente se lía

- **«Voltímetro en serie, amperímetro en paralelo.»** Al revés. Truco de la sección 2: la tensión está *entre* dos puntos (se tocan los dos, en paralelo); la corriente pasa *por* un punto (hay que ponerse en su camino, en serie).
- **«Cuanta más resistencia interna, mejor el instrumento.»** Solo para el voltímetro. Para el amperímetro, cuanta menos, mejor.
- **«Puedo medir una resistencia con el aparato encendido.»** Nunca. El ohmímetro, siempre sin tensión.
- **«Marca cero, luego no hay tensión.»** O el selector está en alterna y la tensión es continua, o el cable rojo está en el agujero equivocado. Antes de fiarte de un cero, comprueba el polímetro midiendo algo que sepas que tiene tensión, como una pila.
- **«Si la pantalla da tres decimales, la medida es exacta hasta el tercero.»** La pantalla enseña cifras; la precisión la da el margen de error del aparato.

## Compruébalo tú

1. Quieres saber qué tensión llega a tu emisora desde la fuente. ¿En qué posición pones el selector, dónde va cada cable y cómo conectas las puntas?
2. Quieres saber cuánta corriente consume un receptor pequeño, de menos de 1 A. ¿Cómo lo conectas ahora?
3. ¿Por qué un voltímetro con poca resistencia interna daría lecturas falsas?
4. Sospechas que una resistencia de un aparato está quemada. ¿Qué dos cosas debes hacer antes de medirla con el ohmímetro?
5. Mides una batería de coche con el selector en V~ y la pantalla marca 0 (o un valor absurdo). ¿Está descargada?
6. Un compañero mide la tensión de una batería y, sin darse cuenta, tiene el cable rojo en el agujero de 10 A. ¿Qué ocurre al tocar los dos bornes?
7. Una emisora de 100 W consume unos 20 A al transmitir, y tu polímetro admite 10 A como máximo. ¿Puedes medir esa corriente intercalándolo?

**Soluciones**

1. Selector en **tensión continua** (V⎓), cable negro en COM, rojo en VΩ. Las puntas, **en paralelo**: una en el borne positivo de la emisora y otra en el negativo, sin desconectar nada.
2. Selector en corriente continua, cable rojo en el agujero de amperios, y el polímetro **en serie**: se desconecta uno de los cables de alimentación y se intercala, de modo que toda la corriente pase por él.
3. Porque dejaría pasar por él una corriente apreciable. El circuito tendría un camino más, cambiarían sus tensiones y medirías algo distinto de lo que había antes de conectar el aparato.
4. **Quitar la tensión** al aparato (desenchufar, desconectar baterías) y, a ser posible, **soltar una pata** de la resistencia para medirla aislada del resto.
5. No se sabe: la batería da tensión **continua** y el selector está en **alterna**. Hay que repetir la medida en V⎓.
6. Un **cortocircuito** a través del polímetro: en ese agujero el aparato es un amperímetro, casi un cable. Con suerte solo se funde su fusible interno.
7. **No.** Se quemaría su fusible, o algo más. Para corrientes así se lee el amperímetro de la propia fuente de alimentación, o se usa una *pinza amperimétrica*, que mide la corriente abrazando el cable, sin abrir el circuito.

## En una frase

El polímetro es voltímetro (en paralelo, con resistencia interna altísima), amperímetro (en serie, con resistencia interna bajísima) y ohmímetro (siempre sin tensión); antes de medir se decide qué, de qué tipo y cuánto, y se mira dónde está el cable rojo; y como ninguna medida es exacta, lo que importa se mide dos veces y se apunta.

El polímetro se queda en la corriente continua y en la de la red. En la lección siguiente, los instrumentos que miden lo que ocurre entre el transmisor y la antena.
