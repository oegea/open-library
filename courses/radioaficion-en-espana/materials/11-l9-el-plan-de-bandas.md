Para el simulacro, Salva repartió el trabajo en una frase: «Estación fija en VHF con el repetidor comarcal, HF en 40». No dijo en qué frecuencia exacta de 40 metros. Dani lo sabía sin preguntarlo, igual que Vicente, en la lección 1, sabía en qué parte de la banda ponerse a hablar.

Lo sabían porque existe un plano. Al terminar esta lección sabrás qué es el plan de bandas, quién lo hace y qué fuerza tiene, cómo se lee, y podrás decidir, ante una frecuencia concreta, si tu modo cabe ahí o no.

## Dos repartos, uno dentro de otro

**El primero dice qué bandas son de los radioaficionados.** De 7.000 a 7.200 kHz, sí; de 7.200 en adelante, en Europa, no: ahí hay emisoras de radiodifusión. Este reparto lo hacen los Estados, reunidos en la Unión Internacional de Telecomunicaciones, y cada país lo convierte en ley. Sus límites son los **bordes de banda**, y salirse de ellos es una infracción. Lo verás en la sección 12.

**El segundo dice qué se hace dentro de cada banda.** Ese es el tema de hoy.

> **Plan de bandas:** acuerdo que reparte cada banda de aficionado en tramos (también llamados *segmentos* o *subbandas*) e indica qué modos de emisión son los adecuados en cada uno.

El plan no lo redacta ningún gobierno. Lo acuerdan los propios radioaficionados a través de su organización mundial, la **IARU** (Unión Internacional de Radioaficionados), que agrupa a las asociaciones nacionales: la URE, en el caso de España. La IARU divide el mundo en tres regiones; la nuestra es la **Región 1**: Europa, África, Oriente Medio y el norte de Asia.

—Si lo hacen los aficionados, será una recomendación —dijo Marina—. ¿Obliga o no obliga?

—En España, más de lo que parece. El reglamento de radioaficionados dispone que, para facilitar las transmisiones y evitar interferencias entre tipos de modulación distintos, se utilizarán «como norma general» los planes de banda de la IARU para la Región 1. Y cae en el examen: el programa oficial pide conocerlos y saber qué objetivos persiguen.

## Por qué hace falta: los modos no caben igual

Recuerda de la sección 6 lo que ocupa cada modo en el dial:

- Una señal de telegrafía: unos 150 Hz.
- Un modo digital de texto: unas decenas o centenas de hercios.
- Una voz en SSB: unos 2.700 Hz.
- Una voz en FM de canal estrecho: unos 11 kHz.

Una sola conversación de voz en SSB ocupa el sitio de quince o veinte contactos de telegrafía. Si alguien se pone a hablar en medio de la zona de telegrafía, no molesta a una estación: aplasta a veinte. Y, al revés, el telegrafista perdido en la zona de voz se oye como un pitido insistente encima de una conversación.

El plan de bandas resuelve esto con una idea simple: **juntar lo que se parece**. Las señales estrechas, con las estrechas; las anchas, con las anchas. Ese es el primero de sus objetivos. Los otros, que verás aparecer en los ejemplos, son reservar sitio para lo que necesita silencio (las balizas, las señales muy débiles, los satélites) y fijar puntos de encuentro (las frecuencias de llamada y los centros de actividad).

Para eso, el plan da a cada tramo un **ancho de banda máximo**: 200 Hz en los tramos de telegrafía, 500 Hz en los de modos estrechos, 2.700 Hz donde cabe la voz en SSB.

## Cómo se ordena una banda de onda corta

Casi todas las bandas de HF siguen el mismo esquema, de abajo arriba:

> **Telegrafía abajo, modos digitales estrechos en medio, voz arriba.**

La banda de 40 metros, según el plan vigente de la Región 1, queda así:

