Antes de enchufar el receptor gris del rastro, Dani intercaló una bombilla de filamento entre el enchufe y el aparato, «en serie», para que un posible cortocircuito no quemara nada más. Marina lo apuntó sin entenderlo.

Al final de esta lección lo entenderás tú, y de paso habrás aprendido la primera regla de gramática del idioma de los circuitos: las dos únicas maneras que existen de conectar dos cosas entre sí, y qué les pasa a la tensión, a la corriente y a la resistencia en cada una.

Todo lo que hace falta ya lo sabes: la ley de Ohm (I = U / R) y la idea de caída de tensión de la sección 2.

## Dos maneras de conectar, y no hay más

Coge dos resistencias —o dos bombillas, o dos aparatos cualesquiera— y una batería. Solo hay dos formas de unirlos:

- **En serie:** una detrás de otra, en fila. La corriente tiene **un solo camino** y tiene que atravesar primero una y después la otra.
- **En paralelo:** una al lado de la otra, las dos conectadas a los mismos dos puntos. La corriente tiene **dos caminos** y se reparte entre ellos.

En el circuito de agua de la sección 2, la serie es una sola tubería con dos estrechamientos seguidos. El paralelo es una tubería que se divide en dos ramales, cada uno con su estrechamiento, y que luego vuelve a juntarse.

![Arriba, dos resistencias en serie con una batería de 12 voltios: un solo camino, la misma corriente de 1 amperio pasa por las dos, y la tensión se reparte en 4 y 8 voltios. Abajo, las mismas dos resistencias en paralelo: las dos tienen los 12 voltios completos y la corriente total de 4,5 amperios se reparte en 3 y 1,5 amperios.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s05-serie-y-paralelo.svg)

## En serie: la misma corriente, la tensión se reparte

Vicente conectó a una batería de 12 V dos resistencias en fila: una de 4 Ω y otra de 8 Ω.

**La corriente es la misma en las dos.** Solo hay un camino, y lo que entra por un extremo tiene que salir por el otro: ya lo viste en la sección 2 con los dos amperímetros. No puede pasar más corriente por la primera que por la segunda.

**La resistencia total es la suma.** La corriente tiene que vencer un estorbo y después el otro, así que el estorbo total es la suma de los dos:

**R total = R1 + R2 + …**

En nuestro caso, 4 + 8 = 12 Ω. Y con la resistencia total ya se puede calcular la corriente con la ley de Ohm, como si hubiera una sola resistencia de 12 Ω:

I = U / R = 12 / 12 = 1 A

**La tensión se reparte.** Ese amperio atraviesa cada resistencia y en cada una deja su caída de tensión, I × R:

- En la de 4 Ω: 1 × 4 = 4 V
- En la de 8 Ω: 1 × 8 = 8 V

Suma las dos caídas: 4 + 8 = 12 V. Justo la tensión de la batería, y no por casualidad: todo el empuje que pone la fuente se gasta entre las cosas que hay en el camino.

Fíjate además en *cómo* se reparte: la resistencia de 8 Ω, que es el doble que la otra, se lleva el doble de voltios. **En serie, la resistencia mayor se queda con la mayor parte de la tensión.** Guarda esta frase, porque es la clave del truco de Dani.

Y una consecuencia que conoce cualquiera que haya tenido luces de Navidad antiguas: si un elemento se rompe, el camino único queda abierto y se apaga todo.

## En paralelo: la misma tensión, la corriente se reparte

Ahora Vicente conecta las mismas dos resistencias, de 4 Ω y 8 Ω, una al lado de la otra, cada una con sus dos extremos unidos directamente a los dos bornes de la batería.

**La tensión es la misma en las dos.** Cada resistencia está conectada a los mismos dos puntos, los bornes de la batería, y entre esos dos puntos hay 12 V. Las dos tienen 12 V completos, como si la otra no existiera.

**Cada una toma su propia corriente.** Como cada una tiene sus 12 V, a cada una se le aplica la ley de Ohm por separado:

- Por la de 4 Ω: I = 12 / 4 = 3 A
- Por la de 8 Ω: I = 12 / 8 = 1,5 A

Mira cómo se reparte: por la resistencia *menor* pasa *más* corriente, pero pasa por las dos.

**La corriente total es la suma.** De la batería tienen que salir las dos corrientes a la vez: 3 + 1,5 = 4,5 A.

**La resistencia total es menor que la menor.** Esta es la parte que sorprende. Calcula qué resistencia «ve» la batería: entrega 4,5 A con 12 V, así que R = U / I = 12 / 4,5 ≈ 2,67 Ω. ¡Menos que la más pequeña de las dos!

—Eso no puede ser —dijo Marina—. He añadido una resistencia. He añadido estorbo. ¿Cómo va a haber menos resistencia que antes?

—No has añadido un estorbo en el camino —dijo Vicente—. Has abierto un camino nuevo. Piensa en el supermercado un sábado: si abren una segunda caja, aunque la cajera sea lenta, la cola avanza más deprisa que con una sola. Cada caja estorba, pero dos cajas dejan pasar más gente que una.

