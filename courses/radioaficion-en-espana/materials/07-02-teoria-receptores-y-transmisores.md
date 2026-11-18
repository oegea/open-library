Este material es el **resumen de la sección**: todo lo que has aprendido en las diez lecciones anteriores sobre receptores y transmisores, condensado en formato de chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si al leer algún apartado notas que no lo entiendes, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## Lo que se le pide a un receptor

| Cualidad | Qué es | Quién la da o la limita |
|---|---|---|
| **Sensibilidad** | Oír lo débil. Se da en µV o dBm para una relación señal/ruido dada; cifra baja = mejor | La limita el **ruido**, no la amplificación |
| **Selectividad** | Separar lo cercano | Los **filtros** (CW 250 a 500 Hz, SSB 2,4 a 2,7 kHz, AM 6 kHz, FM 12 a 15 kHz) |
| **Estabilidad** | No moverse de la frecuencia (lo contrario es la **deriva**) | El oscilador: cristal de cuarzo y sintetizador |

- **Relación señal/ruido:** cuántas veces supera la señal al ruido, en dB de potencia. Amplificar sube las dos por igual y no la mejora; cuenta el ruido de la **primera etapa** (amplificador de bajo ruido; su calidad se llama *figura de ruido*).
- Un filtro que se mueve con el dial no puede ser estrecho: para 3 kHz en 30 MHz haría falta un Q de 10.000, y una bobina con su condensador se queda en unos cientos. Un cristal llega, pero su frecuencia es fija.

## El mezclador

- Circuito **no lineal** al que entran dos frecuencias y del que salen su **suma** y su **diferencia**; un filtro colocado detrás elige una. Ejemplo: 7.100 kHz y 16.100 kHz dan 23.200 y 9.000 kHz.
- **Mezclar es trasladar:** la señal cambia de frecuencia con su ancho y su mensaje intactos (del revés, si el oscilador está por encima).
- **Oscilador local (OL):** el que acompaña al mezclador del receptor. Es lo que mueve el dial.

## El superheterodino

Traslada cualquier emisora a una **frecuencia intermedia (FI) fija**, donde filtros de cristal que no necesitan moverse dan la selectividad. El OL se pone a una FI de distancia de la emisora: con FI de 9 MHz, para oír 7,1 MHz, OL en 16,1 MHz.

> **Antena → filtro de entrada y amplificador de RF → mezclador (con el oscilador local) → filtro de FI → amplificador de FI → demodulador → amplificador de audio → altavoz.**

| Modo | Demodulador |
|---|---|
| AM | Detector de envolvente (un diodo) |
| FM | Limitador + discriminador |
| SSB y CW | Detector de producto, con su BFO |

- **CAG (AGC):** mide la señal detectada y ajusta la ganancia de RF y FI para que el volumen no dependa de lo fuerte que llegue cada estación.
- **Medidor de señal (S-meter):** de S1 a S9, 6 dB por punto; S9 = 50 µV en HF.
- **Silenciador (squelch):** en FM, corta el audio mientras no llega señal.

## La frecuencia imagen y la doble conversión

- **Frecuencia imagen:** la que está al otro lado del oscilador local, a la misma distancia que la deseada; es decir, a **2 × FI** de la deseada. Con FI de 9 MHz y OL en 16,1 MHz: deseada 7,1 MHz, imagen 25,1 MHz.
- Tras el mezclador, deseada e imagen están en la misma frecuencia: hay que quitarla **antes**, con el **filtro de entrada**. Una FI alta la aleja y lo facilita, pero dificulta el filtro estrecho.
- **Doble conversión:** primera FI alta (aleja la imagen) y segunda FI baja (filtros estrechos). Ejemplo para 7.100 kHz: primer OL en 52.100 → 45.000 kHz; segundo OL fijo en 45.455 → 455 kHz.

> **Antena → filtro de entrada y amplificador de RF → primer mezclador (OL variable) → filtro de primera FI → segundo mezclador (OL fijo) → filtro de segunda FI → amplificador de FI → demodulador → amplificador de audio.**

## Conversión directa y SDR

- **Conversión directa:** el OL está en la frecuencia de la emisora y del mezclador sale ya el audio (FI cero). Cinco bloques: filtro de entrada, mezclador, oscilador local, filtro de audio y amplificador de audio. Muy sencillo, pero oye a los dos lados del oscilador a la vez.
- **SDR (radio definida por software):** un conversor analógico-digital convierte la señal en números, y un programa mezcla, filtra y demodula. Mismas operaciones, hechas con cálculos; permite ver la banda en cascada.

## Cómo se juzga un receptor

