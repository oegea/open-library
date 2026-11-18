Dentro del receptor del rastro, atornillado a una esquina del chasis, había un bloque de hierro negro del tamaño de un puño, pesado como una piedra, del que salían cables por dos lados. «El transformador», dijo Vicente. «Por aquí le entran los doscientos treinta voltios del enchufe y por aquí salen los doce que quiere el aparato. Y lo mejor es que entre un lado y otro no hay ni un solo cable que los una.»

Esta lección no trae ninguna idea nueva: el transformador es la inducción de la lección 4, puesta a trabajar. Al terminar sabrás cómo cambia una tensión por otra, por qué no puede regalar potencia y por qué solo funciona con corriente alterna.

## Dos bobinas que comparten campo

Recuerda las dos ideas de la lección 4: una corriente crea un campo magnético, y un campo magnético que cambia induce tensión en las espiras que atraviesa.

En una bobina sola, el campo induce tensión en la propia bobina. Pero al campo le da igual de quién sean las espiras. Si colocas una segunda bobina de modo que el mismo campo pase por dentro de ella, también inducirá tensión en la segunda.

> **Transformador:** dos bobinas enrolladas sobre un mismo núcleo, de manera que el campo magnético creado por una atraviesa también la otra.

- La bobina a la que se le aplica la tensión de entrada se llama **primario**.
- La bobina de la que se toma la tensión de salida se llama **secundario**.
- El **núcleo**, de chapas de hierro o de ferrita, tiene la misión de conducir el campo magnético de una bobina a la otra sin que se pierda por el camino.

El funcionamiento, paso a paso:

1. Se aplica tensión alterna al primario. Por él circula una corriente alterna, que va y viene.
2. Esa corriente crea en el núcleo un campo magnético que también va y viene: crece, mengua, se invierte, sin parar.
3. Ese campo, que cambia continuamente, atraviesa las espiras del secundario e induce en ellas una tensión alterna de la misma frecuencia.

La energía ha pasado del primario al secundario a través del campo magnético. Entre las dos bobinas **no hay conexión eléctrica**: no las une ningún conductor.

![Un transformador: un núcleo de hierro con dos bobinas. A la izquierda, el primario, con 920 espiras, conectado a 230 voltios. A la derecha, el secundario, con 48 espiras, del que salen 12 voltios. El campo magnético circula por el núcleo y enlaza las dos bobinas, que no se tocan.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-transformador.svg)

## La relación de espiras

¿Qué tensión sale por el secundario? Depende de cuántas espiras tenga cada bobina, y la razón es sencilla.

El campo del núcleo es el mismo para todas las espiras, sean del primario o del secundario. Así que en **cada espira** aparece la misma pequeña tensión.

> **Si te choca lo del primario.** A él la tensión se la *ponemos* nosotros con el enchufe; no se induce. Pero el primario es una bobina, y ya sabes lo que hace una bobina con la alterna: su propio campo, al cambiar, induce en ella una tensión que se opone a la del enchufe y casi la iguala. Esa tensión es la que se reparte por igual entre todas sus espiras. Y por eso, sin nada conectado al secundario, por el primario apenas pasa corriente. La tensión total de una bobina es la de una espira multiplicada por el número de espiras que tiene. Más espiras, más tensión.

De ahí sale la regla del transformador:

> **Las tensiones guardan la misma proporción que los números de espiras.** Si el secundario tiene la mitad de espiras que el primario, da la mitad de tensión. Si tiene el doble, da el doble.

Con fórmula, llamando N al número de espiras:

**U secundario = U primario × (N secundario / N primario)**

**Ejemplo, paso a paso.** *El transformador del dibujo tiene 920 espiras en el primario y 48 en el secundario. Se conecta a 230 V. ¿Qué tensión da?*

1. Tensión por espira: en el primario hay 230 V repartidos entre 920 espiras: 230 / 920 = 0,25 V por espira.
2. El secundario tiene 48 espiras, cada una con esos mismos 0,25 V: 48 × 0,25 = **12 V**.

Con la fórmula sale lo mismo: 230 × (48 / 920) = 12 V.