Esa es la idea: **cada elemento que añades en paralelo es un camino más, y con más caminos pasa más corriente.** Por eso la resistencia total siempre baja.

### Las fórmulas del paralelo

La cuenta que acabamos de hacer (sumar las corrientes de cada rama) se puede escribir como fórmula. La corriente total es la suma de las dos corrientes, y cada una es una tensión dividida entre una resistencia:

12 / R total = 12 / 4 + 12 / 8

Los 12 V aparecen en los tres términos. Si divides todo entre 12, desaparecen:

1 / R total = 1/4 + 1/8 = 2/8 + 1/8 = 3/8, y por tanto R total = 8/3 ≈ 2,67 Ω

Lo mismo que antes, y sin que importe la tensión de la batería. Esa es la fórmula general del paralelo:

**1 / R total = 1 / R1 + 1 / R2 + …**

Se llama «la de los inversos» (el inverso de un número es 1 dividido entre ese número) y vale para cualquier número de resistencias. Por ejemplo, tres resistencias de 4 Ω, 6 Ω y 12 Ω en paralelo: 1/4 + 1/6 + 1/12 = 3/12 + 2/12 + 1/12 = 6/12, la mitad; luego R total = 2 Ω.

Como es incómoda de usar, para el examen y para la vida hay dos atajos que resuelven casi todos los casos:

**Atajo 1: resistencias iguales.** Dos resistencias iguales en paralelo dan la mitad. Tres iguales, la tercera parte. En general, **R / número de resistencias**. Dos de 50 Ω en paralelo son 25 Ω. Cuatro de 200 Ω son 50 Ω.

**Atajo 2: dos resistencias distintas.** Se multiplican y se divide entre su suma: «producto partido por suma».

**R total = (R1 × R2) / (R1 + R2)**

Con nuestras resistencias: (4 × 8) / (4 + 8) = 32 / 12 ≈ 2,67 Ω. Lo mismo que salió antes sumando corrientes.

**La comprobación que no falla:** el resultado de un paralelo tiene que ser siempre **menor que la resistencia más pequeña**. Aquí, 2,67 es menor que 4: correcto. Si te sale un número mayor, es que has sumado como si estuvieran en serie.

Un ejemplo que tienes en casa: todos los enchufes de una vivienda están en paralelo. Por eso cada aparato recibe sus 230 V completos, y por eso saltan los plomos cuando enchufas demasiados: cada uno añade su corriente a la total.

## Las dos reglas de Kirchhoff, en palabras llanas

Lo que has visto en los dos apartados anteriores tiene nombre. Son las dos **leyes de Kirchhoff**, por el físico alemán que las enunció en 1845, y dichas en palabras llanas son de puro sentido común:

> **Regla de las corrientes:** en cualquier punto donde se juntan varios cables (a ese punto se le llama **nudo**), la corriente que llega es igual a la corriente que sale. (En una bifurcación de tuberías, el agua que entra es la que sale: no se crea ni desaparece.)

> **Regla de las tensiones:** si das la vuelta completa a un circuito, las caídas de tensión que encuentras suman exactamente la tensión de la fuente. (Todo el empuje que da la bomba se gasta a lo largo de la vuelta.)

La primera es la que usamos en el paralelo (3 + 1,5 = 4,5 A). La segunda, en la serie (4 + 8 = 12 V). No hay más.

## Circuitos mixtos: de dentro hacia fuera

Cuando un circuito mezcla series y paralelos, se resuelve por partes: se localiza un grupo que esté claramente en serie o en paralelo, se sustituye mentalmente por una sola resistencia equivalente y se repite.

**Ejemplo.** *Una resistencia de 10 Ω está en serie con un grupo formado por dos resistencias de 30 Ω en paralelo. ¿Cuál es la resistencia total?*

1. Primero el grupo en paralelo: dos iguales de 30 Ω dan la mitad, 15 Ω.
2. Ahora queda una de 10 Ω en serie con una de 15 Ω: 10 + 15 = **25 Ω**.

## El truco de Dani, explicado

Ya tienes todo para entender la bombilla en serie.

Dani conecta la bombilla (de las antiguas, de 60 W) en serie con el receptor averiado, y el conjunto al enchufe de 230 V. Es una serie de dos elementos, y en una serie la tensión se reparte: **la mayor parte se la lleva el que más resistencia tiene.**

El truco tiene un ingrediente más, que ya conoces de la sección 2: la resistencia de un filamento cambia muchísimo con la temperatura. Frío, el de esa bombilla tiene unos 70 Ω. Encendido a pleno brillo, más de diez veces más: unos 880 Ω. Con eso hay dos casos:

