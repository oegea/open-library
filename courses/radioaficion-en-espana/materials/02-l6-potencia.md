En la lección anterior viste que un cable de medio ohmio puede dejar sin alimentación a una emisora. Esta lección explica por qué ese mismo cable, además, se calienta, y te da la herramienta para saber cuánto pide de verdad cualquier aparato: la **potencia**.

Aparecen dos palabras que en la vida diaria se usan como si fueran lo mismo y no lo son: **energía** y **potencia**. Entender la diferencia es la mitad del trabajo. En esta lección nos ocupamos de la potencia; en la siguiente, de la energía y de las baterías.

## Energía y potencia: el depósito y el ritmo

Piensa en un coche.

- La gasolina que hay en el depósito es **cuánto** tienes. Cuarenta litros son cuarenta litros, los gastes en una hora o en una semana.
- El consumo del motor es **a qué ritmo** la gastas. Subiendo un puerto a fondo gasta deprisa; por ciudad, despacio.

En electricidad:

- La **energía** es el *cuánto*: la cantidad total de trabajo que se puede hacer (encender una luz, mover un altavoz, emitir una señal). Es lo que hay guardado en una batería. Se mide en **julios (J)**.
- La **potencia** es el *ritmo*: cuánta energía se gasta **cada segundo**.

> **Potencia:** la energía que se consume (o se entrega) cada segundo. Se mide en **vatios (W)**. En las fórmulas es la letra **P**.

Una bombilla de 10 W gasta energía despacio. Una estufa de 2.000 W la gasta doscientas veces más deprisa. Ninguna de las dos cifras te dice cuánta energía han gastado en total: eso depende, además, del tiempo que estén encendidas.

## La fórmula de la potencia

¿De qué depende el ritmo al que un aparato gasta energía? De dos cosas que ya conoces.

En el circuito de agua, la rueda de paletas gira con más fuerza cuanta más agua pasa por ella y cuanta más presión trae esa agua. En un circuito eléctrico, la energía que recibe un aparato cada segundo depende de **cuánta corriente lo atraviesa** y de **con cuánta tensión llega empujada**.

—¿Y cómo se juntan las dos? —preguntó Marina—. ¿Se suman, se multiplican…?

—Se multiplican —dijo Vicente—, y no hace falta que te lo creas: se puede ver.

Para verlo hace falta un dato nuevo sobre el voltio, que hasta ahora solo habíamos descrito como «empuje»:

> **Un voltio significa que cada culombio de carga, al atravesar el aparato, deja en él 1 julio de energía.** A 12 voltios, cada culombio deja 12 julios.

Y recuerda qué era un amperio: un culombio que pasa cada segundo.

Ahora junta las dos cosas con la emisora de Vicente, que transmitiendo funciona a 12 V y 10 A:

- 10 amperios: cada segundo la atraviesan 10 culombios.
- 12 voltios: cada uno de esos culombios deja 12 julios.
- En total, cada segundo se quedan en la emisora 10 × 12 = **120 julios**.

«Julios cada segundo» es justo lo que hemos llamado potencia, y su unidad es el vatio: **1 vatio = 1 julio cada segundo**. Por eso se multiplica: lo que deja cada paquete de carga, por el número de paquetes que pasan cada segundo.

**P = U × I**

*La potencia (en vatios) es igual a la tensión (en voltios) multiplicada por la corriente (en amperios).*

**Ejemplo.** *Un equipo funciona a 12 V y por él circulan 3 A. ¿Qué potencia consume?*

P = U × I = 12 × 3 = **36 W**

Volvamos a la emisora, con un aviso que te ahorrará un malentendido: sus 120 W son los que la emisora **toma de la batería**, no los que **emite por la antena**. Una emisora así emite unos 50 W de señal de radio; el resto, unos 70 W, se pierde en forma de calor dentro del equipo (por eso se calienta y lleva aletas de refrigeración). A la proporción entre lo que un aparato entrega de forma útil y lo que consume se le llama **rendimiento**. En este caso, 50 / 120 ≈ 0,42 (el signo ≈ significa «aproximadamente»): un rendimiento del 42 %.

### La misma potencia, de dos maneras

Compara estos dos aparatos:

- Una emisora a 12 V consumiendo 10 A: 12 × 10 = 120 W.
- Una lámpara a 230 V consumiendo 0,52 A: 230 × 0,52 ≈ 120 W.

Las dos gastan energía al mismo ritmo. La primera lo hace con poco empujón y mucha corriente; la segunda, con mucho empujón y poca corriente. De aquí salen dos consecuencias prácticas:

- Los equipos de 12 V necesitan corrientes grandes para dar potencias serias, y las corrientes grandes exigen cables gruesos. Por eso los cables de alimentación de una emisora son gruesos como un lápiz, mientras que el cable de una lámpara de 230 V es fino.
- Las compañías eléctricas transportan la energía a cientos de miles de voltios precisamente para poder hacerlo con poca corriente y perder poco por el camino. Lo entenderás del todo dentro de dos apartados.

## Las otras dos fórmulas, deducidas paso a paso

La fórmula P = U × I necesita que conozcas la tensión y la corriente. A veces no tienes las dos, pero sí la resistencia. Entonces se combina con la ley de Ohm. Vamos a hacerlo despacio, porque el examen pide las tres formas.