Según cuál de las dos bobinas tenga más espiras, el transformador es:

- **Reductor:** menos espiras en el secundario. La tensión baja. Es el de todas las fuentes de alimentación y cargadores.
- **Elevador:** más espiras en el secundario. La tensión sube. Es el de las centrales eléctricas, que elevan la tensión a cientos de miles de voltios para transportarla.

## Nada es gratis: lo que pasa con la corriente

—Un momento —dijo Marina—. Si le pongo más espiras al secundario saco más voltios. ¿Y si le pongo muchísimas? ¿Saco de un enchufe toda la potencia que quiera?

—Eso querrían los inventores de máquinas de movimiento perpetuo —dijo Vicente—. No. Un transformador cambia la tensión, pero no fabrica energía. Lo que sale es, como mucho, lo que entra.

Recuerda de la sección 2 que la potencia es P = U × I. En un transformador perfecto, la potencia que entra por el primario es igual a la que sale por el secundario:

**U primario × I primario = U secundario × I secundario**

Para que ese producto se mantenga, si la tensión sube, la corriente tiene que bajar en la misma proporción, y al revés. Con fórmula, las corrientes van con la relación de espiras puesta del revés que las tensiones:

**I secundario = I primario × (N primario / N secundario)**

> **Un transformador que baja la tensión sube la corriente disponible, y uno que sube la tensión la baja.** La potencia no cambia (salvo las pérdidas).

**Ejemplo.** El transformador de antes entrega en su secundario 12 V y 2 A a un aparato.

- Potencia que entrega: P = 12 × 2 = 24 W.
- Esa misma potencia tiene que entrar por el primario, a 230 V: I = P / U = 24 / 230 ≈ **0,104 A**, una décima de amperio.

¿Y cómo «sabe» el primario que tiene que tomar más corriente de la red cuando al secundario se le conecta algo? Porque la corriente del secundario crea su propio campo magnético, contrario al del primario. El campo del núcleo se debilita un poco, la oposición del primario baja y entra más corriente de la red: justo la necesaria para reponer el campo.

La tensión ha bajado unas 19 veces y la corriente es unas 19 veces mayor en el secundario que en el primario. Por eso, en un transformador reductor, el secundario está hecho con hilo grueso (poca tensión, mucha corriente) y el primario con hilo fino (mucha tensión, poca corriente).

Los transformadores reales pierden algo en forma de calor, en el hilo y en el núcleo. Los buenos entregan más del 90 % de lo que reciben. Recuerda que esa proporción se llama rendimiento.

## Solo funciona con corriente alterna

Repasa los tres pasos del principio y busca la palabra clave de la lección 4: el campo tiene que **cambiar** para inducir tensión.

Si conectas el primario a una batería, la corriente continua crea en el núcleo un campo fijo, que no cambia. Un campo fijo no induce nada. En el secundario no aparece ninguna tensión (salvo un impulso brevísimo en el instante de conectar y otro al desconectar, que es cuando el campo nace y muere).

> **Un transformador no funciona con corriente continua.** Necesita alterna, porque solo un campo que cambia induce tensión.

Peor aún. A la alterna, el primario le oponía su reactancia, que es grande. A la continua solo le opone la resistencia de su hilo, que es muy poca. Conectado a una batería, el primario se comporta casi como un simple cable: pasa por él una corriente enorme y se quema.

Esta es la razón de fondo de que la electricidad llegue a las casas en forma de corriente alterna. Con alterna, un simple transformador sube la tensión para transportarla lejos con poca corriente y pocas pérdidas (recuerda el cuadrado de P = I² × R), y otro la baja al llegar para que sea segura de usar. Con continua, eso no se podía hacer.

## Dos servicios más: aislar y adaptar

Además de cambiar tensiones, el transformador hace otros dos trabajos que en radio son igual de importantes.

**Aislar.** Como primario y secundario no están unidos por ningún conductor, el circuito conectado al secundario queda separado eléctricamente de la red. A esto se le llama **aislamiento galvánico**, y es una barrera de seguridad: lo que tocas en un aparato alimentado por transformador no está conectado directamente al enchufe.

