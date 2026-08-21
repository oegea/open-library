Fue Nadia quien lo dibujó, pero fue Aitor quien lo vio.

Septiembre, sala grande, el ejercicio que Víctor había encargado tras el postmortem: «entender por qué cambiar cualquier cosa transversal en Nido cuesta tanto». Nadia había preparado dos diagramas para la sesión. A la izquierda, el grafo de dependencias del monolito: los módulos de Nido como nodos, las llamadas entre ellos como aristas, el enredo de una década pintado por una herramienta de análisis estático. A la derecha, el organigrama de ingeniería de Aurelia: equipos, líneas de reporte, los canales por los que viajaban los tickets entre grupos.

Aitor se levantó, cogió un rotulador, y sin decir palabra — cómo no — trazó tres círculos en cada diagrama. Los mismos tres círculos.

—Es el mismo dibujo —dijo alguien del Grulla, despacio.

Lo era. El módulo de facturación, enmarañado consigo mismo y casi aislado del resto: el equipo de facturación, en su planta, con su jerga, famoso por responder tarde. Los tres módulos del área clínica, comunicados por un amasijo de llamadas cruzadas: los tres equipos que habían sido uno hasta la reorganización de 2023 y seguían compartiendo código, gente prestada y resentimientos. Y el agujero del centro: la capa de integraciones, tierra de nadie técnica — sin dueño desde hacía dos años — que casualmente era también el sitio del organigrama donde ningún equipo tenía la responsabilidad y por donde había reventado el incidente de julio.

—Hay una ley sobre esto —dijo Nadia, y ya nadie en Aurelia se reía cuando empezaba una frase así—. De 1968. Conway: las organizaciones producen diseños que copian su estructura de comunicación. Nido no está enredado por mala suerte: está enredado *con la forma exacta* de nuestras reuniones. El sistema es el espejo. —Pausa—. Y funciona en los dos sentidos. No puedes arreglar el código sin tocar el organigrama, porque el organigrama lo volverá a enredar. Pero si diseñas los equipos con la forma que quieres que tenga el sistema…

—…el sistema acaba saliendo con esa forma —terminó Víctor, mirando los círculos—. ¿Eso está comprobado o es una frase bonita?

—Está comprobado hasta donde estas cosas se comprueban: estudios de Harvard con pares de productos equivalentes, una revisión de 142 casos. Y el propio Conway lo mandó a Harvard Business Review en el 67 y se lo rechazaron por no poder demostrarlo. —Nadia sonrió—. Tardamos cincuenta años en darle los datos.

---

La reorganización de octubre fue la anti-polinización, y se diseñó con una regla que Sofía escribió en la primera página del documento: *«Primero decidimos qué flujo de valor debe existir; luego, qué equipo lo posee; el organigrama es la consecuencia, no el punto de partida.»*

Salieron cuatro equipos estables, cada uno dueño de un viaje completo del cliente, con nombre de lo que cuidaban y no de pájaro: **Ingreso** (todo lo que pasa desde que una familia llama hasta que el residente está instalado), **Cuidado diario** (medicación, planes, el carrito de Rosa), **Familias** (el portal, las fotos de los martes), y **Plataforma** — este último con un encargo peculiar: no poseer ningún viaje de cliente, sino hacer que los otros tres no necesitaran pensar en infraestructura, «reducir la carga cognitiva ajena» como misión escrita. La capa de integraciones — la tierra de nadie — dejó de ser de nadie.

No fue incruento. Hubo dos semanas de duelo de siglas, un conflicto serio sobre a qué equipo iba cada cual — resuelto con un mecanismo del Cuaderno: preferencias declaradas de las personas primero, necesidades del flujo después, y ni un solo movimiento decidido sin hablar con el afectado — y una discusión memorable cuando el CFO preguntó por qué los equipos nuevos «no estaban al cien por cien de asignación», que Sofía zanjó proyectando la curva de Kingman sin comentarios.

Y hubo una novedad estructural que pasó desapercibida fuera y lo cambió todo dentro: el documento de la reorganización incluía, por primera vez en la historia de Aurelia, **la definición del trabajo de Sofía**. Una página, título: «Qué cubre una Engineering Manager en Aurelia (y qué no)».

—Me pasé seis años haciendo este trabajo sin saber cuál era —le contó Sofía a Nadia, tomando el vermut de los viernes que se había vuelto costumbre—. Proxy de producto, secretaria de tickets, escudo antibalas, psicóloga sin título, scrum master en los ratos libres. Todo urgente, nada mío. El Cuaderno tiene un capítulo que me… bueno. Me vi. Dice: no preguntes qué *es* un EM, pregunta qué *funciones* necesita cubiertas una organización sana, y luego mira cuáles te tocan a ti y cuáles están sin dueño. — Contó con los dedos—: Que la estrategia llegue traducida al equipo y las dudas del equipo lleguen traducidas arriba: alineación. Que la gente crezca: desarrollo, one2ones de verdad — de los de escuchar, no de los de repasar el tablero —. Que el sistema de trabajo funcione: facilitación, quitar piedras. Y que las decisiones técnicas tengan criterio: eso NO me toca a mí, me toca vigilarlo con Bruno y con quien toque. En cuanto lo escribimos, vimos el agujero: en Aurelia, la función «desarrollo de personas» no la cubría nadie. Nadie. Teo preguntó seis meses por el módulo de medicación y su EM de entonces — yo — estaba demasiado ocupada haciendo de secretaria de tickets.

