En la lección anterior, el condensador se cargaba con la batería, la corriente se detenía y ahí acababa todo. Si eso fuera lo único que sabe hacer, sería una curiosidad. Lo que lo convierte en una de las piezas clave de la radio es cómo se comporta con la **corriente alterna**, la que va y viene (la conociste en la sección 3: los electrones avanzan y retroceden, tantas veces por segundo como indique la frecuencia, en hercios).

Al terminar esta lección entenderás la frase que el examen pregunta casi siempre —«el condensador bloquea la continua y deja pasar la alterna»— y sabrás calcular cuánto estorba un condensador a cada frecuencia.

## Con corriente continua: un muro

Repasemos lo que ya sabes, porque es la mitad de la frase.

Al conectar un condensador a una batería circula corriente durante un momento, mientras se carga. En cuanto su tensión iguala a la de la batería, la corriente se detiene y no vuelve a circular. A partir de ahí, para la corriente continua el condensador es lo que parece: un circuito abierto.

> **En corriente continua, un condensador no conduce** (salvo el instante en que se carga). Bloquea el paso.

En el agua: la bomba empuja siempre hacia el mismo lado, la membrana de goma se abomba hasta donde da de sí y el agua se para.

## Con corriente alterna: una puerta

Ahora cambia la batería por una fuente de alterna, que empuja primero hacia un lado y luego hacia el otro, sin parar.

Vicente hizo la prueba con una bombillita, una pequeña fuente que daba unos pocos voltios de corriente alterna y un condensador grande, de unos 100 µF y de un tipo *sin polaridad* (un electrolítico normal no vale para esto: la alterna lo conectaría al revés cincuenta veces por segundo). Los puso en fila. La bombilla se encendió y se quedó encendida.

—No puede ser —dijo Marina—. Me acabas de decir que por dentro hay un aislante. ¿Por dónde pasa?

—No pasa. Mira el agua.

Vuelve a la tubería cerrada por la membrana, pero ahora cambia la bomba por el émbolo de la sección 3, que empuja el agua y tira de ella sin parar:

1. El émbolo empuja hacia la derecha. La membrana se abomba hacia la derecha, y mientras lo hace **se mueve agua en toda la tubería**, a los dos lados de la membrana.
2. Antes de que la membrana llegue a su tope, el émbolo cambia de sentido. La membrana vuelve al centro y se abomba hacia la izquierda. El agua de toda la tubería se mueve ahora en sentido contrario.
3. Y vuelta a empezar.

El agua de la tubería **no para de ir y venir**. Si en algún punto de la tubería hay algo que roza con el agua —recuerda las manos frotadas de la sección 3, que se calientan igual al ir que al volver—, se calentará con ese vaivén. Y sin embargo, ni una gota ha atravesado la membrana.

Eso es exactamente lo que ocurre en el condensador. Sus placas se cargan en un sentido, se descargan, se cargan en el sentido contrario, se descargan… Por los cables, los electrones van y vienen continuamente, y ese ir y venir **es** corriente alterna. La bombilla, que está en el camino, se enciende.

> **En corriente alterna, por el circuito de un condensador circula corriente**, aunque ningún electrón atraviese su dieléctrico. Se dice, abreviando, que el condensador «deja pasar» la alterna.

![Dos tuberías cerradas por una membrana de goma. A la izquierda, con una bomba que empuja siempre hacia el mismo lado (corriente continua), la membrana se abomba, llega a su tope y el agua se detiene. A la derecha, con un émbolo que empuja alternativamente hacia un lado y hacia el otro (corriente alterna), la membrana oscila y el agua de toda la tubería va y viene sin parar.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-condensador-cc-ca.svg)

## Deja pasar… ¿cuánto?

Un condensador no deja pasar igual todas las alternas. Depende de dos cosas, y las dos se entienden con la membrana.

**De la frecuencia.** Si el émbolo cambia de sentido muy despacio (frecuencia baja), a la membrana le da tiempo a abombarse casi hasta su tope en cada empujón, y cuando está tensa frena el agua. Circula poca. Si el émbolo cambia de sentido muy deprisa (frecuencia alta), la membrana apenas ha empezado a moverse cuando ya la empujan hacia el otro lado: nunca llega a tensarse y casi no estorba. Circula mucha.

