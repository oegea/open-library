Con una pila, la pregunta «¿cuántos voltios tiene?» se contesta con un número: 1,5. Con una tensión alterna, la pregunta tiene trampa. En un instante vale cero, un momento después vale mucho, luego vale mucho en sentido contrario. ¿Con qué número te quedas?

Esta lección responde a eso. Al terminar sabrás las tres maneras de decir «cuánto mide» una onda —de pico, de pico a pico y eficaz—, cómo se pasa de una a otra y por qué los 230 voltios de tu enchufe son en realidad 325.

## La amplitud: lo alta que es la onda

En la lección anterior medimos la onda a lo ancho: cuánto dura un ciclo. Ahora la medimos a lo alto.

> **Amplitud:** lo «grande» que es la oscilación, es decir, hasta dónde llega a alejarse del cero. En una tensión alterna se mide en voltios; en una corriente alterna, en amperios.

En el circuito de agua con el émbolo, la amplitud sería la fuerza con la que el émbolo empuja y tira. Con más amplitud, la onda del gráfico es más alta, aunque sus ciclos sigan durando lo mismo. Amplitud y frecuencia son independientes: una dice *cuánto* y la otra *cada cuánto*.

En el examen, «amplitud» a secas es ese alejamiento máximo: el valor de pico. Pero hay otras dos formas habituales de decir lo grande que es una onda, y el examen distingue las tres.

Una nota sobre las letras: aquí escribiremos **Up**, **Upp** y **Uef**, con la U de tensión que usamos desde la sección 2. En los instrumentos y en muchas preguntas de examen verás lo mismo escrito con V: **Vp**, **Vpp** y **Vef** o **Vrms**.

## Valor de pico

> **Valor de pico (o valor máximo):** la tensión en el punto más alto de la onda, medida desde el cero hasta la cresta. Lo escribiremos **Up**.

Es la medida más directa: lo máximo que llega a empujar la tensión en cada ciclo. En el semiciclo negativo llega a ese mismo valor, pero en sentido contrario.

## Valor de pico a pico

> **Valor de pico a pico:** la distancia total entre la cresta y el valle. Lo escribiremos **Upp**.

Como la senoide sube por encima del cero lo mismo que baja por debajo, el valor de pico a pico es siempre el doble del valor de pico:

**Upp = 2 × Up**

Una onda con 10 V de pico tiene 20 V de pico a pico. Esta medida se usa sobre todo al mirar una onda en la pantalla de un osciloscopio (el aparato que dibuja ondas, que conocerás en la sección 10), porque medir «de arriba del todo a abajo del todo» es lo más cómodo.

![Una senoide con tres medidas señaladas. El valor de pico va desde el cero hasta la cresta. El valor de pico a pico va desde el valle hasta la cresta y es el doble. Una línea de puntos horizontal, a algo más de dos tercios de la altura de la cresta, marca el valor eficaz: 0,707 veces el valor de pico.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-pico-y-eficaz.svg)

## Valor eficaz: el que importa de verdad

Aquí viene el concepto menos obvio de la sección, así que vamos despacio.

Vicente lo planteó con un experimento. Puso sobre la mesa dos bombillas iguales. Una la conectó a una batería de 12 V. La otra, a una tensión alterna cuyo valor de pico era también de 12 V.

—¿Cuál brilla más? —preguntó.

—Igual —dijo Lucía—. Doce y doce.

No brillaban igual. La de la alterna brillaba claramente menos.

—Es que la alterna solo vale 12 voltios durante un instante en cada semiciclo —dijo Marina, mirando el gráfico—. El resto del tiempo vale menos. Y dos veces por ciclo vale cero.

Exacto. La batería empuja con 12 V todo el rato. La alterna llega a 12 V solo en las crestas; la mayor parte del tiempo empuja menos. Sumando todo, entrega menos energía, y la bombilla brilla menos.

De ahí sale la pregunta útil: **¿qué tensión continua haría brillar la bombilla exactamente igual que esta alterna?** A esa tensión continua equivalente se le llama valor eficaz.