| Tramo (kHz) | Ancho máximo | Para qué |
|---|---|---|
| 7.000 – 7.040 | 200 Hz | Telegrafía (CW) |
| 7.040 – 7.050 | 500 Hz | Modos estrechos: digitales de texto |
| 7.050 – 7.060 | 2.700 Hz | Todos los modos; preferencia para digitales |
| 7.060 – 7.200 | 2.700 Hz | Todos los modos: aquí es donde se habla en SSB |

Y dentro de esos tramos, unos puntos señalados:

- **7.030 kHz:** centro de actividad de las estaciones de baja potencia (QRP) en telegrafía. **7.090 kHz**, el de las QRP en voz.
- **7.110 kHz:** centro de actividad de **emergencias** de la Región 1.

![La banda de 40 metros dibujada como una regla de 7.000 a 7.200 kilohercios. De 7.000 a 7.040, telegrafía. De 7.040 a 7.050, modos digitales estrechos. De 7.050 a 7.060, todos los modos con preferencia para los digitales. De 7.060 a 7.200, todos los modos: la zona de voz en banda lateral. Marcados sobre la regla, tres puntos: 7.030, centro de baja potencia en telegrafía; 7.090, centro de baja potencia en voz; y 7.110, centro de actividad de emergencias.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s11-plan-40m.svg)

Dos expresiones del plan que se malinterpretan:

- **«Todos los modos»** quiere decir que ahí cabe también la voz, no que la voz tenga exclusiva. La telegrafía está admitida en toda la banda, salvo en los tramos de balizas.
- **«Centro de actividad»** no es una frecuencia reservada. Es un punto de encuentro: donde buscar a quienes practican algo concreto. Nadie es dueño de 7.090 kHz por ser QRP. La excepción moral es la de emergencias: en cuanto hay una emergencia real en marcha, 7.110 kHz y sus alrededores se dejan libres.

## La regla del dial: tu señal no está donde marca

Esta es la idea difícil de la lección. En SSB, el número que marca tu equipo no es el centro de tu señal: es la frecuencia de la portadora suprimida, y la voz ocupa unos 3 kHz **a un lado** de ella. Lo viste en la sección 6:

> **En LSB, tu voz cuelga del dial: ocupa los 3 kHz de debajo. En USB, se apoya en él: ocupa los 3 kHz de encima.**

El plan de bandas habla de las frecuencias que de verdad ocupas, no de la que marca el dial. De ahí salen dos reglas con números.

**En 40 metros, en LSB, el dial no debe bajar de 7.053 kHz.** Con el dial en 7.053, tu voz ocupa de 7.050 a 7.053: justo por encima del tramo de modos estrechos. Con el dial en 7.051, estarías metiendo una señal de 3 kHz de ancho en un tramo de 500 Hz. El propio plan da esa cifra, y la equivalente de 80 metros: 3.603 kHz.

**En 20 metros, en USB, el dial no debe pasar de 14.347 kHz.** El plan pide dejar 3 kHz hasta el borde superior, y la banda termina en 14.350. Con el dial en 14.347, ocupas de 14.347 a 14.350. Con el dial en 14.349, tu voz llega hasta 14.352: dos kilohercios **fuera de la banda**. Y eso ya no es una falta contra el plan: es transmitir donde no tienes autorización.

—Entonces, cerca de los bordes, primero pienso hacia qué lado cae mi voz.

—Exacto. Cerca de un borde inferior en LSB, o de uno superior en USB, tres kilohercios de margen.

## Los tramos protegidos

En la sección 9 conociste las **balizas**: emisoras automáticas que transmiten su indicativo sin parar, en frecuencias fijas, para que cualquiera pueda comprobar si una banda está abierta. Son señales débiles a propósito, y solo sirven si su frecuencia está en silencio.

El plan les reserva tramos **exclusivos**: por ejemplo, de 14.099 a 14.101 kHz en 20 metros, y uno equivalente en cada banda alta. Ahí no se llama, no se prueba y no se ajusta. Una sola transmisión deja sin referencia a todos los que estaban escuchando.

