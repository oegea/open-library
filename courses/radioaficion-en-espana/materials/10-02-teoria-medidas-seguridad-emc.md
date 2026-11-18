Este material es el **resumen de la sección**: lo que has aprendido en las nueve lecciones anteriores sobre medidas, seguridad y compatibilidad electromagnética, condensado en formato de chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si al leer algún apartado notas que no lo entiendes, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## El polímetro

| Como… | Mide | Se conecta | Resistencia interna | Error típico |
|---|---|---|---|---|
| **Voltímetro** | Tensión (V) | En paralelo | Muy alta | Selector en alterna para medir continua, o al revés |
| **Amperímetro** | Corriente (A) | En serie | Muy baja | Conectarlo en paralelo: cortocircuito |
| **Ohmímetro** | Resistencia (Ω) | Sobre la pieza | — | Medir con el circuito con tensión |

- Antes de medir: qué (V, A, Ω), de qué tipo (continua ⎓ o alterna ~) y cuánto (empezar por la escala más alta). Cable negro en COM; rojo en VΩ, salvo para medir corriente.
- El ohmímetro, siempre **sin tensión** y, si se puede, con la pieza desconectada.
- En alterna solo es fiable con la senoide de 50 Hz. No sirve para radiofrecuencia.
- Los analógicos (de aguja) tienen menos resistencia interna que los digitales y alteran más el circuito.
- Todo instrumento altera algo lo que mide y tiene un margen de error. Lo que importa se mide dos veces y se apunta.

## Los instrumentos de la estación

| Instrumento | Qué mide o hace | Dónde va |
|---|---|---|
| Medidor de ROE | La adaptación entre transmisor, cable y antena | Intercalado en el coaxial |
| Vatímetro de RF | Potencia directa y reflejada (media o de cresta, PEP) | Intercalado en el coaxial |
| Frecuencímetro | La frecuencia, contando ciclos | A una muestra de la señal |
| Osciloscopio | La **forma** de la señal en el tiempo | A una muestra de la señal |
| Analizador de espectro | La energía en cada **frecuencia**: armónicos y espurias | A una muestra de la señal |
| Generador de señales | Produce una señal conocida para probar | A la entrada de lo que se prueba |
| Analizador de antenas | La ROE a lo largo de la banda; la resonancia | En lugar del transmisor |
| Carga artificial | Absorbe la potencia sin radiar: 50 Ω, ROE 1 | En lugar de la antena |

- ROE: 1 es perfecto; hasta 1,5, muy bueno; hasta 2 no suele importar.
- Un cable con muchas pérdidas hace que la ROE medida junto al transmisor parezca mejor de lo que es en la antena.
- Un vatímetro sencillo indica potencia media; en banda lateral, la de cresta (PEP) es mayor.
- Frecuencímetro, osciloscopio y analizador de espectro **no se conectan directamente a un transmisor**: solo a una muestra pequeña.

## Seguridad eléctrica

- Lo que daña es la **corriente** que atraviesa el cuerpo. Riesgo grave desde unos **30 mA**; más de 100 mA, muy probablemente mortal. Unas decenas de miliamperios pueden ser mortales.
- A 230 V la piel no protege: quedan los 1.000 a 2.000 Ω del interior del cuerpo, y pasan más de 100 mA con las manos secas o mojadas. La tensión de un enchufe es siempre peligrosa.
- Agravan: la humedad, el camino a través del pecho y el tiempo.
- Las baterías no dan calambre, pero en cortocircuito dan cientos de amperios: fuera anillos, relojes y pulseras.

| Hilo | Color | Función |
|---|---|---|
| Fase | Marrón (también negro o gris) | Con tensión: 230 V respecto al suelo |
| Neutro | Azul | Vuelta; unido a tierra en el origen de la red |
| Tierra de protección | Verde y amarillo | Sin corriente en condiciones normales; actúa en caso de avería |

