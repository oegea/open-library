Ya sabes qué es la ionosfera y qué hace cada una de sus capas. Con eso se entiende *por qué* la banda de 40 metros cambia tanto de la tarde a la noche. Lo que todavía no puedes contestar es la pregunta que un operador se hace cada vez que se sienta ante el equipo: *¿en qué banda me pongo ahora para llegar hasta allí?*

Para contestarla hacen falta tres números, que tienen nombre y que el examen pregunta con su definición: la frecuencia crítica, la MUF y la LUF. Entre los tres dibujan una ventana, y todo el arte de elegir banda consiste en saber dónde está esa ventana en cada momento.

## La frecuencia crítica: el disparo a plomo

Empecemos por el caso más difícil para la ionosfera: una onda lanzada hacia arriba en **vertical**. Para volver tiene que darse la vuelta completa.

Si vas subiendo la frecuencia de esa onda vertical, llega un momento en que la capa ya no consigue devolverla y la onda la atraviesa. La frontera es la **frecuencia crítica**.

> **Frecuencia crítica:** la frecuencia más alta que una capa de la ionosfera devuelve a tierra cuando la onda incide verticalmente.

No es un número fijo: cambia con la hora, la estación y la actividad del sol, porque depende de cuánta ionización haya en ese momento. Se mide continuamente desde el suelo con unos aparatos llamados *ionosondas*, que lanzan pulsos hacia arriba, barriendo frecuencias, y anotan cuáles vuelven. Para la capa F2 suele estar entre 3 y 12 MHz.

## La MUF: la frecuencia más alta que sirve para un trayecto

En la práctica nadie lanza las ondas en vertical: las que van lejos salen tumbadas. Y recuerda el espejismo de la carretera: una onda que llega a la capa muy tumbada necesita girar poco, y vuelve con facilidad. Por eso, para un trayecto largo, la ionosfera devuelve frecuencias bastante más altas que la crítica.

> **MUF (frecuencia máxima utilizable):** la frecuencia más alta que la ionosfera devuelve a tierra para un trayecto concreto en un momento concreto. (Las siglas son del inglés *Maximum Usable Frequency*.)

Tres cosas que conviene tener claras:

- La MUF es **de un trayecto**, no «del día». A la misma hora, la MUF hacia Italia y la MUF hacia Argentina son distintas, porque las ondas llegan a la capa con ángulos distintos y la cruzan por sitios distintos.
- **Cuanto más largo es el salto, más alta es la MUF**, porque la onda llega más tumbada. En saltos largos puede ser hasta unas **tres veces** la frecuencia crítica.
- Por encima de la MUF no hay nada que hacer: la onda atraviesa la capa y se va al espacio. Da igual la potencia.

**Ejemplo.** *La frecuencia crítica de la capa F2 es ahora de 6 MHz. ¿Sirve la banda de 20 metros (14 MHz) para un contacto a 3.000 km?*

En un salto largo la MUF puede llegar a unas tres veces la crítica: 3 × 6 = 18 MHz. Como 14 MHz queda por debajo de 18, la banda de 20 metros debería estar abierta para ese trayecto. En cambio, la de 10 metros (28 MHz) queda muy por encima: estará cerrada.

Cuidado con aplicar ese «por tres» a cualquier distancia. Vale para saltos largos, de 3.000 km o más. Para un trayecto de 1.000 km el factor es de alrededor de 1,5, y para 300 km, apenas 1,1: casi la propia frecuencia crítica. Por eso, para hablar con alguien que está cerca hay que usar una frecuencia **por debajo de la crítica** y lanzar la onda casi en vertical, con una antena horizontal baja. Esa técnica tiene nombre, **NVIS** (del inglés *Near Vertical Incidence Skywave*, onda de cielo de incidencia casi vertical), y es la que usan las redes de emergencia en 80 y 40 metros.

## La LUF: el suelo de la ventana

Si por arriba el límite lo pone la capa que devuelve, por abajo lo pone la capa que absorbe. Recuerda que la capa D se come las frecuencias bajas, y más cuanto más bajas.

> **LUF (frecuencia mínima utilizable):** la frecuencia más baja con la que todavía es posible la comunicación en un trayecto, porque por debajo de ella la absorción de la capa D debilita demasiado la señal. (Del inglés *Lowest Usable Frequency*.)

Hay una diferencia de carácter entre las dos fronteras. La MUF es un muro: por encima, la onda se va y no hay arreglo. La LUF es una cuesta: por debajo, la señal llega cada vez más débil, y con más potencia o mejor antena se puede bajar un poco. De día la LUF es alta, porque la capa D está fuerte. De noche cae, porque la capa D desaparece.

## La ventana

Entre las dos queda el tramo de frecuencias que funcionan en ese trayecto y en ese momento.