Los tramos de **satélites**, que verás enseguida en VHF, son otra cosa: no son de silencio, sino *exclusivos*. Quien trabaja un satélite de aficionados transmite y recibe ahí; lo que no se hace en ellos son contactos terrestres, porque lo que baja del satélite llega debilísimo y cualquier emisión local lo tapa.

## El plan de la banda de 2 metros

En VHF el esquema cambia, porque aquí conviven tres mundos: quienes buscan contactos lejanos con señales débiles (en telegrafía y SSB), los repetidores, y la FM local.

| Tramo (MHz) | Para qué |
|---|---|
| 144,000 – 144,025 | Satélites (solo bajada) |
| 144,025 – 144,150 | Telegrafía y modos digitales de señal débil |
| 144,150 – 144,400 | Telegrafía y SSB. Centro de actividad de SSB: **144,300** |
| 144,400 – 144,490 | **Balizas, exclusivo** |
| 144,500 – 144,794 | Todos los modos |
| 144,794 – 144,9625 | Comunicaciones digitales. **144,800: APRS** |
| 144,975 – 145,194 | **Entradas de repetidores** |
| 145,206 – 145,5625 | FM y voz digital en símplex. **145,500: llamada de FM** |
| 145,575 – 145,794 | **Salidas de repetidores** |
| 145,806 – 146,000 | **Satélites, exclusivo** |

Ahora encaja lo de la lección anterior. Las entradas de repetidor están en 145,0 y pico; las salidas, en 145,6 y pico: exactamente 600 kHz más arriba. Entre unas y otras quedan los canales de símplex, con la frecuencia de llamada en 145,500 MHz. Y el APRS que conociste en la sección 6, el sistema que dibuja posiciones en un mapa, tiene su frecuencia propia para toda Europa.

![La banda de 2 metros dibujada como una regla de 144 a 146 megahercios. De 144,000 a 144,025, bajada de satélites. De 144,025 a 144,400, telegrafía y banda lateral para señales débiles. De 144,400 a 144,490, balizas, donde no se transmite. De 144,500 a 144,794, todos los modos. De 144,794 a 144,9625, digitales, con el APRS en 144,800. De 144,975 a 145,194, entradas de repetidores. De 145,206 a 145,5625, FM en símplex, con la frecuencia de llamada en 145,500. De 145,575 a 145,794, salidas de repetidores. De 145,806 a 146,000, satélites, sin contactos terrestres. Una flecha une entradas y salidas de repetidor con la indicación «600 kilohercios».](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s11-plan-2m.svg)

No hace falta memorizar la tabla. Quédate con cuatro números: **144,300** (SSB), **144,800** (APRS), **145,500** (llamada de FM) y **de 145,6 a 145,8** (salidas de repetidor).

La consecuencia práctica para tu portátil de FM: **su sitio está entre 144,975 y 145,794 MHz**, en un canal símplex o a través de un repetidor. Una emisión de FM en 144,300 MHz, que ocupa más de diez kilohercios, cae encima de quienes intentan sacar del ruido una señal de SSB llegada de ochocientos kilómetros. Tu equipo te deja hacerlo. El plan, no.

## Dónde está el plan y cómo se usa

El plan se revisa en las conferencias de la IARU. Las cifras de esta lección son las del plan de onda corta vigente desde 2020 y las del manual de VHF de la Región 1 en su edición de 2026; la referencia buena es siempre la última versión, publicada en iaru-r1.org. No hace falta aprenderlo de memoria: hace falta tenerlo delante, impreso junto al equipo, y mirarlo antes de transmitir en un sitio nuevo.

## Donde la gente se lía

