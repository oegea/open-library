En la sección anterior aprendiste la electricidad quieta y en fila: la corriente continua. Esta sección la pone a bailar. La corriente alterna es la gramática de todo el espectro radioeléctrico: cuando la domines, el número del dial de Vicente dejará de ser un número y pasará a ser una frase con sujeto y predicado.

## La corriente alterna: el vaivén

La **corriente continua (CC)** fluye siempre en el mismo sentido, como un río. La **corriente alterna (CA)** invierte su sentido periódicamente: los electrones avanzan, frenan, retroceden, frenan, avanzan... Un vaivén. En el enchufe de tu casa ese vaivén completo ocurre 50 veces por segundo.

¿Por qué molestarse con algo tan mareante? Dos razones que lo explican casi todo:

1. La CA se puede **transformar**: subir y bajar de tensión con un simple transformador (lo verás en la sección 4), lo que permite transportarla a grandes distancias con pocas pérdidas. Por eso ganó la «guerra de las corrientes» del siglo XIX y llega alterna a tu casa.
2. Y la razón que nos trae aquí: **una corriente alterna, si oscila lo bastante rápido, se desprende del cable y viaja por el espacio**. Eso es una onda de radio. La radio no usa la CA por comodidad: la radio *es* CA.

## Anatomía de la onda: la senoide

Si dibujas el valor de una corriente (o tensión) alterna a lo largo del tiempo, obtienes la curva más famosa de la ingeniería: la **senoide** (o sinusoide), una ondulación suave y perfectamente regular, como la estela de una serpiente ordenada. Es la forma de onda «pura», la del vaivén simple, y todas las demás formas de onda pueden construirse sumando senoides (guárdate esa frase, que reaparecerá al final).

Vocabulario de la senoide, pieza a pieza:

- **Ciclo:** una oscilación completa (subida, bajada y regreso al punto de partida).
- **Periodo (T):** el tiempo que dura un ciclo. Se mide en segundos.
- **Frecuencia (f):** cuántos ciclos caben en un segundo. Se mide en **hercios (Hz)**, en honor a Heinrich Hertz. 1 Hz = un ciclo por segundo. Frecuencia y periodo son inversos: **f = 1 / T**. Si un ciclo dura una centésima de segundo (T = 0,01 s), la frecuencia es 100 Hz.
- **Amplitud:** el «tamaño» de la oscilación. Aquí hay tres formas de medirla que el examen distingue:
  - **Valor de pico (Vp):** desde el cero hasta la cresta.
  - **Valor pico a pico (Vpp):** de la cresta al valle. Obviamente Vpp = 2 × Vp.
  - **Valor eficaz (RMS):** el más importante y el menos obvio. Es el valor de una corriente continua que calentaría lo mismo que esa alterna. Como la senoide pasa parte del tiempo cerca de cero, su efecto medio es menor que su pico: para una senoide, **valor eficaz = valor de pico / √2 ≈ 0,707 × Vp**. Los «230 V» de tu enchufe son voltios *eficaces*; el pico real ronda los 325 V. Cuando en radio se habla de tensiones y potencias sin apellido, casi siempre son eficaces.
- **Fase:** en qué punto de su ciclo está la onda en un instante dado, medida en grados (un ciclo completo = 360°). Cobra sentido al comparar dos ondas: si van perfectamente a la par están **en fase** (0° de diferencia); si una va medio ciclo por delante están **en oposición de fase** (180°): cuando una sube, la otra baja, y si se suman, se anulan. Este detalle —que dos señales idénticas puedan sumarse o *aniquilarse* según su fase— parece ahora una curiosidad; en las secciones de antenas y propagación resultará ser el mecanismo secreto de media radio.

**Ejemplo resuelto (estilo examen):** *Una tensión alterna senoidal tiene un valor de pico de 100 V. ¿Cuál es su valor eficaz?*
V eficaz = 100 × 0,707 ≈ **70,7 V**. (Y al revés: si te dan el eficaz y piden el pico, multiplica por √2 ≈ 1,414.)

## Del enchufe a la radio: el espectro

Sube ahora el ritmo del vaivén. A 50 Hz, la corriente calienta estufas. A 440 Hz aplicada a un altavoz, suena la nota la. Entre unos 20 Hz y unos 20.000 Hz (20 kHz) está la **audiofrecuencia (AF)**: las oscilaciones que, convertidas en sonido, el oído humano percibe.

Sigue subiendo. A partir de unos pocos miles de hercios, y de forma ya muy eficaz desde las decenas de miles, ocurre el fenómeno que lo cambia todo: la corriente alterna que recorre un conductor comienza a **radiar** parte de su energía en forma de **ondas electromagnéticas** que se propagan por el espacio a la **velocidad de la luz** (c ≈ 300.000 km/s). El conductor se ha convertido en una antena, y la corriente, en **radiofrecuencia (RF)**. (El *cómo* íntimo de esa radiación lo contaremos en las secciones 6 y 8; hoy nos basta el hecho.)

