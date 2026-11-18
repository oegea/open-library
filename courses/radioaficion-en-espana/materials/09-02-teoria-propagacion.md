Este material es el **resumen de la sección**: lo que has aprendido en las ocho lecciones anteriores sobre propagación, condensado en formato de chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si al leer algún apartado notas que no lo entiendes, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## Los tres caminos de una onda

| Camino | Qué hace | Dónde manda |
|---|---|---|
| **Onda de superficie** | Avanza pegada al suelo y sigue su curva; pierde energía en él | Frecuencias bajas (onda media, 160 m). Cuanto más baja la frecuencia, más lejos llega; mejor sobre el mar |
| **Onda directa** | Va en línea recta de antena a antena, hasta el horizonte | VHF y UHF |
| **Onda ionosférica** | Sube, la ionosfera la curva y vuelve a tierra lejos | HF (3 a 30 MHz) |

- **Horizonte radioeléctrico:** distancia (km) = 4,12 × √h, con h en metros sobre el terreno que rodea la antena. Es un 15 % mayor que el horizonte visual. Los horizontes de las dos antenas se suman.
- En VHF y UHF **la altura de la antena importa más que la potencia**.
- **Onda espacial:** el conjunto de la onda directa y la reflejada en el suelo. Las ondas también se reflejan en edificios y se difractan en las aristas.
- Banda **abierta**: sus ondas están llegando a un lugar. Banda **cerrada**: no llegan, se ponga la potencia que se ponga.

## La ionosfera

- Región de la atmósfera entre unos 60 y 400 km donde la radiación del sol (ultravioleta y rayos X) **ioniza** el aire: arranca electrones a los átomos. La **recombinación** la deshace, más deprisa cuanto más denso es el aire.
- No refleja como un espejo: **refracta**. Los electrones libres oscilan con la onda y reemiten; la onda avanza más deprisa donde hay más electrones, y su trayectoria se curva poco a poco hasta volver a tierra.
- Devuelve la onda con más facilidad cuanto **más ionización** hay, cuanto **más baja** es la frecuencia y cuanto **más tumbada** llega la onda. Las frecuencias demasiado altas (VHF, UHF) la atraviesan.

| Capa | Altura | Cuándo | Qué hace |
|---|---|---|---|
| **D** | 60–90 km | Solo de día | **Absorbe** (no refleja), sobre todo las frecuencias bajas |
| **E** | 90–130 km | De día; de noche, muy débil | Devuelve las frecuencias más bajas de HF, en saltos cortos. Esporádica-E |
| **F1** | 130–200 km | Solo de día | Papel menor |
| **F2** (de noche, **F**) | 200–400 km | Día y noche | Devuelve las frecuencias más altas y da los saltos más largos |

- La capa F aguanta toda la noche porque en aire tan tenue los electrones tardan horas en recombinarse.
- Las bandas bajas se abren de noche **porque desaparece la capa D**, no porque aparezca la F.

## La ventana de frecuencias

- **Frecuencia crítica:** la más alta que una capa devuelve con incidencia **vertical**.
- **MUF** (frecuencia máxima utilizable): la más alta que la ionosfera devuelve para un **trayecto** concreto. Hasta unas 3 veces la crítica en saltos largos; apenas algo más que la crítica en trayectos cortos. Por encima, la onda escapa al espacio, con cualquier potencia.
- **LUF** (frecuencia mínima utilizable): por debajo, la absorción de la capa D debilita demasiado la señal. De día es alta; de noche cae.
- Entre LUF y MUF está la ventana útil. Las mejores señales, algo por debajo de la MUF: en torno al 85 % (frecuencia óptima de trabajo, FOT).
- **NVIS:** para distancias cortas, frecuencia por debajo de la crítica y onda casi vertical, con antena horizontal baja (80 y 40 m).

## Saltos, zona de silencio y desvanecimiento

- **Salto:** recorrido antena–ionosfera–tierra. Máximo aproximado: **4.000 km** con la capa F2, **2.000 km** con la E. Más lejos, **multisalto** (el mar refleja mejor que la tierra seca).
- Ángulo de radiación (o de salida) bajo: salto más largo.
- **Distancia de salto:** la distancia **mínima** a la que la onda ionosférica de una frecuencia vuelve a tierra.
- **Zona de silencio:** franja donde no se recibe la estación: más allá de su onda de superficie y más cerca que la distancia de salto. Crece con la frecuencia; en las bandas bajas, de noche, puede no existir.
- **Desvanecimiento (QSB):** la señal llega por varios caminos (multitrayecto) cuyas ondas se suman o se anulan según su fase. Es también la causa del eco de las señales lejanas.

## El sol

