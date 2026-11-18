Este material es el **resumen de la sección**: lo que has aprendido en las diez lecciones anteriores sobre antenas y líneas de transmisión, condensado en una chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si algún apartado no te suena, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## Antena y resonancia

- Una **antena** convierte la corriente de radiofrecuencia en onda de radio, y al revés. Se comporta igual transmitiendo que recibiendo.
- En un hilo de media onda, la corriente y su rebote en las puntas forman una **onda estacionaria** y el hilo entra en **resonancia**: la corriente es máxima en el centro y nula en las puntas; la tensión, máxima en las puntas y mínima en el centro.
- La longitud decide la frecuencia de resonancia. Antena más larga, frecuencia más baja; recortar sube la frecuencia.
- **Factor de acortamiento:** un hilo real se corta alrededor de un 5 % más corto que la media onda teórica.

| Antena | Longitud en metros (f en MHz) |
|---|---|
| Hilo o dipolo de media onda | 142,5 / f |
| Vertical de cuarto de onda | 71,25 / f |

## Dipolo y vertical

| | Dipolo de media onda | Vertical de cuarto de onda |
|---|---|---|
| Forma | Dos brazos de un cuarto de onda, alimentados por el centro | Una varilla sobre un plano de tierra (radiales) |
| Impedancia | Unos 73 Ω (en la práctica, de 40 a 90 Ω según la altura) | Unos 36 Ω |
| Diagrama visto desde arriba | En ocho: máximo perpendicular al hilo, casi nada hacia las puntas | Circular: omnidireccional |
| Polarización | Horizontal, si el hilo está horizontal | Vertical |
| Punto débil | Necesita altura para llegar lejos | Rinde lo que rinde su plano de tierra |

- **Dipolo plegado:** misma longitud, unos 300 Ω.
- **V invertida:** dipolo con el centro en alto y los brazos inclinados; impedancia más cerca de 50 Ω.
- **Ángulo de salida:** inclinación sobre el horizonte a la que sale la mayor parte de la energía. Dipolo bajo (menos de un cuarto de onda de altura), ángulo alto y alcance corto; dipolo alto (media onda o más), ángulo bajo y alcance largo.
- Por el plano de tierra circula la misma corriente que por la varilla.

## Ganancia y antenas directivas

- La **ganancia** no crea energía: la concentra en unas direcciones quitándola de otras.
- **dBi:** respecto a la antena isotrópica (ideal, radia igual en todas las direcciones). **dBd:** respecto al dipolo. **dBd = dBi − 2,15.**
- **PRA** (potencia radiada aparente) = potencia que llega a la antena × ganancia en dBd. **PIRE** = lo mismo con la ganancia en dBi. **PIRE = 1,64 × PRA.**
- **Rendimiento:** parte de la potencia recibida que la antena convierte en onda. La ganancia dice hacia dónde va lo radiado; el rendimiento, cuánto se radia.

**Yagi:** solo el **dipolo activo** está conectado al cable. Los demás elementos son **parásitos**: el **reflector**, más largo, detrás; los **directores**, más cortos, delante. Radia hacia los directores.

Ganancias típicas: unos 5 o 6 dBd con 3 elementos, 7 u 8 dBd con 5 o 6, y 12 dBd o más con más de 10.

- **Relación delante-atrás:** decibelios que la antena radia de más hacia delante que hacia atrás. **Ancho del haz:** grados que abarca el lóbulo principal.
- Otras antenas: **hilo largo** (necesita acoplador), **multibanda con trampas** (circuitos resonantes que cortan eléctricamente la antena), **cuadro**, **parabólica** (solo en microondas).

## Impedancia y adaptación

- El cable que une equipo y antena es una **línea de transmisión**: por él viaja una onda.
- **Impedancia característica:** proporción entre la tensión y la corriente de esa onda. La fija la construcción del cable; no depende de su longitud.
- En una unión entre impedancias distintas, parte de la onda se **refleja**. La **máxima transferencia de potencia** se da con impedancias iguales.
- El valor normalizado en radio es **50 Ω**: transmisor, cable y antena. El cable de televisión es de 75 Ω.
- En resonancia, la antena es una resistencia pura. Antena **larga** para la frecuencia: reactancia **inductiva**. Antena **corta**: reactancia **capacitiva**.

## La ROE

- **ROE** (en inglés, SWR): tensión máxima dividida entre tensión mínima a lo largo del cable. Mide cuánta onda rebota. La mejor posible es 1 (también se escribe 1:1).
- Con carga resistiva: **ROE = impedancia mayor / impedancia menor**.
- Potencia reflejada: se divide (ROE − 1) entre (ROE + 1) y el resultado se multiplica por sí mismo.