El conjunto ordenado de todas las frecuencias posibles se llama **espectro**, y la humanidad le ha puesto nombres por tramos. Esta tabla es de las más rentables del curso, porque **cae en el examen** y porque es el callejero de tu vida futura:

| Sigla | Nombre | Frecuencias | Longitudes de onda | Habitantes conocidos |
|---|---|---|---|---|
| VLF | Muy baja frecuencia | 3–30 kHz | 100–10 km | Comunicación con submarinos |
| LF | Baja frecuencia | 30–300 kHz | 10–1 km | Onda larga, radiofaros |
| MF | Media frecuencia | 300 kHz–3 MHz | 1000–100 m | Onda media (AM), banda de 160 m |
| **HF** | **Alta frecuencia** | **3–30 MHz** | **100–10 m** | **La onda corta: las bandas DX del radioaficionado** |
| **VHF** | **Muy alta frecuencia** | **30–300 MHz** | **10–1 m** | **FM comercial, aviación, banda de 2 m** |
| **UHF** | **Ultra alta frecuencia** | **300 MHz–3 GHz** | **1 m–10 cm** | **TDT, móviles, wifi, banda de 70 cm** |
| SHF | Súper alta frecuencia | 3–30 GHz | 10–1 cm | Satélites, radares, microondas |
| EHF | Extremadamente alta | 30–300 GHz | 1 cm–1 mm | Enlaces milimétricos, radioastronomía |

Fíjate en el patrón: cada escalón multiplica por diez, y las siglas viejas («muy alta», «ultra alta», «súper alta»...) delatan a generaciones de ingenieros quedándose sin adjetivos a medida que la técnica trepaba espectro arriba.

## La fórmula de los trescientos

La **longitud de onda (λ, lambda)** es la distancia que la onda recorre durante un ciclo completo: el «paso» de la onda. Como la onda viaja a la velocidad de la luz:

**λ = c / f**

Con λ en metros, c = 300.000.000 m/s y f en hercios. Y aquí viene el truco que usaba Vicente de cabeza: si expresas f en **megahercios**, los seis ceros se cancelan y queda la fórmula de andar por casa, la más usada de toda la radioafición:

**λ (metros) = 300 / f (MHz)**    y su gemela    **f (MHz) = 300 / λ (metros)**

**Ejemplos resueltos:**

1. *¿Qué longitud de onda corresponde a 7,1 MHz?* λ = 300 / 7,1 ≈ **42 metros** → estás en la «banda de 40 metros». (Los nombres de banda son redondeos tradicionales.)
2. *¿Y a 145 MHz?* λ = 300 / 145 ≈ **2,07 m** → banda de 2 metros.
3. *La banda de 70 cm, ¿en qué frecuencia está?* f = 300 / 0,70 ≈ **428 MHz** → efectivamente, la banda española de 70 cm va de 430 a 440 MHz.

Esta fórmula no es un peaje académico: dimensiona antenas (una antena típica mide media longitud de onda, o un cuarto), explica los nombres de todas las bandas y aparece en el examen con seguridad casi total. La regla de cartulina de Amparo —MHz arriba, metros abajo, escalas invertidas— era exactamente esto: como λ y f se multiplican para dar siempre 300, cuando una crece la otra mengua. Por eso las dos escalas van «al revés».

## Armónicos: los hijos de la onda

Una senoide pura contiene una sola frecuencia. Pero cuando una onda se deforma —porque un amplificador la recorta, porque un circuito no es perfecto—, aparecen automáticamente frecuencias nuevas en múltiplos exactos de la original: los **armónicos**. Si transmites en 7 MHz (la **frecuencia fundamental**), tu segundo armónico asoma en 14 MHz, el tercero en 21 MHz, el cuarto en 28 MHz...

Quédate con la idea doble:

- Es un fenómeno **matemático universal**: toda onda periódica no senoidal equivale a una senoide fundamental más sus armónicos (lo demostró Fourier en 1822; los músicos lo conocen como timbre: un violín y una flauta dando la misma nota se distinguen por sus armónicos).
- Y es un **problema práctico de radio**: tus armónicos caen donde no debes transmitir e interfieren a otros. Curiosidad con doble filo: las bandas clásicas de HF (3,5 – 7 – 14 – 21 – 28 MHz) están *deliberadamente* en relación armónica, herencia de los años veinte, para que los armónicos de un aficionado cayeran... sobre otros aficionados y no sobre servicios ajenos. En la sección 7 aprenderás cómo se filtran.