Hay otra manera aún más sencilla de verlo. En cada vaivén se mueve una cierta cantidad de carga, la que cabe en el condensador. Si ese mismo vaivén se repite más veces por segundo, se mueve más carga cada segundo. Y carga por segundo es, por definición, corriente.

**De la capacidad.** Una membrana grande y blanda (mucha capacidad) admite mucho vaivén de agua sin tensarse apenas. Una pequeña y tiesa (poca capacidad) se tensa enseguida y frena.

La conclusión, que hay que saber de memoria:

> Un condensador se opone a la corriente alterna **tanto menos cuanto mayor es la frecuencia y cuanto mayor es su capacidad.**

## La reactancia capacitiva

A esa oposición que el condensador presenta a la alterna hay que ponerle nombre y número.

> **Reactancia capacitiva:** la oposición que un condensador presenta al paso de la corriente alterna. Se escribe **XC** y se mide en **ohmios**, igual que la resistencia.

Se mide en ohmios porque hace el mismo papel que la resistencia en la ley de Ohm: la corriente que circula es la tensión dividida entre la reactancia, **I = U / XC**. Un condensador con una reactancia de 100 Ω deja pasar, con 10 V de alterna, 10 / 100 = 0,1 A. (Los voltios y amperios de alterna de esta lección son siempre valores eficaces, los que conociste en la sección 3.)

Su valor se calcula así:

**XC = 1 / (2 × π × f × C)**

con f en hercios, C en faradios y el resultado en ohmios. Vamos a leerla sin miedo:

- La **f** y la **C** están *debajo* de la división. Cuanto mayores sean, mayor es el número por el que se divide y menor el resultado. Es justo lo que acabamos de deducir con la membrana: más frecuencia o más capacidad, menos oposición.
- El **2 × π** es un número fijo: aproximadamente 6,28. (π, «pi», vale 3,14 y aparece en cualquier cosa que gire u oscile.) No hay que entenderlo más: trátalo como un factor que siempre está ahí.

Así que, para hacer cuentas, la fórmula es en la práctica:

**XC = 1 / (6,28 × f × C)**

**Ejemplo, paso a paso.** *¿Qué reactancia tiene un condensador de 1 µF a 50 Hz?*

1. Unidades básicas: 1 µF = 0,000001 F.
2. Lo de abajo: 6,28 × 50 × 0,000001 = 0,000314.
3. XC = 1 / 0,000314 ≈ **3.185 Ω**.

Ahora el mismo condensador a frecuencias cada vez mayores:

| Frecuencia | Reactancia del condensador de 1 µF |
|---|---|
| 0 Hz (continua) | infinita: no pasa nada |
| 50 Hz (la red eléctrica) | unos 3.185 Ω |
| 5.000 Hz (un silbido agudo) | unos 32 Ω |
| 5 MHz (una señal de radio) | 0,03 Ω: como un cable |

El mismo componente es un muro para la continua, un buen estorbo a 50 Hz y prácticamente un cable para una señal de radio. Fíjate además en la proporción: al multiplicar la frecuencia por 100, la reactancia se ha dividido entre 100.

Cuando lleguemos a la bobina, en la lección 5, verás las dos reactancias dibujadas juntas, una frente a otra.

### En qué se diferencia de una resistencia

Reactancia y resistencia se miden las dos en ohmios y las dos limitan la corriente, pero hay dos diferencias que conviene conocer:

- **La resistencia gasta; la reactancia no.** Una resistencia convierte en calor la energía que frena. Un condensador no la gasta: la guarda durante un cuarto de ciclo y la devuelve en el cuarto siguiente, como la membrana, que devuelve el empuje que recibió. Un condensador ideal no se calienta.
- **La resistencia vale lo mismo a cualquier frecuencia; la reactancia no.** Esa es precisamente su gracia.

Hay una tercera diferencia más sutil, que el examen menciona. En una resistencia, la corriente y la tensión suben y bajan a la vez. En un condensador van desacompasadas. Sigue un ciclo paso a paso:

