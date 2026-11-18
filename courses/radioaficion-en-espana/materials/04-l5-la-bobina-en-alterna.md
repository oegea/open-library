La lección anterior terminó con una idea: una bobina no se opone a la corriente, sino a que la corriente cambie. Con esa sola idea se deduce todo su comportamiento, y resulta ser el del condensador puesto del revés. Aquel sábado, Vicente dibujó a lápiz en el cuaderno de Amparo una tabla de dos filas, la tapó con la mano y dijo: «Esta tabla la vais a rellenar vosotras. Ya sabéis lo suficiente.»

Al terminar la lección sabrás qué hace una bobina con la corriente continua y con la alterna, calcularás cuánto estorba a cada frecuencia y tendrás completa la tabla de Vicente: la pareja condensador-bobina, que es una de las preguntas más seguras del examen.

## Con corriente continua: un trozo de cable

Una batería empuja siempre igual. Pasado el instante de la conexión, la corriente tiene un valor fijo y no cambia. Sin cambio, la bobina no tiene nada a lo que oponerse.

> **En corriente continua, una bobina deja pasar la corriente** sin más oposición que la pequeña resistencia de su hilo.

En el agua: una vez que el volante de inercia gira a su ritmo, el agua pasa como si no estuviera.

—Entonces con continua es justo al revés que el condensador —dijo Marina—. Aquel era un muro y esta es un cable.

—Primera casilla rellenada —dijo Vicente.

## Con corriente alterna: un freno que crece con la frecuencia

La corriente alterna no para de cambiar: sube, baja, se invierte. La bobina se opone continuamente.

¿Cuánto? Depende de lo deprisa que cambie la corriente, es decir, de la frecuencia. Con el volante se ve bien. Si el émbolo de la sección 3 invierte el sentido despacio, al volante le da tiempo a frenarse, pararse y arrancar hacia el otro lado en cada vaivén: el agua va y viene. Si lo invierte muy deprisa, el volante no ha llegado ni a arrancar en un sentido cuando ya lo empujan hacia el otro, y el agua apenas se mueve.

> **En corriente alterna, una bobina se opone al paso de la corriente, tanto más cuanto mayor es la frecuencia y cuanto mayor es su inductancia.**

## La reactancia inductiva

Esa oposición se llama **reactancia inductiva**, se escribe **XL** y se mide en **ohmios**, igual que la reactancia capacitiva XC del condensador. Y se usa igual en la ley de Ohm: I = U / XL.

Se calcula así:

**XL = 2 × π × f × L**, es decir, **XL = 6,28 × f × L**

con f en hercios, L en henrios y el resultado en ohmios. Léela: aquí la frecuencia y la inductancia *multiplican*. Cuanto mayores sean, más reactancia. Justo al revés que en el condensador, donde estaban dividiendo. (El 6,28 es el mismo factor fijo de entonces, 2 × π.)

**Ejemplo, paso a paso.** *¿Qué reactancia tiene una bobina de 1 mH a 50 Hz?*

1. Unidades básicas: 1 mH = 0,001 H.
2. XL = 6,28 × 50 × 0,001 = **0,314 Ω**. Prácticamente nada.

La misma bobina a otras frecuencias:

| Frecuencia | Reactancia de la bobina de 1 mH |
|---|---|
| 0 Hz (continua) | 0 Ω: pasa libremente |
| 50 Hz (la red eléctrica) | 0,3 Ω |
| 5.000 Hz (un silbido agudo) | unos 31 Ω |
| 5 MHz (una señal de radio) | unos 31.400 Ω: un muro |

Compara esta tabla con la del condensador de 1 µF de la lección 3: aquel era un muro para la continua y un cable para la radio. La bobina es un cable para la continua y un muro para la radio.

Igual que la del condensador, la reactancia de la bobina no gasta energía: la bobina la guarda en su campo magnético durante un cuarto de ciclo y la devuelve en el siguiente. Una bobina ideal no se calienta.

### El desfase, al revés que en el condensador

En el condensador, la corriente iba adelantada un cuarto de ciclo respecto a la tensión. En la bobina ocurre lo contrario, y se entiende con lo que ya sabes: la bobina no deja que la corriente cambie a tiempo. Cuando la tensión aplicada llega a su máximo, la corriente todavía está creciendo, y no alcanza su propio máximo hasta un cuarto de ciclo más tarde.

> En una bobina, **la corriente va retrasada un cuarto de ciclo (90°) respecto a la tensión.**

## La pareja de opuestos

Aquí está la tabla de Vicente, completa. Sobre ella se construye media radio:

| | Corriente continua | Alterna de baja frecuencia | Alterna de alta frecuencia |
|---|---|---|---|
| **Condensador** | La bloquea | Estorba mucho | Pasa con facilidad |
| **Bobina** | La deja pasar | Estorba poco | La bloquea |

Y el retrato de cada uno, lado a lado:

| | Condensador | Bobina |
|---|---|---|
| Qué almacena | Energía en un campo **eléctrico** | Energía en un campo **magnético** |
| Magnitud y unidad | Capacidad (C), en faradios | Inductancia (L), en henrios |
| Reactancia | XC = 1 / (6,28 × f × C) | XL = 6,28 × f × L |
| Al subir la frecuencia | La reactancia **baja** | La reactancia **sube** |
| Corriente respecto a tensión | Adelantada 90° | Retrasada 90° |

