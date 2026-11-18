Con la ley de Ohm en la mano puedes entender ya tres cosas que todo radioaficionado acaba aprendiendo, casi siempre por las malas: que un cable de alimentación no es un detalle sin importancia, que una batería «de doce voltios» no da siempre doce voltios y que un cortocircuito es una ley de Ohm con muy mal carácter.

Esta lección no trae ninguna fórmula nueva de memorizar. Es la misma ley, I = U / R, aplicada a cosas que hasta ahora dábamos por perfectas.

## Los cables también estorban

Hasta aquí hemos tratado los cables como si no tuvieran resistencia. Tienen muy poca, pero la tienen, y depende de cuatro cosas. Esta lista es pregunta clásica de examen:

1. **De la longitud.** A doble longitud, doble resistencia. Una tubería el doble de larga estorba el doble.
2. **De la sección**, que es la superficie del corte del cable: lo «ancho» que es el camino. A doble sección, **mitad** de resistencia: por una tubería más ancha el agua pasa con más facilidad. Fíjate en que va al revés que la longitud.
3. **Del material.** El cobre conduce mejor que el aluminio, y el aluminio mejor que el hierro. La plata es la mejor de todas.
4. **De la temperatura.** En los metales, cuanto más calientes, más resistencia: los átomos vibran más y estorban más a los electrones.

Dos aclaraciones sobre esta lista.

La primera, sobre el grosor. «El doble de grueso» no es lo mismo que «el doble de sección». Un cable con el doble de diámetro tiene **cuatro** veces más sección (igual que una pizza del doble de diámetro tiene cuatro veces más pizza), y por tanto la cuarta parte de resistencia. Por eso los cables no se venden por su diámetro, sino por su sección, en milímetros cuadrados (mm²): cable de 1,5 mm², de 2,5 mm², de 6 mm²…

La segunda, sobre la temperatura. Explica una sorpresa que te llevarás si mides una bombilla con el polímetro: apagada, con el filamento frío, marca muchos menos ohmios que cuando está encendida y al rojo.

### La resistividad: el número de cada material

Lo bien o mal que conduce cada material se resume en un número, la **resistividad**, que se escribe con la letra griega **ρ** («ro»). **Cuanto mayor es la resistividad, peor conduce el material.**

La resistividad del cobre es 0,017. Ese número tiene un significado muy concreto: es la resistencia, en ohmios, de un hilo de cobre de 1 metro de largo y 1 mm² de sección.

Las tres primeras reglas de la lista caben en una sola fórmula:

**R = ρ × L / S**

*La resistencia de un cable es su resistividad, multiplicada por su longitud (L, en metros) y dividida entre su sección (S, en mm²).* Es puro sentido común puesto en letras: más largo, más resistencia (la L multiplica); más ancho, menos (la S divide).

**Ejemplo.** *¿Qué resistencia tienen 10 metros de cable de cobre de 2 mm² de sección?*

R = ρ × L / S = 0,017 × 10 / 2 = **0,085 Ω**

Dos palabras más que el examen conoce, y que son simplemente «lo contrario de»:

- La **conductividad** es lo contrario de la resistividad: cuanto mayor, **mejor** conduce el material.
- La **conductancia** es lo contrario de la resistencia: mide lo fácil que pasa la corriente por un objeto, en vez de lo difícil. Se escribe con la letra **G**, se calcula como **G = 1 / R** y su unidad es el **siemens (S)** (no confundas esta S con la S de «sección» de la fórmula anterior). Una resistencia de 100 Ω tiene una conductancia de 1 / 100 = 0,01 S.

No te líes con las cuatro palabras. Hay dos que hablan de un *objeto* concreto (resistencia y conductancia) y dos que hablan de un *material* (resistividad y conductividad). Y en cada pareja, una dice lo difícil que es pasar y la otra lo fácil.

## La tensión que se queda por el camino

Recuerda la segunda forma de la ley de Ohm: U = I × R. Hasta ahora la hemos leído como «la tensión necesaria para hacer pasar una corriente I por una resistencia R». Tiene otra lectura, que es la misma idea vista desde el otro lado:

> Cuando una corriente I atraviesa una resistencia R, **gasta en ello una tensión I × R**. A esa tensión gastada en cruzar una resistencia se le llama **caída de tensión**.

En el circuito de agua es fácil de ver: el agua pierde presión al atravesar cada estrechamiento, y pierde más cuanto más estrecho es y cuanta más agua intenta pasar.

Vamos a un caso real. Marina alimenta una emisora con una batería de 12 V, pero la batería está lejos y usa un cable largo y fino. Sumando el hilo de ida y el de vuelta, el cable tiene 0,5 Ω.

Mientras la emisora escucha, pasan 0,8 A. La caída en el cable es:

U = I × R = 0,8 × 0,5 = 0,4 V

