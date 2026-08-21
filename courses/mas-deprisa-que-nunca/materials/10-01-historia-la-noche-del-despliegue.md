El éxito trajo al depredador siguiente, como siempre hace. Se llamaba Grupo Albor: cincuenta y seis residencias, justo el doble que Ondara, y un consejo de administración que quería ver «una migración piloto funcionando» el viernes 17 de julio, porque ese día decidía proveedor para los próximos cinco años.

La fecha no salió de ninguna curva. Salió de una comida.

—Dos semanas de esfuerzo extraordinario —dijo el CEO en el all-hands, con el tono de quien pide un último baile—. Sé lo que hemos aprendido este año sobre ritmos. Esto es una excepción. Después del 17, descansamos.

Nadia miró a Bruno. Bruno miró el techo. En el Cuaderno había un capítulo sobre las excepciones — «toda organización tiene un modo normal y un modo excepción; tu cultura real es lo que pasa en el modo excepción, porque es cuando revela qué está dispuesta a sacrificar» — pero era julio, hacía calor, Albor era el doble de Ondara, y el Petirrojo, como todos, se arremangó.

Lo que pasó en esas dos semanas no fue dramático. Fue peor: fue razonable. Una cadena de decisiones pequeñas, cada una defendible en su momento, cada una un grado más de inclinación.

El lunes 6, para ir más deprisa, se acordó que los agentes pudieran desplegar de madrugada «cambios de bajo riesgo» con una sola aprobación en lugar del dueño-de-historia habitual. Tenía lógica: la cola no podía esperar al día siguiente. El miércoles 8, «bajo riesgo» ya incluía cambios de configuración, porque técnicamente no eran código. El viernes 10, Duna pidió mantener los tests cruzados — los que un humano distinto escribía para el código de agente — y se le contestó que «durante el crunch, los tests del agente valen, que para eso están»; lo aceptó, cansada, y lo apuntó en algún sitio. El lunes 13, la daily se saltó por primera vez en meses («no hay tiempo, cada uno sabe lo suyo»). Y todas las noches de esa segunda semana, en el canal de despliegues, la misma liturgia tranquilizadora: *deploy ok, deploy ok, deploy ok*. Catorce despliegues nocturnos sin incidentes.

—¿Ves? —dijo Marc el jueves 16 por la noche, con los ojos rojos y la taza número seis, mirando la cascada de *deploy ok*—. Y decían que la madrugada era peligrosa. Hasta ahora no ha roto nada.

Bruno, que se iba en ese momento, se detuvo en la puerta con el casco de la bici en la mano. Estuvo a punto de decir algo. Estaba demasiado cansado para acordarse de qué. Se fue.

A la 1:40 de la madrugada del viernes, Marc aprobó el último cambio de la lista: un ajuste de configuración del servicio de sincronización, preparando el aislamiento de datos del piloto de Albor. Lo había generado su agente. El test del agente pasaba. Marc llevaba diecisiete horas despierto y una semana a seis horas de sueño, y el diff era pequeño, y la demo era en diez horas, y lo aprobó él mismo porque el otro aprobador posible dormía. *Deploy ok.*

---

El teléfono de guardia sonó a las 7:12 del domingo, y era Nadia quien lo tenía.

—¿Nadia? Soy Encarna, de Miralbueno. Perdona la hora. —La voz venía plana, controlada, la voz de alguien acostumbrado a las emergencias de verdad—. Rosa dice que la hoja de medicación de esta mañana está mal. Que le faltan los cambios de pauta de esta semana. Ha llamado a dos residencias hermanas y les pasa igual. Te lo digo como me lo ha dicho ella: «el ordenador se ha quedado en el martes».

Nadia ya estaba descalza delante del portátil, con el corazón en las orejas y el runbook abierto. Confirmado en dos minutos: el servicio de sincronización llevaba desde la madrugada del viernes sin servir datos vivos. El cambio de configuración de la 1:40 — una línea: un flag de entorno mal acotado, pensado para el piloto de Albor, aplicado a todos — había redirigido silenciosamente las lecturas a la instantánea estática preparada para la demo: una copia de las fichas congelada el martes. Sin errores. Sin alertas, porque el servicio respondía rápido y con datos *válidos en formato*: simplemente, viejos. Más de dos días sirviendo el martes.

