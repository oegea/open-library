La conversación que Sofía llevaba semanas aplazando ocurrió un martes a las cuatro, en la sala pequeña, y salió mal en menos de noventa segundos.

El tema era real y llevaba nombre en el registro nuevo de incidencias: de los últimos once parches con retrabajo, siete venían de PRs aprobados por Marc — aprobados en tandas, a máquina, con la diligencia entusiasta de quien confunde el botón verde con el progreso. Sofía había preparado la charla como le habían enseñado en el único curso de management que había recibido en su vida: técnica sándwich, empezar por lo positivo.

—Marc, eres de los que más aporta al equipo, de verdad, tu energía con los agentes es contagiosa. Pero tengo que decirte que últimamente estás siendo un poco descuidado con las reviews. Necesito que seas más riguroso. Tú vales mucho más que esto.

Lo que pasó en la cara de Marc fue una persiana bajando. Nadia — que estaba en la sala porque el tema tocaba al equipo entero — lo vio en directo: la sonrisa fija, los ojos yéndose a un punto de la mesa, y esa respuesta de manual que no responde a nada:

—Vale. Sí. Claro. Seré más riguroso.

Y durante el resto de la semana, Marc — el Marc que desde la visita a Miralbueno hacía preguntas nuevas — volvió al Marc antiguo, pero en versión defensiva: aprobaba menos PRs, tardaba más, y cada uno llevaba un comentario innecesariamente largo, como un descargo de responsabilidad. No estaba revisando mejor. Estaba protegiéndose.

—La he fastidiado, ¿verdad? —le dijo Sofía a Nadia el jueves—. Le he dicho exactamente lo que había que decirle y lo he empeorado.

—Le has dicho el *qué* sin el *dónde* —dijo Nadia, que llevaba días con el capítulo siete del Cuaderno abierto—. Y se lo has dicho a *él*, no a su trabajo. Mira, léete esto, porque a mí me ha reordenado la cabeza.

---

El capítulo se titulaba «El feedback es un misil que a veces vuelve», y empezaba con una cifra que parecía una errata:

> «En 1996, dos investigadores, Kluger y DeNisi, revisaron un siglo de estudios sobre feedback: 607 experimentos, veintitrés mil personas. Resultado medio: el feedback mejora el rendimiento. Resultado escondido en la media: en más de un tercio de los casos — el 38% — el feedback lo EMPEORÓ. No el feedback duro: el feedback en general. Elogios incluidos.
> Su explicación cabe en una regla: el efecto depende de a qué nivel dirige tu atención. Si el feedback apunta a la TAREA y al proceso ("este cálculo ignora el caso X; con este dato de entrada falla"), la atención va al trabajo y el trabajo mejora. Si apunta al YO ("eres brillante", "eres descuidado", "vales más que esto"), la atención va a defenderse, compararse, rumiar — y el trabajo empeora, porque la cabeza está en el juicio, no en la tarea. Los elogios a la persona no mejoran nada, y los rankings comparativos son de lo peor que se ha medido.
> Corolario incómodo: la mitad de lo que tu empresa llama "cultura de feedback" es maquinaria de apuntar al yo.»

Sofía leyó el paper original esa noche — le costó, era denso, lo leyó igual — y el viernes pidió a Marc otros quince minutos. Empezó distinto:

—Borra lo del martes. Lo hice mal: te hablé de ti y tenía que hablarte del trabajo. ¿Puedo probar otra vez? —Marc, desconcertado, asintió—. Once parches con retrabajo este mes. Siete salen de PRs de tandas de agentes aprobados en menos de cuatro minutos. Este de aquí — abrió el portátil, señaló — descartaba anotaciones clínicas en un caso raro, y el test que lo tenía que pillar era un test que el propio agente había escrito para su propio código. Quiero entender qué pasa en esos cuatro minutos y qué haría falta para que esto se cace antes. No es un juicio, es un problema de sistema: si tú no lo puedes cazar en cuatro minutos, nadie puede.

La conversación duró cincuenta minutos y fue, la contaría Sofía después, la mejor conversación técnica de su año. Porque Marc, con el misil apuntando a la tarea y no a él, resultó saber exactamente dónde dolía: que la cola de PRs de agentes era infinita y aprobar rápido era la única forma de que no se atascara todo; que los tests de los agentes se validaban a sí mismos; que él había propuesto en octubre un límite a la cola y nadie le había hecho caso. Salieron tres acciones concretas, una de ellas gorda — «los tests de un cambio de agente los escribe o los revisa un humano distinto del que aprueba el cambio» — y salió también otra cosa: la persiana subida.

En el jardín: *Mismo mensaje, otra diana, resultado opuesto. El feedback no es un contenido, es una dirección. Y lo del sándwich: el pan habla del yo. Por eso sabe raro.*

---

La retro de marzo — la segunda del formato nuevo — fue la primera a la que asistió Víctor.

