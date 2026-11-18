La antena que Marina colgó en la azotea es la más sencilla que existe y, a la vez, la más importante: el **dipolo de media onda**. Es la antena con la que se comparan todas las demás, la primera que construye casi todo radioaficionado y una de las que más preguntas reúne en el examen.

Al terminar esta lección sabrás cómo es un dipolo, cuánto mide, hacia dónde radia y hacia dónde no, y por qué en la junta de vecinos Vicente insistió tanto en ponerlo alto.

## Cómo es un dipolo

En la lección anterior viste que un hilo de media onda entra en resonancia y que en su centro la corriente es máxima. El dipolo es ese hilo, cortado justo por el centro para poder conectarle ahí el cable del transmisor.

> **Dipolo de media onda:** una antena formada por dos brazos iguales de un cuarto de onda cada uno, colocados en línea uno a continuación del otro, y alimentada por el centro.

«Alimentar» una antena es conectarle el cable que trae la energía del transmisor. El sitio donde se conecta se llama **punto de alimentación**.

El de Marina tiene estas piezas, y cualquier otro dipolo de hilo tiene las mismas:

- **Dos brazos** de hilo de cobre.
- **Un aislador central**, una pieza de plástico que sujeta los dos brazos sin que se toquen entre sí. Ahí llega el cable, que tiene dos conductores (lo abriremos para verlo por dentro en la lección 6): uno se une a un brazo y el otro al otro brazo.
- **Dos aisladores en las puntas**, de los que salen las cuerdas que tensan la antena hacia sus apoyos. Recuerda que en las puntas está la tensión más alta: el hilo nunca se ata directamente a un mástil.
- **El cable de bajada**, que lleva la señal entre la antena y el equipo. Le dedicaremos la lección 9.

![Un dipolo de media onda colgado entre dos apoyos. Tiene dos brazos iguales de un cuarto de onda, un aislador en el centro del que baja el cable hacia el equipo y un aislador en cada punta. La longitud total es de media onda: 142,5 dividido entre la frecuencia en megahercios.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-dipolo-partes.svg)

La longitud total es la que ya sabes calcular, 142,5 / f, y cada brazo mide la mitad.

**Ejemplo.** *Un dipolo para 18,1 MHz.*

Longitud total: 142,5 / 18,1 = 7,87 m. Cada brazo: 7,87 / 2 = **3,94 m**.

Un aviso para el examen: lee bien si te piden la longitud **total** o la de **cada brazo**. Es la manera más tonta de perder una pregunta que sabías.

## La impedancia del dipolo: 73 ohmios

Recuerda de la sección 5 qué era la **impedancia**: la oposición total que algo presenta a la corriente alterna, medida en ohmios. Es la versión para alterna de la resistencia, y se calcula igual: tensión dividida entre corriente.

Una antena también tiene impedancia. Es la que «ve» el transmisor cuando se conecta a ella: la relación entre la tensión que aplica en el punto de alimentación y la corriente que consigue hacer circular.

Mira otra vez las dos curvas de la lección anterior. En el centro del dipolo la corriente es grande y la tensión es pequeña. Poca tensión dividida entre mucha corriente da un número bajo. Para un dipolo de media onda alejado de todo, ese número es:

> **La impedancia de un dipolo de media onda en su centro es de unos 73 Ω.**

(La cifra exacta sale de un cálculo que queda fuera de este curso. Aquí la tomamos como un dato; lo que sí puedes razonar tú es por qué es baja.)

Dos precisiones sobre esa cifra, que el examen pregunta tal cual:

- Es el valor «en el espacio libre», es decir, lejos del suelo y de cualquier objeto. En una azotea real cambia con la altura sobre el suelo y suele quedar **entre 40 y 90 Ω**.
- Si el mismo hilo se alimentara por una punta en vez de por el centro, ocurriría lo contrario: mucha tensión y casi nada de corriente, es decir, una impedancia de miles de ohmios. Se puede hacer, y hay antenas así (se las conoce como *antenas de media onda alimentadas por un extremo*), pero necesitan un transformador que las adapte. Alimentar por el centro es lo que hace cómodo al dipolo.

—¿Y esa impedancia quiere decir que la antena se calienta, como una resistencia? —preguntó Marina.

—No —dijo Dani—. Una resistencia convierte en calor la energía que le llega. La antena la convierte en onda de radio. Al transmisor le da igual: él solo nota que la energía se le va y no vuelve. Por eso la antena se le presenta como si fuera una resistencia de setenta y tres ohmios, aunque dentro del hilo no haya ninguna.

