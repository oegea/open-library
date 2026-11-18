Al fondo de la lata de Amparo, envuelta en un trapo, había una ampolla de vidrio del tamaño de un pulgar, con un bosque de piezas metálicas diminutas dentro y un culote de patillas. «Una válvula», dijo Vicente, sosteniéndola a contraluz. «Con esto se amplificaba cuando yo era chaval. Se encendían como bombillas y calentaban como estufas.» Era la «media familia» que faltaba: ya casi no se ven, pero el examen todavía pregunta por ellas.

Esta lección cierra la sección con tres cosas cortas: las válvulas, que hacían el trabajo del transistor antes de que existiera; los circuitos integrados, que meten miles de transistores en una sola pieza; y los símbolos con los que todos los componentes que has conocido se dibujan en un esquema. Al terminar sabrás reconocer cada componente de la sección por su símbolo, que es justo lo que el examen suele pedir.

## La media familia: las válvulas

Antes de que existiera el transistor, amplificar se hacía con **válvulas de vacío** (o *válvulas termoiónicas*, o *tubos*).

Una válvula es una ampolla de vidrio de la que se ha extraído el aire, con varias piezas metálicas dentro:

- Un **cátodo**, que un filamento calienta al rojo. En caliente, el metal suelta electrones al vacío.
- Una **placa** (o *ánodo*), conectada a una tensión positiva alta, que atrae a esos electrones. Entre cátodo y placa circula así una corriente a través del vacío.
- Entre los dos, una **rejilla**: una malla de alambre fino. Una pequeña tensión negativa en la rejilla repele a los electrones y frena su paso.

Es el mismo principio del grifo: la rejilla es la manecilla, y una tensión pequeña en ella controla la corriente grande entre cátodo y placa. La válvula con estas tres piezas se llama **triodo**. Añadiendo más rejillas para mejorar su comportamiento se obtienen el **tetrodo** (dos rejillas) y el **pentodo** (tres), que son los habituales en los amplificadores de potencia. Y con solo cátodo y placa, sin rejilla, la válvula deja pasar la corriente en un único sentido: fue el primer **diodo**. El diodo de silicio heredó de ella el nombre y hasta las palabras *ánodo* y *cátodo*.

Comparadas con un transistor, las válvulas son grandes, frágiles, necesitan cientos de voltios y gastan mucha energía solo en calentar el filamento. Sobreviven en dos sitios: los amplificadores de gran potencia para onda corta y los equipos de audio de los aficionados al sonido clásico.

## Circuitos integrados

Un **circuito integrado** (**CI**, o *chip*) no es un componente nuevo: es un circuito completo —transistores, diodos, resistencias y condensadores, con sus conexiones— fabricado de una sola vez sobre una plaquita de silicio de pocos milímetros, y encerrado en una cápsula con patas.

Los hay desde muy sencillos, con unas decenas de transistores, hasta los procesadores, que contienen miles de millones. El ejemplo clásico de integrado sencillo es el **amplificador operacional**: un amplificador completo y de ganancia enorme metido en una cápsula de ocho patas, al que basta añadir un par de resistencias para que amplifique exactamente lo que uno quiera. En un equipo de radio encontrarás integrados haciendo de amplificadores, de generadores de frecuencia o, en los walkies más baratos, de radio completa: un solo chip al que se le añade poco más que el micrófono, el altavoz y la antena.

Para el examen basta con la idea: muchos componentes en una sola pieza, más pequeños, más baratos y más fiables que montados uno a uno.

## Los símbolos de un esquema

Un **esquema** es el plano de un circuito: un dibujo que muestra qué componentes tiene y cómo están conectados entre sí, sin preocuparse de su aspecto real. En él, cada componente se representa con un símbolo. Has ido viendo algunos por el camino (el zigzag de la resistencia, el triángulo del diodo); aquí están todos los de la sección. El examen suele enseñar un símbolo y preguntar qué es, así que merece la pena mirarlos con calma.