A la emisora le llegan 12 − 0,4 = 11,6 V. Ni se entera.

Pero al pulsar el micrófono, la emisora pide 10 A, y esos 10 A tienen que atravesar el mismo cable:

U = I × R = 10 × 0,5 = 5 V

Cinco voltios que se quedan en el cable. A la emisora le llegan 12 − 5 = 7 V, y lo más probable es que se apague cada vez que Marina intente hablar. (Es una cuenta aproximada: con tan poca tensión, la emisora tampoco llegaría a tomar los 10 A. Pero el problema es exactamente ese.)

—No lo entiendo —dijo Marina—. ¿No habíamos quedado en que la batería ponía doce voltios, conectara lo que conectara?

—Y los pone —dijo Vicente—. Los doce voltios están ahí, en los bornes de la batería. Lo que pasa es que ahora no le has conectado una cosa, sino dos, una detrás de otra: el cable y la emisora. Y los doce voltios se reparten entre las dos. Lo que se queda el cable no le llega a la emisora.

Esa es la idea, y la usaremos mucho:

> **Cuando hay varias cosas una detrás de otra, la tensión de la fuente se reparte entre ellas.** Cada una se queda con su caída de tensión, I × R, y la suma de todas las caídas es la tensión de la fuente.

![Una batería de 12 voltios alimenta una emisora a través de un cable largo de 0,5 ohmios. Escuchando, con 0,8 amperios, el cable se queda con 0,4 voltios y a la emisora le llegan 11,6. Transmitiendo, con 10 amperios, el cable se queda con 5 voltios y a la emisora solo le llegan 7.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s02-caida-de-tension.svg)

De aquí sale el consejo que oirás en todos los radioclubes: **los cables de alimentación, cortos y gruesos.** Corto y grueso significa poca resistencia; poca resistencia significa poca caída. Y ahora entiendes también lo del pájaro de la lección 2: entre dos puntos de un mismo cable separados tres centímetros hay tan poca resistencia que la caída de tensión entre ellos es de milésimas de voltio.

## La batería también estorba

Hemos dicho que la batería pone doce voltios, conectes lo que conectes. Es *casi* verdad, y el «casi» tiene nombre.

Los electrones dan la vuelta completa al circuito, y eso incluye atravesar la batería por dentro. La batería, como todo, tiene algo de resistencia. Se llama **resistencia interna**. Imagínala como una resistencia pequeña metida dentro de la caja de la batería, en fila con todo lo demás, que no se puede quitar.

Las consecuencias salen solas de lo que acabas de aprender:

- **Con la batería sin conectar**, no circula corriente. Sin corriente no hay caída de tensión dentro (I × R con I igual a cero da cero), y entre los bornes está todo el empuje que la química de la batería es capaz de dar. A ese empuje completo, medido sin que circule nada, se le llama **fuerza electromotriz**, abreviado **f.e.m.**
- **Cuando circula corriente**, una parte del empuje se gasta dentro de la propia batería, en su resistencia interna. En los bornes queda algo menos:

  **tensión en los bornes = f.e.m. − caída en la resistencia interna**

**Ejemplo.** Una batería de coche tiene una f.e.m. de 12,6 V y una resistencia interna de 0,02 Ω.

- Con la emisora transmitiendo (10 A), dentro de la batería se quedan 10 × 0,02 = 0,2 V. En los bornes hay 12,6 − 0,2 = 12,4 V. Apenas se nota.
- Al arrancar el coche (200 A), dentro se quedan 200 × 0,02 = 4 V. En los bornes quedan 12,6 − 4 = 8,6 V. Por eso las luces del coche se atenúan un instante cuando giras la llave.

Así que la frase exacta es: una batería mantiene su tensión casi constante **mientras no le pidas una corriente muy grande**. Cuanto menor es su resistencia interna, más corriente puede dar sin que su tensión se hunda.

Y de paso se aclara qué es una pila gastada. Es, sobre todo, una pila cuya resistencia interna ha crecido mucho. Si la mides suelta con el voltímetro puede marcar todavía cerca de 1,5 V, porque el voltímetro apenas le pide corriente. Pero en cuanto la pones a trabajar, casi todo su empuje se queda dentro de ella y al aparato no le llega nada.

## Los dos extremos: circuito abierto y cortocircuito

La ley de Ohm explica también los dos casos límite de un circuito.

**Circuito abierto.** El camino está cortado. El aire del corte tiene una resistencia enorme, y una tensión dividida entre una resistencia enorme da una corriente prácticamente nula. No circula nada.

**Cortocircuito.** Es lo contrario: los dos bornes de una fuente quedan unidos directamente por un camino sin apenas resistencia. Por ejemplo, una llave inglesa que cae sobre los dos bornes de una batería. O un amperímetro conectado por error a los dos bornes: era el aviso de la lección 3. La palabra lo dice: la corriente ha encontrado un camino *corto* que se salta el aparato.

