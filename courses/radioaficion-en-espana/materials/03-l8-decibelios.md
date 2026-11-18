«Los decibelios te van a encantar», le dijo Vicente a Marina. «Son la manera que tienen los ingenieros de multiplicar sumando.» Marina, que se los había cruzado en el temario y la habían mirado mal, no estaba tan segura.

El decibelio tiene fama de difícil porque suele presentarse con una fórmula llena de logaritmos. No la necesitas. Lo que necesitas es entender una idea, memorizar tres números y practicar un poco. Al terminar esta lección sabrás leer cualquier cifra en decibelios y convertirla en «tantas veces más» o «tantas veces menos». En la siguiente, la última de la sección, los usarás para hacer las cuentas de una estación completa con sumas y restas.

## El problema: números que no caben en la cabeza

En radio, las potencias varían de una forma descomunal. Un transmisor puede emitir 100 vatios. De esos 100 vatios, a la antena de un receptor situado al otro lado del océano le llega quizá una billonésima de vatio: 0,000000000001 W. Y entre uno y otro hay cables que se quedan con parte de la potencia, antenas que la concentran y amplificadores que la multiplican.

Calcular con esos números es una pesadilla de ceros. Y además casi nunca interesa la cifra exacta, sino la **comparación**: «el cable se come la mitad», «esta antena da cuatro veces más señal que aquella», «el amplificador multiplica por diez».

El decibelio es una herramienta para expresar comparaciones así, de manera que las cuentas largas se conviertan en sumas.

## Primera idea: un decibelio no mide una cantidad, mide una comparación

Esto es lo primero que hay que tener claro, y lo que más confunde:

> **El decibelio (dB)** no es una unidad como el vatio o el voltio. No dice *cuánto hay*: dice **cuántas veces es una potencia mayor o menor que otra**.

—¿Los decibelios no eran lo del ruido? —preguntó Marina—. Lo de «la discoteca está a cien decibelios».

—Son lo mismo, usados para comparar otra cosa —dijo Vicente—. Cuando se dice que un ruido tiene cien decibelios, lo que se está diciendo es cuántas veces es más intenso que el sonido más flojo que un oído puede percibir. Siempre es una comparación; lo que pasa es que en el ruido nadie nombra con qué se compara. En radio comparamos potencias: la que sale con la que entra, la de esta antena con la de aquella.

Decir «+10 dB», como verás enseguida, es como decir «diez veces más». ¿Diez veces más que qué? Que lo que hubiera antes. Diez vatios pasan a ser cien; una milésima de vatio pasa a ser diez milésimas. El «+10 dB» es el mismo en los dos casos.

## Segunda idea: contar multiplicaciones en lugar de escribir el resultado

Ahora el truco que lo hace útil. En lugar de decir *por cuánto* se ha multiplicado una potencia, se cuenta *cuántas veces se ha multiplicado por diez*.

El invento original fue el **belio** (por Alexander Graham Bell, el del teléfono): 1 belio es haber multiplicado la potencia por 10. Resultó un escalón demasiado grande para el uso diario, así que se partió en diez escalones iguales, los **decibelios** («deci» es la décima parte, como en *decímetro*). Subir los diez escalones es haber multiplicado por 10:

- Multiplicar la potencia **por 10** es subir **10 dB**.
- Multiplicar por 10 dos veces seguidas (por 100) es subir 10 dB dos veces: **20 dB**.
- Multiplicar por 10 tres veces (por 1.000): **30 dB**.

Fíjate en lo que ha ocurrido: a la izquierda, los números crecen multiplicándose (10, 100, 1.000…) y se hacen enormes enseguida. A la derecha crecen sumando (10, 20, 30…) y siguen siendo manejables. Un millón de veces más potencia son solo 60 dB. **Ese es todo el secreto del decibelio: convierte multiplicaciones en sumas.**

## El tercer número: 3 dB es el doble

Con saltos de «por diez» no basta: hace falta poder decir «el doble». Duplicar una potencia son, muy aproximadamente, **3 dB**.

—¿Y por qué tres, y no cinco, que es la mitad de diez? —preguntó Lucía.

Compruébalo duplicando diez veces seguidas:

2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 1.024

Diez duplicaciones multiplican por 1.024, que es casi exactamente 1.000. Y multiplicar por 1.000 eran 30 dB. Si diez duplicaciones valen 30 dB, cada duplicación vale 30 / 10 = **3 dB**.

Y duplicar dos veces (el cuádruple) son 3 + 3 = 6 dB.

## Los decibelios negativos: dividir en lugar de multiplicar

Si sumar decibelios es multiplicar, restarlos es dividir. Un número de decibelios **negativo** indica que la potencia ha disminuido:

- **−3 dB:** la potencia se divide entre 2. Queda la mitad.
- **−10 dB:** se divide entre 10. Queda la décima parte.
- **−20 dB:** se divide entre 100.

A una disminución se le llama **pérdida** o **atenuación**; a un aumento, **ganancia**. Es habitual oír «este cable tiene 3 dB de pérdida», que es lo mismo que decir «−3 dB».

Y un caso que despista mucho: **0 dB no significa «nada de potencia».** Significa «ningún cambio»: la potencia se ha multiplicado por 1 y sigue igual.

## La tabla que hay que saberse

Con esto se completa la tabla. Es de las más rentables del examen:

| Decibelios | La potencia… |
|---|---|
| +30 dB | se multiplica por 1.000 |
| +20 dB | se multiplica por 100 |
| **+10 dB** | **se multiplica por 10** |
| +6 dB | se multiplica por 4 |
| **+3 dB** | **se multiplica por 2** |
| **0 dB** | **no cambia (× 1)** |
| **−3 dB** | **se divide entre 2** |
| −6 dB | se divide entre 4 |
| **−10 dB** | **se divide entre 10** |
| −20 dB | se divide entre 100 |
| −30 dB | se divide entre 1.000 |