![Lámina con los símbolos de los componentes de la sección. Resistencia: una línea en zigzag. Potenciómetro: una resistencia con una flecha que la toca. Condensador: dos rayas paralelas. Condensador electrolítico: lo mismo con un signo más en una placa. Condensador variable: un condensador atravesado por una flecha. Bobina: una serie de bucles. Bobina con núcleo: los bucles con dos rayas al lado. Transformador: dos bobinas enfrentadas con dos rayas entre ellas. Diodo: un triángulo que choca contra una barra. LED: un diodo con dos flechitas que salen. Zéner: un diodo con la barra doblada en los extremos. Varicap: un diodo con una segunda barra paralela. Transistor NPN: un círculo con tres patas y la flecha del emisor hacia fuera. Transistor PNP: igual con la flecha hacia dentro. Transistor de efecto de campo: un círculo con la puerta señalada por una flecha.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-simbolos.svg)

Tres pistas para no confundirlos:

- Los diodos se distinguen entre sí por la **barra**: recta en el diodo normal, con los extremos doblados en el zéner, doble en el varicap. El LED es el que tiene flechitas saliendo (la luz).
- NPN y PNP se distinguen por la **flecha del emisor**: hacia fuera en el NPN, hacia dentro en el PNP.
- El condensador electrolítico es el que lleva el signo **+**; todo lo que lleve una flecha atravesada (condensador variable, potenciómetro) es ajustable.

## Donde la gente se lía

- **«Las válvulas son una tecnología distinta que no tiene nada que ver con el transistor.»** Hacen lo mismo con otros medios: una rejilla controla un flujo de electrones, igual que la base o la puerta controlan el de un transistor.
- **«Un circuito integrado es un tipo de componente nuevo.»** Es un circuito entero, hecho con los componentes de siempre, fabricado en una sola pieza.
- **«Triodo, tetrodo y pentodo tienen tres, cuatro y cinco rejillas.»** El nombre cuenta todas las piezas activas, no solo las rejillas: el triodo tiene una rejilla (más cátodo y placa), el tetrodo dos y el pentodo tres.
- **«El símbolo se parece al componente.»** Un símbolo no dice nada del aspecto ni del tamaño real de la pieza; solo dice qué es y cómo está conectada.

## Compruébalo tú

1. En una válvula triodo, ¿qué pieza hace el papel de la base de un transistor?
2. ¿Por qué necesita una válvula un filamento que se pone al rojo?
3. ¿Cómo se llama la válvula que tiene tres rejillas?
4. En un esquema ves dos series de bucles enfrentadas, con dos rayas entre ellas. ¿Qué componente es, y qué te dicen las dos rayas?
5. En un esquema ves un triángulo que choca contra una barra con los extremos doblados. ¿Qué componente es y para qué sirve?
6. ¿Y dos rayas paralelas, una de ellas con un signo «+»? ¿Qué precaución exige ese componente?
7. ¿En qué se distingue el símbolo de un potenciómetro del de una resistencia normal?

**Soluciones**

1. La **rejilla**: una pequeña tensión en ella controla la corriente entre cátodo y placa.
2. Para calentar el cátodo: solo en caliente suelta el metal los electrones que luego viajan por el vacío hasta la placa.
3. **Pentodo.** (Con una rejilla, triodo; con dos, tetrodo.)
4. Un **transformador**. Las dos rayas representan su núcleo de hierro o ferrita.
5. Un **diodo zéner**: mantiene una tensión fija y estable entre sus patas, y se usa como referencia o regulador de tensión.
6. Un **condensador electrolítico**. Tiene polaridad: hay que conectarlo con el positivo y el negativo en su sitio, porque al revés se destruye.
7. En que lleva una **flecha** que toca la resistencia: representa el cursor que se desliza sobre ella.

## En una frase

Las válvulas amplificaban con una rejilla que gobierna electrones en el vacío; un circuito integrado reúne miles o millones de transistores en una sola pieza; y cada componente tiene un símbolo con el que se dibuja en los esquemas, que conviene reconocer a primera vista.

Con esto quedan presentadas, ahora sí, las cuatro familias y media. Marina y Lucía ya sabían llamar por su nombre a cada pieza de la «ciudad de cobre» del receptor gris; faltaba entender qué hacen juntas, porque un componente suelto es como una letra: no dice nada hasta que se combina con otras. De eso trata la sección siguiente. Antes, el resumen de esta sección incluye un regalo de Vicente que no entra en el examen pero vale una reparación: cómo se estropea cada familia de componentes.
