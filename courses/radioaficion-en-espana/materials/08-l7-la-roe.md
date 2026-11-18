«Uno coma dos», dijo el analizador en la azotea, y Dani silbó. Marina apuntó en su cuaderno que tenía que preguntar qué pasaba «cuando el acuerdo se rompe».

Esta lección es la respuesta. Al terminar sabrás qué mide exactamente la ROE, cómo leer sus valores y qué daños causa de verdad una ROE alta, que no son los que casi todo el mundo cree. Es pregunta segura de examen.

## De dónde sale el nombre

En la lección anterior quedó una imagen pendiente. Cuando la antena no está bien adaptada, por el cable viajan a la vez dos ondas: la **directa**, que va del transmisor a la antena, y la **reflejada**, que vuelve de la antena al transmisor.

Y en la lección 1 viste qué ocurre cuando una onda se cruza continuamente con su propio rebote: se forma una **onda estacionaria**. Allí, dentro de la antena, la buscábamos; aquí, en el cable, es el síntoma de que algo rebota. En unos puntos del cable las dos ondas se suman siempre y la tensión entre el vivo y la malla es alta; en otros puntos se restan siempre y esa tensión es baja. Esos puntos no se mueven.

Si pudieras recorrer el cable con un voltímetro de radiofrecuencia, verías:

- **Con la antena perfectamente adaptada**, no hay onda reflejada. Nada se suma ni se resta: la tensión es igual en todos los puntos del cable.
- **Con la antena desadaptada**, la tensión sube y baja a lo largo del cable, con máximos y mínimos fijos. Cuanto mayor es la onda reflejada, más diferencia hay entre los máximos y los mínimos.

Pues bien, la ROE es simplemente esa comparación:

> **ROE (relación de ondas estacionarias):** el número que resulta de dividir la tensión máxima entre la tensión mínima a lo largo de la línea. Mide cuánta onda reflejada hay, es decir, lo mal adaptada que está la antena al cable.

En inglés se llama **SWR** (*standing wave ratio*), y lo verás escrito así en casi todos los aparatos.

Si no hay reflexión, el máximo y el mínimo son iguales, y un número dividido entre sí mismo da 1. Por eso:

- **La mejor ROE posible es 1.** No puede haber una ROE menor que 1. (Verás la ROE escrita también como una proporción: 1:1, 2:1, 3:1. Es lo mismo; en este curso escribimos solo el primer número.)
- Cuanto más por encima de 1, peor adaptación.

![Tres cables con la tensión dibujada a lo largo de cada uno. Con ROE 1, la tensión es una línea plana: no hay onda reflejada. Con ROE 2, la tensión ondula y su máximo es el doble que su mínimo. Con ROE 5, ondula mucho más: el máximo es cinco veces el mínimo.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-ondas-estacionarias-en-la-linea.svg)

## La forma fácil de calcularla

Hay una manera muy sencilla de saber qué ROE va a salir. Cuando la antena se comporta como una resistencia pura (lo que ocurre en su frecuencia de resonancia), la ROE es la división entre las dos impedancias, **poniendo siempre arriba la mayor**:

**ROE = impedancia mayor / impedancia menor**

| Antena conectada a un cable de 50 Ω | Cuenta | ROE |
|---|---|---|
| 50 Ω | 50 / 50 | 1 |
| Dipolo, 73 Ω | 73 / 50 | 1,46 |
| Vertical, 36 Ω | 50 / 36 | 1,39 |
| 100 Ω | 100 / 50 | 2 |
| 25 Ω | 50 / 25 | 2 |
| 150 Ω | 150 / 50 | 3 |

Fíjate en las filas de 100 Ω y de 25 Ω. Una tiene el doble de impedancia que el cable y la otra la mitad, y las dos dan ROE 2. A la ROE le da igual hacia qué lado esté el desacuerdo: solo mide cuánto hay.

## Cuánta potencia rebota

La otra pregunta natural es qué parte de la potencia se refleja con cada ROE. La cuenta se hace en dos pasos y no necesita más que restar, sumar, dividir y multiplicar:

1. Divide (ROE − 1) entre (ROE + 1).
2. Multiplica el resultado por sí mismo.

Lo que sale es la fracción de la potencia que se refleja.

**Ejemplo, con ROE 2.** Paso 1: (2 − 1) / (2 + 1) = 1 / 3 = 0,333. Paso 2: 0,333 × 0,333 = 0,111. Se refleja el **11 %**.

**Ejemplo, con ROE 3.** Paso 1: (3 − 1) / (3 + 1) = 2 / 4 = 0,5. Paso 2: 0,5 × 0,5 = 0,25. Se refleja el **25 %**.

(El primer paso da la proporción entre la *tensión* de la onda reflejada y la de la directa. Se multiplica por sí misma porque, como viste en la sección 2, la potencia va con el cuadrado de la tensión.)

En el examen basta con conocer la tabla que sale de esa cuenta:

| ROE | Potencia reflejada | Valoración |
|---|---|---|
| 1 | 0 % | Perfecta |
| 1,2 | menos del 1 % | Excelente (la de la azotea de Marina) |
| 1,5 | 4 % | Muy buena |
| 2 | 11 % | Aceptable. Límite cómodo de muchos equipos |
| 3 | 25 % | Mala. Los equipos empiezan a protegerse |
| 5 | 44 % | Muy mala |
| Infinita | 100 % | Cable cortado o en cortocircuito: rebota todo |

