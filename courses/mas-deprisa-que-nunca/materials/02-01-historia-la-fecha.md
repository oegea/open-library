La reunión con el Grupo Ondara duró dos horas y once minutos, y Nadia no estaba invitada, pero en Aurelia las reuniones importantes tenían la propiedad física de filtrarse por las paredes.

La delegación de Ondara llegó un martes a las diez: la directora de operaciones, un responsable de sistemas con cara de haber dormido poco, y — esto sorprendió a todos — Encarna Millán, directora de la residencia Miralbueno, la más grande del grupo, que había pedido venir en persona. Por la parte de Aurelia: el CEO, Víctor, y Marga Estévez, CPO, con su roadmap impreso en A3 a color, cuarenta y dos features ordenadas en trimestres como un parte meteorológico del año entero.

Lo que se supo después, por fragmentos: que la directora de operaciones abrió con la frase que ya circulaba («Nido cada vez hace más cosas y cada vez nos sirve menos»); que Encarna puso sobre la mesa una lista de tres folios escrita a mano por sus gobernantas — cosas pequeñas, concretas, ninguna de las cuales estaba en el A3 —; que alguien de Ondara mencionó, como quien no quiere la cosa, que «otras plataformas» les habían contactado; y que en el momento crítico, con el contrato de renovación flotando sobre la mesa, Marga señaló la esquina superior derecha de su roadmap y dijo:

—Todo esto queda resuelto con Atlas. Cuadro de mando predictivo, alertas inteligentes, todo. Lo tendréis completo el quince de marzo.

Era 11 de noviembre.

—¿El quince de marzo? —preguntó la directora de operaciones.

—El quince de marzo —confirmó Marga.

En la sala, dijeron luego, Víctor asintió. En el equipo Petirrojo, que se enteró a las cuatro de la tarde por un mensaje de Sofía con el asunto «no os va a gustar», la reacción fue menos diplomática.

—¿Marzo? —Bruno se quitó las gafas, gesto que en él precedía a las grandes ocasiones—. ¿De qué año?

---

Atlas era el proyecto favorito de Víctor y la palabra maldita del Petirrojo. Un cuadro de mando predictivo para directores de residencia: ocupación proyectada, riesgos de dependencia creciente, previsión de plantilla. Llevaba catorce meses en desarrollo. Se había «terminado» dos veces — hubo tarta la primera — y las dos veces hubo que reabrirlo porque lo entregado no era lo que nadie necesitaba. Ahora «Atlas completo» significaba: el módulo de previsión de plantilla, la integración con los datos históricos de veintiocho residencias con veintiocho variantes de configuración, y un rediseño del panel que Renata, la designer, tenía a medias.

Sofía convocó al equipo para «dimensionar el compromiso». La palabra compromiso hizo un ruido raro en la sala.

—A ver —dijo Marc, compartiendo pantalla con el desparpajo de siempre—. Yo le he pedido una estimación al agente. Desglosa el trabajo en ciento doce tareas y dice que, con el nivel de paralelización actual, seis semanas. Mediados de enero. Sobra margen.

—El agente —dijo Bruno— también me desglosó en doce tareas la migración del módulo de facturación, ¿te acuerdas? Tres semanas, dijo. Fueron once. No porque programara lento, ojo. Programaba rapidísimo. Es que ocho de las once semanas se fueron en cosas que no estaban en el desglose: que si los datos históricos de Ondara venían en tres formatos, que si la validación clínica, que si el fleco del RGPD. Lo que no está en la lista es lo que te mata, chaval. Y lo que no está en la lista no está, precisamente, porque nadie lo sabe todavía.

—Algo habrá que decirle a dirección —dijo Sofía, con la voz de quien lleva el escudo—. ¿Qué les digo? ¿Cuál es la estimación del equipo?

Silencio. Y entonces Nadia, que llevaba dos noches leyendo el Cuaderno de a bordo, carraspeó y dijo la frase que había ensayado en el espejo:

