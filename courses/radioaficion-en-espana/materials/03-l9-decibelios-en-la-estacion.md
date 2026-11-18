Entre el transmisor de Vicente y el señor de Uruguay hay un cable, una antena, once mil kilómetros de aire y otra antena. Cada tramo multiplica o divide la potencia. En la lección anterior aprendiste a leer decibelios; en esta los usas para lo que se inventaron: convertir esa cadena de multiplicaciones en una suma.

Al terminar sabrás hacer el balance de una estación, aplicar los decibelios a tensiones (donde el doble no son 3 dB, sino 6) y leer los decibelios «con apellido», dBm y dBW, que sí indican una potencia concreta. Recuerda las dos filas que lo sostienen todo: **3 dB es el doble; 10 dB es diez veces.**

## La cuenta de una estación

Una estación sencilla:

- El transmisor entrega **100 W**.
- El cable hasta la antena tiene una pérdida de **3 dB**.
- La antena tiene una ganancia de **6 dB**: concentra la señal hacia una dirección, como el reflector de una linterna.

—Un momento —dijo Marina—. ¿No habíamos quedado en que un decibelio siempre compara? Una ganancia de seis decibelios, ¿comparada con qué?

—Con una antena sencilla que se toma como referencia —dijo Vicente—. Seis decibelios de ganancia quiere decir que, en su dirección buena, esta antena pone cuatro veces más señal que la de referencia con los mismos vatios. No fabrica potencia: la que da de más hacia un lado se la quita a los demás.

(La antena de referencia habitual es el *dipolo*, que conocerás en la sección 8.)

Balance: −3 + 6 = **+3 dB**. Y +3 dB es el doble. En la dirección hacia la que apunta la antena, la estación se oye como si emitiera 200 W con la antena de referencia. A esa potencia equivalente se le llama **potencia radiada aparente (PRA)**. (Si la comparación se hace con una antena ideal que radiara igual en todas direcciones, se llama **PIRE**.) Algunos límites de la normativa se expresan de esta manera, y por eso conviene que las siglas te suenen.

![La cadena de una estación. El transmisor entrega 100 vatios. El cable resta 3 decibelios: quedan 50 vatios. La antena suma 6 decibelios: en su dirección favorita equivale a 200 vatios. Debajo, la cuenta en decibelios: menos 3 más 6 igual a más 3 decibelios, el doble de los 100 vatios iniciales.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-cadena-en-decibelios.svg)

Puedes comprobarlo por el camino largo: 100 W entre 2 son 50 W a la entrada de la antena; multiplicados por 4 son 200 W. Sale lo mismo, pero con decibelios ha bastado una suma. Con una cadena de diez elementos, la diferencia es enorme.

Y los decibelios ayudan a decidir en qué gastar el dinero. Si tu cable pierde 3 dB, la mitad de la potencia que has pagado se queda calentándolo. Un cable mejor, que pierda solo 1 dB, deja pasar 80 W de cada 100 en lugar de 50, y cuesta muchísimo menos que un transmisor más potente.

## Los decibelios y la tensión

Hasta aquí, todo eran potencias. A veces lo que se compara son tensiones, y entonces la tabla cambia: **duplicar la tensión no son 3 dB, sino 6 dB.**

No es una regla nueva que haya que creerse: sale de una fórmula de la sección 2. La potencia depende de la tensión **al cuadrado**, P = U² / R. Si la tensión se duplica sobre la misma resistencia, la potencia no se duplica: se multiplica por 2 × 2 = 4. Y multiplicar la potencia por 4 son 6 dB. El decibelio sigue hablando siempre de potencia; lo que ocurre es que al doble de tensión le corresponde el cuádruple de potencia.

| Decibelios | La potencia se multiplica por | La tensión se multiplica por |
|---|---|---|
| 3 dB | 2 | 1,41 |
| **6 dB** | 4 | **2** |
| 10 dB | 10 | 3,16 |
| **20 dB** | 100 | **10** |

Para el examen, quédate con las dos filas en negrita: **en tensión (sobre la misma resistencia), 6 dB es el doble y 20 dB es diez veces.** Y lee bien el enunciado, porque la pregunta dirá si se refiere a potencia o a tensión.

## Decibelios con apellido: dBm y dBW

Hemos dicho que el decibelio compara y que no mide cantidades. Pero si se acuerda de antemano *con qué* se compara, entonces sí sirve para dar una cantidad. Para eso se le añade una letra:

> **dBm:** decibelios respecto a **1 milivatio**. Dice cuántas veces mayor (o menor) que un milivatio es una potencia.
>
> **dBW:** decibelios respecto a **1 vatio**.

Como la referencia es fija, cada cifra corresponde a una potencia concreta:

| Potencia | En dBm | En dBW |
|---|---|---|
| 0,1 mW | −10 dBm | −40 dBW |
| **1 mW** | **0 dBm** | −30 dBW |
| 10 mW | 10 dBm | −20 dBW |
| 100 mW | 20 dBm | −10 dBW |
| **1 W** | 30 dBm | **0 dBW** |
| 10 W | 40 dBm | 10 dBW |
| 100 W | 50 dBm | 20 dBW |
| 1.000 W | 60 dBm | 30 dBW |

