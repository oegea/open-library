El lunes, Nadia le explicó a Víctor la simulación. Duró más de la hora prevista, porque Víctor era de los que preguntan hasta el fondo — de dónde salía cada dato, por qué barajar semanas y no promediarlas, qué pasaba con la curva si el equipo mejoraba — y al final se quedó mirando la gráfica con los brazos cruzados.

—¿Sabes lo que más me molesta de esto? —dijo—. Que tenemos telemetría de todo. Absolutamente de todo. Y nunca la usamos para nada que importe.

—Ya que lo dices… —Nadia llevaba días queriendo pedirlo y no sabía a quién—. ¿Puedo tener acceso de lectura a la telemetría de uso de Nido? La de producto, no la de sistemas.

Víctor se lo concedió con dos clics y una ceja levantada.

—¿Qué buscas?

—Todavía no lo sé. Eso es lo que quiero mirar.

---

Lo que encontró le quitó el sueño dos noches, y no en el sentido bueno.

Nido tenía ciento treinta y una pantallas. Nadia escribió un script que cruzaba los eventos de uso de los últimos seis meses con el inventario de funcionalidades, y ordenó el resultado. La cabeza de la lista era previsible: hoja de medicación, plan de cuidados, turnos, el portal de familias. Uso diario, intenso, de miles de personas. El cuerpo de la lista adelgazaba rápido. Y la cola de la lista era un cementerio.

Cuarenta y una pantallas — casi un tercio — con menos de diez usuarios únicos al mes. Módulos enteros que se habían anunciado en newsletters con signos de exclamación: el planificador de menús con control nutricional (196 residencias podían usarlo; lo usaban 9), el módulo de actividades con gamificación (usuarios activos: 7), la integración con pulseras de actividad que había costado un trimestre entero (usuarios activos: 0 — cero — desde hacía cuatro meses).

Y Atlas. El cuadro de mando predictivo, catorce meses de trabajo, el proyecto que había comprometido la fecha de marzo. Nadia miró tres veces la consulta porque pensó que había escrito mal el filtro.

Usuarios activos mensuales de Atlas: **4**.

Dos eran empleados de Aurelia. Uno era un consultor externo que hacía demos. El cuarto era un director de residencia de Albacete que entraba el último viernes de cada mes, miraba una pantalla durante unos noventa segundos y se iba.

Nadia se echó hacia atrás en la silla y oyó, sin querer, la voz de Marga en el all-hands de la semana anterior: «Cuarenta y cinco features entregadas este año. Nunca habíamos construido tanto.» Era verdad. Y allí estaban, en la telemetría, brillando en fila como una estantería de trofeos en una casa vacía.

Abrió el Cuaderno. Sabía exactamente qué capítulo tocaba, porque lo había dejado a medias como quien deja un caramelo:

> «Ahora viene la parte que duele. Cuando Microsoft empezó a medir con experimentos controlados el efecto real de sus ideas — ideas de gente lista, filtradas por comités de gente lista —, encontró que solo un tercio mejoraba las métricas que pretendía mejorar. Otro tercio no hacía nada. El último tercio empeoraba las cosas. Un tercio, un tercio, un tercio. Y Microsoft no es especial: en dominios maduros, la tasa de acierto baja aún más.
> Lee esa cifra otra vez y luego mira tu roadmap. Si está lleno de promesas con fecha y vacío de experimentos, no es un plan: es un billete de lotería con formato de Gantt. La pregunta correcta casi nunca es "¿cuándo estará la feature?". Es: "¿qué evidencia tenemos de que esta feature debería existir?"»

En el jardín, Nadia escribió: *Kohavi. Buscar el paper original del 1/3. Enseñarle la telemetría a Sofía antes que a nadie. Con cuidado: esto es dinamita.*

---

Era dinamita, y explotó en la reunión menos pensada: la revisión mensual de roadmap, con Marga presente.

Sofía había preparado el terreno con la prudencia de un artificiero — «datos de uso interesantes», «oportunidad de aprender» — pero cuando la lista apareció en pantalla, ordenada de más a menos, con la columna de usuarios activos en rojo hacia el final, el silencio duró lo que dura una mala noticia entrando en un cuerpo.

—Esos números no pueden estar bien —dijo Marga por fin—. El planificador de menús lo pidieron los clientes. Lo pidió Ondara, de hecho. Me acuerdo de la reunión.

—Lo pidieron —dijo Nadia, con el corazón a mil pero la voz firme, porque llevaba la respuesta preparada—. Y lo usamos para venderles la renovación de 2024. Pero pedir no es usar. Hay un estudio buenísimo de 1934, sale en el Cuaderno… — se frenó; demasiado, demasiado pronto—. Lo que quiero decir es que lo que la gente dice que quiere y lo que la gente hace son datos distintos. Y nosotros solo medimos el primero.

—El Cuaderno —repitió Marga, con un filo nuevo en la voz—. El manual ese de Lantana que anda circulando. ¿Ahora la estrategia de producto la marca la competencia?

—Ahora mismo —dijo Bruno, suave, sin levantar la vista— la estrategia de producto la marca una lista de cuarenta y dos features de las que, según esto, unas catorce van a acabar en el cementerio de las cuarenta y una. No lo dice Lantana. Lo dice nuestra propia telemetría, que llevaba dos años encendida sin que nadie la mirara.

Marga no contestó enseguida. Miró la lista entera, despacio, y Nadia — que esperaba furia — vio otra cosa: cansancio. El cansancio de alguien que llevaba años corriendo delante de un tren llamado «lo pide el mercado», y a la que acababan de enseñar una foto del tren vacío.