En realidad basta con memorizar **dos filas: 3 dB es el doble y 10 dB es diez veces.** Todas las demás salen de combinar esas dos.

Un valor más, solo para tenerlo a mano porque aparece mucho en cables: **1 dB** es multiplicar por 1,26 aproximadamente; como pérdida, −1 dB deja pasar unas cuatro quintas partes de la potencia (80 W de cada 100).

![La escalera de los decibelios. En el centro, 0 decibelios: la potencia no cambia. Hacia arriba, ganancias: más 3 decibelios multiplica por 2, más 6 por 4, más 10 por 10, más 20 por 100, más 30 por 1.000. Hacia abajo, pérdidas: menos 3 decibelios divide entre 2, menos 6 entre 4, menos 10 entre 10, menos 20 entre 100, menos 30 entre 1.000.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-escalera-decibelios.svg)

## La regla de combinación

> **Sumar decibelios equivale a multiplicar los factores. Restar decibelios equivale a dividirlos.**

Para traducir cualquier cifra en decibelios, se descompone en trozos de 10 y de 3, y cada trozo se convierte en su multiplicación:

- **13 dB** = 10 + 3 → × 10 y × 2 → **× 20**
- **16 dB** = 10 + 3 + 3 → × 10 × 2 × 2 → **× 40**
- **9 dB** = 3 + 3 + 3 → × 2 × 2 × 2 → **× 8**
- **23 dB** = 10 + 10 + 3 → × 10 × 10 × 2 → **× 200**
- **7 dB** = 10 − 3 → × 10 y ÷ 2 → **× 5**
- **−13 dB** = −10 − 3 → ÷ 10 y ÷ 2 → **÷ 20**

El penúltimo merece una mirada: también se puede *restar*. Siete decibelios son diez menos tres: multiplicar por diez y quedarse con la mitad.

**Ejemplo 1.** *Un amplificador tiene una ganancia de 10 dB. Si le entran 50 W, ¿cuánto sale?*

+10 dB es multiplicar por 10: 50 × 10 = **500 W**.

**Ejemplo 2.** *Un transmisor entrega 20 W a un cable que tiene 3 dB de pérdida. ¿Qué potencia llega al otro extremo?*

−3 dB es dividir entre 2: 20 / 2 = **10 W**. La otra mitad se ha quedado en el cable, convertida en calor.

**Ejemplo 3.** *Una señal de 2 W pasa por un amplificador de 13 dB. ¿Qué potencia sale?*

13 dB = 10 + 3 → × 10 × 2 = × 20. Salen 2 × 20 = **40 W**.

### Y al revés: de «tantas veces» a decibelios

A veces la pregunta viene en el otro sentido: te dan las dos potencias y te piden los decibelios. Se hace en dos pasos: primero averiguas por cuánto se ha multiplicado (o dividido), y luego buscas ese factor en la tabla.

**Ejemplo 4.** *Un amplificador convierte 4 W en 400 W. ¿Cuál es su ganancia?*

400 / 4 = 100: ha multiplicado por 100. En la tabla, × 100 son **20 dB**.

**Ejemplo 5.** *A un cable le entran 60 W y salen 30 W. ¿Cuánto pierde?*

Ha dividido entre 2: **3 dB** de pérdida (−3 dB).

## Donde la gente se lía

- **«0 dB es que no hay señal.»** 0 dB es que no ha cambiado nada.
- **«6 dB es el doble de 3 dB, así que es el doble de potencia que 3 dB.»** 6 dB son dos duplicaciones: el cuádruple. Y 20 dB no es el doble que 10 dB: es diez veces más (× 100 frente a × 10).
- **Sumar los factores en vez de multiplicarlos.** 13 dB es × 10 **por** × 2 = × 20, no 10 + 2 = 12.

## Compruébalo tú

1. Una potencia aumenta 20 dB. ¿Por cuánto se ha multiplicado?
2. Un cable tiene una pérdida de 10 dB. Si le entran 50 W, ¿cuánto llega al final?
3. ¿Por cuánto multiplica la potencia una ganancia de 16 dB?
4. Un amplificador convierte 5 W en 50 W. ¿Cuál es su ganancia en decibelios?
5. Una potencia pasa de 80 W a 20 W. ¿Cuántos decibelios ha perdido?
6. ¿Por cuánto se divide la potencia con una pérdida de 23 dB?
7. ¿A qué factor corresponden 7 dB? (Pista: 7 = 10 − 3.)

**Soluciones**

1. 20 dB = 10 + 10 → × 10 × 10 = **× 100**.
2. −10 dB es dividir entre 10: 50 / 10 = **5 W**.
3. 16 dB = 10 + 3 + 3 → × 10 × 2 × 2 = **× 40**.
4. De 5 a 50 W se ha multiplicado por 10: **10 dB**.
5. De 80 a 20 W se ha dividido entre 4, que es dividir entre 2 dos veces: **6 dB** de pérdida (−6 dB).
6. 23 dB = 10 + 10 + 3 → se divide entre 10 × 10 × 2 = **200**.
7. Multiplicar por 10 y dividir entre 2: **× 5**.

## En una frase

El decibelio expresa cuántas veces una potencia es mayor o menor que otra, contando multiplicaciones en lugar de escribir el resultado: **3 dB es el doble, 10 dB es diez veces**, sumar decibelios es multiplicar y restarlos es dividir.

Ya sabes leer decibelios. En la lección siguiente, la última de la sección, los pones a trabajar: la cuenta de una estación entera, los decibelios aplicados a tensiones y los decibelios «con apellido».