> **Valor eficaz** de una tensión alterna: el valor de la tensión continua que produciría el mismo calor en una resistencia. Se escribe **Uef**. En los aparatos lo verás con sus siglas inglesas: **RMS**.

Es la medida más importante porque es la que dice *lo que la alterna es capaz de hacer*: cuánto calienta, cuánta potencia entrega. Con el valor eficaz, las fórmulas de la sección 2 —la ley de Ohm, P = U × I, P = U² / R— funcionan en alterna igual que en continua, mientras lo conectado sea una resistencia (una bombilla, una estufa). Con bobinas y condensadores hay un matiz, que llegará en las secciones 4 y 5.

### De dónde sale el 0,707

Para una senoide, la relación es fija:

**Uef = 0,707 × Up**

*El valor eficaz es 0,707 veces el valor de pico* (algo más de dos tercios).

—¿Y por qué 0,707 y no la mitad? —preguntó Lucía—. Si va de cero al máximo, la media será la mitad.

Buena objeción, y la respuesta está en una fórmula de la sección 2. La potencia que se disipa en una resistencia no depende de la tensión a secas, sino de la tensión **al cuadrado**: P = U² / R. Lo que hay que promediar no es la tensión, sino su cuadrado.

Sigue el razonamiento en dos pasos.

**Paso 1: dibuja la potencia instante a instante.** Como depende de la tensión al cuadrado, y un número multiplicado por sí mismo nunca da negativo, la potencia nunca es negativa: es máxima en las crestas *y también en los valles*, y es nula en los pasos por cero. Sale una curva de jorobas, todas por encima del cero, dos por cada ciclo de la tensión.

![Arriba, la tensión alterna: una senoide que sube y baja alrededor del cero. Abajo, la potencia que entrega a una resistencia: una curva de jorobas siempre por encima del cero, con un máximo en cada cresta y en cada valle de la tensión. Una línea horizontal a media altura marca la potencia media: la parte de cada joroba que sobresale por encima de esa línea tiene la misma forma que el hueco que queda por debajo de ella entre joroba y joroba.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-potencia-media.svg)

Ahora fíjate en la línea trazada a media altura. La parte de cada joroba que sobresale por encima de esa línea tiene exactamente la misma forma que el hueco que queda por debajo de ella, entre una joroba y la siguiente. Si recortaras esas cimas y les dieras la vuelta, encajarían en los huecos y lo dejarían todo liso, a media altura. Por eso la potencia media es justo **la mitad de la potencia de cresta**.

**Paso 2: la mitad de potencia no es la mitad de tensión.** Buscamos, entonces, la tensión continua que entrega de forma constante esa mitad de potencia. Y aquí está la clave. Con la mitad de tensión, como la potencia va con el cuadrado, tendrías la cuarta parte de potencia (½ × ½ = ¼), no la mitad. Hay que buscar el número que multiplicado por sí mismo dé un medio. Ese número es 0,707, porque 0,707 × 0,707 = 0,5.

Ese 0,707 es 1 dividido entre 1,414, y 1,414 es la *raíz cuadrada de 2* (se escribe √2): el número que multiplicado por sí mismo da 2. Por eso verás la fórmula escrita también así: Uef = Up / √2. Es lo mismo. Y para ir en sentido contrario, del eficaz al pico, se multiplica por ese 1,414:

**Up = 1,414 × Uef**

*El valor de pico es 1,414 veces el valor eficaz.*

Guarda los dos números juntos: **0,707 para bajar de pico a eficaz; 1,414 para subir de eficaz a pico.** Si dudas de cuál toca, piensa que el pico es lo más alto de la onda, así que siempre es el mayor de los dos.

### Los 230 voltios del enchufe son eficaces

Cuando se dice que la red eléctrica es de 230 V, se está dando el valor **eficaz**. Es lo lógico: lo que interesa de un enchufe es lo que puede hacer. El valor de pico es bastante mayor:

Up = 1,414 × 230 ≈ **325 V**

Y de pico a pico, el doble: 650 V. La tensión de tu enchufe oscila entre +325 V y −325 V, cincuenta veces por segundo, y hace el mismo trabajo que harían 230 V de continua.

La regla general para no perderse:

