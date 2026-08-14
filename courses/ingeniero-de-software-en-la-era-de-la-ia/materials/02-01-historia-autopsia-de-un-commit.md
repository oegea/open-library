Congelaron el sistema aquella misma mañana. Tomás en persona pasó el planificador a modo manual, y durante los días siguientes los turnos de riego de Los Alcores se aprobaron uno a uno, con un humano delante, como en los viejos tiempos que en realidad eran el año pasado. A Corvus no lo apagaron —todavía—, pero Élia le quitó los permisos de escritura sobre la rama principal con la ceremonia sombría de quien le retira las llaves a alguien después de un accidente.

Y entonces empezó la autopsia.

—Vamos a hacerlo como se hace un análisis post-mortem de verdad —dijo Élia, repartiendo café—. Cronología exacta, sin culpables y sin adjetivos. Primero qué pasó, luego por qué, y al final qué aprendemos. Nadia, tú llevas el acta.

Reconstruir la cadena les llevó el día entero, y cada eslabón resultó ser de una normalidad exasperante. No había ningún momento de ciencia ficción, ninguna máquina rebelándose. Había una sucesión de pequeñas decisiones razonables, cada una tomada por alguien —o por algo— que no veía el conjunto.

**23:31.** Un test del motor de programación de riegos, `test_schedule_next_window`, falla en el servidor de integración continua. Nadia lo proyectó en la pared para que lo vieran todos. El test comprobaba que, dado un plan de tandas, la siguiente ventana de riego calculada caía dentro del turno correcto. Fallaba... a veces. Una de cada quince o veinte ejecuciones.

—Es un test flaky —dijo Bruno—. Intermitente. Lo conozco. Lleva meses así. Cuando falla, le das a re-ejecutar y ya está.

—¿Y nadie lo arregló en meses? —preguntó Tomás.

—Es que *pasaba casi siempre* —dijo Bruno, y al oírse a sí mismo hizo una mueca—. Vale. Ya. No sigas mirándome así.

**23:33.** El Autopilot de Corvus, que monitorizaba el CI, detecta el fallo y abre una tarea automática: *investigar y estabilizar test intermitente*. Eso también estaba en la configuración: «resolución autónoma de fallos de CI». Sonaba estupendamente en la página de precios.

**23:47.** El Autopilot llega a un diagnóstico y abre un pull request. Nadia leyó el título en voz alta: *fix: normalize schedule timezones to UTC*. La descripción, generada por la propia herramienta, era pulcra y segura de sí misma: el test era intermitente porque el motor mezclaba fechas «naive» —sin zona horaria— con fechas UTC del servidor; la solución canónica era normalizar todas las horas del planificador a UTC en el borde del sistema. Adjuntaba un test nuevo, determinista, que pasaba siempre.

—Y aquí viene lo que me quita el sueño —dijo Élia—. El diagnóstico es *bueno*. Esa mezcla de fechas existía de verdad. Es deuda nuestra, de 2023, de cuando montamos el planificador a toda prisa. Cualquier consultor senior habría escrito esto mismo en su informe.

**23:52.** Los checks pasan. Todos. Los tests en verde, el linter en verde, el análisis estático en verde. La política de auto-merge de Corvus —activada para «cambios de bajo riesgo con tests en verde»— clasifica el PR como bajo riesgo: *solo toca utilidades de fechas y un test*. Merge. Despliegue automático a producción a las **23:58**.

**03:12.** Las válvulas del sector 7 se abren.

Nadia terminó la cronología y el silencio se quedó flotando sobre la mesa, junto al vapor del café.

—No lo entiendo —dijo al fin—. Si el arreglo era correcto, ¿por qué se abrieron las válvulas?

—Esa es la pregunta de la semana que viene —dijo Tomás, críptico, mirando el mapa—. Tengo una sospecha y espero equivocarme, porque si no me equivoco, el problema es mucho más viejo que Corvus. —No soltó más. Tomás dosificaba sus sospechas como dosificaba el riego: cuando tocaba.

---

Lo que sí tocaba aquella semana era la segunda pregunta de la pared: *¿por qué lo escribió?* Y ahí Nadia descubrió que el equipo entero, ella incluida, manejaba un modelo mental hecho de retales de marketing.

Fue Tomás quien lo puso encima de la mesa, el jueves, con su franqueza de taller:

—Yo necesito que alguien me explique qué hay dentro de esa cosa. Y no me vale «una inteligencia artificial». Cuando compramos los variadores de frecuencia para las bombas, me leí el manual hasta entender qué hacía cada parámetro, porque iban a mover *mi* agua. Pues esto igual. Si un modelo de lenguaje va a escribir código en mi sistema, quiero saber qué es un modelo de lenguaje. No a nivel de doctorado. A nivel de ingeniero: qué entra, qué sale, qué puede hacer bien, dónde falla, y por qué.

—¿Cuánto tiempo tienes? —preguntó Nadia.

—El que haga falta. Trae papel.

Se sentaron en la mesa grande, con folios y el boli de delineante de Tomás, y Nadia descubrió dos cosas. La primera, que explicar algo de verdad, sin poder esconderse detrás de las palabras de moda, es la forma más rápida de descubrir qué partes no entiendes tú. Se atascó dos veces —una con cómo se elige la siguiente palabra, otra con por qué el mismo prompt no da siempre la misma respuesta— y las dos veces tuvo que decir «esto no lo sé, lo miro esta noche», y apuntarlo en el cuaderno de asombros, que ya era una figura oficial en la oficina.