![Gráfica de la reactancia frente a la frecuencia. La reactancia de la bobina es una recta que sube: a más frecuencia, más oposición. La reactancia del condensador es una curva que baja: a más frecuencia, menos oposición. Las dos líneas se cruzan en un punto, donde ambos estorban lo mismo.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s04-reactancias.svg)

Fíjate en que las dos líneas se cruzan: hay una frecuencia a la que el condensador y la bobina estorban exactamente lo mismo. Lo tienes en las dos tablas: a 5.000 Hz, el condensador de 1 µF estorbaba unos 32 Ω y la bobina de 1 mH, unos 31 Ω. Cerca de esa frecuencia ocurre algo extraordinario, que se llama resonancia y es el fundamento de la sintonía. Será el plato fuerte de la sección 5.

## Una palabra para más adelante: impedancia

En un circuito de alterna real suele haber de todo: resistencias, condensadores, bobinas. A la oposición total que el conjunto presenta a la corriente alterna se le da un nombre propio:

> **Impedancia:** la oposición total que un circuito presenta al paso de la corriente alterna, **combinando** sus resistencias y sus reactancias. Se escribe **Z** y se mide en ohmios.

Hemos dicho «combinando» y no «sumando» a propósito: no es una simple suma. La reactancia de la bobina y la del condensador tiran en sentidos opuestos (una retrasa la corriente y la otra la adelanta) y pueden llegar a anularse entre sí. Cómo se combinan lo verás en la sección 5. De momento quédate con la palabra y con la idea: *la impedancia es a la alterna lo que la resistencia es a la continua*. En la sección 8, cuando hablemos de antenas y cables, será el número que más se vigila en una estación.

## Para qué sirven las bobinas

- **Frenar las frecuencias altas y dejar pasar la continua.** Una bobina en fila con un cable de alimentación deja pasar los 12 V y detiene las señales de radio que quieran colarse por él. A la bobina que hace este trabajo se le llama **choque**. Los anillos de ferrita que se ponen abrazando algunos cables hacen lo mismo.
- **Formar filtros y circuitos de sintonía**, en pareja con el condensador (sección 5).
- **Fabricar transformadores**, que son dos bobinas trabajando juntas: la lección siguiente.

## Donde la gente se lía

- **Cruzar las dos reactancias.** Bobina: sube con la frecuencia (la f multiplica). Condensador: baja con la frecuencia (la f divide). Un truco: la **b**obina **b**loquea lo rápido.
- **Cruzar los desfases.** En el condensador la corriente se adelanta; en la bobina se retrasa.
- **«Como deja pasar la continua, una bobina conectada a una batería es inofensiva.»** Al contrario: sin más oposición que la resistencia de su hilo, es casi un cortocircuito.
- **Meter milihenrios o microhenrios en la fórmula.** La fórmula quiere henrios: 1 mH = 0,001 H y 1 µH = 0,000001 H.
- **«Impedancia es la suma de resistencia y reactancias.»** Es su combinación, y no una suma corriente: bobina y condensador se restan entre sí.

## Compruébalo tú

1. Conectas una bobina (de hilo grueso, con muy poca resistencia) directamente a una batería. Pasado el primer instante, ¿cómo se comporta?
2. Una bobina tiene una reactancia de 50 Ω a 1 MHz. Sin usar la fórmula, ¿cuánta tendrá a 3 MHz?
3. Calcula la reactancia de una bobina de 10 mH a 1.000 Hz.
4. Calcula la reactancia de una bobina de 10 µH a 7 MHz.
5. A una bobina cuya reactancia es de 200 Ω se le aplican 10 V de alterna. ¿Qué corriente circula?
6. Quieres que por un cable pase la corriente continua de alimentación pero no una señal de radio de alta frecuencia. ¿Pones en fila un condensador o una bobina?
7. ¿Y si quieres lo contrario: que pase la señal de radio y no la continua?
8. En un componente, la corriente alterna va retrasada 90° respecto a la tensión. ¿Es un condensador o una bobina?

**Soluciones**

1. Como un simple cable: con corriente continua estable, la bobina no se opone. Con tan poca resistencia, sería casi un cortocircuito para la batería.
2. A triple frecuencia, triple reactancia: **150 Ω**.
3. 10 mH = 0,01 H. XL = 6,28 × 1.000 × 0,01 = **62,8 Ω**.
4. 10 µH = 0,00001 H y 7 MHz = 7.000.000 Hz. XL = 6,28 × 7.000.000 × 0,00001 = **unos 440 Ω**.
5. I = U / XL = 10 / 200 = **0,05 A** (50 mA).
6. Una **bobina** (un choque): deja pasar la continua y frena la alta frecuencia.
7. Un **condensador**: bloquea la continua y deja pasar la alta frecuencia.
8. Una **bobina**. En el condensador iría adelantada.

## En una frase

Una bobina deja pasar la corriente continua y frena la alterna tanto más cuanto mayor es la frecuencia (XL = 6,28 × f × L), justo al revés que el condensador; a la oposición total de un circuito a la alterna, combinando resistencias y reactancias, se le llama impedancia.

Si una bobina es capaz de inducir tensión en sí misma, también puede inducirla en otra bobina que tenga al lado. Eso es un transformador.