- **Ciclo solar:** unos **11 años**. Más manchas, más radiación ionizante, MUF más alta. En el máximo se abren las bandas altas; en el mínimo, se cierran. El ciclo 25 empezó a finales de 2019 y tuvo su máximo hacia 2024.
- **Flujo solar (SFI):** medida diaria de la emisión del sol en 10,7 cm. Cuanto más alto, mejor para las bandas altas (más de 100, bueno; más de 150, excelente).
- **Índice K:** agitación del campo magnético terrestre en las últimas 3 horas, de 0 a 9; de 5 en adelante, tormenta geomagnética. **Índice A:** lo mismo, resumido para el día entero. Cuanto más bajos, mejor.
- **SFI alto y K bajo:** las mejores condiciones.

| | Perturbación ionosférica súbita (efecto Dellinger) | Tormenta geomagnética |
|---|---|---|
| Causa | Rayos X de una fulguración | Partículas lanzadas por el sol |
| Tarda en llegar | 8 minutos | De 1 a 3 días |
| Afecta a | El lado diurno | Todo el planeta, sobre todo rutas polares |
| Capa | La D absorbe mucho más | La F2 pierde ionización: baja la MUF |
| Dura | De minutos a un par de horas | De horas a días |

- Otros ritmos: día y noche; rotación del sol cada 27 días; estaciones. La capa F2 está más ionizada a mediodía en invierno que en verano: las bandas altas rinden más de otoño a primavera.

## Las bandas de HF

Bandas **bajas**: 160, 80 y 40 m. Bandas **altas**: de 17 a 10 m.

| Banda | De día | De noche | Ciclo solar |
|---|---|---|---|
| 160 y 80 m | Solo local (capa D) | Regional y lejana; mejor en invierno | Influye poco |
| 40 m | España y países vecinos | Lejana, con zona de silencio de cientos de km | Influye poco |
| 30 y 20 m | Larga distancia, casi siempre | A ratos; más con sol activo | Influye algo |
| 17 a 10 m | Excelentes con sol activo | Cerradas | Influye mucho |

- De noche, para hablar con alguien cercano, 80 m.
- **Balizas:** emisoras automáticas en frecuencias fijas; permiten saber si una banda está abierta aunque esté vacía.
- **Línea gris:** franja de amanecer y anochecer; sin capa D y con la F aún ionizada, abre trayectos muy largos en las bandas bajas.

## VHF y UHF más allá del horizonte

| Fenómeno | Dónde | Alcance | Cuándo |
|---|---|---|---|
| **Conducto troposférico** | Troposfera, por inversión térmica | De cientos a más de 1.000 km | Anticiclón estable |
| **Esporádica-E** | Nubes densas en la capa E | 1.000 a 2.000 km (50 y hasta 144 MHz) | Mayo a agosto; no depende del ciclo solar |
| **Aurora** | Unos 100 km, cerca del polo | De cientos a más de 1.000 km | Tormenta geomagnética; antenas al norte, señal ronca |
| **Dispersión meteórica** | Estelas de meteoros | Hasta 2.000 km, en ráfagas | Mejor en lluvias de estrellas |
| **Rebote lunar (EME)** | La Luna | Unos 770.000 km de ida y vuelta; 2,5 s | Con la Luna visible |

## Ruido y balance de enlace

- En HF domina el **ruido atmosférico** (tormentas), más el de origen doméstico. En la parte baja de VHF cuenta el **galáctico**; en UHF, el **térmico** del receptor.
- Una señal solo se entiende si supera al ruido: **relación señal/ruido**.
- **Balance de enlace**, en decibelios: potencia + ganancia de antenas − pérdidas de cables − pérdidas del trayecto = señal que llega.

## Para el examen

- La capa D **absorbe**; no refleja. Solo existe de día.
- La capa de la larga distancia nocturna es la F (F2).
- Definiciones de frecuencia crítica (vertical), MUF (trayecto) y LUF.
- Salto máximo vía F2: unos 4.000 km. Zona de silencio: entre la onda de superficie y la distancia de salto.
- Ciclo solar de 11 años; K alto significa perturbación geomagnética; el apagón súbito afecta al lado diurno.
- Esporádica-E: verano, 50 y 144 MHz, 1.000 a 2.000 km.
- VHF y UHF: línea de vista, y conductos troposféricos con inversión térmica.
- QSB: multitrayecto e interferencia de fases.

## Para profundizar

- El blog de telecomunicaciones de emergencia de Ismael Pellejero (EA4FSI), emercomms.ipellejero.es, tiene introducciones en español a la propagación en HF aplicadas a emergencias.
- Índices en vivo: swpc.noaa.gov (meteorología espacial de la NOAA), solarham.com y hamqsl.com/solar. Compara el SFI y el K de hoy con lo que oigas esta noche en un receptor por Internet.
- pskreporter.info muestra en un mapa qué trayectos están abiertos en cada banda en este momento. Mirarlo a distintas horas durante una semana vale por un repaso entero.
- Wikipedia (CC BY-SA): «Ionosfera» y «Propagación por onda de cielo», para ampliar la física.