Veintiocho residencias de Ondara con las hojas de medicación congeladas en una semana con docenas de cambios de pauta.

Lo que salvó la mañana no fue el software. Fue el protocolo de papel que Rosa y las gobernantas de su generación jamás habían soltado del todo — el cuaderno donde cada cambio de pauta se apuntaba a mano al recibirlo del médico — y fue la propia Rosa, que a las 6:50, repasando la hoja impresa con su boli, había visto que faltaba la anticoagulación nueva del 214 y no se había encogido de hombros. A las 7:40, el protocolo de contingencia estaba activo en las veintiocho residencias: medicación por cuaderno y doble verificación telefónica. A las 9:15, el equipo — todos, domingo, en pijama en la videollamada — tenía el servicio restaurado y los datos verificados. A las 10:00 se confirmó lo importante: ninguna dosis incorrecta administrada. Por el papel. Por Rosa. Por treinta años de oficio que no confiaban del todo en las máquinas, ni siquiera en las buenas.

En la videollamada, cuando se confirmó el «ninguna dosis», nadie celebró. Marc tenía la cara gris. Escribió en el chat, para todos: «El cambio de la 1:40 es mío. Lo aprobé yo solo. Lo siento muchísimo». Y luego, un mensaje solo para Sofía: «Si hay que rodar una cabeza que sea la mía, pero que sea rápido, por favor».

Sofía miró ese mensaje mucho rato. Luego abrió el Cuaderno, buscó el capítulo que sabía que iba a necesitar — «Cuando pase lo grave (pasará)» — y empezó a preparar el lunes.

---

El postmortem se hizo el martes, con una sala llena y las reglas escritas en la primera diapositiva. Sofía las leyó en voz alta, despacio:

—Uno: asumimos que todos actuaron razonablemente con la información, la presión y el cansancio que tenían — si no lo creéis, mirad la cronología antes de opinar. Dos: buscamos causas en el sistema, no culpables con nombre; el «error humano» no es una conclusión, es el punto donde empieza la pregunta. Tres: todo lo que se diga aquí sirve para arreglar; nada de lo que se diga aquí sale hacia una evaluación. Y cuatro — miró a Víctor y al CEO, sentados atrás —: esto vale también para los de la última fila.

La cronología ocupó una pared. No empezaba a la 1:40 del viernes: empezaba el lunes 6, con la primera excepción razonable. Verla entera, dibujada, hizo un silencio espeso: nueve decisiones, ninguna escandalosa, cada una apoyada en la anterior. «Cambios de bajo riesgo con una aprobación.» «La configuración no es código.» «Los tests del agente valen.» «La daily se salta.» «Deploy ok, deploy ok.» Cada *deploy ok* nocturno había sido, sin que nadie lo dijera así, un dato a favor de la siguiente rebaja: *hasta ahora no ha roto nada.*

—Aquí está la parte que quiero que veáis —dijo Nadia, señalando la secuencia—. No es que el viernes hiciéramos algo raro. Es que el viernes ya era *normal* lo que el lunes 6 nos habría parecido inaceptable. El Cuaderno tiene nombre para esto, y viene de la investigación del accidente del Challenger: normalización de la desviación. Cada vez que te saltas el margen y no pasa nada, el margen nuevo se convierte en el margen. La víspera del Challenger, la NASA discutió las juntas que acabaron fallando y concluyó que volar era aceptable — porque llevaban años erosionándose «sin pasar nada». Los ingenieros estimaban un riesgo mil veces mayor que sus directivos. Nadie mentía. El sistema entero había aprendido a no ver.

—Y hay otra parte —dijo Duna, y puso una transparencia con dos columnas—. Lo que nos quitamos «solo durante el crunch»: el dueño por historia, los tests cruzados, la daily, el límite de despliegues nocturnos. Es exactamente la lista de lo que este año nos había salvado. No es casualidad: las defensas parecen fricción precisamente porque funcionan — solo notas su ausencia. —Pausa—. Yo pedí mantener los tests cruzados el viernes 10 y acepté un no. La próxima vez no voy a aceptarlo, y necesito saber que la organización me respalda.