A esa «resistencia» que no calienta, sino que representa la energía que se marcha en forma de onda, se le llama **resistencia de radiación**. El nombre aparece en algunos libros y conviene que te suene.

Por qué 73 Ω es una cifra afortunada lo verás en la lección 6. Adelanto: los equipos y los cables de radio están hechos para 50 Ω, y 73 queda lo bastante cerca para conectarlos sin más complicaciones.

## Hacia dónde radia: el diagrama en ocho

Un dipolo no radia igual en todas las direcciones, y esto es de lo más útil que puedes saber de él.

- Radia con la máxima fuerza en las direcciones **perpendiculares al hilo**: de frente y de espaldas.
- No radia prácticamente nada en la dirección **de sus puntas**.

Si miras el dipolo desde arriba y dibujas alrededor de él con cuánta fuerza radia hacia cada lado, sale una figura con dos lóbulos, uno a cada lado del hilo, parecida a un ocho. A ese dibujo se le llama **diagrama de radiación**.

> **Diagrama de radiación:** el dibujo que muestra con qué intensidad radia una antena en cada dirección. Cuanto más se aleja la curva del centro en una dirección, más fuerte radia hacia allí.

![Un dipolo visto desde arriba, como en un mapa: el hilo está tendido de norte a sur. Su diagrama de radiación son dos lóbulos redondos, uno hacia el este y otro hacia el oeste, que juntos forman un ocho. La radiación es máxima de frente y de espaldas al hilo y casi nula hacia las puntas, es decir, hacia el norte y el sur.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-diagrama-ocho.svg)

La consecuencia práctica es inmediata: **importa cómo orientas el hilo.** Un dipolo tendido de norte a sur radia sobre todo hacia el este y hacia el oeste, y deja en sombra el norte y el sur. Desde Valencia, un hilo tendido de norte a sur favorece América por un lado y el Mediterráneo oriental por el otro.

Esto vale del todo para un dipolo colocado alto. En uno bajo, como verás enseguida, la señal sale tan hacia arriba que la orientación del hilo apenas se nota.

A una antena que radia igual en todas las direcciones del horizonte se le llama **omnidireccional**. El dipolo horizontal no lo es. Tampoco es una antena muy dirigida: sus dos lóbulos son anchos y solo las direcciones cercanas a las puntas quedan mal servidas.

Recuerda, además, lo que viste en la sección 6 sobre la **polarización**: la onda sale polarizada en la misma orientación que el hilo. Un dipolo tendido en horizontal emite con polarización horizontal.

## La altura lo cambia casi todo

Hasta aquí hemos imaginado el dipolo flotando en el vacío. En una azotea, debajo tiene el suelo, y el suelo refleja parte de la onda. La onda que sale directamente de la antena y la que rebota en el suelo se juntan en el aire, y según la altura se refuerzan en unos ángulos y se anulan en otros. (Es lo mismo que viste en la sección 3: dos ondas pueden sumarse o cancelarse según su fase.)

Para describir el resultado hace falta una expresión nueva:

> **Ángulo de salida:** la inclinación, medida desde el horizonte, a la que una antena lanza la mayor parte de su energía. Un ángulo de 90° es recto hacia el cielo; uno de 10° es casi rasante.

Hasta ahora mirábamos la antena desde arriba. El ángulo de salida se ve mirándola de lado:

- **Un dipolo bajo**, a menos de un cuarto de onda del suelo, lanza casi toda su energía hacia arriba, con un ángulo de salida muy alto.
- **Un dipolo alto**, a media onda del suelo o más, lanza su energía mucho más rasante, a unos 30° del horizonte o menos.

![Dos dipolos vistos de lado, con el suelo debajo. El de la izquierda está bajo, a un octavo de onda del suelo: su radiación forma un solo lóbulo que apunta hacia el cielo. El de la derecha está alto, a media onda del suelo: su radiación forma dos lóbulos inclinados, a unos 30 grados del horizonte.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-angulo-de-salida.svg)

¿Y qué más da hacia dónde salga? En onda corta, las señales llegan lejos porque suben hasta unas capas altas de la atmósfera que las devuelven hacia el suelo, como una pelota que bota en el techo. Cómo y por qué ocurre es el tema de la sección 9; aquí basta la geometría. Una señal lanzada casi en vertical vuelve a caer cerca, a unos cientos de kilómetros. Una lanzada rasante recorre muchísima distancia antes de volver a tierra.

De ahí la regla: **para llegar lejos, la antena, alta.**