- Basta tocar la fase y cualquier cosa unida a tierra. «Apagado» no es «sin tensión»: sin tensión es desenchufado.
- La **tierra de protección** deriva a tierra la corriente de una avería (fase contra carcasa); quien corta es el diferencial. Nunca se anula.

| | Diferencial | Magnetotérmico |
|---|---|---|
| Salta con | Fuga a tierra de 30 mA | Sobrecargas y cortocircuitos |
| Protege | A las **personas** | A la **instalación** |

- El diferencial no limita la corriente: acorta el tiempo. No detecta un contacto entre fase y neutro. Se prueba con su botón T.
- **Fusibles:** rápidos (F) o lentos (T). Se sustituyen por otro del mismo tipo y valor; si vuelve a fundirse, hay avería.
- **Condensadores:** siguen cargados horas o días después de desenchufar. En una fuente conmutada, a unos 325 V (el valor de pico de la red: 230 × 1,41). Desenchufar, esperar, comprobar el polímetro, medir; si queda tensión, no se toca. La primera vez, acompañado. Los equipos de válvulas y de alta tensión no son para principiantes.
- No se trabaja ni se mide dentro de un aparato enchufado a la red. Con tensión solo se miden tensiones muy bajas de continua (13,8 V, baterías).
- En la estación, un interruptor general accesible.
- Ante una descarga: no tocar a la persona, cortar la corriente, llamar al 112; que la vea un médico.

## Radiofrecuencia y alturas

- La RF **quema** al contacto (quemadura profunda): nadie toca antenas ni cables descubiertos mientras se transmite.
- Cerca de una antena con mucha potencia, el cuerpo absorbe energía y se calienta: hay **límites de exposición**. Dependen de la potencia, la distancia (al doble, la cuarta parte de potencia por metro cuadrado), la antena y la frecuencia (más estrictos en VHF).
- El reglamento (anexo I, apartado 3.5) advierte de que las potencias máximas no eximen de reducir la potencia donde las personas pudieran quedar expuestas por encima de 3,5 mW/cm².
- Antenas altas y lejos de las personas; la potencia justa.
- En un tejado: nunca solo, con arnés siempre, nunca con viento, lluvia o prisa. El mástil, mejor un instalador.
- **Líneas eléctricas:** jamás se monta una antena donde, al caer o al manejarla, pueda tocar una. Si no hay distancia de sobra con el mástil cayendo en la peor dirección, se elige otro sitio.
- Artículo 31 del reglamento: obligación de cumplir las normas de seguridad y de mantener en buen estado equipos, antenas y accesorios.

## Rayos y tierras

- El peligro habitual no es el impacto directo, sino la tensión que un rayo cercano **induce** en la antena. También la electricidad estática.
- **Con tormenta cerca o anunciada:** desconectar las antenas de los equipos y alejar los cables de aparatos y personas, **antes** de que llegue; desenchufar también de la red. Si ya truena, no se toca nada. Nadie en la azotea ni tocando el mástil.
- Instalación fija: **descargador de gas** en la entrada del coaxial, y mástil unido a tierra con un conductor **corto, grueso y recto**.
- En un edificio, el mástil se une a la **red de tierra del edificio**, y lo hace un instalador autorizado. La pica propia es para casas con terreno, y debe quedar unida a la tierra de la casa, también por un instalador.

| | Tierra de protección eléctrica | Tierra de RF y de tormentas |
|---|---|---|
| Dónde | En el enchufe | En el mástil y el descargador |
| Protege de | Averías de la red dentro de los aparatos | Picos inducidos por rayos y electricidad estática |

- Tienen funciones distintas, pero deben estar **unidas** (conexión equipotencial). Una tierra de antena separada de la eléctrica es la configuración peligrosa.

## Interferencias causadas por la estación

**Compatibilidad electromagnética (EMC):** que un aparato funcione sin perturbar a otros (emisión) y sin ser perturbado por ellos (inmunidad).

