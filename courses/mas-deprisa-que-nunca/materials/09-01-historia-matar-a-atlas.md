El quince de marzo llegó y pasó, y no se pareció a ninguna de las dos catástrofes previstas.

No hubo Atlas completo — la curva de Nadia lo había dicho en noviembre y las curvas no negocian —, pero tampoco hubo cliente furioso, porque para marzo la relación con Ondara ya era otra cosa. Los meses de experimentos habían hecho su trabajo silencioso: la lista de Encarna convertida en mejoras que las gobernantas notaban cada mañana, el modo quiosco, el parte de treinta segundos, las fotos que las familias abrían los martes. En la reunión de marzo, Marga llevó — por primera vez en su vida, confesaría después — una presentación sin roadmap: llevó los datos de uso de lo entregado y a Rosa en una videollamada de diez minutos contando lo de los cuatro segundos. La directora de operaciones de Ondara escuchó, miró los datos y dijo la frase que en Aurelia enmarcarían: «Esto es lo primero que nos enseñáis en dos años que va de nuestro trabajo y no del vuestro.» La renovación — tres años — quedó encarrilada esa mañana y se firmó en mayo. Atlas ni se mencionó.

Y ese era, precisamente, el problema. Atlas seguía ahí.

Veinte meses ya. «Terminado» dos veces. Cuatro usuarios — los mismos cuatro; Nadia comprobaba la telemetría cada mes con una mezcla de morbo y pena —. Y en la planificación del tercer trimestre, como cada trimestre, Atlas reclamaba su porción: la integración con el histórico completo, «la fase que le falta para despegar». Nadie la defendía con entusiasmo. Nadie la atacaba tampoco. Los proyectos zombis no necesitan defensores: les basta con la inercia y con una frase — Nadia la había oído ya en tres reuniones distintas, dicha por tres personas distintas con idéntico tono razonable:

*«A estas alturas, con todo lo que llevamos invertido…»*

El Cuaderno tenía un capítulo entero sobre esa frase. Se titulaba «El dinero de ayer no vota», y Nadia lo había subrayado hasta estropearlo:

> «Lo invertido está invertido: no vuelve, hagas lo que hagas. La única pregunta racional ante un proyecto es hacia delante: con lo que sabemos HOY, ¿esta siguiente inversión es la mejor que podemos hacer? Si la respuesta es no, cada euro adicional no honra a los anteriores: los acompaña. Esto lo sabe todo el mundo y no lo aplica casi nadie, porque quien decidió la inversión original está en la sala, y matar el proyecto se siente como matar su juicio. Hay ciencia sobre esto — se llama escalada de compromiso, y el hallazgo clave es que quien más refuerza una apuesta que va mal es precisamente quien la eligió —. Y hay antídotos con evidencia: decide ANTES los criterios de parada, y que evalúe la continuidad alguien distinto de quien propuso. No porque el proponente sea tonto. Porque es humano.»

—El problema —dijo Sofía, cuando el Petirrojo preparaba la planificación— es que «quien la eligió» es Víctor. Y una cosa es que Víctor acepte gráficas del equipo, y otra es que el equipo le mate el proyecto al CTO delante del comité.

—Por eso no vamos a matarlo nosotros —dijo Nadia—. Vamos a montar la estructura donde pueda morirse solo. El Cuaderno trae el formato exacto. Se llama premortem.

---

La sesión de planificación del Q3 empezó de una manera que descolocó a todos los asistentes menos a los cinco que la habían tramado.

—Antes de repartir nada —anunció Sofía, con Víctor, Marga y los leads de tres equipos en la sala— vamos a hacer un ejercicio de veinte minutos. Es septiembre. El trimestre ha terminado y ha sido **un desastre**. No un desastre genérico: el peor trimestre de la historia de Aurelia. Cada uno, en silencio, escribid la historia: qué pasó, por qué, en qué orden. Sed concretos. Tenéis ocho minutos.

—¿Esto no es un poco derrotista? —preguntó el lead del Grulla.

—Al contrario. Imaginarse el fracaso como *ya ocurrido* saca a la luz cosas que la pregunta «¿qué podría salir mal?» no saca. Hay un estudio de los ochenta: la gente genera muchas más razones, y más concretas, cuando el resultado se da por cierto. Es un truco para desactivar el optimismo obligatorio de las planificaciones. Ocho minutos. Escribid.

El silencio de bolígrafos duró lo suyo. Luego, la ronda — los nuevos primero, la costumbre ya instaurada — y las historias de desastre empezaron a caer sobre la mesa. Y con ellas, como el Cuaderno prometía, la información que nadie había pedido nunca.

Paula: «El desastre empezó cuando la integración del histórico de Atlas se comió el trimestre: los datos de las 28 residencias tienen veintiocho esquemas, lo sé porque migré tres en mi época del Jilguero y cada una fue un mes.» Nadie sabía que Paula había hecho esas migraciones. El lead del Grulla: «Para mí empezó cuando volvimos a prometer fecha a Ondara sin curva.» Y Duna — Duna, que llevaba meses con aquello en el buche esperando exactamente esta pregunta —: «El mío es más simple. En septiembre descubrimos que Atlas nunca tuvo mercado. Lo digo con datos: tengo el registro de los cuatro usuarios de los últimos doce meses. El de Albacete entra el último viernes de mes, noventa segundos, una pantalla: exporta un número para un informe que le pide su gestoría. Eso es Atlas. Veinte meses de cuatro equipos para el informe de una gestoría. Los datos los tengo desde febrero. No los había enseñado enteros porque… —miró a Víctor, y decidió terminar la frase— porque nadie con capacidad de decidir los había pedido, y ofrecerlos parecía una declaración de guerra.»