¿Cuánta corriente circula? Si la llave no tiene prácticamente resistencia, lo único que queda en el circuito para frenar la corriente es la resistencia interna de la propia batería:

I = f.e.m. / resistencia interna = 12,6 / 0,02 = **630 A**

Seiscientos treinta amperios. La llave se pone al rojo en segundos, puede soldarse a los bornes y provocar un incendio, y la batería puede reventar. A esa corriente máxima que una fuente puede dar se le llama **corriente de cortocircuito**.

Compara con una pila pequeña, que tiene mucha más resistencia interna (pongamos 0,3 Ω): 1,5 / 0,3 = 5 A. Una pila en cortocircuito se calienta y se agota enseguida, pero no suelda nada. Por eso las pilas son juguetes y las baterías de coche hay que tratarlas con mucho respeto, aunque sus 12 V no den calambre.

### El fusible: un punto débil puesto a propósito

Para protegerse de los cortocircuitos existen los **fusibles**. Un fusible es un trocito de hilo fino, calibrado para fundirse cuando la corriente supera un valor determinado: 5 A, 20 A, el que indique.

Se coloca en serie, de modo que toda la corriente del circuito pase por él. Mientras todo va bien, se comporta como un trozo más de cable. Si algo falla y la corriente se dispara, el hilo se funde, el circuito queda abierto y todo se detiene antes de que se queme nada más.

Dos reglas que no admiten excepciones:

- **Todo cable que sale de una batería lleva su fusible**, y lo más cerca posible de la batería.
- **Un fusible fundido se sustituye por otro del mismo valor.** Nunca por uno «más gordo para que no salte»: si saltó, es que algo iba mal, y un fusible mayor solo consigue que lo siguiente en quemarse sea el cable.

## Donde la gente se lía

- **«Un cable más grueso tiene más resistencia, porque hay más cobre que atravesar.»** Al revés: más grueso es más ancho, y por lo ancho se pasa mejor. Lo que aumenta la resistencia es que sea más *largo*.
- **«Si el aparato no funciona, la culpa es de la batería o del aparato.»** Muchas veces es del cable que los une. Con corrientes grandes, medio ohmio lo estropea todo.
- **«Una batería de 12 V da 12 V pase lo que pase.»** Da su f.e.m. menos lo que se queda en su resistencia interna, y eso depende de la corriente que le pidas.
- **«Como 12 V no dan calambre, una batería de coche es inofensiva.»** No da calambre, pero en cortocircuito entrega cientos de amperios.

## Compruébalo tú

1. Tienes dos cables de cobre de la misma longitud, uno de 1 mm² y otro de 4 mm². ¿Cuál tiene más resistencia, y cuántas veces más?
2. ¿Qué resistencia tienen 20 metros de cable de cobre (ρ = 0,017) de 1 mm² de sección?
3. Un cable de alimentación tiene 0,2 Ω y por él pasan 20 A. ¿Cuántos voltios se quedan en el cable? Si la batería es de 12 V, ¿cuántos le llegan al equipo?
4. Una batería tiene una f.e.m. de 12,6 V y una resistencia interna de 0,05 Ω. ¿Qué tensión hay en sus bornes cuando entrega 20 A?
5. ¿Cuál es la corriente de cortocircuito de esa misma batería?
6. ¿Qué conductancia tiene una resistencia de 50 Ω?
7. Un fusible de 10 A se funde cada vez que transmites. Un compañero te propone cambiarlo por uno de 30 A. ¿Qué le contestas?

**Soluciones**

1. El de **1 mm²**, que tiene la cuarta parte de sección: **cuatro veces más** resistencia.
2. R = ρ × L / S = 0,017 × 20 / 1 = **0,34 Ω**.
3. Caída en el cable: U = I × R = 20 × 0,2 = **4 V**. Al equipo le llegan 12 − 4 = **8 V**.
4. Dentro de la batería se quedan 20 × 0,05 = 1 V. En los bornes hay 12,6 − 1 = **11,6 V**.
5. I = f.e.m. / resistencia interna = 12,6 / 0,05 = **252 A**.
6. G = 1 / R = 1 / 50 = **0,02 S**.
7. Que no. Si el fusible salta es porque pasa más corriente de la prevista, y hay que averiguar por qué (o comprobar qué fusible indica el fabricante del equipo). Poner uno mayor sin saberlo es quitarle la protección al cable.

## En una frase

Los cables y las baterías también tienen resistencia: cada resistencia que la corriente atraviesa se queda con una parte de la tensión (I × R), y por eso los cables se quieren cortos y gruesos, las baterías bajan de tensión cuando se les pide mucho, y un cortocircuito, sin nada que lo frene, es tan peligroso.

Quedan las dos piezas que le permitieron a Vicente saber cuánta voz le quedaba en la batería: la potencia y la energía.