| | Emisión no deseada | Sobrecarga por la fundamental |
|---|---|---|
| Qué ocurre | El transmisor emite armónicos o espurias | Una señal limpia y fuerte entra en un aparato mal protegido |
| Defecto técnico | En el transmisor | En el aparato afectado |
| Remedio | Filtro paso bajo, no saturar, reparar | Ferritas, filtros y blindaje en el aparato |
| Pista | Una frecuencia concreta, múltiplo de la de transmisión | Todo, o aparatos que no son receptores |

- En el aparato afectado, la sobrecarga se manifiesta como **bloqueo**, **intermodulación** o **detección** en circuitos de audio. La señal entra por la antena, por los demás cables o a través de la caja.
- Televisión digital: imagen pixelada, congelada o «sin señal». Si se pierde un solo múltiple cuya frecuencia es múltiplo de la de transmisión, armónico; si se pierden todos, sobrecarga.
- Diagnóstico: comprobar que coincide con las transmisiones; probar potencias (no distingue causas, pero da un remedio provisional); probar bandas; probar el filtro paso bajo; apuntar.
- Remedios: **filtrar** (ferritas junto al aparato afectado, contra la corriente de modo común; filtro paso alto en la antena del televisor; filtro de red; paso bajo en el transmisor), **desacoplar** (condensador a masa) y **apantallar** (envoltura metálica).
- En la estación: antena alta y lejos, balun, potencia justa.
- **Artículo 32 del reglamento:** si el personal de la Administración comprueba una interferencia perjudicial a un servicio autorizado o a la recepción de radiodifusión, el titular debe dejar de emitir y, siguiendo sus instrucciones y a su costa, aplicar las medidas técnicas razonables; las comunica formalmente y puede volver a emitir; si persiste, la Administración puede restringir bandas, potencia u horario. Ayudar al vecino sin esperar a eso es buena práctica.

## Interferencias que recibe la estación

- Lo que limita la escucha es el **ruido de fondo**, no el receptor. Cada 10 dB más de ruido exigen una señal diez veces más potente.
- Fuentes: fuentes conmutadas (cargadores, iluminación LED), motores, reguladores, instalaciones solares, PLC.
- Se reconoce porque tiene dibujo regular y horario.
- Localización, con un receptor de onda corta a pilas: primero el **interruptor general** de la propia vivienda (más de la mitad de las veces el ruido es propio); luego circuito a circuito; luego aparato a aparato, desenchufando.
- Remedios: sustituir el aparato, ferritas en sus cables, alejar la antena, buen coaxial y balun.
- Marco legal: los aparatos deben cumplir las normas de compatibilidad electromagnética (marcado CE); el aficionado tiene el deber de no causar interferencia perjudicial a otros servicios y puede reclamar protección en sus bandas, con el matiz de primario y secundario de la sección 12; el árbitro es la Administración de telecomunicaciones.

## Para el examen

- Voltímetro en paralelo y con resistencia interna muy alta; amperímetro en serie y muy baja; ohmímetro sin tensión.
- La forma de onda se ve en el osciloscopio; los armónicos, en el analizador de espectro.
- Medidor de ROE: intercalado en la línea. Carga artificial: 50 Ω que no radian.
- Diferencial: fugas a tierra de 30 mA. Magnetotérmico: sobrecargas y cortocircuitos.
- Condensadores cargados tras desenchufar.
- Tormenta: desconectar antenas y alejar cables.
- Armónico frente a sobrecarga por la fundamental; ferritas y filtro paso bajo.

## Para profundizar

- El documento de la IARU *Ética y procedimientos operativos para el radioaficionado* trata con buen criterio la actitud ante las interferencias.
- Busca «EMC for radio amateurs RSGB»: la sociedad británica de radioaficionados publica guías abiertas de diagnóstico y remedios.
- Un ejercicio que no requiere licencia: con una radio portátil de onda media, recorre tu casa acercándola a cargadores, routers y lámparas LED. Te dará el mapa de ruido de tu propia vivienda.
