Este material es el **resumen de la sección**: lo que has aprendido en las ocho lecciones anteriores, condensado en formato de chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si al leer algún apartado notas que no lo entiendes, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## La onda electromagnética (lección 1)

- **Radiar:** que parte de la energía de una corriente alterna abandone el conductor en forma de campos que se alejan y no vuelven.
- **Onda electromagnética:** un campo eléctrico (**E**) y un campo magnético (**H**) que se regeneran el uno al otro mientras avanzan. No necesita ningún medio: cruza el vacío. Viaja a la velocidad de la luz, c ≈ 300.000 km/s.
- E y H son **perpendiculares entre sí** y **perpendiculares a la dirección de avance** (onda transversal). Crecen y menguan a la vez.
- Un conductor radia bien cuando mide del orden de **media longitud de onda o un cuarto**. Por eso la radio usa frecuencias altas.
- **Polarización:** la orientación del campo eléctrico, que es la de la antena que emite. Antena vertical, polarización vertical; antena horizontal, polarización horizontal. Cruzadas, en comunicación directa, se pierden hasta 20 dB.
- En el espacio libre la señal se reparte: **al doble de distancia, la cuarta parte de la potencia (−6 dB)**.

## Modular (lección 2)

- La voz (**banda vocal**, de 300 a 3.000 Hz) no puede radiarse sola: la antena mediría decenas de kilómetros y todas las voces coincidirían en frecuencia.
- **Portadora:** onda de radiofrecuencia pura y estable; es el vehículo y no lleva información.
- **Modular:** alterar la **amplitud**, la **frecuencia** o la **fase** de la portadora al ritmo de la información. **Demodular** (o detectar) es la operación inversa.
- **Ancho de banda:** el tamaño de la franja del dial que ocupa una señal. Cuanta más información por segundo, más ancho de banda como mínimo; cada modo añade lo suyo.

## CW y el batido (lección 3)

- **CW:** encender y apagar la portadora (manipularla) siguiendo el código morse. Ocupa **100–200 Hz**: donde cabe una señal de voz en SSB caben unas dieciocho de CW (2.700 / 150).
- **Chasquidos de manipulación:** ensanchamiento de la señal cuando la portadora se conmuta de golpe.
- **Batido:** dos oscilaciones de frecuencias parecidas, juntas, se refuerzan y se debilitan a un ritmo igual a la **diferencia** de sus frecuencias.
- **BFO:** oscilador del receptor que se mezcla con la señal para dar un tono audible por diferencia. Señal en 7.030.000 Hz y BFO en 7.030.700 Hz: tono de 700 Hz. El tono lo pone el receptor, no el transmisor.

## AM (lección 4)

- La amplitud de la portadora sigue la forma de la voz, dibujada en la **envolvente**. Receptor muy sencillo.
- Modular una portadora de frecuencia f con un tono de frecuencia a crea dos señales: en **f + a** y en **f − a**. Portadora de 7.000 kHz y tono de 1 kHz: 6.999, 7.000 y 7.001 kHz.
- Con voz aparecen dos **bandas laterales**, superior (USB) e inferior (LSB), cada una con la voz completa.
- **Ancho de banda de AM = 2 × frecuencia máxima del audio.** Voz hasta 3 kHz: 6 kHz.
- La información está en las bandas laterales, no en la portadora. Reparto de potencia al 100 % de modulación: cada banda lateral lleva la cuarta parte de la portadora. Portadora de 100 W: 100 + 25 + 25 = 150 W (portadora, dos tercios; cada banda, una sexta parte).
- **Profundidad de modulación = (máximo − mínimo) / (máximo + mínimo)** de la envolvente. Por encima del 100 % hay sobremodulación: distorsión y señal ensanchada.

## SSB (lección 5)

- Se suprimen la portadora y una banda lateral; se emite solo la otra. Ocupa **2,4–2,7 kHz**, menos de la mitad que la AM, y toda la potencia va al mensaje. Sin voz no se emite nada.
- A igual potencia total, el triple de potencia útil que la AM; a igual tope de potencia, unas ocho veces (9 dB).
- El receptor debe **reinsertar la portadora** con su BFO. Si la coloca desplazada, a todos los tonos de la voz se les suma la misma cantidad y se pierden sus proporciones: la «voz de pato».
- En LSB cada tono sale por debajo de la portadora suprimida; en USB, por encima. Portadora en 7.100 kHz, tono de 1 kHz, LSB: 7.099 kHz.
- **Convenio:** **LSB por debajo de 10 MHz** (160, 80 y 40 metros); **USB por encima** (20 metros en adelante, VHF y UHF). Los modos digitales, casi todos en USB.

