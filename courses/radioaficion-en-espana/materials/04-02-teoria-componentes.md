Todo aparato de radio, del walkie más barato al transceptor de la mesa de Vicente, está hecho combinando un puñado de tipos de componentes. Esta sección te los presenta uno a uno: qué hacen, cómo se leen, en qué unidades se miden y qué papel jugarán después. Es la sección más «de catálogo» del curso; a cambio, cada pieza que fiches aquí te la encontrarás trabajando en las secciones siguientes.

## Resistencias: las que frenan

La **resistencia** (el componente; también llamada *resistor*) es un cilindro o pastilla fabricado para oponer una resistencia concreta al paso de la corriente. Sus dos datos vitales:

- **Valor** en ohmios (Ω), de fracciones de ohmio a millones (MΩ).
- **Potencia máxima** que puede disipar sin quemarse (recuerda P = I²R): las comunes de electrónica son de 0,25 W o 0,5 W; las «de potencia», cerámicas y gordas, aguantan decenas de vatios.

Sus usos: limitar corrientes (proteger un LED), repartir tensiones (el divisor que verás en la sección 5), cargar circuitos para pruebas... Es el componente más numeroso de cualquier placa.

**El código de colores** identifica el valor mediante franjas pintadas. En el formato clásico de 4 franjas: las dos primeras son cifras, la tercera es el multiplicador (cuántos ceros añadir) y la cuarta, la tolerancia (precisión del valor: dorado ±5 %, plateado ±10 %).

| Color | Cifra | Multiplicador |
|---|---|---|
| Negro | 0 | ×1 |
| Marrón | 1 | ×10 |
| Rojo | 2 | ×100 |
| Naranja | 3 | ×1.000 |
| Amarillo | 4 | ×10.000 |
| Verde | 5 | ×100.000 |
| Azul | 6 | ×1.000.000 |
| Violeta | 7 | — |
| Gris | 8 | — |
| Blanco | 9 | — |

Ejemplos: **marrón-negro-rojo** = 1, 0, ×100 = 1.000 Ω = 1 kΩ (la que levantó Vicente en el rastro). **Amarillo-violeta-naranja** = 4, 7, ×1.000 = 47 kΩ. **Rojo-rojo-negro** = 22 Ω. Regla nemotécnica veterana para el orden de los colores: son los del arcoíris con negro y marrón delante y gris y blanco detrás.

Variantes con nombre propio: el **potenciómetro** es una resistencia variable con un eje (el mando de volumen clásico); la **LDR** baja su resistencia con la luz; el **termistor** la cambia con la temperatura (así mide tu equipo su propia calentura).

## Condensadores: los que almacenan campo eléctrico

Un **condensador** son dos placas conductoras enfrentadas y separadas por un aislante (el **dieléctrico**: aire, cerámica, plástico...). Al conectarlo a una tensión, las placas se cargan (una +, otra −) y entre ellas queda almacenada energía en forma de **campo eléctrico**. Es un almacén diminuto y rapidísimo de electricidad.

- **Magnitud: capacidad (C)**, medida en **faradios (F)**. El faradio es descomunal, así que vivirás entre **microfaradios (µF), nanofaradios (nF) y picofaradios (pF)**. (1 µF = 1.000 nF = 1.000.000 pF: conversión que cae en exámenes.)
- La capacidad crece con la superficie de las placas, y crece al acercarlas o al usar mejor dieléctrico.

El comportamiento que lo hace precioso para la radio:

- **En corriente continua, no conduce.** Se carga en un instante y luego bloquea el paso: es un muro para la CC.
- **En corriente alterna, «deja pasar»**: como la tensión no para de invertirse, el condensador se carga y descarga sin cesar, y la corriente circula por el circuito (aunque ningún electrón cruce el dieléctrico). Cuanto **mayor la frecuencia o mayor la capacidad, más fácil pasa**. Esa oposición variable con la frecuencia se llama **reactancia capacitiva** (Xc, en ohmios): baja cuando la frecuencia sube.

Ese doble carácter —muro para la CC, puerta para la CA que se abre con la frecuencia— convierte al condensador en el portero de los circuitos: separa la señal de la alimentación, desvía a tierra las frecuencias indeseadas, y forma filtros y circuitos resonantes (sección 5).

Tipos que conviene reconocer: **cerámicos** (pequeños, pF a nF, para RF), **de plástico/film** (estables, audio y filtros), **electrolíticos** (los cilindros con polaridad: µF grandes para alisar alimentaciones; OJO: tienen + y −, y conectarlos al revés los hace literalmente explotar; son además los que peor envejecen: se secan, y por eso la lata de Amparo avisaba «¡MIRAR FECHA!» y el receptor del rastro «olía a condensador reventado»), y **variables** (el clásico mando de sintonía de las radios antiguas: placas que se enfrentan más o menos al girar).

## Bobinas: las que almacenan campo magnético