## El decibelio: multiplicar sumando

Última pieza de la gramática, y la que peor fama tiene sin merecerla. En radio, las potencias varían en proporciones gigantescas: entre los 1.000 W que permite la ley en HF y la señal de un picovatio que llega de la otra punta del mundo hay quince órdenes de magnitud. Manejar esos números a pelo es inhumano. La solución es el **decibelio (dB)**: una escala **logarítmica** que expresa *cuántas veces* una potencia es mayor o menor que otra.

No necesitas pelearte con logaritmos: necesitas tres valores de memoria y una regla de combinación.

| dB | La potencia se multiplica por |
|---|---|
| +3 dB | × 2 |
| +6 dB | × 4 |
| +10 dB | × 10 |
| −3 dB | ÷ 2 |
| −10 dB | ÷ 10 |
| +20 dB | × 100 |
| +30 dB | × 1000 |

La regla de combinación: **sumar decibelios equivale a multiplicar proporciones**. ¿+13 dB? Es +10 y +3: ×10 y ×2 = **×20**. ¿−6 dB? ÷4. ¿+16 dB? +10 +3 +3 = ×10×2×2 = ×40. Con esto resuelves el 95 % de los casos reales y de examen.

¿Para qué sirve en la práctica? Toda la cadena de tu estación habla en dB: el cable coaxial *pierde* 3 dB (llega la mitad de tu potencia a la antena), la antena *gana* 6 dB (concentra tu señal ×4 en una dirección), el amplificador añade 10 dB (×10)... y como todo son sumas y restas, puedes auditar la cadena completa con aritmética de servilleta: −3 + 6 + 10 = +13 dB desde el transmisor hasta el frente de la antena. Multiplicar sumando, como prometió Vicente.

Dos variantes con «apellido» que conviene reconocer:

- **dBm:** decibelios *respecto a 1 milivatio*. No comparan dos potencias cualesquiera: dan un valor absoluto. 0 dBm = 1 mW; 30 dBm = 1 W; 10 dBm = 10 mW. Es la unidad de los instrumentos de medida.
- **dBW:** lo mismo respecto a 1 vatio. 0 dBW = 1 W; 20 dBW = 100 W. Aparece en normativa internacional (y en el anexo de potencias de algún reglamento).

**Ejemplo resuelto completo:** *Tu transmisor entrega 100 W. El cable hasta la antena pierde 3 dB. ¿Qué potencia llega a la antena?* −3 dB = ÷2 → **50 W**. La mitad de tu potencia calentando gaviotas, por usar cable malo o demasiado largo: los decibelios también sirven para decidir en qué gastarse el dinero (spoiler de la sección 8: antes en cable y antena que en amplificador).

## Para llevar

- La radio **es** corriente alterna de alta frecuencia; sintonizar es elegir un ritmo de oscilación.
- Senoide: periodo T y frecuencia f = 1/T (Hz); amplitudes de pico, pico a pico y **eficaz** (= 0,707 × pico en senoides; el eficaz es el que calienta y el que se usa por defecto).
- Espectro por décadas: **HF 3-30 MHz** (onda corta, DX), **VHF 30-300 MHz**, **UHF 300 MHz-3 GHz**. Memoriza la tabla completa.
- **λ = 300 / f(MHz)**: la fórmula de andar por casa que dimensiona antenas y da nombre a las bandas.
- Armónicos: múltiplos enteros de la fundamental; inevitables al deformarse una onda, hay que filtrarlos.
- Decibelios: 3 dB = doble, 10 dB = ×10, sumar dB = multiplicar proporciones; dBm = respecto a 1 mW.

## Para el examen

- «300 entre los megahercios» cae prácticamente siempre, en un sentido u otro. Hazla hasta en sueños.
- Conversión pico ↔ eficaz (×0,707 o ×1,414): pregunta clásica de la primera prueba.
- Nombres y límites de las bandas del espectro (HF/VHF/UHF sobre todo).
- f = 1/T con conversiones de unidades (milisegundos, microsegundos).
- Decibelios de la tabla (3, 6, 10, 20 dB) aplicados a potencias, y qué es un dBm.

## Para profundizar

- OpenStax, *Física universitaria* vol. 1 (ondas) y vol. 2 (corriente alterna) — CC BY 4.0, en español, con toda la matemática que aquí hemos dejado en la trastienda.
- Entra en un receptor SDR público (por ejemplo, los enlazados en websdr.org) y mira el espectro *dibujado en vivo*: verás las señales como picos sobre un paisaje de ruido, con sus frecuencias debajo. Quince minutos allí convierten esta sección entera en algo evidente. En la sección 6 lo usaremos a fondo.
