En el simulacro, Marina no tocó el micrófono. Su trabajo fue apuntar: cada mensaje «con su hora, su origen, su destino y su texto literal». Al final, el evaluador hojeó esas hojas y dijo que eran el mejor registro que había visto en todo el día.

Apuntar es la mitad callada de operar. Al terminar esta lección sabrás qué se anota de cada contacto y para qué, y convertir la hora de tu reloj a la que usa toda la radioafición.

## El libro de guardia

> **Libro de guardia** (en inglés, *log*): el registro de los contactos de una estación, uno por línea.

El nombre viene de las estaciones de barco, donde el operador «de guardia» anotaba todo lo que oía y transmitía. Hoy casi siempre es un programa de ordenador, pero una libreta sirve igual.

De cada contacto se apunta, como mínimo:

| Dato | Ejemplo | Para qué |
|---|---|---|
| Fecha | 14-9-2025 | Saber qué día fue |
| Hora (en UTC, ahora verás qué es) | 08:42 | Poder casar tu anotación con la de tu corresponsal |
| Frecuencia o banda | 7.130 kHz (40 m) | Dónde fue |
| Modo | SSB | Cómo fue |
| Indicativo del corresponsal | EA1XYZ | Con quién |
| Informe enviado | 59 | Lo que tú le diste |
| Informe recibido | 57 | Lo que te dio él |

Es la línea que habría escrito Vicente tras el contacto de la lección 1. Lo habitual es añadir el nombre, la ubicación y cualquier nota útil («dipolo, 100 W», «QSB fuerte», «quiere QSL»).

—¿Es obligatorio? —preguntó Marina.

—El reglamento vigente no obliga al aficionado a llevarlo. Lo lleva todo el mundo, por cuatro razones.

- **Es tu memoria.** Dentro de dos años Teresa te llamará por tu nombre, porque lo tiene apuntado. Queda mucho mejor si tú también.
- **Es la base de las confirmaciones y los diplomas**, que verás en la lección siguiente. Un contacto que no está anotado con su fecha y hora exactas no se puede confirmar.
- **Es tu defensa.** Si un vecino asegura que el martes a las nueve de la noche le estropeaste la televisión (las interferencias de la sección 10), tu libro dice si a esa hora estabas transmitiendo, en qué banda y con qué potencia. O que no estabas.
- **Es un cuaderno de laboratorio.** Con los informes de un año sabes qué bandas te funcionan a qué horas y si la antena nueva es mejor que la vieja.

Los programas de registro añaden comodidades: avisan de si ya has contactado antes con una estación, leen la frecuencia directamente del equipo y exportan los contactos en un formato común que entienden los demás programas y servicios. Los hay gratuitos y muy buenos. Una costumbre recomendable, uses el que uses: guardar copias.

## El problema de la hora

Un sábado de julio, Vicente habla desde Vallverd con una estación de Buenos Aires. Son las diez de la noche en Valencia y las cinco de la tarde en Argentina. Con una de Tokio, serían las cinco de la madrugada… del domingo.

Si cada uno apunta su hora local, el mismo contacto queda registrado a tres horas distintas y en dos fechas diferentes. Cuando quieran confirmarlo, no habrá manera de saber si hablan del mismo.

> **UTC** (*Tiempo Universal Coordinado*): la hora de referencia mundial, la misma en todo el planeta. Es, a efectos prácticos, la hora del meridiano de Greenwich, sin cambios de verano ni de invierno.

**En radioafición, todas las horas se apuntan y se dicen en UTC.** El contacto con Tokio tiene así una sola hora y una sola fecha en los dos libros.

Verás la hora UTC escrita de tres formas equivalentes: «20:00 UTC», «2000 UTC» (cuatro cifras seguidas, sin separador) y «2000Z». La Z es la letra con la que se designa esa hora en navegación, y como la Z en el alfabeto fonético es Zulu, mucha gente dice «hora zulú». Siempre en formato de 24 horas.

## Convertir la hora

España peninsular y Baleares van **por delante** de UTC:

| | Hora oficial peninsular | Para obtener UTC |
|---|---|---|
| Horario de invierno | UTC + 1 | **Resta 1 hora** |
| Horario de verano | UTC + 2 | **Resta 2 horas** |

Canarias va una hora por detrás de la península: en invierno coincide con UTC y en verano resta 1.

El horario de verano empieza el último domingo de marzo y acaba el último domingo de octubre. Si un día dudas, mira la hora UTC en cualquier web de hora oficial y compárala con tu reloj: la diferencia es lo que tienes que restar ese día.

**Ejemplo 1.** *Un 15 de enero, a las 19:30 de tu reloj en Valencia.* Invierno: restas 1. Son las **18:30 UTC**.

**Ejemplo 2.** *Un 15 de julio, a las 19:30.* Verano: restas 2. Son las **17:30 UTC**.