Una **bobina** (o **inductor**, o *choque*) es un hilo enrollado, a veces alrededor de un núcleo de hierro o **ferrita** (cerámica magnética). Su secreto es que **toda corriente crea un campo magnético** (lo descubrió Ørsted en 1820 al ver moverse una brújula junto a un cable), y un campo magnético que cambia induce a su vez tensión en los conductores que abraza (Faraday, 1831). La bobina almacena energía en su **campo magnético** y, por esa inercia magnética, *se resiste a los cambios de corriente*.

- **Magnitud: inductancia (L)**, medida en **henrios (H)**; en la práctica, milihenrios (mH) y microhenrios (µH).
- Comportamiento espejo del condensador: **deja pasar la CC** (es solo un hilo enrollado) y **se opone a la CA**, tanto más cuanto mayor la frecuencia. Su oposición es la **reactancia inductiva** (XL, en ohmios): sube cuando la frecuencia sube.

Memoriza el dúo como pareja de opuestos, porque el examen lo pregunta y toda la radio se apoya en él:

| | Corriente continua | CA de baja frecuencia | CA de alta frecuencia |
|---|---|---|---|
| **Condensador** | Bloquea | Pasa a regañadientes | Pasa fácil |
| **Bobina** | Pasa | Pasa a regañadientes* | Bloquea |

(*con oposición creciente con la frecuencia)

Juntos forman el matrimonio más productivo de la electrónica: el circuito resonante LC, corazón de la sintonía, que es el plato fuerte de la sección 5.

## Transformadores: las bobinas casadas

Pon dos bobinas juntas, compartiendo núcleo, y tendrás un **transformador**: la corriente alterna del **primario** crea un campo magnético cambiante que induce tensión en el **secundario**, sin contacto eléctrico alguno. Dos consecuencias:

1. **Cambia tensiones:** la relación de tensiones es igual a la relación de espiras (vueltas de hilo). Un primario de 1.000 espiras a 230 V con un secundario de 50 espiras entrega 230 × 50/1.000 = **11,5 V**. (La potencia no se multiplica, ni gratis ni nunca: si la tensión baja 20 veces, la corriente disponible sube hasta 20 veces, menos las pérdidas.)
2. **Aísla:** como no hay conexión física entre primario y secundario, separa circuitos galvánicamente (seguridad) y adapta impedancias (concepto que florecerá en la sección 8: los baluns de antena son transformadores).

Solo funciona con **corriente alterna**: con CC el campo no cambia y no induce nada (un transformador conectado a una batería es un calentador caro). Esta es la razón profunda de que la red eléctrica sea alterna, como viste en la ampliación anterior.

## Diodos: las válvulas antirretorno

Con el **diodo** entramos en los **semiconductores**. Recuerda de la sección 2: silicio, conducción «a medias» y controlable. El control se consigue **dopando** el cristal: añadiendo impurezas que le sobran electrones (material **tipo N**) o que le faltan (material **tipo P**; a los huecos que dejan los electrones ausentes se les trata como cargas positivas móviles, los famosos «huecos»).

Al unir un trozo P con un trozo N se forma la **unión PN**, y ocurre el milagro asimétrico: **la corriente solo puede cruzarla en un sentido**. Polarizado en **directa** (P al +, N al −), el diodo conduce en cuanto se supera una pequeña tensión umbral (~0,7 V en silicio, ~0,3 V en germanio); en **inversa**, bloquea. Es una válvula antirretorno para electrones.

Usos y parientes que debes conocer:

- **Rectificar:** convertir CA en CC dejando pasar solo los semiciclos de un sentido: el primer paso de toda fuente de alimentación (sección 5).
- **Detectar:** extraer el sonido de una señal de radio AM (así funcionaban las radios de galena: la galena era un diodo mineral; los «diodos Ge, tesoro» de la lata de Amparo son sus nietos de germanio, apreciados justo por su umbral bajo).
- **LED:** diodo que emite luz al conducir. Como todo diodo, no se autolimita: se conecta siempre con una resistencia en serie que fije su corriente (ley de Ohm en acto de servicio).
- **Zéner:** diodo diseñado para conducir en inversa a una tensión exacta y estable: se usa como referencia y regulador de tensión.
- **Varicap:** diodo que, en inversa, se comporta como un pequeño condensador cuya capacidad depende de la tensión aplicada: es el «mando de sintonía electrónico» de los equipos modernos.

## Transistores: los que amplifican

El componente que cambió el mundo (Bell Labs, 1947; Nobel para Bardeen, Brattain y Shockley). Un **transistor** es un semiconductor de tres capas y tres patas en el que **una corriente o tensión pequeña en una pata controla una corriente grande entre las otras dos**. Es un grifo electrónico: la manecilla apenas requiere esfuerzo, y gobierna un caudal enorme.

Dos grandes familias:

- **Bipolar (BJT):** capas NPN o PNP; patas **emisor, base y colector**. Una corriente pequeña de base controla una corriente de colector decenas o cientos de veces mayor (esa proporción es la **ganancia de corriente**, llamada beta o hFE). Controlado por *corriente*.
- **De efecto de campo (FET, y su variante MOSFET):** patas **fuente, puerta y drenador**. La *tensión* en la puerta controla la corriente fuente-drenador, casi sin consumir nada. Controlado por *tensión*. Los amplificadores de potencia de RF modernos y prácticamente toda la informática son MOSFET.