—Te respalda —dijo Víctor, desde la última fila. Se levantó y fue a la pared de la cronología—. A la cronología le falta una línea. La primera. —Cogió el rotulador y escribió, arriba del lunes 6: *«30 de junio: dirección acepta una fecha de demo decidida en una comida, sin consultar capacidad, y pide 'esfuerzo extraordinario'.»* —Se volvió—. Esta es mía y del CEO, que me ha autorizado a escribirla. Todo lo demás cuelga de ahí. Marc aprobó solo a la 1:40 porque una cadena de decisiones, que empieza en esa comida, lo puso a la 1:40, solo, con diecisiete horas de vigilia y una demo encima. Si mañana ponéis a otra persona en esa silla con esa cadena, hace lo mismo. La cabeza que pediste que rodara, Marc, no te pertenece: es de la cadena. Y las cadenas no se despiden: se rediseñan.

El informe del postmortem — doce páginas, cronología completa, sin un solo nombre propio salvo en los agradecimientos, donde estaban Rosa y las gobernantas — produjo cinco cambios que quedaron escritos como política:

*Las defensas no se suspenden bajo presión: se refuerzan; cualquier excepción requiere decisión escrita de dirección con fecha de caducidad. Presupuesto de error explícito: si la tasa de fallos de cambio supera el umbral, el ritmo baja automáticamente — sin negociación, como un fusible. Ningún despliegue con impacto clínico fuera de horario con capacidad de respuesta reducida. Las fechas de compromiso externas se contrastan con la curva antes de aceptarse, también las que nacen en comidas. Y ritmo sostenible como norma: el estudio que Nadia llevó al board — trabajadoras de munición de 1915, la productividad plana a partir de las 50 horas, «los domingos no suman» — se citó en la sesión del consejo, y la frase que quedó en acta fue del propio CEO: «hemos comprado velocidad con sueño y nos ha salido al precio del sueño».*

Y hubo una decisión más, la más discutida: enviar el postmortem completo, sin editar, a los veintiocho directores de residencia de Ondara. Legal se opuso. Marga dudó. Fue Encarna quien zanjó, cuando Sofía la llamó para consultarle:

—Mandadlo. ¿Sabéis por qué Rosa revisa vuestras hojas con boli? Porque nunca ha sabido qué hay detrás. Enseñadle lo que hay detrás — lo bueno y el domingo — y a lo mejor empieza a fiarse con conocimiento, que es la única confianza que dura.

Rosa leyó las doce páginas. Contestó con dos líneas, que Sofía imprimió y puso junto a la Directiva Prima:

*«Ahora sé qué mirar cuando algo falle, y sé que me lo contaréis. Seguiré con mi cuaderno, no os ofendáis. Los buenos sistemas son los que aguantan que una vieja desconfíe de ellos.»*

¿Y Albor? La demo del viernes había ido bien, para lo que sirvió: la decisión llegaría en septiembre y sería para el proveedor grande de siempre — por precio, dijeron; no por el incidente, que Aurelia les contó ella misma antes de que se enteraran por otros —. A la Aurelia de un año antes le habría costado una crisis y tres cabezas; a esta le costó una tarde de disgusto y una norma escrita, propuesta por Marga, de todas las personas posibles: *las fechas nacidas en comidas se rechazan también cuando la demo sale bien.*

En el jardín, esa noche, Nadia escribió poco: *Sin daño, por Rosa y por el papel. La cronología en la pared: nueve decisiones razonables = una desviación normalizada. Víctor escribiendo la línea cero. La frase de Duna: las defensas parecen fricción porque funcionan. Y la de Rosa, que es la mejor definición de resiliencia que he leído: los buenos sistemas aguantan que una vieja desconfíe de ellos. Mañana: leer entero el Apéndice F de Feynman. Bruno dice que la última frase me va a gustar. La naturaleza no se deja engañar, dice.*
