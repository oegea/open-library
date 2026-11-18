Además del cable, Dani subió a la azotea un cacharro que parecía un yoyó gordo: unas vueltas de coaxial enrolladas sobre un anillo negro.

—Esto es para que el cable no se ponga a hacer de antena por fuera —dijo.

—Pero si el otro día dijiste que el coaxial estaba blindado y que de él no salía nada —protestó Lucía.

—Por dentro. Por fuera es otra historia.

Esta lección cuenta esa otra historia. Al terminar sabrás por qué un cable blindado puede ponerse a radiar, qué síntomas da cuando lo hace y cómo lo impide el balun. Es pregunta directa de examen.

Un recordatorio antes de empezar: el coaxial tiene dos conductores, el vivo en el centro y la malla alrededor, y la onda viaja encerrada entre los dos.

## Antena simétrica, cable asimétrico

Para entender el yoyó hay que fijarse en una diferencia entre la antena y el cable.

- Un **dipolo** tiene dos brazos idénticos. Ninguno de los dos está conectado a tierra ni a nada más. Se dice que es una antena **simétrica**, o *equilibrada*: sus dos mitades son iguales.
- Un **cable coaxial** tiene dos conductores completamente distintos: un hilo en el centro y un tubo alrededor, que además va unido a la carcasa del equipo. Es una línea **asimétrica**, o *no equilibrada*.

Al conectar directamente uno con otro aparece un problema.

## Un dato nuevo: el efecto pelicular

Para entender ese problema hace falta un dato que no ha salido hasta ahora en el curso.

La corriente de radiofrecuencia no circula por todo el grosor de un conductor. Circula solo por una capa finísima de su superficie, de centésimas de milímetro. Se llama **efecto pelicular** (de *película*, capa fina), y es tanto más acusado cuanto mayor es la frecuencia.

La consecuencia es que la malla del coaxial, aunque sea una sola pieza de cobre, se comporta como dos conductores distintos: su **cara interior**, que mira al vivo, y su **cara exterior**, que mira al mundo. La corriente que va por una cara no se entera de la que va por la otra. Lo que dijimos en la lección 6 —que la onda viaja encerrada dentro del cable— se refiere a la cara interior. La exterior es, para la radiofrecuencia, un conductor aparte.

## La corriente que no debería estar ahí

Ahora sí. Al final del cable, la corriente que sube por el vivo se va al brazo que le corresponde. La que circula por la **cara interior** de la malla debería irse entera al otro brazo. Pero al llegar al final del cable se encuentra con dos caminos posibles: el brazo del dipolo, que es por donde debe ir, y la **cara exterior** de la propia malla, que es otro conductor que baja desde ahí hasta la casa.

Una parte de la corriente toma ese segundo camino y baja por el exterior del cable. A esa corriente indeseada se le llama **corriente de modo común**. El nombre quiere decir que el cable, visto desde fuera, se comporta como un simple hilo con corriente.

Y un hilo con corriente de radiofrecuencia por fuera es, como ya sabes, una antena. El cable de bajada se pone a radiar. Las consecuencias:

- El cable radia a lo largo de toda su bajada, pegado a la fachada y dentro de casa: justo donde están los televisores, los teléfonos y los vecinos. Es una fuente clásica de interferencias.
- La radiofrecuencia llega por el exterior del cable hasta el equipo. Síntomas típicos: el micrófono da pequeños «mordiscos» en los labios, o el ordenador se bloquea al transmitir. En la jerga se dice que hay «RF en la estación».
- El diagrama de la antena se deforma, porque ya no radia solo el dipolo.
- En recepción, el cable recoge por fuera el ruido de todos los aparatos de la casa y lo lleva hasta el receptor.

![Dos dipolos alimentados con cable coaxial. A la izquierda, sin balun: una parte de la corriente baja por el exterior de la malla y el cable radia hacia la casa. A la derecha, con un balun en el punto de alimentación: la corriente exterior queda bloqueada y solo radia la antena.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-balun.svg)

## El balun

La solución es el **balun**. El nombre junta dos palabras inglesas: *BALanced* (equilibrado) y *UNbalanced* (no equilibrado).

> **Balun:** dispositivo que se coloca entre una línea asimétrica (el coaxial) y una antena simétrica (el dipolo) para pasar de una a otra e impedir que circule corriente por el exterior de la malla del cable.

