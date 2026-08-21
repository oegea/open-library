El peligro llegó disfrazado de homenaje, como llegan los peligros listos.

Se llamaba «Manual de Operativa Aurelia v1.0» y lo propuso, con la mejor intención del mundo, el nuevo director de operaciones: consolidar todo lo aprendido aquel año — las retros con datos, los límites de WIP, los postmortems, las curvas, los experimentos — en un manual corporativo **obligatorio**, con auditorías trimestrales de cumplimiento y una formación certificada interna «para garantizar la adopción homogénea». Adjuntaba, de una consultora, un presupuesto para «acompañar el despliegue», con un framework registrado cuyo nombre Bruno se negó a pronunciar («si lo dices tres veces aparece un consultor con certificaciones»).

—A ver si lo entiendo —dijo Bruno en la reunión donde se presentó, con la calma peligrosa de sus grandes tardes—. Nos ha ido bien haciendo exactamente lo contrario de esto — equipos decidiendo su forma de trabajar, reglas que cambian cuando los datos lo piden, cero liturgia impuesta — ¿y la conclusión es *congelarlo* en un PDF y mandar auditores? — Se quitó las gafas—. Yo esto ya lo he vivido dos veces. Se llama «institucionalizar el éxito» y es el certificado de defunción del éxito. La primera vez fue con el agile: primero el manifiesto, cuatro valores en una página; y detrás, década y pico mediante, vino la industria — certificaciones, frameworks de dieciocho roles, auditores del sprint —, y los propios firmantes del manifiesto acabaron renegando en público. Uno dijo que la palabra «agile» ya no significaba nada. Otro directamente pidió a los desarrolladores que la abandonaran. Y no eran cuñados: eran los fundadores. —Volvió a ponerse las gafas—. El manual no es el problema. El *obligatorio* es el problema. En el momento en que la práctica se separa de su porqué y se convierte en norma auditable, tienes cargo cult con presupuesto.

—¿Y qué alternativa hay? —preguntó el director de operaciones, sinceramente—. Porque «que cada equipo haga lo que quiera» tampoco escala. Hay equipos nuevos que necesitan de dónde partir. Hay mínimos — el postmortem, el presupuesto de error — que no pueden ser opcionales.

Y ahí, por primera vez en una reunión de dirección, Nadia abrió el Cuaderno en el proyector. El capítulo se llamaba «Cómo se gobierna esto (o: lo que aprendimos de una politóloga que estudiaba acequias)».

> «Toda comunidad que comparte un recurso — pastos, acequias, un codebase, una forma de trabajar — enfrenta el mismo problema: ¿cómo mantener reglas comunes sin un jefe que las imponga ni un caos que las disuelva? Durante décadas, la teoría decía que solo había dos salidas: privatizar o mandar. Una investigadora llamada Elinor Ostrom se dedicó a mirar la realidad — regantes valencianos incluidos, buscad "Tribunal de las Aguas" — y encontró la tercera: comunidades que se autogobiernan con éxito durante siglos. Y encontró que las que sobreviven comparten unos principios de diseño. Le dieron el Nobel de Economía por esto, la primera mujer en recibirlo.
> Nosotros gobernamos este cuaderno — y nuestra forma de trabajar — con esos principios. Las reglas las escriben quienes las cumplen y se cambian por procedimientos que cualquiera puede iniciar. Todo es transparente: quien monitorea el cumplimiento es la propia comunidad, no un auditor externo. Las sanciones son graduadas y empiezan por una conversación. Hay un sitio barato y rápido donde resolver los conflictos. Y cada equipo puede adaptar — bifurcar — lo que necesite, con una condición: contar qué cambió y por qué, para que el común aprenda. Si esto os suena al software libre, no es casualidad: el open source lleva treinta años siendo el mayor experimento de gobierno de comunes intelectuales de la historia. Funciona. Está documentado. Copiadle la gobernanza, no solo el código.»

—Lo que proponemos —dijo Sofía— es un Cuaderno de Aurelia. Público dentro de la empresa, versionado como el código, con dueños que son todos. Los mínimos innegociables existen — postmortem, presupuesto de error, seguridad de datos — pero son pocos, están justificados con su porqué, y hasta ellos tienen procedimiento de cambio. Todo lo demás son **prácticas por defecto**: el equipo nuevo parte de ahí; el equipo veterano adapta, documentando qué y por qué. Sin auditores. Con algo mejor que auditores: transparencia. Cualquiera puede ver qué hace cada equipo y qué resultados tiene. La presión buena, la de los pares mirando, no la del inspector.

—¿Y la consultora? —preguntó alguien.