**Ejemplo 3, el que hace fallar.** *Un 15 de julio, a las 00:40 de la madrugada.* Verano: restas 2. Cuarenta minutos después de medianoche menos dos horas es antes de medianoche: son las **22:40 UTC… del día 14**.

> **Al restar, si cruzas la medianoche, la fecha UTC es la del día anterior.** Le ocurre a cualquier contacto hecho en la península antes de la 1 (en invierno) o de las 2 (en verano) de la madrugada.

![Dos relojes digitales comparados en tres situaciones. Primera fila, invierno: reloj local 19:30, reloj UTC 18:30, una hora menos. Segunda fila, verano: reloj local 19:30, reloj UTC 17:30, dos horas menos. Tercera fila, madrugada de verano: reloj local 00:40 del día 15, reloj UTC 22:40 del día 14, con el aviso de que cambia la fecha.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s11-hora-utc.svg)

El remedio de los veteranos es no hacer la cuenta nunca: tienen en la estación un reloj que marca siempre UTC, y los programas de registro la ponen solos. Aun así, la conversión es pregunta de examen y te hará falta para quedar con alguien: «nos vemos a las 18:00 UTC en 7.150» significa las siete de la tarde en invierno y las ocho en verano.

## Donde la gente se lía

- **Apuntar la hora del reloj de la pared.** Es el error más frecuente y el más difícil de arreglar después: meses de contactos con una o dos horas de desfase.
- **Restar bien la hora y olvidar la fecha.** Un contacto a las 00:40 de un día de verano pertenece, en UTC, al día anterior.
- **Sumar en vez de restar.** La península va *por delante* de UTC: nuestro reloj marca más. Para llegar a UTC se resta.
- **Apuntar el informe al revés.** En el libro van los dos: el que tú diste y el que te dieron. Si los cruzas, tu anotación no coincidirá con la de tu corresponsal.

## Compruébalo tú

1. Un 3 de diciembre haces un contacto a las 21:15 de tu reloj, en Valencia. ¿Qué hora y qué fecha apuntas?
2. Un 20 de agosto, a las 01:20 de la madrugada. ¿Qué hora y qué fecha apuntas?
3. Un 20 de marzo, a las 23:30. ¿Horario de invierno o de verano? ¿Qué apuntas?
4. Un amigo de Tenerife te propone contactar «a las 19:00 UTC» un día de febrero. ¿Qué hora será en tu reloj de Valencia? ¿Y en el suyo?
5. Escribe la línea del libro de guardia de EA1XYZ (Teresa) para el contacto de la lección 1, suponiendo que fue un 14 de septiembre a las 10:42, hora de Valencia.
6. Dos aficionados de la península comparan sus libros de un contacto hecho en verano. Uno apuntó 18:05 y el otro 20:05. ¿Quién se ha equivocado, y cómo lo sabes?
7. Un vecino te reclama por una interferencia «el jueves pasado a las diez de la noche». Tu libro de guardia dice que el último contacto del jueves fue a las 17:50 UTC. Era invierno. ¿Estabas transmitiendo a la hora de la queja?

**Soluciones**

1. Diciembre, horario de invierno: restas 1. **20:15 UTC del 3 de diciembre.**
2. Agosto, horario de verano: restas 2. 01:20 menos dos horas cruza la medianoche: **23:20 UTC del 19 de agosto.**
3. El último domingo de marzo cae siempre entre el 25 y el 31: el 20 todavía es **invierno**. Restas 1: **22:30 UTC del 20 de marzo**.
4. Febrero, invierno: la península es UTC + 1, así que en Valencia serán las **20:00**. Canarias en invierno coincide con UTC: en Tenerife, las **19:00**.
5. Septiembre es horario de verano: 10:42 − 2 = 08:42 UTC. Línea de Teresa: *14-9 · 08:42 UTC · 7.130 kHz · SSB · EA5RKV · enviado 57 · recibido 59 · Vicente, Vallverd (Valencia)*. Fíjate en que sus informes van al revés que en el libro de Vicente: ella envió el 57 y recibió el 59.
6. En verano la península va dos horas por delante de UTC, y las dos anotaciones difieren justo en dos horas: el que apuntó 20:05 puso su hora local. El correcto es 18:05.
7. Las diez de la noche en invierno son las 21:00 UTC. Tu último contacto fue a las 17:50 UTC (las 18:50 locales), más de tres horas antes. Según tu libro, **no estabas transmitiendo**: un dato muy útil para buscar la causa en otra parte.

## En una frase

De cada contacto se apuntan fecha, hora, frecuencia, modo, indicativo e informes, siempre en hora UTC (en la península, una hora menos en invierno y dos en verano, vigilando la fecha de madrugada), porque es lo único que permite casar tu libro con el de tu corresponsal.

Y casar los dos libros sirve para algo concreto: confirmar que el contacto existió. De eso, y de cómo decir dónde estás en seis caracteres, trata la lección siguiente.
