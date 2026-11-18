El sábado de la obra, Dani subió a la azotea un rollo de cable «del bueno», y lo justificó a su manera: «el barato se come tus vatios como churros».

Esta lección pone números a esa frase. Al terminar sabrás cuánta potencia se queda en el cable y de qué depende, qué es el factor de velocidad, qué otras líneas existen además del coaxial y qué conectores te vas a encontrar.

Ya conoces el coaxial por dentro desde la lección 6: un conductor central (el vivo), un aislante (el dieléctrico), una malla y una cubierta, con la onda viajando encerrada entre el vivo y la malla. Y conoces su dato principal: una impedancia característica de 50 Ω que no depende de su longitud.

## Las pérdidas: los vatios que se quedan por el camino

Ningún cable es perfecto. El cobre tiene algo de resistencia y el dieléctrico no es un aislante ideal, de modo que una parte de la potencia que entra en el cable se convierte en calor y no llega al otro extremo. A eso se le llama **pérdidas** o **atenuación** del cable.

Se miden en decibelios, y los fabricantes las indican en **decibelios por cada 100 metros** a una frecuencia determinada.

Dependen de tres cosas. Las dos primeras hay que saberlas de memoria:

> **Las pérdidas de un cable coaxial aumentan con la longitud del cable y aumentan con la frecuencia.**

- **La longitud.** Si 100 metros pierden 6 dB, 50 metros pierden 3 dB y 25 metros pierden 1,5 dB. Los decibelios de pérdida son proporcionales a los metros.
- **La frecuencia.** El mismo cable pierde poco en las bandas bajas de HF y muchísimo en VHF y UHF.
- **El cable.** A igualdad de lo demás, un cable más grueso y mejor construido pierde menos.

Para traducir decibelios a vatios, recuerda de la sección 3 que perder 3 dB es quedarse con la mitad, perder 6 dB es quedarse con la cuarta parte y perder 10 dB es quedarse con la décima parte.

**Ejemplo con un cable fino y barato.** Uno de los coaxiales más comunes es el RG-58, de medio centímetro de grueso. Estos son valores típicos, solo orientativos (cada fabricante publica los de su cable, y conviene consultar su hoja de características):

| Frecuencia | Pérdida en 100 m | Pérdida en 30 m | De 100 W llegan |
|---|---|---|---|
| 7 MHz (banda de 40 m) | unos 4 dB | 1,2 dB | unos 75 W |
| 145 MHz (banda de 2 m) | unos 19 dB | 5,7 dB | unos 27 W |
| 435 MHz (banda de 70 cm) | unos 35 dB | 10,5 dB | unos 9 W |

Las dos últimas columnas corresponden a los treinta metros de bajada de una azotea normal. (Los decibelios de esa tercera columna no están entre los que sabes convertir de memoria; los vatios se han calculado con calculadora y te los damos hechos. Fíjate, eso sí, en que cuadran con lo que sabes: 10,5 dB es un poco más que 10 dB, y llegan un poco menos de la décima parte.)

- **En 7 MHz** se pierde una cuarta parte. Es tolerable.
- **En 145 MHz** se pierden casi tres cuartas partes.
- **En 435 MHz** se pierden más de nueve de cada diez vatios.

—O sea, que en setenta centímetros, con ese cable, compro un equipo de cien vatios para radiar nueve —dijo Marina.

—Y para oír menos de la décima parte de lo que te llega —añadió Dani—. El cable pierde igual en los dos sentidos. La señal que capta tu antena también tiene que bajar por él.

Esa es la mitad que se suele olvidar: las pérdidas del cable debilitan lo que transmites **y** lo que recibes.

De aquí salen tres reglas prácticas:

- **El cable, lo más corto posible.** Cada metro de sobra es pérdida de regalo. El cable sobrante no se deja enrollado detrás de la mesa «por si acaso»: se corta.
- **En VHF y UHF, cable grueso de bajas pérdidas.** En HF un cable modesto puede bastar; en UHF, el cable es media estación.
- **Antes de gastar en vatios, gasta en cable y en antena.** Cambiar un cable que pierde 3 dB por uno que pierde 1 dB equivale a pasar de un equipo de 100 W a uno de casi 160 W. Y mejora en la misma medida tu recepción, cosa que ningún amplificador hace.

Recuerda, además, lo que viste en la lección 7: con una ROE alta, las pérdidas del cable son todavía mayores que las de la tabla.

## El factor de velocidad

Dentro del cable, la onda no viaja a la velocidad de la luz, sino algo más despacio, frenada por el plástico del dieléctrico.

> **Factor de velocidad:** la proporción entre la velocidad de la onda dentro del cable y la velocidad de la luz. Vale alrededor de **0,66** en los coaxiales de dieléctrico macizo y de 0,80 a 0,85 en los de dieléctrico de espuma, que son los de bajas pérdidas.

Si la onda va más despacio y la frecuencia es la misma, cada ciclo avanza menos: **dentro del cable, la longitud de onda es más corta que en el aire.** Se calcula multiplicando la longitud de onda normal por el factor de velocidad.

En el uso corriente no tienes que preocuparte de esto: un cable de bajada puede medir lo que haga falta. Importa solo cuando se necesita un trozo de cable que mida una fracción exacta de la longitud de onda, y el examen pide alguna vez la cuenta.

**Ejemplo.** *¿Cuánto mide un cuarto de onda de cable coaxial de factor 0,66 para 145 MHz?*

- Longitud de onda en el aire: 300 / 145 = 2,07 m.
- Un cuarto de onda en el aire: 2,07 / 4 = 0,52 m.
- Dentro del cable: 0,52 × 0,66 = 0,34 m. **34 centímetros.**