## FM (lección 6)

- La voz mueve la **frecuencia** de la portadora; la amplitud es constante.
- **Desviación:** lo máximo que la frecuencia se aparta de su centro. Depende de lo fuerte que se habla. En la FM de voz de radioaficionado: ±5 kHz («ancha» en los equipos) o ±2,5 kHz («estrecha»).
- **Regla de Carson: ancho de banda ≈ 2 × (desviación + frecuencia máxima del audio).** Con 5 y 3 kHz: 16 kHz. Con 2,5 y 3 kHz: 11 kHz.
- **Índice de modulación = desviación / frecuencia del audio.**
- El receptor recorta la amplitud con un **limitador** y lee la frecuencia con un **discriminador**: el ruido, que altera la amplitud, queda fuera. Solo funciona con señal suficiente; con señales débiles rinden más la SSB y el CW.
- **Silenciador** (*squelch*): enmudece el altavoz cuando no hay señal. **Efecto captura:** de dos señales en la misma frecuencia, solo se oye la más fuerte.

## Modos digitales (lección 7)

- Envían **símbolos** en lugar de una señal continua. Se cambian de símbolo por saltos de frecuencia (**FSK**) o de fase (**PSK**). **Baudios:** símbolos por segundo.
- **RTTY:** dos frecuencias separadas 170 Hz, 45 baudios, unos 250 Hz. **PSK31:** 31–60 Hz. **FT8:** turnos de 15 segundos, 50 Hz, descifra hasta unos 20 dB por debajo del ruido; intercambio mínimo. **Voz digital** (DMR, D-STAR, C4FM) y **packet/APRS**, en VHF y UHF.

## Los modos, su ancho y su sitio (lección 8)

| Modo | Qué se cambia en la portadora | Ancho de banda | Dónde vive | Punto fuerte |
|---|---|---|---|---|
| CW | Encendida o apagada | 100–200 Hz | HF sobre todo | Eficacia con medios mínimos |
| AM | La amplitud | 6 kHz | Radiodifusión, aviación | Receptor sencillo |
| SSB | La amplitud, sin portadora y con una banda lateral | 2,4–2,7 kHz | Voz en HF | Toda la potencia en el mensaje |
| FM | La frecuencia | 11–16 kHz | VHF y UHF local | Sonido limpio |
| Digitales | Frecuencia o fase, a saltos | de 31 Hz a unos cientos de Hz | HF con señales débiles | Descifran bajo el ruido |

De menor a mayor ancho: **digitales estrechos y CW < SSB < AM < FM**.

En una **cascada** (frecuencia en horizontal, tiempo en vertical, brillo según la fuerza): la AM es una columna simétrica con línea central; la SSB, una mancha de un solo lado que sigue a la voz; el CW, un hilo a trazos; el FT8, rayitas en turnos regulares.

**Denominación de las emisiones** (tres símbolos): el primero indica la modulación (A, amplitud con dos bandas; J, banda lateral única; F, frecuencia; G, fase); el segundo, la señal que modula (1, digital sin tonos; 2, digital con tonos de audio; 3, analógica); el tercero, lo transmitido (A, telegrafía de oído; B, telegrafía para máquinas; D, datos; E, voz).

| A1A | A3E | J3E | F3E |
|---|---|---|---|
| Morse | Voz en AM | Voz en SSB | Voz en FM |

## Para el examen

Lo que más se pregunta, y casi siempre con números:

- Geometría de la onda y qué es la polarización.
- AM: frecuencias de las bandas laterales, ancho de banda (2 × audio máximo) y reparto de potencia.
- SSB: qué suprime, convenio LSB/USB (frontera en 10 MHz) y frecuencia a la que sale un tono.
- FM: regla de Carson, índice de modulación y por qué resiste el ruido.
- Orden de los modos por ancho de banda.
- El BFO y el tono que produce (una resta).
- Denominaciones A1A, A3E, J3E y F3E.

## Para profundizar

- **websdr.org** y las redes KiwiSDR: receptores reales que se manejan desde el navegador, gratis. Ejercicio: en 40 metros, sintoniza una SSB «en pato» y encájala tú.
- *Ética y procedimientos operativos para el radioaficionado* (Devoldere y Demeuleneere, IARU, edición española, de libre distribución): su capítulo de modos y procedimientos adelanta la sección 11.
- Wikipedia (CC BY-SA): «Banda lateral única» y «Frecuencia modulada» desarrollan las matemáticas de lo que aquí queda dicho con palabras.