Del grifo salen los dos empleos universales:

1. **Amplificador:** la señal débil mueve la manecilla, y el caudal grande reproduce sus movimientos ampliados. De la antena al altavoz, tu receptor es una cadena de grifos cada vez mayores.
2. **Conmutador:** manecilla solo abierta o cerrada: un interruptor sin partes móviles, capaz de abrir y cerrar millones de veces por segundo. Sobre ese uso está construida toda la electrónica digital.

**La media familia: las válvulas.** Antes del transistor, amplificaban las **válvulas termoiónicas** (tubos de vacío): un filamento incandescente libera electrones que vuelan hasta una placa, y una rejilla intermedia los gobierna. Mismo principio de grifo, con botella de cristal, cientos de voltios y calor de estufa. Sobreviven dignamente en dos reductos: amplificadores de gran potencia de HF y equipos de audio de culto. El examen todavía les guarda una pregunta ocasional; tu curso, este párrafo y el cariño.

## Circuitos integrados: la ciudad en un grano

Un **circuito integrado (CI, chip)** no es un componente nuevo: son miles, millones o miles de millones de transistores, diodos, resistencias y condensadores fabricados de una vez sobre una lasca de silicio. Desde el amplificadorcito de ocho patas hasta el procesador de tu móvil. En radio los encontrarás haciendo de amplificadores, mezcladores, sintetizadores de frecuencia o radios completas en un chip (los walkies baratos son básicamente *un* chip con micrófono). Para el examen basta el concepto; para el asombro, el dato: el primer CI (Kilby, 1958) tenía un transistor; los actuales superan los cien mil millones.

## Cómo se muere cada familia (el regalo de Vicente)

No cae en el examen, pero vale una reparación: cada componente tiene su muerte típica. Las **resistencias** se abren (se queman y dejan de conducir; a menudo se ve el tostado). Los **electrolíticos** se secan con los años y pierden capacidad, o se hinchan por arriba y hasta revientan: son el sospechoso número uno en aparatos viejos, como el receptor del rastro. Los **semiconductores** mueren de golpe y en silencio, casi siempre por calor o sobretensión: un diodo o transistor muerto suele estar en cortocircuito (conduce en ambos sentidos: se delata con el polímetro). Las **bobinas y transformadores** casi nunca mueren... salvo que algo los haya cocinado antes. Orden de sospecha en un aparato antiguo: electrolíticos, semiconductores calientes, soldaduras agrietadas, y solo al final lo demás.

## Para llevar

- **Resistencia** (Ω): frena corriente; valor por código de colores (cifra-cifra-multiplicador-tolerancia); vigila su potencia máxima.
- **Condensador** (F → µF/nF/pF): almacena campo *eléctrico*; bloquea CC, pasa CA tanto mejor cuanto mayor la frecuencia (reactancia capacitiva ↓ con f).
- **Bobina** (H → mH/µH): almacena campo *magnético*; pasa CC, frena CA tanto más cuanto mayor la frecuencia (reactancia inductiva ↑ con f).
- **Transformador:** dos bobinas acopladas; cambia tensión según relación de espiras; solo CA; aísla y adapta.
- **Diodo:** conduce en un solo sentido (umbral ~0,7 V silicio); rectifica y detecta; variantes zéner (tensión estable), LED (luz), varicap (capacidad variable).
- **Transistor:** señal pequeña controla corriente grande; bipolar (emisor/base/colector, controlado por corriente) y FET (fuente/puerta/drenador, controlado por tensión); amplifica o conmuta.
- **CI:** miles/millones de todo lo anterior en un chip.

## Para el examen

- Código de colores: cae con enorme frecuencia. Practica una docena de combinaciones en ambos sentidos.
- El dúo reactancias: condensador y bobina frente a CC/CA y frente a la frecuencia. Pregunta segura, a menudo formulada como «¿qué componente bloquea la CC y deja pasar la CA?».
- Unidades: faradio (y sus submúltiplos µF/nF/pF con conversiones), henrio, y a quién pertenece cada una.
- Nombres de las patas: emisor/base/colector (bipolar), fuente/puerta/drenador (FET), primario/secundario (transformador).
- Relación de espiras del transformador con un cálculo sencillo.
- Umbral del diodo de silicio (~0,6-0,7 V) y funciones del zéner y el varicap.

## Para profundizar

- OpenStax, *Física universitaria* vol. 2 (CC BY 4.0): capacidad, inductancia e inducción electromagnética, con los experimentos de Faraday contados como merecen.
- Cualquier «kit de iniciación a la electrónica» (protoboard, resistencias, LEDs, pila) por menos de 20 €: montar un LED con su resistencia calculada por ti convierte esta sección de catálogo en memoria muscular.
- El simulador gratuito falstad.com/circuit: dibujas circuitos y *ves* las corrientes animadas moverse por ellos, condensadores cargándose incluidos. Juega con un condensador y una bobina; la sección 5 te espera.