![La ventana de frecuencias útiles para un trayecto. Por debajo de la LUF, la capa D absorbe la señal. Entre la LUF y la MUF está la ventana útil, y las mejores señales se obtienen cerca de la MUF. Por encima de la MUF, la onda atraviesa la ionosfera y se pierde en el espacio.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s09-ventana-muf-luf.svg)

Y dentro de la ventana no todas las frecuencias son iguales:

> **Las mejores señales se consiguen algo por debajo de la MUF.** Cuanto más alta es la frecuencia, menos absorbe la capa D, así que conviene usar la banda más alta que todavía esté abierta.

Como la MUF sube y baja de un minuto a otro, no se apura hasta el límite: se trabaja en torno al 85 % de la MUF. Los manuales llaman a ese valor *frecuencia óptima de trabajo* (FOT).

Esa es la regla práctica que usan todos los operadores de HF: de día se sube de banda (20, 15, 10 metros), porque la MUF está alta y abajo la capa D absorbe; de noche se baja (40, 80 metros), porque la MUF cae y abajo ya no hay quien absorba.

Hay días en que la ventana se estrecha hasta cerrarse, porque sube la LUF, porque baja la MUF o por las dos cosas. Las causas son perturbaciones que vienen del sol, y las verás dentro de dos lecciones. Es lo que los aficionados llaman «las bandas muertas».

## Donde la gente se lía

- **Confundir frecuencia crítica y MUF.** La crítica es para una onda **vertical** y es propia de la capa. La MUF es para un **trayecto** concreto, con la onda inclinada, y es siempre igual o mayor que la crítica.
- **«Por encima de la MUF, con más potencia paso.»** No. Por encima de la MUF la onda atraviesa la ionosfera, con un vatio o con mil.
- **«Cuanto más baja la frecuencia, más seguro.»** De día, al revés: cuanto más baja, más absorbe la capa D. Lo mejor es estar algo por debajo de la MUF.
- **«La MUF es tres veces la crítica.»** Solo en saltos muy largos. Para distancias cortas es poco mayor que la crítica.
- **«La MUF de hoy es tal.»** No hay una MUF del día: hay una para cada trayecto y cada hora.

## Compruébalo tú

1. La frecuencia crítica de la capa F2 es de 8 MHz. Para un trayecto muy largo, ¿hasta qué frecuencia, aproximadamente, podría llegar la MUF?
2. Para un trayecto, la LUF es 5 MHz y la MUF es 16 MHz. ¿Cuál de estas bandas elegirías: 80 m (3,6 MHz), 20 m (14 MHz) o 15 m (21 MHz)? ¿Por qué?
3. Con una MUF de 20 MHz para tu trayecto, ¿en torno a qué frecuencia conviene trabajar según la regla del 85 %?
4. La frecuencia crítica es ahora de 5 MHz. Quieres hablar con una estación situada a 150 km. ¿Te sirve la banda de 40 metros (7 MHz)? ¿Y la de 80 (3,6 MHz)?
5. Al anochecer, ¿qué le pasa a la LUF y por qué?
6. ¿Qué diferencia hay entre lo que ocurre por encima de la MUF y lo que ocurre por debajo de la LUF?

**Soluciones**

1. Hasta unas tres veces la crítica: 3 × 8 = **unos 24 MHz**.
2. **20 metros**. Los 3,6 MHz están por debajo de la LUF (la capa D los absorbe) y los 21 MHz por encima de la MUF (atraviesan la ionosfera). Los 14 MHz están dentro de la ventana y, además, cerca de la MUF, donde la absorción es menor.
3. 0,85 × 20 = **17 MHz**. La banda de 20 metros (14 MHz) es la elección segura; la de 17 metros (18 MHz) queda algo por encima del 85 %, más cerca del límite.
4. La de 40 **no**: para una distancia tan corta la onda tiene que subir casi vertical, y a 7 MHz, por encima de la crítica, atravesaría la capa. La de **80 sí**: 3,6 MHz está por debajo de la crítica y vuelve aunque suba casi a plomo. Es la técnica NVIS.
5. **Baja**, porque la capa D, que es la que absorbe las frecuencias bajas, desaparece al ponerse el sol.
6. Por encima de la MUF la onda **se escapa** al espacio y no hay arreglo. Por debajo de la LUF la señal **se debilita** por absorción: es gradual, y algo se gana con más potencia o mejor antena.

## En una frase

Para cada trayecto y cada momento hay una ventana de frecuencias útiles: por arriba la cierra la MUF (más allá, la onda atraviesa la ionosfera) y por abajo la LUF (más abajo, la capa D la absorbe); lo mejor es trabajar algo por debajo de la MUF, y para distancias cortas, por debajo de la frecuencia crítica.

Sabemos ya qué frecuencias vuelven. En la lección siguiente, adónde: cuánto mide un salto, por qué a veces se oye Berlín y no Teruel, y por qué las señales lejanas respiran.