Lo había pedido él, para sorpresa general, después de que el informe de la charla de Marc subiera por la cadena («¿cómo que un test del agente validaba al agente? ¿en cuántos equipos pasa esto?»). Sofía puso una condición que había sacado, cómo no, del Cuaderno: podía venir, pero con las reglas de todos — y la primera regla estaba impresa en un A4 pegado a la pared, una frase de un tal Norm Kerth que el Cuaderno llamaba «la Directiva Prima»:

*«Independientemente de lo que descubramos, entendemos y creemos sinceramente que cada uno hizo el mejor trabajo que pudo, dado lo que sabía en ese momento, sus habilidades y capacidades, los recursos disponibles y la situación que se daba.»*

—¿Y esto? —preguntó Víctor, leyéndolo desde la puerta—. ¿Amnistía general?

—No —dijo Sofía—. Es una hipótesis de trabajo. Si asumes que la gente hizo lo mejor que pudo con lo que había, entonces cuando algo sale mal la pregunta interesante deja de ser «quién» y pasa a ser «qué había»: qué información faltaba, qué presión sobraba, qué herramienta engañó. Si asumes lo contrario, la retro se convierte en un juicio, la gente se defiende, y te vas sin aprender nada. Lo hemos probado de las dos maneras, Víctor. Esta funciona.

La retro siguió el formato que Sofía ya manejaba con oficio: datos primero — el registro de incidencias del mes, la cola de PRs, el gráfico de retrabajo —, escritura en silencio, ronda. Y a la media hora, la conversación llegó al sitio al que llevaba meses sin llegar.

—A ver, es que todas las acciones que estamos proponiendo — más revisión, límites de cola, tests cruzados — van de lo mismo —dijo Bruno—. Van de frenar. Y me parecen bien. Pero nadie ha dicho la palabra que sobrevuela, así que la digo yo: velocity. Todo lo que ha salido este mes — las tandas de cuatro minutos, los tests del agente para el agente, el retrabajo — pasa porque el objetivo del programa Prometeo es multiplicar la velocidad de entrega. La gente no es tonta: optimiza lo que se le pide. ¿Queremos arreglar las goteras o queremos hablar de por qué llueve?

Silencio. Del bueno, esta vez: del que precede a las frases que cuestan.

—El objetivo lo puso el board —dijo Víctor, por fin—. Con mi apoyo. «Por cuatro» lo dije yo, de hecho. —Miró el A4 de la pared un momento—. Con lo que sabía en ese momento.

—¿Y qué sabemos ahora? —preguntó Sofía, con la neutralidad exacta de quien facilita.

—Ahora sé que cuatrocientos PRs semanales no me dicen nada de si Ondara renueva —dijo Víctor, lentamente, como quien pisa hielo—. Sé que tengo una empresa entera optimizando un número que elegí yo, y que el número no distingue entre avanzar y agitarse. Y sospecho — lo sospecho desde lo de la curvita, jardinera, no me mires así — que medir otra cosa nos cambiaría más que cualquier iniciativa. —Se levantó, sacó una foto del A4 de la pared con el móvil—. No prometo nada del board. Pero traedme una propuesta: qué mediríamos en lugar de qué. Y esta frase me la llevo.

Cuando salió, el equipo se quedó en un silencio distinto de todos los anteriores. Lo rompió Duna:

—¿Acabamos de hacer una retro sobre las retros del CTO?

—Técnicamente —dijo Nadia, mirando sus notas—, acabamos de subir un bucle. El Cuaderno lo llama de otra manera… —buscó la página— aprendizaje de doble bucle. El bucle simple corrige la acción: revisa mejor, frena la cola. El doble cuestiona la variable de arriba: por qué estamos midiendo esto, quién eligió este objetivo, qué pasaría si fuera otro. Dice que las organizaciones hacen el simple todo el rato y el doble casi nunca, porque el doble toca cosas de gente con despacho.

—El termostato —dijo Aitor, inesperadamente. Todos lo miraron—. Lo pone en ese capítulo. El bucle simple es el termostato que enciende la calefacción cuando hace frío. El doble es preguntarse quién fijó la temperatura y por qué. —Se encogió de hombros—. Me lo leí anoche. Está bien el Cuaderno ese.

Esa noche, el jardín ganó tres entradas. *Una: el feedback es una dirección, no un contenido — y ahora tengo el paper. Dos: la Directiva Prima no es buenismo, es una hipótesis que cambia qué pregunta haces. Tres: hoy el termostato ha preguntado por la temperatura. Víctor se ha llevado la foto. Veremos.*

Y una posdata, subrayada: *El Cuaderno cita el meta-análisis de los debriefs: los equipos que revisan de forma estructurada rinden ~20-25% más. Lo firma un tal Tannenbaum. Si esto es verdad, la retro no es la ceremonia prescindible de los viernes: es posiblemente la práctica con más evidencia de todas las que hacemos. Contárselo a Sofía con estas palabras exactas.*