—Creo que la pregunta está mal hecha. No deberíamos dar un número. Deberíamos dar una distribución.

---

El capítulo cuatro del Cuaderno se titulaba «Nunca prometas un punto; entrega una curva», y a Nadia le había volado la cabeza con suavidad, como hacen las ideas verdaderas.

> «Cuando alguien pregunta "¿cuándo estará?", pide un número. Pero tu incertidumbre no tiene forma de número: tiene forma de curva. Un proyecto no "dura 6 semanas"; dura "entre 4 y 14, con la joroba de la probabilidad hacia las 7". Darle a negocio el número 6 no es información: es una apuesta disfrazada de hecho. Hay dos maneras honestas de responder. La vista externa: mira cuánto duraron de verdad tus últimos veinte proyectos parecidos, no cuánto crees que durará este (tu historial sabe de ti más que tu optimismo; los psicólogos llaman a esto "reference class forecasting" y a tu optimismo, "planning fallacy": está medido — la gente estima 34 días y tarda 55, incluso conociendo su propio historial). Y la simulación: si tienes datos de cuánto tarda tu equipo por unidad de trabajo, no calcules el promedio; simula diez mil futuros posibles y mira la curva entera. Veinte líneas de código. Las regalamos en el apéndice.»

Las veinte líneas estaban, en efecto, en el apéndice. Nadia las adaptó esa noche. Sacó del sistema de tickets los últimos catorce meses del Petirrojo: cuántos ítems de trabajo real completaba el equipo por semana — no los de los agentes: los verificados, integrados, en producción sin reabrirse. La serie era humillantemente irregular: 9, 4, 11, 2 (la semana del incidente de agosto), 7, 6, 13, 3… Luego contó, con Bruno y Duna, el trabajo restante de «Atlas completo», troceado en ítems del mismo tamaño aproximado: salieron 74, «y los que aparecerán», dijo Duna, que llevaba la cuenta de todas las veces que Atlas había escupido trabajo imprevisto. Miraron el historial de los dos «Atlas terminado» anteriores: en ambos, el trabajo descubierto por el camino había añadido en torno a un 40%.

La simulación hacía lo obvio: barajar miles de veces las semanas históricas reales, sumar hasta cubrir el trabajo restante (con el descubrimiento del 40% metido como rango), y anotar en qué semana caía el final. Nadia la ejecutó y la curva apareció en su terminal como un pequeño veredicto en ASCII.

—El cincuenta por ciento de los futuros acaba antes del veintidós de abril —resumió, en la reunión del jueves, con la gráfica proyectada—. El ochenta y cinco por ciento, antes del veinte de mayo. El quince de marzo está… aquí. —Señaló la cola izquierda de la curva—. Percentil doce. Es decir: hay un ochenta y ocho por ciento de probabilidades de incumplir la fecha que hemos prometido. No porque el equipo sea lento. Porque la fecha se eligió sin mirar ningún dato.

Sofía miró la curva un rato largo.

—¿Y esto se lo puedo enseñar a Víctor?

—Hay más —dijo Nadia, y le brillaban los ojos porque llevaba dos días queriendo contar esto—. He encontrado una cosa. De 1970.

---

Lo había encontrado siguiendo las notas del Cuaderno, que en el capítulo de plazos citaba un paper con un comentario críptico: «El documento fundacional del desarrollo en cascada advierte contra el desarrollo en cascada. Casi nadie lo ha leído. Léelo.»

El paper se llamaba *Managing the Development of Large Software Systems*, firmado por un tal Winston W. Royce. Nadia lo encontró en PDF, un facsímil escaneado con la tipografía de máquina de escribir de la época. Allí estaba el famoso diagrama: requisitos → análisis → diseño → código → pruebas → operación, la cascada perfecta que ella había estudiado en la carrera como «el modelo tradicional». Y justo debajo del diagrama, una frase que nadie le había enseñado:

> «Creo en este concepto, pero la implementación descrita arriba es arriesgada e invita al fracaso.»

Siguió leyendo con la sensación de estar abriendo un correo del pasado dirigido exactamente a su empresa. Royce explicaba por qué: las pruebas llegan al final, y el final es el primer momento en que el sistema se *experimenta* en lugar de *analizarse*; si algo fundamental falla ahí, vuelves al principio, y «cabe esperar hasta un cien por cien de sobrecoste en plazo o presupuesto». Cincuenta y seis años antes de Atlas, con sus dos finales reabiertos y su 40% de trabajo descubierto tarde. Y las recomendaciones de Royce: documenta el diseño, planifica las pruebas, involucra al cliente formalmente en puntos tempranos — y una que parecía escrita con fosforito para Marga: **hazlo dos veces** — que lo que entregues al cliente sea, en realidad, la segunda versión, porque la primera siempre enseña cosas que ningún plan contenía.

—En mil novecientos setenta —le dijo a Bruno, enseñándole el PDF—. Ya lo sabían en mil novecientos setenta.

—Sabían más cosas —dijo Bruno, con una media sonrisa que Nadia no le conocía—. Busca el informe de la OTAN del sesenta y ocho. La primera conferencia de ingeniería del software de la historia. Doscientas páginas de gente muy seria descubriendo que el software no se deja fabricar como un puente. —Hizo una pausa y añadió, como quien enseña una cicatriz—: Yo iba a las reuniones de XP en 2003, ¿sabes? En un bar de Ruzafa. Éramos ocho. Todo esto que estás descubriendo tú ahora con tu curvita y tus PDFs… nosotros lo teníamos medio ganado. Y luego vinieron a vendérnoslo en diapositivas, con certificado incluido, y perdimos la parte que importaba.

—¿Qué parte?

Bruno se puso las gafas y volvió a su pantalla.

—Esa es una conversación para otro día, jardinera.

---

El viernes, Sofía hizo algo que no había hecho nunca: pidió quince minutos del comité de dirección y entró con dos diapositivas. La primera era la curva de Nadia, con tres flechas: *marzo (12%), abril (50%), mayo (85%)*. La segunda decía, en letra grande: «Propuesta: comprometer el percentil 85 con Ondara, y enseñarles la curva. Los tratamos como adultos.»

Salió veinte minutos después con cara de haber corrido cien kilómetros.

—¿Y bien? —preguntó todo el Petirrojo a la vez.

—Marga dice que un cliente no puede recibir una curva, que necesita una fecha. Víctor ha preguntado de dónde salían los datos y se ha quedado callado un rato largo, que en Víctor es buena señal. Y luego ha dicho una cosa interesante. —Sofía se dejó caer en la silla—. Ha dicho: «Si esta curva es verdad, el problema no es que el equipo estime mal. Es que llevamos años decidiendo fechas primero y preguntando después». Y Marga ha contestado que las fechas las pide el mercado. Y ahí lo han dejado, mirándose.

—¿Entonces? —dijo Duna.

—Entonces la fecha de marzo sigue en pie, de momento. Pero hemos plantado algo. —Sofía miró a Nadia—. Víctor quiere que le expliques la simulación el lunes. A solas. Trae la curvita.

Esa noche, Nadia actualizó el jardín: *Royce 1970 leído. Informe OTAN 1968: pendiente. Bruno estuvo en los meetups de XP y le duele algo de aquella época — investigar con delicadeza. La curva ha entrado en dirección. La fecha sigue viva, pero herida.*

Y debajo, la pregunta que el Cuaderno le había dejado clavada, en un capítulo cuyo título entendería del todo tres secciones más tarde:

*«Si dos de cada tres ideas no funcionan, ¿por qué tu roadmap está lleno de apuestas y no tiene un solo experimento?»*