El silencio que siguió tenía muchos pisos. Víctor lo habitó entero, sin prisa. Cuando habló, no miró a Duna: miró la pizarra donde alguien había escrito, meses atrás, la regla del preregistro de experimentos que Marga había institucionalizado — *criterios de éxito antes, evaluador distinto del proponente*.

—Vamos a hacer una cosa —dijo—. Propongo aplicar a Atlas nuestra propia medicina, la que aprobé yo para los experimentos de producto. Regla de parada, hoy, por escrito: si en seis semanas no encontramos veinte usuarios reales con un problema que Atlas resuelva mejor que un informe mensual — no «interés», no «me encantaría»: uso — Atlas se archiva. Y la evaluación no la hago yo. —Se volvió hacia Sofía—. La facilita tu equipo, que para eso lleva medio año haciendo de laboratorio. Yo me comprometo por escrito a aceptar el resultado.

—¿Y si el resultado es archivar? —preguntó Marga, muy despacio, como quien desactiva una bomba—. ¿Qué le decimos al board, que llevamos veinte meses…?

—Le decimos la verdad —dijo Víctor—. Que compramos una lección cara y que dejamos de pagarla a plazos. —Hizo una pausa y algo se le aflojó en la cara, un cansancio viejo saliendo a respirar—. Llevo un año sabiendo lo de Atlas, ¿sabéis? Sabiéndolo así, como se saben las cosas que no te puedes decir en voz alta. Cada trimestre pensaba: una fase más y despega, y así no tengo que explicar las anteriores. —Miró a Duna, ahora sí—. La próxima vez no esperes a que alguien con capacidad de decidir te pida los datos. Tráelos y ponlos encima de mi mesa. Es una orden, y me la puedes recordar con este momento.

Las seis semanas se cumplieron en julio. El equipo de discovery — Renata al frente — entrevistó a diecinueve directores de residencia con las reglas del oficio: comportamiento pasado, no intenciones. Encontraron dos usuarios potenciales reales, un caso de uso legítimo (el informe de la gestoría, que resultó ser una necesidad común) y ninguna evidencia del cuadro de mando predictivo que Atlas quería ser. La recomendación: archivar Atlas; extraer el informe mensual como feature simple de dos semanas; devolver el resto de la capacidad a la lista viva de Ondara.

Víctor lo comunicó él mismo, en el all-hands, con una diapositiva que decía «Qué aprendimos de Atlas (2024-2026)» y una franqueza que dejó la cafetería en un silencio de otra categoría. Contó los veinte meses, los cuatro usuarios, la escalada («cada fase nueva era mi manera de no mirar las anteriores»), la regla de parada y quién la había evaluado. Terminó con una frase que Nadia apuntó literal:

—Si en esta empresa matar un proyecto malo cuesta veinte meses, el problema no son los proyectos: es lo que cuesta decir la verdad cerca de un despacho. Eso es lo que estamos arreglando. Atlas es la factura de lo que costaba antes. Que sea la última grande.

---

Hubo una coda, una semana después, que Nadia guardó para el jardín porque le pareció más importante que el funeral.

En la resaca del all-hands, alguien de dirección propuso «institucionalizar el éxito»: contratar una consultora para «implantar el modelo del Petirrojo en toda Aurelia, con playbook y formación certificada». Y, de paso, «mirar el modelo Lantana, que está claro que funciona, y adoptarlo».

—Ay —dijo Bruno, cuando se enteró—. Ya llegó la termomix. Veinte años viendo el mismo ciclo: algo funciona porque unas personas concretas aprendieron a pensar juntas, y la organización concluye que lo que funciona es el *formato*, lo empaqueta, lo impone, y se pregunta después por qué la copia no respira.

—Es el sesgo del superviviente además —dijo Nadia—. Copiar a Lantana porque le va bien: no sabemos cuántas empresas hicieron exactamente lo mismo que Lantana y cerraron. Ni siquiera sabemos si lo que le funciona a Lantana es lo que pone en su Cuaderno o las siete personas concretas que son. —Se quedó pensando—. Es curioso. El Cuaderno lo advierte de sí mismo, ¿sabes? Hay una nota en el prólogo que nunca te he enseñado.

Se la enseñó. Decía:

> «Advertencia de M.: este cuaderno documenta lo que hacemos y por qué, con las fuentes de las que lo aprendimos. No es un método. Si copias nuestras prácticas sin sus porqués, fabricarás una maqueta de Lantana a tamaño real: se parecerá muchísimo y no volará. Los aviones de los isleños tampoco volaban, y estaban muy bien hechos. Busca "cargo cult", Feynman, 1974. Y luego no copies: entiende, y construye lo tuyo.»

—¿Los aviones de los isleños? —preguntó Bruno.

—Es una historia buenísima —dijo Nadia—. Te la cuento con la teoría. Pero antes apunto una cosa. —Abrió el jardín y escribió: *Hoy hemos matado a Atlas con una regla que escribimos hace meses para otra cosa. La estructura decide lo que el valor no se atreve. Y el peligro nuevo ya asoma: convertir lo aprendido en liturgia. La frase de M.: no copies — entiende, y construye lo tuyo. Sospecho que la sección más difícil del Cuaderno va a ser la que explica cómo se gobierna eso.*