El de Dani era del tipo más sencillo, un **balun de choque**: unas cuantas vueltas del propio cable enrolladas sobre un anillo de ferrita. (Recuerda de la sección 4 que un choque es una bobina puesta para cerrar el paso a la radiofrecuencia.) (La ferrita es ese material cerámico magnético que conociste en la sección 4.) Para la corriente que viaja *por dentro* del cable, esas vueltas no existen: sigue encerrada entre el vivo y la malla y no se entera. Para la corriente que intenta bajar *por fuera* de la malla, las vueltas sobre la ferrita son una bobina con muchísima oposición a la radiofrecuencia. Se le cierra el paso.

Hay también baluns que, además de eso, **transforman la impedancia**. Son pequeños transformadores, y se nombran por su relación de impedancias: uno de 4:1 convierte 200 Ω en 50 Ω. (Ojo: 4:1 es la relación de *impedancias*. En espiras es 2:1, porque la impedancia va con el cuadrado de la relación de espiras, como viste al estudiar el transformador.) Se usan con antenas cuya impedancia queda lejos de la del cable: un dipolo plegado de 300 Ω, por ejemplo, o una bajada de línea paralela. Un balun que no transforma se llama 1:1.

¿Y la vertical de cuarto de onda? Ya es una antena asimétrica: una varilla por un lado y un plano de tierra por otro, igual que el coaxial tiene un vivo y una malla. No necesita balun para adaptarse, aunque un choque en el cable ayuda muchas veces a mantener limpia la bajada.

## Donde la gente se lía

- **«El coaxial está blindado, así que no puede radiar.»** Lo que va por dentro está blindado. La cara exterior de la malla es otro conductor, y radia si le llega corriente.
- **«El balun es un amplificador» o «el balun es un filtro».** Ni una cosa ni otra. Permite unir una línea asimétrica a una antena simétrica y evita que la malla del cable radie.
- **«Un balun 4:1 tiene cuatro veces más espiras en un lado.»** 4:1 es la relación de impedancias. En espiras es 2:1.
- **«Si mi ROE es buena, no tengo corriente por fuera del cable.»** La ROE mide lo que pasa por dentro del cable. Una instalación puede tener una ROE excelente y un cable que radia.

## Compruébalo tú

1. Al transmitir, notas un cosquilleo en los labios al acercarlos al micrófono y el televisor del vecino hace rayas. ¿Qué sospechas y qué pieza probarías a añadir?
2. ¿Qué impedancia transforma en 50 Ω un balun de relación 4:1? ¿Cuál es su relación de espiras?
3. De estas tres cosas, ¿cuáles son simétricas y cuáles asimétricas: un dipolo, un cable coaxial, una línea paralela?
4. La malla de un coaxial es una sola pieza de cobre. ¿Por qué se dice que, para la radiofrecuencia, se comporta como dos conductores?
5. ¿Dónde se coloca el balun de un dipolo: junto al equipo o en el punto de alimentación de la antena?
6. ¿Necesita un balun una vertical de cuarto de onda alimentada con cable coaxial? ¿Por qué?

**Soluciones**

1. **Corriente de modo común**: la cara exterior de la malla está radiando y llevando radiofrecuencia hasta el equipo y hacia la casa del vecino. Probaría a añadir un **balun** (un choque) en el punto de alimentación de la antena.
2. Cuatro veces 50: **200 Ω**. En espiras, **2:1**, porque la impedancia va con el cuadrado de la relación de espiras.
3. El **dipolo** y la **línea paralela** son simétricos: sus dos mitades son iguales. El **coaxial** es asimétrico.
4. Por el **efecto pelicular**: la radiofrecuencia circula solo por una capa finísima de la superficie de los conductores, de modo que la cara interior y la cara exterior de la malla llevan corrientes independientes.
5. En el **punto de alimentación de la antena**, que es donde la corriente encuentra el camino indebido hacia el exterior de la malla.
6. Para pasar de simétrico a asimétrico, **no**: la vertical ya es asimétrica (una varilla y un plano de tierra), igual que el coaxial (un vivo y una malla). Aun así, un choque en el cable suele ayudar a que la bajada no radie.

## En una frase

Para la radiofrecuencia, la cara exterior de la malla del coaxial es un conductor aparte; al unir un cable asimétrico con una antena simétrica, parte de la corriente se escapa por ella y el cable radia, y el balun, colocado en el punto de alimentación, le cierra ese camino.

Con esto tienes la estación entera, de la mesa a la azotea. Marina lo resumió esa noche en su cuaderno mejor que cualquier manual: la diferencia entre el hilo del balcón y el dipolo de la azotea no la hace ningún amplificador de ninguna tienda; la hacen la altura, la medida y el acuerdo. El material siguiente resume toda la sección en una chuleta para repasar antes del examen.
