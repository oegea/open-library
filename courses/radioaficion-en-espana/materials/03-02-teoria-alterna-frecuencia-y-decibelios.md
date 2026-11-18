Este material es el **resumen de la sección**: lo esencial de las nueve lecciones anteriores, condensado para repasar antes del examen. Aquí no se explica nada desde cero; si algún apartado no te suena, vuelve a la lección indicada, que es donde está la explicación paso a paso.

## Corriente alterna (lección 1)

- **Continua (CC, DC):** la tensión empuja siempre en el mismo sentido. **Alterna (CA, AC):** cambia de sentido de forma regular; los electrones oscilan alrededor de su sitio.
- Se dibuja como una **senoide**: de izquierda a derecha, el tiempo; la altura, la tensión en cada instante (**valor instantáneo**). Por debajo del cero empuja en el sentido contrario.
- **Ciclo:** una oscilación completa (semiciclo positivo y semiciclo negativo).
- Entrega energía en los dos sentidos. Se usa porque se transforma fácilmente y porque, si oscila muy deprisa, radia: **una señal de radio es corriente alterna de alta frecuencia**.

## Periodo y frecuencia (lección 2)

- **Periodo (T):** lo que dura un ciclo, en segundos. **Frecuencia (f):** ciclos por segundo, en **hercios (Hz)**.
- **f = 1 / T** y **T = 1 / f**. A más frecuencia, menos periodo.
- Con el periodo en ms, 1 / T da kHz; con el periodo en µs, da MHz. Ejemplo: T = 2 ms → 1.000 / 2 = 500 Hz.
- La red eléctrica: 50 Hz, T = 20 ms.
- **Audiofrecuencia (AF):** de unos 20 Hz a unos 20 kHz. **Radiofrecuencia (RF):** de unos 3 kHz hacia arriba.

## Cuánto mide una onda (lección 3)

| Medida | Qué es | Relación |
|---|---|---|
| Valor de pico (Up) | Del cero a la cresta. Es la «amplitud» | — |
| Valor de pico a pico (Upp) | Del valle a la cresta | Upp = 2 × Up |
| Valor eficaz (Uef, RMS) | La tensión continua que calentaría lo mismo | Uef = 0,707 × Up; Up = 1,414 × Uef |

- Los 0,707 y 1,414 solo valen para senoides. Si no se dice nada, un valor en alterna es **eficaz**: los 230 V del enchufe son eficaces (pico ≈ 325 V).
- Valor medio de un ciclo completo: cero. De medio ciclo: 0,637 × Up.
- En instrumentos y preguntas de examen: Vp, Vpp, Vef o Vrms.

## Fase (lección 4)

- **Fase:** punto del ciclo en que está la onda, en grados. Ciclo completo: 360°; cresta: 90°; medio ciclo: 180°.
- Dos ondas de la misma frecuencia: **en fase** (0°) se refuerzan; **en oposición de fase** (180°) se anulan si son iguales.
- La que llega antes a su cresta va **adelantada**; la otra, **retrasada**.

## La onda y su longitud (lección 5)

- Una corriente alterna rápida desprende **ondas electromagnéticas**: campo que se suelta del conductor y se aleja (el palo agitado en el estanque). Cómo se sostienen los dos campos, eléctrico y magnético, se ve en la sección 6.
- Viajan a la **velocidad de la luz**, c ≈ 300.000 km/s, sea cual sea su frecuencia, y no necesitan ningún medio.
- **Longitud de onda (λ):** distancia que avanza la onda en un ciclo, en metros. λ = c / f.
- Fórmula práctica: **λ (m) = 300 / f (MHz)**, y **f (MHz) = 300 / λ (m)**. El producto de ambas es siempre 300.
- Ejemplos: 7,088 MHz → 42,3 m; 145 MHz → 2,07 m; 0,70 m → 429 MHz.
- Un conductor radia bien cuando su tamaño es comparable a la longitud de onda (la mitad o un cuarto). Las bandas se nombran por su longitud de onda redondeada.

## El espectro (lección 6)