Mira la tabla con calma, porque desmonta una obsesión muy extendida. Entre una ROE de 1 y una de 1,5 la diferencia es un 4 % de potencia: nadie en el mundo distinguiría tu señal de una a otra.

## Qué daña de verdad una ROE alta

—Entonces, con ROE tres pierdo la cuarta parte de mis vatios —dijo Marina—. No me parece para tanto.

—Es que el problema de la ROE alta no es ese —contestó Vicente—. Son otros dos.

**Lo que no es el problema.** La potencia reflejada no se evapora en el aire ni «se pierde» sin más. Lo que ocurre en la práctica es que el transmisor, al encontrarse con una carga que no es de 50 Ω, trabaja forzado y entrega menos potencia de la que podría. Si se le ayuda a entregarla, con el acoplador que conocerás en la lección siguiente, casi toda acaba radiada, salvo lo que el cable se quede por el camino.

**El primer problema: el transmisor sufre.** La onda que vuelve se suma en el transmisor a la que sale. La etapa final del equipo, que conociste en la sección 7 (sus transistores de potencia), queda sometida a tensiones y corrientes mayores que aquellas para las que fue diseñada, y se calienta. Con una ROE muy alta, esos transistores pueden destruirse en segundos.

Por eso los equipos modernos llevan un **circuito de protección**: miden la ROE continuamente y, cuando pasa de un cierto valor (normalmente entre 2 y 3), **reducen la potencia por su cuenta**. Con ROE alta no es que tu equipo radie el 75 % de sus cien vatios: es que decide entregar veinte, o diez, para no romperse. Ahí está la pérdida grande.

**El segundo problema: el cable pierde más.** Todo cable convierte en calor una parte de la potencia que lo recorre. Con ROE alta, una parte de la energía recorre el cable no una vez, sino varias, de ida y de vuelta, y paga peaje en cada viaje. Con un cable corto y bueno, el efecto es pequeño. Con un cable largo o de mala calidad, y sobre todo en VHF y UHF, puede ser enorme.

Y hay todavía un efecto más: con ROE alta, las tensiones en algunos puntos del cable y del equipo son mucho mayores de lo normal, y con potencias grandes pueden saltar chispas en conectores y condensadores.

> **Una ROE alta es mala, sobre todo, porque pone en peligro la etapa final del transmisor (que se protege reduciendo potencia) y porque aumenta las pérdidas en el cable.**

## Donde la gente se lía

- **«Una ROE de 1 significa que la antena es buena.»** Significa que está bien adaptada, nada más. Una simple resistencia de 50 Ω conectada al final del cable da una ROE perfecta de 1 y no radia nada. La ROE mide el acuerdo, no la calidad de la antena.
- **«Con ROE 2 pierdo la mitad de la potencia.»** Se refleja un 11 %.
- **«Hay que conseguir ROE 1,0 a toda costa.»** Por debajo de 1,5 la diferencia es imperceptible. Por debajo de 2, casi siempre irrelevante.
- **«Una antena de 25 Ω da mejor ROE que una de 100 Ω, porque tiene menos impedancia.»** Las dos dan ROE 2. Cuenta lo lejos que están de 50, no hacia qué lado.

## Compruébalo tú

1. Un compañero presume de que su antena tiene «ROE 0,8». ¿Qué le contestas?
2. Una antena presenta 200 Ω resistivos y se conecta a un cable de 50 Ω. ¿Qué ROE habrá?
3. ¿Y si la antena presentara 12,5 Ω?
4. Con una ROE de 4, ¿qué porcentaje de la potencia se refleja? Usa los dos pasos.
5. Tu equipo, de 100 W, solo da 30 W en una antena con ROE 3,5. ¿Por qué?
6. En la lección anterior quedó pendiente una comparación: ¿cuál está mejor adaptada a un cable de 50 Ω, una vertical de 36 Ω o un dipolo de 73 Ω?
7. ¿Dónde hace más daño una ROE de 3: con un cable corto y bueno en onda corta, o con un cable largo y fino en UHF? ¿Por qué?

**Soluciones**

1. Que es imposible: la ROE es un máximo dividido entre un mínimo, y nunca baja de **1**, que ya significa que no hay onda reflejada. Si su medidor marca menos, lo que falla es el medidor.
2. 200 / 50 = **4**.
3. Se pone arriba la mayor: 50 / 12,5 = **4**. La misma ROE que con 200 Ω.
4. Paso 1: (4 − 1) / (4 + 1) = 3 / 5 = 0,6. Paso 2: 0,6 × 0,6 = 0,36. Se refleja el **36 %**.
5. Porque el **circuito de protección** ha detectado la ROE alta y ha reducido la potencia para no dañar la etapa final.
6. La vertical: 50 / 36 = 1,39. El dipolo: 73 / 50 = 1,46. Gana la **vertical**, por muy poco. En la práctica, las dos están muy bien adaptadas.
7. Con el **cable largo y fino en UHF**. El transmisor sufre igual en los dos casos, pero el segundo daño, el aumento de las pérdidas en el cable, es pequeño cuando el cable pierde poco y muy grande cuando ya pierde mucho.

## En una frase

La ROE compara el máximo y el mínimo de tensión a lo largo del cable para decir cuánta onda rebota de la antena: 1 es perfecto, hasta 2 es aceptable, y por encima el transmisor se protege reduciendo potencia y el cable pierde más.

Ya sabes leer el número. En la lección siguiente conocerás los aparatos con los que se mide, el que lo «arregla» sin arreglarlo y el que permite probarlo todo sin salir al aire.
