Todas las ondas de las lecciones anteriores eran senoides perfectas. En el mundo real, las ondas se deforman: un **amplificador** (el circuito que hace más grande una señal; lo conocerás en las secciones 4 y 5) forzado más de la cuenta las aplasta, un circuito defectuoso las recorta. Y una onda deformada trae consigo una sorpresa que, para quien transmite, es un problema serio: aparece en frecuencias donde nadie la ha puesto.

Al terminar esta lección sabrás qué es un armónico, cómo se calcula en qué frecuencia cae cada uno, por qué una onda que no es senoidal los lleva dentro, y por qué eso obliga a todo transmisor a salir al aire a través de un filtro.

## Una senoide es una sola frecuencia

Empecemos por una propiedad de la senoide que hasta ahora no hemos dicho con todas las letras:

> **Una senoide pura contiene una única frecuencia.**

Si una emisora transmitiera una senoide perfecta de 7 MHz, en un receptor aparecería en 7 MHz y en ningún otro punto del dial. Es la onda más «limpia» que existe. En sonido, una senoide pura suena como un silbido liso, sin carácter: el pitido de un diapasón.

Ahora la pregunta es qué pasa con las ondas que **no** son senoides.

## Ondas con otras formas

Una onda puede repetirse ciclo tras ciclo, con su periodo y su frecuencia bien definidos, y no tener la forma suave de la senoide. Algunas formas son tan habituales que tienen nombre:

- La **onda cuadrada**: la tensión salta de golpe a un valor, se queda ahí medio ciclo, salta de golpe al valor contrario y se queda el otro medio. Es lo que produce un interruptor que se abre y se cierra a ritmo regular, y es la forma de las señales de los ordenadores.
- La **onda en diente de sierra**: sube en rampa y cae de golpe.
- La **onda triangular**: sube en rampa y baja en rampa.
- Y la **senoide recortada**: una senoide a la que le han cortado las crestas, como si hubiera chocado con un techo. Es la que más nos va a importar.

A todas ellas se les llama **ondas no senoidales**. Tienen su frecuencia —siguen completando tantos ciclos por segundo—, pero su forma es otra.

## El descubrimiento: toda onda es una suma de senoides

A principios del siglo XIX, el matemático francés Joseph Fourier demostró algo que nadie esperaba:

> **Cualquier onda que se repite, tenga la forma que tenga, es igual a una suma de senoides:** una senoide de la misma frecuencia que la onda, más otras senoides de frecuencias dos, tres, cuatro… veces mayores.

Dicho así cuesta creerlo, así que mira cómo se fabrica una onda cuadrada a base de sumar senoides.

![Tres gráficos apilados. En el primero, una senoide sola: la fundamental. En el segundo, la suma de la fundamental y su tercer armónico, tres veces más rápido y más pequeño: la onda resultante tiene los lados más verticales y la parte alta más plana. En el tercero se añade además el quinto armónico: la onda ya se parece claramente a una onda cuadrada, que aparece dibujada con línea de puntos.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-suma-de-armonicos.svg)

- Arriba, una senoide sola.
- En el centro, a esa senoide se le ha sumado otra tres veces más rápida y tres veces más pequeña. La onda que resulta ya no es una senoide: sus subidas y bajadas son más empinadas y su parte alta, más plana. Puedes comprobar por qué. Justo donde la primera senoide tiene su cresta, la pequeña está en su valle y le resta: le muerde la cima y la aplana. En cambio, en las subidas y bajadas las dos empujan hacia el mismo lado, y la pendiente se hace más brusca.
- Abajo, se ha sumado además otra cinco veces más rápida y cinco veces más pequeña. El resultado se parece ya mucho a una onda cuadrada.

Si siguieras añadiendo senoides (siete veces más rápida, nueve veces…), la onda se iría acercando cada vez más a una cuadrada perfecta.

Y lo importante es que funciona en los dos sentidos. Si sumando senoides se obtiene una onda cuadrada, entonces **una onda cuadrada lleva dentro todas esas senoides**. No es una forma de hablar: un receptor sintonizado a la frecuencia de cualquiera de ellas la encontraría ahí, real, medible.

Un detalle para completar la receta: a veces hay que añadir además una parte fija, que no oscila: la **componente continua**. Es lo que tiene, por ejemplo, una onda cuadrada que va de 0 a 5 V en lugar de ir de −2,5 a +2,5 V: es la misma onda, subida 2,5 V.

—O sea, que una onda fea es un montón de ondas bonitas juntas —dijo Lucía.

—Y que si tú emites una onda fea, estás emitiendo todas esas a la vez —contestó Vicente—. En frecuencias que no son tuyas.

