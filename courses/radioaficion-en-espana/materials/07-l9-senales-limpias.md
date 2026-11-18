Un receptor mediocre es un problema privado: quien oye mal es su dueño. Un transmisor que funciona mal es un problema público: lo sufren todos los que comparten la banda, y a veces el televisor del vecino. Por eso el examen insiste mucho más en los defectos del transmisor que en los del receptor, y por eso Vicente, el pesado de la exactitud, le dedicó a Marina una tarde entera.

Al terminar esta lección sabrás reconocer las formas en que un transmisor ensucia las frecuencias de los demás, con el nombre que les da el reglamento, qué las causa, cómo se evita cada una y qué indicador del equipo te avisa antes de que ocurra. La lección siguiente, más corta, cierra la sección con los defectos que estropean tu propia señal y con la manera de comprobarla.

## La regla: emitir solo lo que toca

Una emisión limpia ocupa **una sola franja del espectro**: la de tu señal, con el ancho que corresponde a su modo (unos 2,7 kHz en SSB, por ejemplo), y nada más. Todo lo que tu transmisor emita fuera de esa franja es energía desperdiciada para ti y una interferencia para otros.

A todo eso que no debería salir se le llama **emisiones no deseadas**, y el Reglamento de Radiocomunicaciones internacional las divide en dos familias, según dónde aparezcan:

| Familia | Dónde aparecen | Qué incluye |
|---|---|---|
| **Emisiones fuera de banda** | **Pegadas** a tu señal, a los dos lados | Lo que la modulación desparrama cuando se hace mal: el splatter, la sobredesviación, los chasquidos de manipulación |
| **Emisiones no esenciales**, o **espurias** | **Lejos** de tu señal | Los armónicos, las oscilaciones parásitas y los productos de mezcla que se escapan |

Ojo con el nombre de la primera: «fuera de banda» no significa fuera de la banda de radioaficionados, sino fuera del ancho de banda que tu señal necesita.

Vamos por orden: primero las espurias, que dependen sobre todo del equipo, y después las emisiones fuera de banda, que dependen sobre todo de quien lo maneja.

## Espurias (1): los armónicos

Los conoces desde la sección 3 y has vuelto a verlos al hablar del filtro paso bajo: copias de tu señal en el doble, el triple, el cuádruple de tu frecuencia. Nacen en los amplificadores, porque ninguno es perfectamente fiel, y nacen muchos más cuando un amplificador trabaja forzado. Son la clase de espuria más conocida.

- **Remedio:** el **filtro paso bajo** a la salida, y no forzar la etapa final.
- **Síntoma típico:** emites en 7 MHz y alguien te oye en 14 o en 21.

## Espurias (2): las que no son armónicos

Hay emisiones espurias que no caen en múltiplos de tu frecuencia. Salen de dos sitios, sobre todo:

- **De los mezcladores.** En la lección anterior viste que un transmisor de SSB lleva su señal a la frecuencia de emisión mezclando, y que de un mezclador salen la suma, la diferencia y restos de las señales originales. El filtro paso banda que va detrás se queda con lo que interesa, pero si está mal ajustado o es pobre, algo de lo demás llega a la antena. Son los **productos de mezcla**.
- **De oscilaciones parásitas.** Un oscilador, como viste en la sección 5, es un amplificador cuya salida vuelve a su entrada. Si en un amplificador de potencia mal diseñado, o mal blindado, parte de la salida se cuela de vuelta a la entrada, se pone a oscilar por su cuenta en una frecuencia que nadie ha elegido.

Estas espurias delatan un diseño pobre, un ajuste incorrecto o una avería. El filtro paso bajo no las quita si caen por debajo de tu frecuencia. Y si la caja del equipo no cierra bien o le falta algún blindaje, pueden salir directamente por ella y por los cables, sin pasar siquiera por la antena.

## Fuera de banda (1): sobremodulación y splatter

Este es el defecto más frecuente, porque no lo causa el equipo: lo causa el operador con ganas de que le oigan.

Todo amplificador tiene un tope. Recuerda la saturación de la sección 5: si se le pide más de lo que puede dar, deja de entregar una copia fiel y deforma la señal. En un transmisor de SSB se llega ahí subiendo demasiado la **ganancia del micrófono** (el mando que decide cuánta señal de voz entra en el transmisor), gritando, o pidiéndole al equipo más potencia de la que da limpiamente.