—¿Y qué proponéis? —dijo al fin—. ¿Que paremos de construir? Porque Ondara está a tres meses de decidir si se va, y os garantizo que no se queda por un experimento.

—Proponemos construir una cosa menos —dijo Sofía— y usar el hueco para comprobar una cosa más. Una. Como prueba del método.

---

La cosa a comprobar la eligió la propia Marga, con lógica impecable: la apuesta más cara del roadmap del trimestre siguiente. **Resúmenes semanales inteligentes**: un informe narrativo generado por IA para las familias de cada residente — «su madre ha participado esta semana en…» —, la feature estrella de la próxima renovación, tres meses de trabajo estimado (vieja escuela) para el Petirrojo y el equipo de plataforma.

—Si vuestro método sirve para algo —dijo Marga—, servirá para esto. Y si el experimento dice que sí, lo construís sin rechistar y llegamos a la feria del sector con ello.

—Y si dice que no —dijo Nadia—, nos hemos ahorrado tres meses.

—Si dice que no —dijo Marga— querré ver los datos con lupa.

El diseño del experimento se lo llevó Renata, la designer, que resultó llevar años pidiendo hacer exactamente esto y que desenterró de un cajón su formación en investigación de usuarios como quien desentierra una espada. Tres patas, una semana de trabajo total:

Primera: **entrevistas de verdad**. Ocho familias, seis gobernantas, remoto, preguntando por comportamiento pasado, no por deseos — no «¿le gustaría recibir un resumen semanal?» (a esa pregunta todo el mundo dice sí, explicó Renata: preguntar por intenciones infla las respuestas; hay hasta un factor medido) sino «enséñeme la última vez que quiso saber cómo estaba su padre; ¿qué hizo?».

Segunda: una **puerta pintada**. En el portal de familias, un botón nuevo: «Resumen semanal — próximamente». Medir cuántos lo pulsaban. Coste: una tarde.

Tercera: el **prototipo con las gobernantas**. Cuatro resúmenes de ejemplo generados con datos reales anonimizados, enseñados a quienes tendrían que revisarlos antes del envío. Porque alguien tendría que revisarlos, ¿verdad? Esa pregunta resultó ser la bisagra de todo.

Los resultados llegaron en doce días, y fueron los tres en la misma dirección, que no era la esperada por nadie del comité.

Las familias no querían un informe semanal: querían **señales de vida frecuentes**. Lo que hacían — telemetría de la puerta pintada aparte — era entrar al portal los martes y viernes por la tarde, mirar si había fotos nuevas de las actividades, y escribir por el chat preguntas de una línea. El botón del resumen lo pulsó un 11%, una vez, por curiosidad; las fotos las abría el 74% cada semana. «Un texto largo el domingo no me dice si mi madre sonríe», dijo una hija en la entrevista, y Renata puso la frase en la primera diapositiva.

Y las gobernantas — esto fue lo decisivo — leyeron los resúmenes generados y dijeron que ni hablar. No sin revisarlos frase a frase. «Aquí pone que participó activamente en el taller de memoria. Estuvo dormida. Si la familia lee esto y luego viene de visita, ¿quién da la cara? Yo.» Revisar veinte resúmenes semanales por planta era media jornada que no existía. La feature estrella, en producción real, habría sido o un generador de desconfianza o un generador de trabajo — probablemente ambos, en ese orden.

—O sea, que no —dijo Marga en la revisión, mirando los datos con la lupa prometida. Nadie habló—. ¿Sabéis cuánto le habíamos dicho al consejo que iba a aportar esto a la renovación? —Se frotó los ojos—. Tres meses de cuatro equipos. Lo teníamos en el roadmap con fecha y todo. Lo he presentado en dos comités como cosa hecha.

—Ya —dijo Sofía, con cuidado.

—Es lo más barato que hemos comprado este año —dijo Marga de pronto, y soltó una risa corta, sin alegría pero sin veneno—. Doce días y nos ahorra un trimestre de construir un problema. —Miró a Renata, luego a Nadia—. ¿Qué pedían las familias? ¿Fotos y chat? ¿Y qué pedía la lista de Encarna, la de los tres folios a mano? Porque me la sé de memoria y juraría que la mitad era de este tamaño.

—Hoja de medicación en letra grande para las rondas de noche —recitó Duna, que también se la sabía—. Que el parte de incidencias se pueda rellenar en treinta segundos desde el pasillo. Que el portal no cierre la sesión cada diez minutos, que las auxiliares van con guantes…

—Cosas pequeñas —dijo Marga, despacio, como si la palabra le supiera nueva—. Cosas pequeñas que se usan mil veces al día. —Se levantó, recogió su portátil, y en la puerta se giró—: Quiero un experimento por cada apuesta gorda del roadmap. Empezando por las tres de la renovación de Ondara. Y quiero que alguien me explique con calma lo del estudio ese de 1934.

Cuando salió, Bruno alzó las cejas por encima de las gafas.

—¿Qué acaba de pasar?

—Creo —dijo Sofía— que acabamos de matar nuestra primera feature antes de construirla. Y creo que a Marga le ha gustado más que a nosotros.

Esa noche, en el jardín: *Primera victoria del método. La puerta pintada costó una tarde y valía tres meses. Preguntar por comportamiento pasado, no por intenciones (buscar: LaPiere 1934, sesgo hipotético). Renata sabía hacer todo esto DESDE SIEMPRE y nadie se lo había pedido — ¿cuánta gente así tenemos escondida? Y una cosa más: Marga no era el enemigo. Era la persona con más miedo de la sala.*