| Sigla | Frecuencias | Longitud de onda | Nombre métrico |
|---|---|---|---|
| VLF | 3 a 30 kHz | 100 a 10 km | miriamétricas |
| LF | 30 a 300 kHz | 10 a 1 km | kilométricas |
| MF | 300 kHz a 3 MHz | 1.000 a 100 m | hectométricas |
| **HF** | **3 a 30 MHz** | **100 a 10 m** | **decamétricas** |
| **VHF** | **30 a 300 MHz** | **10 a 1 m** | **métricas** |
| **UHF** | **300 MHz a 3 GHz** | **1 m a 10 cm** | **decimétricas** |
| SHF | 3 a 30 GHz | 10 a 1 cm | centimétricas |
| EHF | 30 a 300 GHz | 1 cm a 1 mm | milimétricas |

- Cada tramo multiplica por diez la frecuencia del anterior. El límite superior pertenece al tramo que termina en él.
- HF es la onda corta (larga distancia); VHF y UHF, alcance local, casi en línea recta.
- Bandas de aficionado: 160 m (MF); 80, 40, 20, 15 y 10 m (HF); 6 m y 2 m (VHF); 70 cm (UHF).

## Armónicos (lección 7)

- Una **senoide pura** contiene una sola frecuencia. Cualquier otra onda periódica (cuadrada, diente de sierra, senoide recortada) equivale a una **fundamental** más **armónicos**, a veces con una **componente continua**.
- **Frecuencia del armónico = número del armónico × fundamental.** Para 7 MHz: segundo en 14 MHz, tercero en 21 MHz, cuarto en 28 MHz.
- Un amplificador forzado recorta la onda y genera armónicos, que interfieren en otras frecuencias. Se evitan no forzando el equipo y con un **filtro paso bajo** a la salida del transmisor (cómo se construye, en la sección 5).

## Decibelios (lecciones 8 y 9)

El decibelio compara dos potencias. Sumar decibelios es multiplicar; restarlos es dividir.

| Decibelios | Si es ganancia (+) | Si es pérdida (−) |
|---|---|---|
| 3 dB | × 2 | ÷ 2 |
| 6 dB | × 4 | ÷ 4 |
| 10 dB | × 10 | ÷ 10 |
| 20 dB | × 100 | ÷ 100 |
| 30 dB | × 1.000 | ÷ 1.000 |

- 0 dB: sin cambio. Combinaciones: 13 dB = 10 + 3 → × 20; 7 dB = 10 − 3 → × 5.
- **En tensión** (sobre la misma resistencia): 6 dB es el doble; 20 dB, diez veces.
- **Balance de una estación:** se suman ganancias y se restan pérdidas. Cable −3 dB y antena +6 dB: +3 dB, el doble. La potencia equivalente en la dirección de la antena es la **potencia radiada aparente (PRA)**; referida a una antena ideal que radia igual en todas direcciones, **PIRE**.
- **dBm:** respecto a 1 mW (0 dBm = 1 mW; 30 dBm = 1 W). **dBW:** respecto a 1 W (0 dBW = 1 W; 20 dBW = 100 W). Entre ambas, 30 dB: 0 dBW = 30 dBm.
- Fórmulas: dB = 10 × log (P2 / P1); para tensiones, dB = 20 × log (U2 / U1).

## Para el examen

- «300 entre los megahercios», en los dos sentidos, con la frecuencia en MHz y la longitud de onda en metros.
- f = 1 / T con el periodo en milisegundos o microsegundos.
- Conversión pico ↔ eficaz (× 0,707 o × 1,414), y pico a pico = 2 × pico.
- Nombres y límites de HF, VHF y UHF, y a qué tramo pertenece cada banda.
- Número del armónico = número por el que se multiplica la fundamental; el filtro paso bajo los atenúa.
- Fase: 180° es oposición (se anulan); un cuarto de ciclo son 90°.
- Decibelios de la tabla aplicados a potencias y a tensiones; balance de una cadena; qué son dBm y dBW.

## Para profundizar

- OpenStax, *Física universitaria*, vol. 1 (ondas) y vol. 2 (corriente alterna), con licencia CC BY 4.0 y disponible en español: la matemática completa de todo lo anterior.
- Un receptor SDR público, como los enlazados en websdr.org: muestra el espectro dibujado en vivo, con cada señal como un pico sobre el ruido y su frecuencia debajo. En la sección 6 lo usarás a fondo.