—La consultora —dijo Víctor, que llevaba un rato hojeando el presupuesto adjunto— cobra ciento veinte mil euros por instalarnos un framework cuyo contenido no podemos ni reproducir sin permiso escrito. Mientras que el manual del que esta gente lleva un año aprendiendo — señaló el Cuaderno proyectado — es de la competencia, es gratis, y tiene una licencia que nos deja copiarlo, adaptarlo y hasta contribuirle. —Cerró la carpeta—. Como experimento de esta sección me parece redondo: una forma de trabajar que se vende cara y cerrada contra una que se regala abierta y funciona. Votemos.

El Manual v1.0 murió en esa sala. El Cuaderno de Aurelia nació esa semana, en un repositorio interno, con un primer commit que Sofía redactó y que empezaba: «Estas reglas las escriben quienes las cumplen».

---

Lo del patch fue idea de Duna, y nació de una deuda.

—Llevamos un año sacando de ahí —dijo en la última retro de noviembre, señalando la pestaña eterna del Cuaderno de Lantana—. La licencia dice que podemos usarlo, y lo hemos exprimido. Pero es de doble sentido, ¿no? Compartir-igual. Nosotros hemos aprendido cosas que ahí no están. Lo del Becario Fantasma, por ejemplo: el test de auditar métricas con un agente sin propósito. Eso no lo tienen. —Se encogió de hombros—. Deberíamos devolverlo. Es de justicia, y además quiero ver qué pasa.

Lo que pasó fue esto. Nadia preparó la contribución con el esmero de quien manda una sonda a otro planeta: un apéndice para el capítulo de métricas del Cuaderno de Lantana, titulado «El test del becario fantasma», con la historia anonimizada del IPA, el método, el código de la simulación y las referencias en el formato de la casa. Lo envió por el procedimiento público del repositorio del Cuaderno, un viernes por la tarde.

El lunes a las 8:40 había respuesta. La propuesta estaba **aceptada e integrada**, con un comentario público firmado por M.:

> «Apéndice aceptado con gratitud y una sola edición (os he quitado dos adverbios; ocupaban sitio). El test es excelente y el nombre, mejor. Me recuerda a un dashboard que vi nacer hace años — entonces no lo llamamos becario fantasma; lo llamamos "el sistema de incentivos", y tardamos mucho más que vosotros en matarlo, porque no teníamos la regla de que las medidas se auditan como se audita el código.
> Por lo demás: llevo un año siguiendo con interés los cambios en cierta empresa que conozco bien. Se nota desde fuera, ¿sabéis? Se nota en cómo responde vuestro soporte, en lo que cuentan las gobernantas cuando coincidimos en el sector, en un postmortem que circuló y que estuvo entre lo más honesto que he leído este año. Sea quien sea la gente que está empujando eso ahí dentro: buen trabajo. El cuaderno es vuestro también. Siempre lo fue un poco. — M.»

Nadia leyó el comentario tres veces. Después cogió el teléfono y bajó a la mesa de Bruno, que ya lo estaba leyendo, con una expresión que ella no le había visto nunca: la sonrisa entera, sin ironía, de un hombre al que le devuelven algo.

—«Siempre lo fue un poco» —leyó Bruno en voz alta—. Será cabezota. —Se quitó las gafas, y esta vez no era para limpiarlas—. Es ella, jardinera. Lo sabes desde hace meses. Maia Ferrán. La pizarra del 2019, el Tribunal de las Aguas — eso lo contaba ella, su familia era de la huerta —, hasta lo de quitar adverbios. Es ella entera.

—¿Y ahora qué? —dijo Nadia—. ¿Le escribo? ¿Le escribes tú? ¿Qué se le dice a…?

—Se le dice la verdad —dijo Bruno—. Que su cuaderno encontró el camino de vuelta a casa. Y que hay una cría de veintisiete años que lleva un año replantándole la huerta a su empresa vieja con las semillas que ella dejó en abierto, y que a esa cría le debemos todos una, y que si tiene una tarde, hay mucha gente aquí que querría… — se le fue la voz un momento, y lo arregló con su tono de siempre—: que querría hacerle unas preguntas técnicas. Muchas. Con vermut.

Esa noche, el jardín recibió la entrada más corta de su historia:

*Le he escrito. Asunto: «Su cuaderno. Nuestro año. ¿Un vermut?». Ha contestado en once minutos. Dice que sí. Dice que el patio de Lantana tiene limonero y que los viernes a las seis es la mejor hora. Dice — cito — «trae al de los teclados, si quiere; dile que el mío sigue siendo mejor que el suyo».*

*PD: El Cuaderno de Aurelia, commit inicial, ya tiene su primera regla bifurcada: hemos adaptado el formato de retro al nuestro. Documentado el qué y el porqué, como manda el común. Me ha costado no ponerle adverbios.*