- **Rango dinámico** (dB, cifra alta = mejor): capacidad de oír lo débil junto a lo muy fuerte sin que las primeras etapas deformen.
- **Intermodulación:** dos señales fuertes A y B fabrican dentro del receptor señales que no existen, en **2 × A − B** y **2 × B − A**. Con 7.200 y 7.210 kHz: 7.190 y 7.220 kHz.
- **Desensibilización o bloqueo:** una sola señal fuerte hace que las débiles bajen o desaparezcan. **Modulación cruzada:** su modulación se oye encima de otra estación.
- **Remedio:** el **atenuador** (o apagar el preamplificador). Con 10 dB de atenuación, los productos de intermodulación bajan unos 30 dB.
- **Estabilidad** en partes por millón: 1 ppm en 14 MHz son 14 Hz.

## Los transmisores

Todo transmisor genera una portadora, la modula, la amplifica y la limpia.

> **CW:** oscilador → separador → excitador → amplificador de potencia (clase C) → filtro paso bajo → antena. La llave actúa después del oscilador.

> **FM:** micrófono → amplificador de micrófono → limitador de desviación → oscilador modulado en frecuencia → (multiplicadores) → amplificador de potencia (clase C) → filtro paso bajo → antena.

> **SSB:** micrófono → modulador balanceado (con el oscilador de portadora) → filtro de cristal → mezclador (con el oscilador variable) → filtro paso banda → excitador → amplificador de potencia (clase AB) → filtro paso bajo → antena.

- **Multiplicadores de frecuencia:** se quedan con un armónico; multiplican también la desviación. Solo para CW y FM.
- **Modulador balanceado:** suprime la **portadora**. **Filtro de cristal:** suprime **una banda lateral**.
- **Clase AB (lineal) para SSB; clase C solo para CW y FM.**
- **Filtro paso bajo:** elimina los armónicos de la etapa final.
- **Rendimiento:** potencia útil / potencia consumida. Un equipo que toma 20 A a 13,8 V (276 W) y entrega 100 W rinde un 36 %.
- **PEP, potencia de cresta de envolvente:** la potencia en los picos de la modulación. Es la medida de los límites legales (sección 12). Cálculo: tensión de pico × 0,707, y luego U² / R. Con 100 V de pico sobre 50 Ω: 100 W. La potencia media con la voz es entre 20 y 30 W por cada 100 W PEP.

## Los defectos del transmisor

**Emisiones no deseadas**, en dos familias:

| Familia | Dónde | Qué incluye | Remedio |
|---|---|---|---|
| **Espurias** (no esenciales) | Lejos de tu señal | Armónicos, oscilaciones parásitas, productos de mezcla | Filtro paso bajo, buen diseño y ajuste |
| **Fuera de banda** | Pegadas a tu señal | Splatter, sobredesviación, chasquidos de manipulación | No forzar el micrófono ni la etapa final |

- **Splatter:** la etapa saturada mezcla entre sí los tonos de la voz (intermodulación del transmisor) y la señal de 2,7 kHz pasa a ocupar ocho o diez kilohercios.
- **ALC:** frena el exceso de excitación. Su indicador debe moverse solo en los picos de voz y sin salirse de su zona.
- **Sobredesviación:** FM ancha (±5 kHz) en un canal de FM estrecha (±2,5 kHz), o limitador mal ajustado.
- **Chasquidos de manipulación:** portadora que sube y baja con demasiada brusquedad.
- **Deriva:** desplazamiento lento de la frecuencia. **Chirp:** la frecuencia resbala en cada signo de morse; se evita con el oscilador siempre en marcha, bien alimentado y con su separador.
- **Zumbido:** rizado de 100 Hz de una fuente que filtra mal.
- Doblar la potencia son 3 dB: **medio punto** del medidor de señal.

## Para el examen

- Definiciones de sensibilidad y selectividad: las preguntan cruzadas.
- Bloques del superheterodino en orden y función de cada uno (la selectividad, en los filtros de FI); a veces como diagrama.
- Cálculo del oscilador local (emisora ± FI) y de la **frecuencia imagen** (deseada ± 2 × FI). Es la pregunta estrella de receptores.
- Para qué sirve la doble conversión, y qué hacen el CAG, el silenciador y el detector de producto.
- Bloques del transmisor de SSB: modulador balanceado (portadora) y filtro de cristal (banda lateral); clase AB, nunca C.
- Qué es la PEP, qué es el splatter y qué lo causa, y para qué sirve el filtro paso bajo.
- Intermodulación frente a frecuencia imagen: no confundirlas.

## Para profundizar

- Ejercicio de un minuto que fija el superheterodino: elige una FI de 9 MHz y calcula el oscilador local y la imagen para tres emisoras cualesquiera. Verás que la imagen cae siempre a 18 MHz de la deseada.
- En un receptor por Internet (websdr.org, que es una SDR real), abre la cascada al máximo de ancho: estás viendo de golpe todo el trozo de banda que la SDR ha digitalizado.
- Wikipedia (CC BY-SA): «Receptor superheterodino», con los diagramas de bloques clásicos, y «Radio definida por software».