| ROE | Potencia reflejada | Valoración |
|---|---|---|
| 1 | 0 % | Perfecta |
| 1,5 | 4 % | Muy buena |
| 2 | 11 % | Aceptable |
| 3 | 25 % | Mala: el equipo empieza a protegerse |
| Infinita | 100 % | Cable cortado o en cortocircuito |

- Los dos daños de una ROE alta: la **etapa final del transmisor** sufre (y el equipo reduce potencia para protegerse) y **aumentan las pérdidas en el cable**.

## Medir y domar la ROE

- **Medidor de ROE:** intercalado entre el transmisor y la antena; compara la potencia directa con la reflejada.
- **Analizador de antenas:** dibuja la ROE a lo largo de la frecuencia. El fondo del valle es la resonancia; la anchura del valle por debajo de ROE 2, el **ancho de banda**.
- Un cable con muchas pérdidas hace que el medidor, junto al equipo, marque una ROE mejor que la real.
- **Acoplador:** red de bobinas y condensadores, en **π** o en **T**. Hace que el transmisor vea 50 Ω, pero no arregla la antena: entre el cable y la antena la ROE sigue igual.
- **Carga artificial:** resistencia de 50 Ω que absorbe la potencia sin radiarla. Da ROE 1. Sirve para probar sin salir al aire y para localizar averías.

## El cable coaxial

- Cuatro capas: **conductor central** (vivo), **dieléctrico**, **malla** y **cubierta**.
- **Las pérdidas aumentan con la longitud y con la frecuencia**, y afectan por igual a lo que se transmite y a lo que se recibe. Valores típicos orientativos para un cable fino, el RG-58 (consulta la hoja del fabricante):

| Frecuencia | Pérdida en 100 m | En 30 m, de 100 W llegan |
|---|---|---|
| 7 MHz | unos 4 dB | unos 75 W |
| 145 MHz | unos 19 dB | unos 27 W |
| 435 MHz | unos 35 dB | unos 9 W |

- **Factor de velocidad:** velocidad de la onda en el cable respecto a la de la luz. Unos 0,66 con dieléctrico macizo; de 0,80 a 0,85 con espuma. Dentro del cable, la longitud de onda se acorta en esa proporción.
- Un **cuarto de onda** de línea transforma impedancias (transformador de cuarto de onda).
- **Línea paralela** (escalerilla): simétrica, de 300 a 600 Ω, pierde menos, pero no está blindada. **Guía de ondas:** tubo metálico hueco, para microondas.
- Conectores: **PL-259 / SO-239** (HF), **BNC**, **N** (VHF y UHF), **SMA**.

## El balun

- **Efecto pelicular:** la radiofrecuencia circula solo por la superficie de los conductores. La cara exterior de la malla es un conductor aparte.
- El dipolo es **simétrico** y el coaxial **asimétrico**. Al unirlos sin más, parte de la corriente baja por el exterior de la malla (**corriente de modo común**): el cable radia y causa interferencias.
- **Balun:** une la línea asimétrica con la antena simétrica e impide esa corriente. El de choque (vueltas de cable sobre ferrita) no transforma: es 1:1. Los hay que transforman la impedancia: un 4:1 convierte 200 Ω en 50 Ω.

## Para el examen

- Longitud del dipolo y de la vertical para una frecuencia. Lee si piden la longitud total, un brazo, media onda o un cuarto.
- Impedancias: dipolo, 73 Ω; vertical, 36 Ω; dipolo plegado, 300 Ω; coaxial, 50 Ω.
- Diagramas (ocho, omnidireccional, directiva), reflector y directores, relación delante-atrás.
- dBi frente a dBd, y cálculo de la PRA y la PIRE.
- ROE: qué es, valores, porcentaje reflejado, con qué se mide y qué daños causa. Acoplador en π y en T.
- Pérdidas del coaxial (crecen con frecuencia y longitud), paso de decibelios a vatios y factor de velocidad.
- Función del balun y de la carga artificial. Antena larga, inductiva; corta, capacitiva. Qué es una trampa.

## Para profundizar

- Una calculadora de dipolos en línea, hilo, tres aisladores y el analizador de un radioclub: el dipolo de Marina cuesta menos de 30 € en materiales.
- Programas gratuitos de simulación de antenas, como MMANA-GAL o 4nec2, para ver el diagrama de un dipolo a distintas alturas.
- El *ARRL Antenna Book* (en inglés, de pago) es la obra de referencia para seguir.