¿Y qué hace un circuito cuando deforma? Lo viste en la lección sobre cómo leer un receptor: se convierte en un mezclador que nadie ha pedido. Allí mezclaba entre sí dos estaciones fuertes. Aquí mezcla entre sí **los tonos de tu propia voz**, que no es un tono solo, sino muchos a la vez.

Haz la misma cuenta. Toma dos de esos tonos, que dentro de tu señal de radio están en A = 7.101 kHz y B = 7.102 kHz:

- 2 × A − B = 14.202 − 7.102 = **7.100 kHz**
- 2 × B − A = 14.204 − 7.101 = **7.103 kHz**

Han aparecido dos frecuencias nuevas, pegadas a las originales, una a cada lado. Cada pareja de tonos de tu voz añade vecinos así, y los vecinos se combinan a su vez con los demás. El resultado es que tu emisión, que debía ocupar 2,7 kHz, se desparrama y ocupa ocho o diez kilohercios. A esta mezcla involuntaria dentro del transmisor se le llama **intermodulación del transmisor**, y a su efecto en el aire:

> **Splatter** (salpicadura): ensanchamiento de una señal por sobremodulación o por saturación del amplificador, que invade las frecuencias vecinas.

Y aquí se ve la diferencia con los armónicos, aunque la causa sea la misma deformación: los armónicos caen lejísimos y el filtro paso bajo los elimina; estos productos caen **pegados a tu señal**, donde ningún filtro de salida puede tocarlos sin tocarte a ti.

![Dos espectros con la frecuencia en horizontal. Arriba, una señal de SSB limpia: un bloque de 2,7 kilohercios de ancho con los lados casi verticales, y a cada lado una estación vecina sin molestar. Abajo, la misma señal sobremodulada: el bloque central tiene a los dos lados unas faldas anchas que se extienden varios kilohercios y cubren a las dos estaciones vecinas.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-splatter.svg)

—Pero algo ganará el que lo hace —dijo Marina—. Si no, no lo haría nadie.

—Gana un poco de potencia media: al aplastar los picos, la voz va más «llena». Por eso existen los procesadores de voz, que hacen eso mismo con cuidado y dentro de un límite —dijo Vicente—. Pasado ese límite, lo que ganas en vatios lo pierdes en claridad: la voz sale áspera y se entiende peor. Y encima tapas a los vecinos de arriba y de abajo, que no pueden defenderse: el filtro de su receptor no les sirve, porque lo que tú emites de más cae dentro de su ventana. Es como hablar a gritos en un bar. No se te entiende mejor; se entiende peor a todos los demás.

En **AM**, el equivalente es pasar del 100 % de modulación: la envolvente llega a cero y se corta, y el efecto es el mismo.

### El ALC, tu chivato

Los transceptores llevan un circuito para frenar el exceso.

> **ALC** (*Automatic Level Control*, control automático de nivel): circuito del transmisor que vigila la señal que llega a la etapa final y reduce la amplificación cuando es excesiva, para evitar que esa etapa se sature.

El ALC es un freno de emergencia, no un permiso. Los equipos tienen un indicador de ALC con una zona marcada. La norma de buen operador es ajustar la ganancia de micrófono de modo que, hablando con voz normal, **el indicador se mueva solo en los picos de voz y sin salirse de esa zona**. Si la aguja está en movimiento todo el rato o se clava arriba, estás empujando demasiado. Con los modos digitales, que usan la tarjeta de sonido del ordenador como micrófono, la costumbre es todavía más estricta: el nivel de audio se baja hasta que el ALC no actúe o apenas lo haga.

## Fuera de banda (2): sobredesviación

En FM el exceso de audio no recorta nada, pero aumenta la desviación, y con ella el ancho de la señal: te sales de tu canal e invades el de al lado.

Al estudiar el transmisor de FM viste que hay un bloque, el limitador de desviación, puesto justo para impedirlo. Hay **sobredesviación** cuando ese limitador está mal ajustado o falta, y también en un caso muy corriente que no es una avería: usar la FM ancha (desviación de ±5 kHz, canales de 25 kHz) en un canal o en un repetidor pensado para la estrecha (±2,5 kHz, canales de 12,5 kHz). El remedio es elegir en el equipo el ancho de FM que corresponde.

## Fuera de banda (3): chasquidos de manipulación