## Fundamental y armónicos

Las senoides que componen una onda tienen nombre:

> **Frecuencia fundamental:** la frecuencia de la onda, la más baja de todas las que la componen. Es la que queremos emitir.
>
> **Armónicos:** las demás senoides que la acompañan. Sus frecuencias son múltiplos exactos de la fundamental: el doble, el triple, el cuádruple…

Los armónicos se numeran por el número que multiplica a la fundamental:

**Frecuencia del armónico = número del armónico × frecuencia fundamental**

| | Para una fundamental de 3,5 MHz |
|---|---|
| Fundamental (a veces llamada «primer armónico») | 3,5 MHz |
| Segundo armónico (× 2) | 7 MHz |
| Tercer armónico (× 3) | 10,5 MHz |
| Cuarto armónico (× 4) | 14 MHz |
| Quinto armónico (× 5) | 17,5 MHz |

Un detalle de numeración que el examen aprovecha para poner trampas: **el número del armónico es directamente el número por el que se multiplica.** El segundo armónico es × 2 y el tercero es × 3. El error típico es contar «el segundo que aparece después de la fundamental» (que sería el triple) como si fuera el segundo armónico.

Cuáles aparecen y con cuánta fuerza depende de la forma exacta de la onda. En general se debilitan al subir de número, pero no siempre de forma ordenada: en la onda cuadrada perfecta, por ejemplo, los pares no existen y solo están los impares (tercero, quinto, séptimo…).

**Ejemplo 1.** *Un transmisor emite en 3,6 MHz. ¿En qué frecuencia aparece su segundo armónico? ¿Y el tercero?*

Segundo: 2 × 3,6 = **7,2 MHz**. Tercero: 3 × 3,6 = **10,8 MHz**.

**Ejemplo 2.** *Un compañero te avisa de que, cuando transmites en 145 MHz, te oye también en 435 MHz. ¿Puede ser un armónico tuyo?*

435 / 145 = 3. Sí: es exactamente tu **tercer armónico**.

## Los armónicos en la música: el timbre

Los armónicos no son un invento de la radio. Los oyes todos los días.

Cuando un violín y una flauta tocan la misma nota, por ejemplo el *la* de 440 Hz, las dos producen una onda de 440 ciclos por segundo. Y sin embargo no suenan igual: los distingues al instante. La diferencia está en la forma de la onda, es decir, en sus armónicos. La flauta produce una onda casi senoidal, con pocos armónicos y débiles: suena «limpia». El violín produce una onda muy distinta de una senoide, cargada de armónicos en 880, 1.320, 1.760 Hz…: suena «rica», «áspera». A esa cualidad se le llama **timbre**, y es lo que te permite reconocer la voz de una persona.

En música, los armónicos son lo que hace interesante un sonido. En un transmisor de radio son justo lo contrario.

## Por qué son un problema en radio

Un transmisor ideal emitiría una senoide perfecta en su frecuencia y nada más. Un transmisor real tiene dentro amplificadores, y un amplificador nunca reproduce la onda con total fidelidad: siempre la deforma un poco. Si además se le exige más potencia de la que puede dar, hace algo peor: **recorta las crestas**, porque no puede subir más. Sale una senoide con la cima aplanada.

![Arriba, una senoide limpia y, a su derecha, su contenido en frecuencias: una sola barra en 7 megahercios. Abajo, la misma senoide con la cresta de arriba recortada y, a su derecha, su contenido en frecuencias: la barra de 7 megahercios y, además, barras cada vez más pequeñas en 14, 21 y 28 megahercios. Deformar la onda hace aparecer armónicos.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-onda-recortada.svg)

Y una senoide recortada ya no es una senoide. Por lo que acabas de aprender, eso significa que lleva armónicos: la emisora que debía estar solo en 7 MHz aparece también en 14, en 21, en 28… En esas frecuencias puede haber otros radioaficionados, o servicios que no tienen nada que ver contigo: aviación, policía, la televisión del vecino.

Emitir fuera de la frecuencia que te corresponde es una de las faltas técnicas más serias de un radioaficionado, y la normativa obliga a evitarlo. Hay dos remedios, y los dos reaparecerán en el curso:

- **No forzar el equipo.** Un transmisor trabajando dentro de sus límites deforma poco. Subir la potencia «a tope» no hace que llegues mucho más lejos, y sí que ensucies.
- **Filtrar la salida.** Entre el transmisor y la antena se coloca un **filtro paso bajo**: un circuito que deja pasar las frecuencias que están por debajo de un cierto valor y frena las que están por encima. Como los armónicos están siempre *por encima* de la fundamental, el filtro deja salir tu señal y retiene sus armónicos. Cómo se construye es materia de la sección 5; todos los equipos comerciales lo llevan dentro.