### Para curiosos: trozos de cable a medida

Este apartado no hace falta dominarlo; basta con que te suenen los dos nombres que aparecen en él.

¿Y para qué querría nadie un trozo de cable de un cuarto de onda exacto? Porque tiene una propiedad curiosa: **transforma impedancias**. Un cuarto de onda de cable de 75 Ω, por ejemplo, hace que una antena de 112,5 Ω se vea desde el otro extremo como si fuera de 50 Ω. (La regla es que la impedancia del cable, multiplicada por sí misma, iguala al producto de las otras dos: 75 × 75 = 5.625, y 50 × 112,5 = 5.625.) Se le llama **transformador de cuarto de onda**, y es una de las maneras clásicas de adaptar una antena.

Los trozos de línea cortados a medida tienen otro uso que conviene que te suene. Un trozo de un cuarto de onda con el extremo en cortocircuito, o con el extremo abierto, se comporta como un circuito resonante de bobina y condensador, y se emplea como filtro. A esos trozos de línea se les llama *stubs*.

## Otras líneas de transmisión

El coaxial no es la única línea que existe.

**La línea paralela.** Son dos hilos iguales que corren uno junto al otro, mantenidos a distancia fija por separadores de plástico. Por su aspecto se la llama también *escalerilla*. Sus impedancias típicas son altas, de 300 a 600 Ω.

Es una línea **simétrica**: sus dos hilos son idénticos, como los dos brazos de un dipolo. (Guarda esa palabra, que vuelve en la lección siguiente.) Tiene una ventaja y un inconveniente, los dos grandes. Pierde muchísimo menos que el coaxial. Pero no está blindada: no puede pasar cerca de objetos metálicos ni pegarse a una pared, porque todo lo que tiene cerca la perturba. Por comodidad ganó el coaxial, aunque la escalerilla sigue teniendo sus fieles.

**La guía de ondas.** En las frecuencias más altas, las microondas, incluso el mejor coaxial pierde demasiado. Allí se usa un simple tubo metálico hueco, sin conductor central, por cuyo interior viaja la onda. Para el examen basta saber que existe y que es cosa de microondas.

## Los conectores

El cable termina en conectores. Hay tres que debes reconocer por su nombre: el **PL-259** (con su hembra, la **SO-239**), roscado y robusto, que es el clásico de HF y el que llevan casi todos los equipos de base; el **BNC**, de bayoneta, que se encaja con un cuarto de vuelta y se usa en portátiles e instrumentos; y el **N**, roscado y estanco, de pocas pérdidas, que es el indicado para VHF, UHF y potencias altas. En los walkies modernos encontrarás además el **SMA**, pequeño y roscado.

Un conector mal soldado o mal apretado es la avería más frecuente de cualquier instalación de antena. Y todo conector que quede a la intemperie debe sellarse contra el agua: un cable con agua dentro multiplica sus pérdidas y hay que tirarlo.

## Donde la gente se lía

- **«El cable no importa, lo que cuenta es la antena.»** En VHF y UHF, un cable malo puede quedarse con la mayor parte de la potencia, y de la señal recibida.
- **«Las pérdidas solo afectan a la transmisión.»** Afectan por igual a lo que sale y a lo que entra.
- **«A más frecuencia, menos pérdidas.»** Al revés: las pérdidas **aumentan** con la frecuencia.
- **«Un cable con más pérdidas tiene más impedancia.»** Son cosas independientes. Un cable de 50 Ω puede perder muy poco o muchísimo.

## Compruébalo tú

1. Un cable pierde 8 dB por cada 100 metros a cierta frecuencia. ¿Cuánto pierden 25 metros de ese cable?
2. Un transmisor entrega 40 W a un cable que pierde 3 dB. ¿Qué potencia llega a la antena?
3. Un transmisor de 80 W alimenta una antena a través de un cable que pierde 6 dB. ¿Cuántos vatios llegan? ¿Cuántos se quedan en el cable?
4. Tienes el mismo cable y la misma longitud en dos instalaciones, una para 14 MHz y otra para 432 MHz. ¿En cuál pierde más?
5. ¿Cuánto mide media onda de cable coaxial de factor de velocidad 0,66 para 50 MHz?
6. ¿Qué línea es simétrica: el coaxial o la línea paralela? ¿Cuál de las dos tiene menos pérdidas?

**Soluciones**

1. 25 metros son la cuarta parte de 100: 8 / 4 = **2 dB**.
2. Perder 3 dB es quedarse con la mitad: **20 W**.
3. Perder 6 dB es quedarse con la cuarta parte: llegan 80 / 4 = **20 W**. Los otros **60 W** se convierten en calor en el cable.
4. En **432 MHz**. Las pérdidas aumentan con la frecuencia.
5. Longitud de onda en el aire: 300 / 50 = 6 m. Media onda: 3 m. Dentro del cable: 3 × 0,66 = **1,98 m**.
6. La **línea paralela** es la simétrica, y es también la que tiene **menos pérdidas**. El coaxial es asimétrico; a cambio, está blindado.

## En una frase

El coaxial se queda con una parte de la potencia que crece con la longitud y con la frecuencia, y eso vale igual para lo que transmites y para lo que recibes: cable corto y bueno, sobre todo en VHF y UHF; dentro de él la onda viaja más despacio que la luz, en la proporción que marca su factor de velocidad.

Queda la última pieza que Dani subió a la azotea: un cacharro que parecía un yoyó gordo, y que está ahí para impedir que el cable haga algo que, en teoría, un cable blindado no debería poder hacer.