Se leen con la tabla de siempre. **20 dBm** es «100 veces un milivatio»: 100 mW. **0 dBm** no es cero potencia: es «una vez un milivatio», o sea, 1 mW. Y los valores negativos son potencias *menores* que la de referencia, no potencias negativas: −10 dBm es la décima parte de un milivatio.

Como un vatio son mil milivatios, y mil veces son 30 dB, entre las dos columnas hay siempre 30 de diferencia: **0 dBW = 30 dBm.**

El dBm es la unidad habitual de los instrumentos de medida y de las especificaciones de los receptores. El dBW aparece en la normativa.

Una regla de escritura que evita errores: los **dB** a secas se pueden sumar y restar entre sí y se pueden sumar a una cifra en dBm. Una potencia de 20 dBm que pasa por un amplificador de 10 dB sale con 30 dBm. Es la misma cuenta de la cadena, aún más corta. Lo que **no** se puede es sumar dBm con dBm: dos señales de 20 dBm juntas no son 40 dBm. Son 100 mW + 100 mW = 200 mW, el doble, es decir, 23 dBm.

## La fórmula, para quien quiera verla

Por completar, esta es la fórmula que hay detrás de todo lo anterior:

**dB = 10 × log (P2 / P1)**

donde P1 es la potencia de referencia y P2 la que se compara con ella. El «log» es el logaritmo decimal, una operación que tienen todas las calculadoras y que responde exactamente a la pregunta que nos hemos hecho antes: *¿cuántas veces hay que multiplicar por diez para llegar a este número?* El logaritmo de 100 es 2; el de 1.000 es 3.

Para comparar tensiones, la fórmula es la misma con un 20 en lugar del 10 (por lo del cuadrado): **dB = 20 × log (U2 / U1)**.

Para las preguntas del examen español, la tabla de 3 y de 10 es suficiente. La fórmula solo hace falta para cifras que no salen de combinar esos dos números, y no se suelen preguntar.

## Donde la gente se lía

- **«El decibelio es una unidad de potencia.»** Es una comparación entre dos potencias. Solo con apellido (dBm, dBW) indica una potencia concreta.
- **Confundir potencia y tensión.** El doble de potencia son 3 dB; el doble de tensión, 6 dB.
- **«0 dBm es que no hay potencia», o «−10 dBm es una potencia negativa».** 0 dBm es 1 mW, y −10 dBm es la décima parte de un milivatio. El signo indica «menos que la referencia», no «menos que nada».

## Compruébalo tú

1. Una estación: transmisor de 50 W, cable con 3 dB de pérdida, antena con 9 dB de ganancia. ¿Cuál es el balance en decibelios? ¿A qué potencia equivale en la dirección de la antena?
2. Con un transmisor de 100 W, ¿cuánta potencia llega a la antena por un cable que pierde 1 dB? ¿Y por uno que pierde 6 dB?
3. ¿Qué potencia son 20 dBm? ¿Y 40 dBm?
4. Expresa 10 W en dBW y en dBm.
5. La tensión de una señal se multiplica por 10 sobre la misma resistencia. ¿Cuántos decibelios ha aumentado?
6. Una señal de 10 dBm pasa por un amplificador de 20 dB. ¿Qué potencia sale, en dBm y en vatios?
7. Un transmisor entrega 25 W y su antena tiene 6 dB de ganancia; el cable es tan corto que su pérdida no cuenta. ¿Cuál es la potencia radiada aparente?

**Soluciones**

1. Balance: −3 + 9 = **+6 dB**, que es × 4. Equivale a 50 × 4 = **200 W**.
2. Con 1 dB de pérdida pasan unas cuatro quintas partes: unos **80 W**. Con 6 dB se divide entre 4: 100 / 4 = **25 W**; tres cuartas partes de la potencia se quedan en el cable.
3. 20 dBm = 100 veces 1 mW = **100 mW**. 40 dBm = 10.000 veces 1 mW = 10.000 mW = **10 W**.
4. 10 W es 10 veces 1 W: **10 dBW**. En dBm son 30 más: **40 dBm** (coincide con el ejercicio anterior).
5. En tensión, diez veces son **20 dB**.
6. 10 dBm + 20 dB = **30 dBm**, que son 1.000 mW: **1 W**.
7. +6 dB es × 4: 25 × 4 = **100 W** de potencia radiada aparente.

## En una frase

En decibelios, la cadena de una estación se resuelve sumando ganancias y restando pérdidas; aplicados a tensiones, el doble son 6 dB; y con apellido indican una potencia concreta: **dBm** respecto a 1 milivatio y **dBW** respecto a 1 vatio, con 30 de diferencia entre ambos.

Con esto terminas la gramática del dial: sabes qué es una corriente alterna, cómo se miden su ritmo, su tamaño y su fase, cómo se convierte en una onda que viaja, dónde vive cada frecuencia y cómo se comparan potencias. El material siguiente es el resumen de toda la sección, en formato de chuleta, para repasar antes del examen.