- **«El plan de bandas es una recomendación, cada uno hace lo que quiere.»** En España, el reglamento dispone que se use como norma general. Y aunque no lo dijera: es lo que permite que quepamos todos.
- **Confundir borde de banda y tramo del plan.** Fuera del borde transmites sin autorización, en frecuencias de otro servicio. Fuera de tu tramo, pero dentro de la banda, incumples el plan y molestas a otros aficionados. Las dos cosas están mal; la primera es bastante más grave.
- **Olvidar hacia dónde cae la banda lateral.** El dial marca un extremo de tu voz, no el centro.
- **Pensar que una baliza es «una frecuencia libre con un pitido».** Ese pitido es el instrumento de medida de mucha gente.

## Compruébalo tú

1. Quieres llamar CQ en SSB en 40 metros. De estas frecuencias de dial, ¿cuáles son adecuadas según el plan? 7.020 kHz, 7.045 kHz, 7.100 kHz, 7.180 kHz.
2. Transmites en LSB con el dial en 7.051 kHz. ¿Qué frecuencias ocupa tu voz, y qué tramo del plan estás invadiendo?
3. La banda de 20 metros va de 14.000 a 14.350 kHz. Pones el dial en 14.348 kHz en USB. ¿Hasta dónde llega tu señal? ¿Qué clase de falta es?
4. Tu dial marca 7.055 kHz en LSB. ¿Qué frecuencias ocupas? ¿Cumples el plan? ¿Y con el dial en 7.052?
5. Quieres quedar con un amigo en FM símplex en 2 metros. ¿Cuál de estas frecuencias es adecuada: 144,300 MHz, 145,450 MHz, 145,650 MHz, 145,900 MHz? Di por qué no las otras tres.
6. Un repetidor tiene su salida en 145,7125 MHz. Sin mirar su ficha, ¿en qué tramo del plan estará su entrada, y en qué frecuencia exacta si el desplazamiento es el habitual?
7. Hay una emergencia real en curso en tu región y oyes tráfico en 7.110 kHz. Ibas a llamar CQ en 7.112 kHz. ¿Qué haces?

**Soluciones**

1. **7.100 y 7.180 kHz**, las dos en el tramo de todos los modos donde se habla. 7.020 está en el tramo de telegrafía; 7.045, en el de modos estrechos.
2. En LSB la voz va del dial hacia abajo: ocupa de **7.048 a 7.051 kHz**. Invades el tramo de 7.040 a 7.050, reservado a modos de hasta 500 Hz. Por eso el plan fija el dial mínimo en 7.053.
3. En USB la voz va hacia arriba: llega hasta **14.351 kHz**, un kilohercio por encima del borde. Es una emisión **fuera de banda**: no una descortesía, sino transmitir sin autorización.
4. Con el dial en 7.055 ocupas de 7.052 a 7.055 kHz: todo dentro del tramo de 2.700 Hz, cumples. Con el dial en 7.052 ocupas de 7.049 a 7.052: el kilohercio inferior invade el tramo de modos estrechos. Por eso el mínimo es 7.053.
5. **145,450 MHz**, en el tramo de FM símplex. 144,300 es el centro de actividad de SSB, en la zona de señales débiles. 145,650 es una salida de repetidor. 145,900 está en el tramo exclusivo de satélites, donde no se hacen contactos terrestres.
6. En el tramo de entradas de repetidores (144,975 – 145,194 MHz). Con −600 kHz: 145,7125 − 0,600 = **145,1125 MHz**.
7. Irte lejos: a otra parte de la banda, o a otra banda. 7.110 kHz es el centro de actividad de emergencias y, con tráfico real, se deja libre con margen de sobra. Y, de paso, escuchas por si puedes ser útil; las lecciones 12 y 13 explican cómo.

## En una frase

El plan de bandas de la IARU reparte cada banda en tramos para que las señales estrechas no convivan con las anchas —en onda corta, telegrafía abajo, digitales en medio y voz arriba—, protege los tramos de balizas y de satélites y fija puntos de encuentro; en España el reglamento dispone que se siga como norma general, y para cumplirlo hay que recordar que en SSB la voz cae a un lado del dial.

Ya sabes dónde y cómo hacer un contacto. Falta lo que queda después de él: apuntarlo, y saber qué hora poner.