> **Cuando una tensión o una corriente alterna se dan sin apellido, son valores eficaces.** También lo que marca un polímetro en la posición de alterna. Si se quiere decir «de pico» o «de pico a pico», se dice expresamente.

### Ejemplos

**Ejemplo 1.** *Una tensión alterna senoidal tiene un valor de pico de 100 V. ¿Cuál es su valor eficaz?*

De pico a eficaz se baja: Uef = 0,707 × 100 = **70,7 V**.

**Ejemplo 2.** *Un transformador entrega 12 V eficaces. ¿Cuál es su valor de pico?*

De eficaz a pico se sube: Up = 1,414 × 12 ≈ **17 V**.

**Ejemplo 3.** *En un osciloscopio se mide una senoide de 20 V de pico a pico. ¿Cuál es su valor eficaz?*

Hay que ir por pasos. Primero, de pico a pico a pico: Up = 20 / 2 = 10 V. Después, de pico a eficaz: Uef = 0,707 × 10 = **7,07 V**.

Un aviso: los números 0,707 y 1,414 solo valen para **senoides**. Una onda con otra forma tiene otra relación entre su pico y su valor eficaz. En el examen, salvo que se diga otra cosa, la onda es senoidal.

## Donde la gente se lía

- **Multiplicar por 0,707 cuando tocaba 1,414, o al revés.** El pico es siempre el mayor. Si te piden el pico, el resultado tiene que ser más grande que el eficaz.
- **«El valor eficaz es la media de la onda.»** La media de una senoide a lo largo de un ciclo completo (su **valor medio**) es cero, porque la mitad positiva compensa a la negativa. El valor eficaz es otra cosa: la tensión continua que calentaría lo mismo. (La media de *medio* ciclo sí tiene valor, 0,637 × Up: es un dato que el examen puede pedir, pero no volveremos a usarlo.)
- **Olvidar que pico a pico es el doble del pico.** De pico a pico a eficaz hay dos pasos: primero dividir entre 2, después multiplicar por 0,707.

## Compruébalo tú

1. Una senoide tiene un valor de pico de 50 V. ¿Cuánto vale de pico a pico? ¿Y su valor eficaz?
2. Un polímetro, en la posición de alterna, marca 24 V en la salida de un transformador. ¿Cuál es el valor de pico de esa tensión?
3. En una pantalla se mide una senoide de 10 V de pico a pico. ¿Cuál es su valor eficaz?
4. En Estados Unidos la red eléctrica es de 120 V. ¿Qué valor de pico alcanza?
5. Una resistencia de 10 Ω se conecta a una tensión alterna de 20 V eficaces. ¿Qué potencia disipa? (Pista: con valores eficaces, las fórmulas de la sección 2 valen tal cual.)
6. El valor instantáneo de una tensión alterna en un momento dado es de 0 V. ¿Significa eso que su valor eficaz es cero?

**Soluciones**

1. De pico a pico, el doble: **100 V**. Eficaz: 0,707 × 50 = **35,4 V** (redondeando 35,35).
2. El polímetro da valores eficaces. Up = 1,414 × 24 ≈ **34 V**.
3. Pico: 10 / 2 = 5 V. Eficaz: 0,707 × 5 ≈ **3,5 V**.
4. Los 120 V son eficaces. Up = 1,414 × 120 ≈ **170 V**.
5. P = U² / R = 20² / 10 = 400 / 10 = **40 W**.
6. No. El valor instantáneo es lo que vale la tensión en ese instante concreto, y pasa por cero dos veces en cada ciclo. El valor eficaz resume lo que la onda hace a lo largo de todo el ciclo, y no cambia de un instante a otro.

## En una frase

Una onda senoidal se mide por su valor de pico (del cero a la cresta), de pico a pico (el doble) o eficaz (0,707 veces el pico: la tensión continua que haría el mismo trabajo, y el valor que se sobreentiende si no se dice nada).

Ya sabes medir el ritmo de una onda y su tamaño. Queda una tercera propiedad, que no dice cuánto ni cada cuánto, sino *por dónde va*: la fase. Es una lección corta, y de ella depende que dos señales juntas den el doble… o nada.