—¿Y ahora?

—Ahora tengo one2ones quincenales que son sagrados, una pregunta fija — «¿qué te está frenando y qué te está haciendo crecer?» — y prohibido usarlos para repasar el estado de nada. —Sofía miró su vaso—. ¿Sabes lo que me dijo Duna en el primero? Que en cuatro años nadie le había preguntado qué quería aprender. Cuatro años. La teníamos a un metro.

---

La otra herramienta de octubre fue un cuestionario de siete preguntas que Nadia sacó del Cuaderno y que produjo el número más comentado del trimestre.

Se llamaba tipología de Westrum, y no preguntaba por valores ni por satisfacción: preguntaba qué pasa en tu equipo con la información. *Cuando llegan malas noticias, ¿qué ocurre? Cuando alguien señala un problema, ¿se le trata como mensajero o como responsable? ¿La gente coopera entre áreas o defiende su parcela? ¿Los fallos llevan a indagación o a búsqueda de culpable?* Cada respuesta situaba al equipo en una de tres culturas: patológica (la información es poder y se esconde), burocrática (la información sigue el conducto reglamentario y se atasca en él) o generativa (la información fluye hacia quien la necesita).

Los resultados, anónimos y por equipo, se presentaron sin nombres en el all-hands de noviembre. La media de Aurelia salía «burocrática con episodios generativos» — nadie se sorprendió — pero el dato que hizo época fue otro: el contraste entre el equipo mejor y el peor era enorme, y el mejor era el heredero directo del Petirrojo. Víctor lo señaló en la diapositiva y dijo la frase que llevaba un año fermentando:

—Hace un año os habría dicho que la cultura era cosa de carteles y de valores en la pared. Lo que dice este cuestionario es otra cosa: la cultura es *lo que le pasa aquí a una mala noticia*. Y eso no se cambia con carteles. Se cambia como lo ha cambiado este equipo: con retros donde se puede hablar, postmortems sin culpa, datos que cualquiera puede mirar y fechas que se discuten con curvas. La buena noticia es que sabemos que se puede, porque lo hemos visto. La mala es que no hay atajo. — Miró la sala—. La consultora que quería venderos el «modelo Petirrojo» en diapositivas ya no viene, por cierto. Esto no se instala. Se cultiva.

---

El vermut de aquel viernes se alargó, y fue Bruno quien lo alargó, cosa rara. Estuvo un rato callado, girando el vaso, y luego dijo:

—El dibujo de Aitor. Los dos diagramas iguales. —Se puso las gafas, se las volvió a quitar—. Yo ya había visto ese dibujo. En 2019. Lo hizo la otra fundadora, en la pizarra de la sala grande, la semana de la reorganización de la discordia. Dijo casi lo mismo que tu Conway, con otras palabras: «si partimos los equipos por capas técnicas, el producto se partirá por capas técnicas, y el cliente no vive en capas». —Bebió—. Se llamaba Maia. Maia Ferrán. Llevaba el producto y la manera de trabajar; el otro llevaba el negocio y el crecimiento. Aquel año entró el fondo, y con el fondo las prisas, y hubo que elegir entre crecer ordenado o crecer rápido. Maia perdió la votación del consejo. Dimitió esa semana. — Miró a Nadia—. Y como en las empresas los que se van pierden también el relato, en la historia oficial pasó a ser «una fundadora que no supo escalar». La borraron de la web en la siguiente redada de marketing. Yo estaba en aquella pizarra, jardinera. Lo que tú llevas un año trayéndonos del Cuaderno ese… yo lo había oído casi todo antes, en esta casa, con la voz de Maia. Por eso me dolía tanto oírtelo. Y por eso te dejé seguir.

Nadia estuvo un rato sin decir nada. Luego, con cuidado, como quien mueve una pieza de museo:

—Bruno. El Cuaderno de Lantana lo firma «M.».

—Ya —dijo Bruno—. Ya lo sé, jardinera. —Se levantó y dejó una moneda en la mesa, su gesto de siempre para «la siguiente la pago yo»—. ¿Y sabes qué es lo que más rabia me da? Que no volvió para vengarse. Montó una empresa pequeña a veinte minutos de aquí, escribió todo lo que sabía en un cuaderno público con licencia libre, y esperó. Como quien planta una cosa y no le hace falta verla crecer. —Se puso el casco—. La semana que viene te cuento el resto. O mejor: la semana que viene igual te enseño cómo se le escribe.

En el jardín, esa noche, Nadia escribió una sola línea, y la subrayó dos veces:

*El sistema es el espejo. También el Cuaderno: llevábamos un año leyéndonos a nosotros mismos, escritos por alguien que se fue para poder escribirlo.*