En CW, si la portadora se enciende y se apaga de golpe, cada punto y cada raya produce un chasquido que se oye varios kilohercios a los lados: los **chasquidos de manipulación** (*key clicks*). Un cambio brusco es, también, una forma de deformar la onda. Se evitan haciendo que la señal suba y baje con una rampa suave, de unas milésimas de segundo.

## Donde la gente se lía

- **«Con más micrófono me oyen mejor.»** Te oyen distorsionado y tapas a los vecinos. La ganancia de micro se ajusta mirando el ALC.
- **«El ALC ya lo arregla todo; puedo subir lo que quiera.»** El ALC es un freno de emergencia. Si actúa a fondo todo el rato, la señal ya sale sucia.
- **«Los armónicos no son espurias.»** Lo son: son la clase de espuria más conocida. Lo que los distingue de las demás es que caen en múltiplos exactos de tu frecuencia.
- **«Fuera de banda quiere decir fuera de la banda de radioaficionados.»** Quiere decir fuera del ancho que tu señal debería ocupar, aunque siga dentro de la banda.
- **«El filtro paso bajo me protege de todo.»** Quita los armónicos. No puede con el splatter, que está pegado a tu señal, ni con las espurias que caen por debajo de tu frecuencia.

## Compruébalo tú

1. Un transmisor emite en 3.650 kHz. Un vecino de banda oye una señal suya en 7.300 kHz y otra en 5.210 kHz. Las dos son espurias: ¿cuál de ellas es un armónico y cuál no?
2. Un corresponsal te dice: «Tu audio suena áspero y ocupas ocho kilohercios». ¿Qué está pasando y qué mando tocas primero?
3. ¿Por qué el filtro del receptor de tu vecino de banda no puede librarle de tu splatter? ¿Y por qué no lo elimina tu filtro paso bajo?
4. Un portátil configurado en FM ancha (±5 kHz) se usa en un repetidor de canales estrechos, y le dicen que se le oye también en el canal contiguo. ¿Cómo se llama ese defecto y cómo se corrige?
5. Te dicen que tu morse se oye limpio en tu frecuencia, pero que a 2 kHz de ti se oye un «clac» con cada signo. ¿Qué defecto es, a cuál de las dos familias pertenece y cómo se corrige?
6. Dentro de una señal de SSB hay dos tonos en 14.201 y 14.203 kHz. Si la etapa final se satura, ¿en qué dos frecuencias aparecen los productos más cercanos?

**Soluciones**

1. 7.300 kHz es justo el doble de 3.650: es el **segundo armónico**. 5.210 kHz no es múltiplo de 3.650: es una espuria de otra clase, probablemente un producto de mezcla o una oscilación parásita.
2. Estás **sobremodulando** y produciendo splatter. Lo primero, **bajar la ganancia de micrófono** hasta que el ALC solo se mueva en los picos y dentro de su zona.
3. Porque el splatter cae **dentro** de la franja que su filtro deja pasar: son frecuencias que tu transmisor está emitiendo de verdad encima de su canal. Y tu filtro paso bajo tampoco puede: el splatter está a pocos kilohercios de tu señal, muy por debajo de donde ese filtro empieza a cortar.
4. **Sobredesviación**: la señal ocupa más ancho del que cabe en el canal. Se corrige seleccionando en el equipo la FM estrecha.
5. **Chasquidos de manipulación**: la portadora se enciende y se apaga con demasiada brusquedad. Es una emisión **fuera de banda**, porque aparece pegada a tu señal. Se corrige suavizando la subida y la bajada de cada signo.
6. 2 × 14.201 − 14.203 = 28.402 − 14.203 = **14.199 kHz**, y 2 × 14.203 − 14.201 = 28.406 − 14.201 = **14.205 kHz**: a 2 kHz a cada lado de la pareja, que es lo que la separa.

## En una frase

Lo que un transmisor emite de más se divide en espurias, lejos de tu señal (armónicos, oscilaciones parásitas, productos de mezcla), y emisiones fuera de banda, pegadas a ella (splatter, sobredesviación, chasquidos); las primeras se evitan con filtros, buen diseño y buen ajuste, y las segundas no forzando el micrófono ni la etapa final, con el ALC como chivato.

Quedan los defectos que no molestan al vecino, sino a quien intenta escucharte, y la manera de saber cómo sales al aire.