Un aviso para que no saques la conclusión equivocada: el filtro quita lo que cae lejos, por arriba. Un equipo forzado ensucia además justo al lado de su propia frecuencia (lo llamarás *splatter* en la sección 7), y eso no hay filtro que lo arregle. Llevar filtro no da permiso para forzar: el primer remedio no es opcional.

### Una herencia curiosa: las bandas en escalera

En la lección anterior quedó pendiente una observación: las bandas clásicas de HF están en 3,5 – 7 – 14 – 21 – 28 MHz. Ahora puedes ver el patrón: 7 es el doble de 3,5; 14, el cuádruple; 21, seis veces; 28, ocho veces. Están **en relación armónica**.

No es casualidad. Las primeras (80, 40, 20 y 10 metros) se fijaron así en los años veinte del siglo pasado, cuando los transmisores eran mucho más sucios que hoy, y la de 15 metros se añadió en 1947 respetando la misma escalera. La intención era doble: que los armónicos de un radioaficionado cayeran sobre otra banda de radioaficionados y no sobre un servicio ajeno, y que una misma antena y un mismo circuito pudieran aprovecharse en varias bandas. El reparto sigue ahí.

## Donde la gente se lía

- **«Los armónicos están por debajo de la fundamental.»** Nunca. Siempre son múltiplos enteros: el doble, el triple… Siempre por encima.
- **«Los armónicos son un defecto de fabricación.»** Son una consecuencia matemática de deformar una onda. Ningún equipo real está totalmente libre de ellos; lo que se hace es mantenerlos muy débiles y filtrarlos.
- **«Si transmito con más potencia, solo sube mi señal.»** Si al subir la potencia el amplificador empieza a recortar, lo que más sube es la suciedad.

## Compruébalo tú

1. Un transmisor emite en 14,1 MHz. ¿En qué frecuencia está su segundo armónico?
2. ¿Cuál es el tercer armónico de una señal de 145 MHz? ¿En qué tramo del espectro cae?
3. Un transmisor trabaja en 3,55 MHz. ¿Cae alguno de sus armónicos dentro de la banda de 40 metros (de 7,0 a 7,2 MHz)?
4. Aparece una señal no deseada en 84 MHz. ¿Puede ser un armónico de una emisora que transmite en 28 MHz? ¿Y de una que transmite en 50 MHz?
5. ¿Cuántas frecuencias contiene una senoide pura de 1 MHz?
6. Dos instrumentos tocan la misma nota y suenan distinto. ¿En qué se diferencian sus ondas?
7. Para eliminar los armónicos de un transmisor, ¿hace falta un filtro que deje pasar las frecuencias altas y frene las bajas, o al revés? ¿Por qué?
8. Un amplificador recorta las crestas de la señal porque se le exige demasiada potencia. ¿Qué consecuencia tiene eso en lo que sale por la antena?

**Soluciones**

1. 2 × 14,1 = **28,2 MHz**. (Dentro de la banda de 10 metros.)
2. 3 × 145 = **435 MHz**. Está entre 300 MHz y 3 GHz: **UHF**. (Y dentro de la banda de 70 cm.)
3. Sí: su segundo armónico está en 2 × 3,55 = **7,1 MHz**, dentro de la banda de 40 metros.
4. De la de 28 MHz, sí: 84 / 28 = 3, es su **tercer armónico**. De la de 50 MHz, no: 84 / 50 = 1,68, que no es un número entero, y los armónicos son siempre múltiplos enteros.
5. **Una sola**: 1 MHz. Es lo que distingue a la senoide.
6. En su **forma**, es decir, en sus armónicos: cuáles tienen y con qué fuerza. Eso es el timbre. La frecuencia fundamental es la misma.
7. Al revés: uno que deje pasar las bajas y frene las altas, un **filtro paso bajo**. Los armónicos están siempre por encima de la fundamental.
8. La onda deja de ser senoidal, así que aparecen **armónicos**: el transmisor emite también en el doble, el triple… de su frecuencia, e interfiere a quien esté allí.

## En una frase

Solo la senoide contiene una única frecuencia; cualquier otra forma de onda lleva dentro, además de su frecuencia fundamental, armónicos en el doble, el triple, el cuádruple… y por eso un transmisor que deforma su señal aparece donde no debe y necesita un filtro paso bajo a la salida.

Queda la última herramienta de la sección, la que a Marina la miró mal desde el temario: el decibelio. Vicente prometió que iba a gustarle.