**Si conoces la corriente y la resistencia** (pero no la tensión): la ley de Ohm dice que U = I × R. Sustituye esa U en la fórmula de la potencia:

P = U × I = (I × R) × I

Como todo son multiplicaciones, el orden da igual y los paréntesis sobran: P = I × I × R

Y como I × I se escribe I² («I al cuadrado»):

**P = I² × R**

**Si conoces la tensión y la resistencia** (pero no la corriente): la ley de Ohm dice que I = U / R. Sustituye esa I:

P = U × I = U × (U / R) = (U × U) / R

**P = U² / R**

Resumen, para tener a mano:

| Conozco… | Uso… |
|---|---|
| tensión y corriente | **P = U × I** |
| corriente y resistencia | **P = I² × R** |
| tensión y resistencia | **P = U² / R** |

No hace falta memorizar las tres si entiendes de dónde salen: con P = U × I y la ley de Ohm las reconstruyes en diez segundos.

**Ejemplo.** *¿Qué potencia disipa una resistencia de 50 Ω por la que circulan 2 A?*

Conozco corriente y resistencia: P = I² × R = 2² × 50 = 4 × 50 = **200 W**.

(«Disipar» es la palabra técnica para «convertir en calor y soltarlo al ambiente».)

**Ejemplo.** *¿Qué potencia consume una resistencia de 6 Ω conectada a 12 V?*

Conozco tensión y resistencia: P = U² / R = 12² / 6 = 144 / 6 = **24 W**.

## El cuadrado que quema cables

Fíjate bien en P = I² × R, porque ese cuadrado tiene consecuencias.

Toda resistencia atravesada por una corriente se calienta, y la potencia que se convierte en calor crece con el **cuadrado** de la corriente. Si la corriente se duplica, el calor no se duplica: se multiplica por cuatro. Si se triplica, por nueve.

Recupera el cable de la lección anterior, el de 0,5 Ω con el que Marina alimentaba la emisora:

- Con 2 A, el cable disipa 2² × 0,5 = 2 W. Ni se nota.
- Con 10 A, disipa 10² × 0,5 = 50 W. Eso ya es un cable caliente y medio equipo sin alimentar.

Es la razón de tres cosas que ya han ido saliendo:

- Un cortocircuito pone los cables al rojo: la corriente es enorme, y su cuadrado, más.
- Los fusibles funcionan: están hechos para fundirse con el calor de una corriente determinada.
- La red eléctrica usa alta tensión: para transportar la misma potencia con menos corriente y así perder mucho menos en los cables.

Y una advertencia sobre los componentes. Cada resistencia que compres tendrá dos datos: su valor en ohmios y la **potencia máxima** que puede disipar sin quemarse. Las pequeñas de electrónica aguantan un cuarto de vatio (0,25 W). La resistencia del ejemplo de arriba, que tenía que disipar 200 W, debería ser una pieza del tamaño de un ladrillo y con aletas. Si pusieras en su lugar una de 0,25 W, duraría una fracción de segundo.

## Donde la gente se lía

- **Confundir potencia y energía.** La potencia es un ritmo (cuánto se gasta cada segundo); la energía, una cantidad. La lección siguiente está dedicada a no mezclarlas.
- **Creer que los vatios consumidos son los vatios emitidos.** Ningún aparato convierte toda la energía que consume en lo que queremos de él. La diferencia se va en calor.
- **Olvidar el cuadrado en P = I² × R.** Primero se eleva la corriente al cuadrado y después se multiplica por la resistencia. Con 4 A y 5 Ω son 16 × 5 = 80 W, no 20 W.

## Compruébalo tú

1. Un equipo consume 5 A a 13,8 V. ¿Qué potencia consume?
2. Por una resistencia de 20 Ω circulan 3 A. ¿Qué potencia disipa?
3. Una resistencia de 100 Ω se conecta a 10 V. ¿Qué potencia disipa? ¿Sirve para eso una resistencia de un cuarto de vatio?
4. Una bombilla de 12 V consume 24 W. ¿Qué corriente pasa por ella?
5. Un transmisor emite 30 W de señal y consume 75 W de la batería. ¿Cuál es su rendimiento?

**Soluciones**

1. P = U × I = 13,8 × 5 = **69 W**.
2. P = I² × R = 3² × 20 = 9 × 20 = **180 W**.
3. P = U² / R = 10² / 100 = 100 / 100 = **1 W**. No sirve una de 0,25 W: se quemaría. Hace falta una de al menos 1 W, y mejor de 2 W para ir con margen.
4. De P = U × I se despeja I = P / U = 24 / 12 = **2 A**.
5. Rendimiento = potencia útil / potencia consumida = 30 / 75 = 0,4, es decir, un **40 %**.

## En una frase

La potencia es el ritmo al que un aparato gasta energía: se calcula multiplicando su tensión por su corriente (**P = U × I**, en vatios), y en una resistencia crece con el cuadrado de la corriente.

Con la potencia ya puedes saber cuánto pide un aparato. Falta saber cuánto le puedes dar: la energía que cabe en una batería y las horas que dura. Es la cuenta de Vicente, y es la lección siguiente.