- **El receptor está sano.** Toma poca corriente, y visto desde el enchufe se comporta como una resistencia de varios miles de ohmios. Con tan poca corriente, el filamento apenas se calienta y sigue teniendo poca resistencia: en el reparto se queda con unos 20 V, y el receptor con el resto. La bombilla da, como mucho, un resplandor rojizo, y el aparato funciona casi con normalidad.
- **El receptor tiene un cortocircuito dentro.** Su resistencia es casi cero, y el elemento con más resistencia de la serie pasa a ser la bombilla. Se queda con casi los 230 V, se pone al rojo blanco y su resistencia sube hasta los 880 Ω. La corriente ya no es la brutal de un cortocircuito: es la que deja pasar la bombilla encendida, un cuarto de amperio (I = U / R = 230 / 880 ≈ 0,26 A). Al receptor averiado apenas le llega tensión, y no se quema nada más.

Así que la bombilla hace dos trabajos a la vez: **limita** la corriente a un valor inofensivo y **avisa**: si brilla fuerte, hay un corto. Es un fusible que no se funde y que además da el diagnóstico. Por eso «examen aprobado» fue ver la bombilla casi apagada.

![El truco de la bombilla en serie. Con el aparato sano, casi toda la tensión cae en el aparato y la bombilla apenas luce. Con el aparato en cortocircuito, casi toda la tensión cae en la bombilla, que brilla a tope y limita la corriente a un cuarto de amperio.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s05-bombilla-en-serie.svg)

Una nota de seguridad: este truco es de taller y de gente que sabe lo que toca. Dentro de un aparato enchufado hay 230 V, con o sin bombilla.

## Donde la gente se lía

- **«En paralelo hay más resistencias, luego más resistencia.»** Al revés: más caminos, menos resistencia total. Siempre menor que la menor.
- **«En serie, la corriente se va gastando: a la segunda resistencia le llega menos.»** No. La corriente es idéntica en todos los puntos de una serie. Lo que se reparte es la tensión.
- **Confundir qué se reparte en cada caso.** En serie: misma corriente, la tensión se reparte. En paralelo: misma tensión, la corriente se reparte.

## Compruébalo tú

1. Tres resistencias de 10 Ω, 20 Ω y 30 Ω se conectan en serie a 12 V. ¿Qué corriente circula y qué tensión hay en la de 30 Ω?
2. En una tira de bombillas en serie se funde una. ¿Qué les pasa a las demás? ¿Y si estuvieran en paralelo?
3. Dos resistencias de 50 Ω en paralelo. ¿Resistencia total?
4. Una resistencia de 20 Ω y otra de 5 Ω en paralelo. ¿Resistencia total? Haz la comprobación.
5. A una batería de 12 V conectas en paralelo una resistencia de 6 Ω y otra de 12 Ω. ¿Cuánta corriente pasa por cada una y cuánta sale de la batería?
6. Tres resistencias de 10 Ω, 20 Ω y 20 Ω en paralelo. ¿Resistencia total? (Pista: empieza por las dos iguales.)
7. Una resistencia de 40 Ω está en serie con dos de 20 Ω en paralelo. ¿Resistencia total?
8. En el truco de Dani, la bombilla brilla con toda su fuerza. ¿Qué te está diciendo?

**Soluciones**

1. En serie se suman: 10 + 20 + 30 = 60 Ω. I = U / R = 12 / 60 = **0,2 A**, la misma en las tres. En la de 30 Ω caen U = I × R = 0,2 × 30 = **6 V** (la mitad de la tensión, porque tiene la mitad de la resistencia total).
2. En serie se apagan todas: el camino único queda abierto. En paralelo las demás siguen luciendo, porque cada una tiene su propio camino y sus voltios completos.
3. Dos iguales: la mitad, **25 Ω**.
4. Producto partido por suma: (20 × 5) / (20 + 5) = 100 / 25 = **4 Ω**. Comprobación: 4 es menor que 5, la más pequeña. Correcto.
5. Cada una tiene los 12 V completos. Por la de 6 Ω: 12 / 6 = **2 A**. Por la de 12 Ω: 12 / 12 = **1 A**. De la batería salen 2 + 1 = **3 A**.
6. Las dos de 20 Ω en paralelo dan 10 Ω. Quedan dos de 10 Ω en paralelo: **5 Ω**. (Con la fórmula de los inversos: 1/10 + 1/20 + 1/20 = 4/20, luego 20/4 = 5 Ω.)
7. Primero el paralelo: dos de 20 Ω dan 10 Ω. Luego la serie: 40 + 10 = **50 Ω**.
8. Que la bombilla se está quedando con casi toda la tensión, es decir, que el aparato tiene muy poca resistencia: hay un cortocircuito dentro (o algo que consume muchísimo más de lo normal).

## En una frase

En serie hay un solo camino: la corriente es la misma, las resistencias se suman y la tensión se reparte; en paralelo hay varios caminos: la tensión es la misma, las corrientes se suman y la resistencia total es menor que la menor.

En la lección siguiente le sacamos partido a ese «la tensión se reparte»: con dos resistencias se puede fabricar cualquier tensión que haga falta.