1. La tensión entre las placas pasa por cero: el condensador está vacío, nada frena la carga y **la corriente es máxima**.
2. Un cuarto de ciclo después, la tensión llega a su máximo: el condensador está lleno y **la corriente es cero**.
3. La tensión empieza a bajar: la corriente ya circula en sentido contrario, descargándolo.

La corriente llega a cada punto de su ciclo —a su máximo, a su cero— un cuarto de ciclo *antes* de que la tensión llegue al suyo. Por eso se dice que en un condensador **la corriente va adelantada un cuarto de ciclo respecto a la tensión**; en el lenguaje de la fase que viste en la sección 3, un desfase de 90°.

## Para qué sirve todo esto

Con este comportamiento, el condensador se convierte en el portero de los circuitos: decide qué pasa y qué no según la frecuencia. Tres trabajos que hace constantemente en cualquier radio:

- **Separar la señal de la alimentación.** En un punto de un circuito suelen convivir una tensión continua (la que hace funcionar esa parte del aparato) y una señal alterna pequeña (la voz, la radio). Un condensador en fila deja seguir a la señal hacia la parte siguiente del circuito y detiene a la continua. Se le llama **condensador de acoplo**.
- **Tirar a la basura lo que sobra.** Un condensador colocado entre un cable y la masa ofrece a las frecuencias altas un camino fácil para irse por ahí en vez de seguir adelante. Así se limpian de ruido las alimentaciones. Se le llama **condensador de desacoplo**.
- **Formar filtros y circuitos de sintonía**, en pareja con la bobina. Es el tema estrella de la sección 5.

## Donde la gente se lía

- **«Si deja pasar la alterna, es que los electrones lo cruzan.»** No lo cruzan nunca. Van y vienen por los cables, cargando y descargando las placas.
- **«A más frecuencia, más reactancia.»** Al revés en el condensador: a más frecuencia, **menos** reactancia. (En la bobina será al contrario, y el examen juega con esa confusión.)
- **«A más capacidad, más oposición.»** También al revés: un condensador mayor estorba menos.
- **Meter microfaradios en la fórmula.** La fórmula quiere faradios. 1 µF son 0,000001 F.
- **«Bloquea la continua» no significa que no le afecte.** Se carga con ella y se queda con su tensión; lo que no hace es dejar que siga circulando.

## Compruébalo tú

1. Conectas una bombilla en fila con un condensador a una batería de 12 V. ¿Se queda encendida?
2. ¿Y si los conectas a una fuente de corriente alterna?
3. La reactancia de un condensador a 1.000 Hz es de 200 Ω. Sin usar la fórmula, ¿cuánto valdrá a 2.000 Hz?
4. Calcula la reactancia de un condensador de 10 µF a 100 Hz.
5. A un condensador cuya reactancia es de 50 Ω se le aplican 5 V de alterna. ¿Qué corriente circula?
6. Tienes dos condensadores, uno de 1 nF y otro de 100 nF. ¿Cuál ofrece más oposición a una misma señal?
7. En un cable hay 9 V de continua y, superpuesta, una pequeña señal de audio. ¿Qué pones para que a la parte siguiente del circuito llegue solo el audio?

**Soluciones**

1. No. Puede dar un destello en el instante de la carga, pero en cuanto el condensador se carga, la corriente se detiene.
2. Sí: el condensador se carga y descarga continuamente, por los cables circula corriente alterna y la bombilla luce.
3. A doble frecuencia, mitad de reactancia: **100 Ω**.
4. 10 µF = 0,00001 F. Abajo: 6,28 × 100 × 0,00001 = 0,00628. XC = 1 / 0,00628 ≈ **159 Ω**.
5. I = U / XC = 5 / 50 = **0,1 A**.
6. El de **1 nF**: menos capacidad, más reactancia. En concreto, cien veces más.
7. Un condensador en fila (de acoplo): detiene la continua y deja pasar la señal alterna.

## En una frase

Un condensador bloquea la corriente continua y deja circular la alterna, tanto mejor cuanto mayor es la frecuencia y mayor su capacidad; esa oposición se llama reactancia capacitiva, se mide en ohmios y vale XC = 1 / (6,28 × f × C).

El condensador tiene un hermano que hace exactamente lo contrario. Para entenderlo hay que hablar primero de imanes.