**Adaptar impedancias.** Al cambiar tensiones y corrientes, el transformador cambia también lo «difícil de alimentar» que parece un aparato visto desde el otro lado. Compruébalo con el ejemplo de antes:

- El aparato del secundario toma 2 A con 12 V. Se comporta como una resistencia de 12 / 2 = **6 Ω**.
- Pero el enchufe ve salir solo 0,104 A con 230 V. Para él, lo que tiene conectado se comporta como 230 / 0,104 ≈ **2.200 Ω**.

El transformador ha hecho que 6 Ω parezcan 2.200 Ω. La proporción es 2.200 / 6 ≈ 367, y ese número no es casual: la relación de espiras era 920 / 48 ≈ 19,2, y 19,2 × 19,2 ≈ 367.

> La impedancia se transforma con el **cuadrado** de la relación de espiras. Un transformador con el doble de espiras en un lado multiplica la impedancia por cuatro; con el triple, por nueve.

Esto permite acoplar entre sí cosas que de otro modo no encajarían, como un cable y una antena de impedancias distintas. En la sección 8 aparecerán los *baluns* de las antenas, que son transformadores dedicados a eso.

En los circuitos de radiofrecuencia, los transformadores no son bloques de hierro, sino unas pocas vueltas de hilo sobre un anillo de ferrita: los anillos grises de la cajita de Amparo.

## Donde la gente se lía

- **«Un transformador elevador da más potencia.»** Da más voltios y, a cambio, menos amperios. La potencia es la misma, menos las pérdidas.
- **«Las dos bobinas están conectadas por dentro.»** No se tocan. Lo que las une es el campo magnético del núcleo.
- **«Un transformador también sirve para subir la tensión de una batería.»** Con continua no induce nada. (Los aparatos que sí lo consiguen primero convierten la continua en alterna con transistores.)
- **Dar la vuelta a la fracción.** Si dudas de cuál va arriba, usa el sentido común: menos espiras en el secundario tienen que dar menos tensión. Si te sale más, la has puesto al revés.

## Compruébalo tú

1. Un transformador tiene 500 espiras en el primario y 50 en el secundario. Se conecta a 120 V de alterna. ¿Qué tensión da el secundario?
2. ¿Es reductor o elevador?
3. Ese secundario entrega 5 A a un aparato. ¿Qué potencia entrega? ¿Qué corriente circula por el primario, suponiendo que no hay pérdidas?
4. Un transformador tiene 100 espiras en el primario y 1.000 en el secundario. Se le aplican 10 V de alterna. ¿Qué sale?
5. Conectas el primario de un transformador a una batería de coche. ¿Qué tensión aparece en el secundario al cabo de unos segundos?
6. En un transformador reductor, ¿cuál de las dos bobinas tiene el hilo más grueso, y por qué?

**Soluciones**

1. U = 120 × (50 / 500) = 120 × 0,1 = **12 V**.
2. **Reductor**: el secundario tiene menos espiras y da menos tensión.
3. Potencia: P = 12 × 5 = **60 W**. Por el primario: I = P / U = 60 / 120 = **0,5 A**. (La tensión ha bajado diez veces; la corriente del secundario es diez veces la del primario.)
4. U = 10 × (1.000 / 100) = **100 V**. Es un elevador.
5. **Ninguna.** Con corriente continua el campo no cambia y no se induce tensión. Además, el primario se calentaría peligrosamente.
6. El **secundario**: trabaja con menos tensión y más corriente, y las corrientes grandes necesitan hilo grueso.

## En una frase

Un transformador son dos bobinas sobre un mismo núcleo: la tensión de salida es la de entrada multiplicada por la relación de espiras, la corriente cambia en la proporción contraria para que la potencia se conserve, solo funciona con alterna y además aísla y adapta impedancias.

Con resistencias, condensadores, bobinas y transformadores se puede hacer mucho, pero falta algo: ninguno de ellos puede decidir en qué sentido pasa la corriente, ni hacer que una señal débil controle a una fuerte. Para eso hace falta un material distinto.