Haz la cuenta con la de Marina. En la banda de 40 metros, media onda son unos 20 metros de altura. Su azotea le da bastante menos, así que su dipolo es más bien «bajo»: excelente para hablar con toda España, que es justo lo que hace falta en una emergencia, y algo menos brillante para Australia. Y por lo mismo, a ella la orientación del hilo le importa poco. No es un defecto: es saber qué se puede esperar de cada instalación.

La altura trae otros dos regalos. Aleja la antena de los aparatos de la casa, que son la principal fuente de ruido en recepción. Y aleja la señal de los vecinos, que es lo que Vicente le explicó a Puri en la junta: cuanto más arriba, menos se queda en el edificio.

### Si no hay sitio: la V invertida

Un dipolo no tiene por qué estar perfectamente recto y horizontal. La variante más usada necesita un solo mástil: el centro se sube a lo más alto y los dos brazos bajan inclinados hacia los lados, como las dos aguas de un tejado. Se llama **V invertida**. Rinde casi igual que el dipolo horizontal, radia de forma algo más repartida, ocupa algo menos de largo, necesita un solo apoyo alto y su impedancia baja desde los 73 Ω hacia los 50 Ω, que es una ventaja, como verás en la lección 6.

### Un pariente con nombre de examen: el dipolo plegado

Si al dipolo le añades un segundo hilo paralelo, unido al primero por las dos puntas, y conectas el cable solo a uno de los dos, obtienes un **dipolo plegado**. Mide lo mismo y radia igual, pero su impedancia es cuatro veces mayor: unos **300 Ω**. Trabaja bien en un tramo más ancho de frecuencias, y es el elemento al que llega el cable en muchas antenas de televisión.

## Donde la gente se lía

- **«El dipolo radia hacia donde apuntan sus puntas.»** Al revés. Hacia las puntas es hacia donde menos radia. El máximo está de frente y de espaldas al hilo.
- **«Los 73 Ω son la resistencia del hilo.»** El hilo de cobre tiene una resistencia minúscula. Los 73 Ω son la impedancia que la antena presenta al transmisor, y representan la energía que se va radiada.
- **«La altura da igual, lo importante es que el hilo mida lo suyo.»** La medida decide la frecuencia; la altura decide con qué ángulo sale la señal y cuánto ruido recoges.

## Compruébalo tú

1. Calcula la longitud total y la de cada brazo de un dipolo para 28,5 MHz.
2. Quieres hablar sobre todo con estaciones situadas al norte y al sur de tu casa. ¿En qué dirección tiendes el hilo del dipolo?
3. Un dipolo está tendido de este a oeste. Una estación situada exactamente al este, ¿te oirá bien o mal?
4. ¿Por qué se alimenta el dipolo por el centro y no por una punta?
5. Tienes dos sitios para colgar el mismo dipolo: un balcón a 4 metros del suelo y una azotea a 15 metros. Nombra dos ventajas de la azotea.
6. Verdadero o falso: «un dipolo de media onda en el espacio libre tiene una impedancia de unos 50 Ω».
7. ¿Qué impedancia aproximada tiene un dipolo plegado? ¿Mide más que un dipolo normal?

**Soluciones**

1. Total: 142,5 / 28,5 = **5,0 m**. Cada brazo: **2,5 m**.
2. De **este a oeste**. El dipolo radia más en perpendicular al hilo, y lo perpendicular a este-oeste es norte-sur.
3. **Mal.** El este es la dirección de una de las puntas, que es donde el dipolo apenas radia.
4. Porque en el centro la corriente es máxima y la tensión mínima, lo que da una impedancia baja (unos 73 Ω), fácil de conectar a los cables y equipos habituales. En una punta la impedancia sería de miles de ohmios.
5. Mayor altura significa un ángulo de salida más bajo, mejor para distancias largas; y además la antena queda más lejos de los aparatos de la casa (menos ruido al recibir) y de los vecinos (menos riesgo de interferencias).
6. **Falso.** En el espacio libre son unos **73 Ω**. En instalaciones reales cambia con la altura, pero el dato «de libro» es 73.
7. Unos **300 Ω**, cuatro veces la del dipolo sencillo. Mide **lo mismo**: media onda.

## En una frase

El dipolo de media onda son dos brazos de un cuarto de onda alimentados por el centro: mide 142,5 / f, presenta unos 73 Ω, radia en ocho —de frente y de espaldas al hilo, casi nada por las puntas— y rinde tanto más lejos cuanto más alto esté.

¿Y quien no tiene veinte metros para tender un hilo? Hay una manera de construir solo media antena y dejar que el suelo ponga la otra mitad. Es la lección siguiente.