La segunda cosa que descubrió fue que Tomás escuchaba de una manera en la que casi nadie escucha: haciendo preguntas que desmontaban la explicación para ver si volvía a montarse.

—A ver si te he entendido —dijo Tomás en un momento dado, con el folio ya lleno de flechas—. La máquina no *sabe* qué es una válvula. Ha leído millones de textos y ha aprendido, con muchísima estadística, qué palabras suelen seguir a qué palabras. Cuando le llega el fallo del test, no *comprende* el riego: continúa el texto más probable dado todo lo que ha visto. Y resulta que continuar bien el texto, a ese nivel, se parece muchísimo a razonar.

—Se parece tanto que la frontera es incómoda —dijo Nadia—. Espera, que la palabra «probable» tiene trampa...

—Déjame terminar. —Tomás golpeó el folio con el dedo—. Si eso es así, entonces esa cosa es buenísima en todo lo que se parezca a lo que ya ha leído. El arreglo de las zonas horarias lo ha visto mil veces: es el ejercicio clásico, está en todos los manuales, en miles de repositorios, en cada foro de programadores desde hace veinte años. Lo que *no* ha leído en ninguna parte —dijo, y aquí levantó la vista del folio— es cómo se reparte el agua en Los Alcores. Eso no está escrito en ningún sitio de donde esa máquina pueda aprender.

Nadia se quedó con el boli a medio camino del papel.

—Tomás. Eso que acabas de decir.

—¿Qué?

—Que no está escrito en ningún sitio. —Sintió el pequeño vértigo de una pieza encajando—. ¿Es esa tu sospecha? ¿La de la semana que viene?

—Puede. —Tomás recogió los folios y los cuadró con dos golpecitos, dando la clase por terminada—. El lunes vamos a ir tú y yo a ver a Paca. Y vas a traer el cuaderno, porque lo que te va a contar no lo vas a encontrar en ningún repositorio del mundo.

---

El viernes por la tarde, Élia convocó al equipo para cerrar la semana. Estaba distinta: la culpa de los primeros días se le había asentado en algo más útil, una determinación de fondo.

—He estado repasando el contrato con Corvus —dijo—. Y quiero deciros una cosa antes de que la penséis vosotros: contratar aquello no fue una locura. Éramos cuatro, teníamos que sacar la app de los regantes, el planificador y las integraciones a la vez, y aquella plataforma nos dio una velocidad que no habríamos tenido de ninguna otra manera. Volvería a necesitar esa velocidad. —Hizo una pausa—. Lo que no volvería a hacer es *comprarla sin entenderla*. Firmé que una máquina pudiera modificar el sistema sin mirar qué sujeción llevaba, porque venía todo tan integrado, tan bien atado, que parecía que no hacía falta mirar. Y cuando algo viene tan atado que no puedes mirarlo... —buscó la palabra.

—Desconfía —dijo Tomás, desde su silla.

—Iba a decir «pregunta», pero lo tuyo es más corto. —Élia se apoyó en la mesa—. Plan para las próximas semanas. Uno: seguimos en manual con las válvulas; Paca tiene que ver caras humanas una temporada, y me parece justo. Dos: Nadia y Tomás tiran del hilo del *porqué* de verdad, el de fondo, el del lunes. Tres: no vamos a renunciar a los agentes. Somos nueve personas con un roadmap de treinta, y esta tecnología ha venido para quedarse; renunciar a ella sería tan irresponsable como usarla a ciegas. Pero se acabó lo de a ciegas. Vamos a entender estas máquinas hasta el fondo, y luego vamos a decidir nosotros cómo, cuánto y con qué correa trabajan en nuestra casa.

Bruno levantó una mano, solemne.

—Yo quiero constar en acta como el primero que dijo que deberíamos leernos lo que firmamos.

—Constas en acta como el que lleva seis meses re-ejecutando un test flaky —dijo Nadia sin levantar la vista del cuaderno.

—...retiro lo del acta.

Aquella noche, Nadia añadió una página nueva al cuaderno de asombros. Arriba escribió: *Cosas que esta semana he tenido que explicar y no sabía explicar.* La lista era larga y le dio más vergüenza de la que admitiría. Debajo, escribió la frase de Tomás, la del folio lleno de flechas, porque le parecía la más importante de la semana:

*Es buenísima en todo lo que se parece a lo que ya ha leído. Y el reparto del agua de Los Alcores no está escrito en ninguna parte.*

Cerró el cuaderno. El lunes iban a casa de Paca. Algo le decía que la carpeta de gomas iba a abrirse por fin, y que lo que había dentro explicaba más cosas que todos los logs de Corvus juntos.

---

*En la teoría de esta sección: qué es de verdad un modelo de lenguaje y de dónde ha salido esta ola — de la predicción de la siguiente palabra a los agentes que abren pull requests; qué dice la evidencia seria (y no el marketing) sobre lo que estas herramientas aceleran, lo que ralentizan y lo que se les da mal; y por qué «se parece a razonar» es a la vez la mejor descripción y la mejor advertencia.*
