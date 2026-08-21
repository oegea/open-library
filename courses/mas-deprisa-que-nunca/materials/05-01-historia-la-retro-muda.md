En enero, a alguien de dirección se le ocurrió que los equipos llevaban demasiado tiempo siendo los mismos.

La palabra oficial fue «polinización». El plan: barajar a la gente entre equipos «para romper silos, difundir las mejores prácticas de IA y oxigenar la organización». El Petirrojo perdió a Renata tres días por semana — compartida ahora con otros dos equipos — y recibió a dos personas: Paula, una developer mid del disuelto equipo Jilguero, habladora y prudentísima a la vez, como quien ha aprendido que hablar mucho de cosas seguras es la mejor manera de no decir nada; y Aitor, un backend veterano del Alcaudón, que en dos semanas pronunció aproximadamente cuarenta palabras, doce de ellas «depende».

—Nos han dado dos personas para ir más rápido —resumió Bruno—. Ahora somos siete para no saber a dónde vamos. La aritmética del management, jardinera: si un equipo de cinco tarda tres meses, uno de siete tarda cuatro. Lo dijo un señor en 1975 y lo llevamos comprobando desde entonces.

Nadia lo apuntó para buscarlo luego (*¿Brooks? El Cuaderno lo cita: «canales de comunicación n(n−1)/2» — con 5 son 10 conversaciones posibles, con 7 son 21, hemos doblado el ruido sin doblar las manos*). Pero lo que de verdad se notaba no era el ruido: era el silencio.

El equipo había perdido el pulso. Esa cosa invisible que hacía que Duna supiera cuándo Bruno necesitaba que no le hablaran, que Marc supiera qué PRs revisaba mejor Nadia, que cualquiera pudiera decir «esto me huele mal» sin preparar la frase — eso ya no estaba. En las dailys, la gente informaba *hacia* Sofía en lugar de hablar *entre* sí. Paula decía «todo bien por mi parte» con puntualidad suiza. Aitor decía «depende». Y la retro de enero fue el punto más bajo: cuarenta y cinco minutos, un tablero con tres columnas casi vacías, dos post-its («mejorar comunicación», «seguir así con los experimentos») y un silencio tan educado que dolía.

—¿Nadie tiene nada más? —preguntó Sofía, y oyó su propia voz rebotar—. ¿De verdad? ¿Después del mes que llevamos?

Nada. Miradas al portátil. Marc hizo un chiste. Se acabó el tiempo.

Sofía cerró la sala y se quedó dentro, sola, con la sensación exacta de haber presidido una función de teatro. Esa noche escribió a Nadia: «¿El Cuaderno dice algo de retros donde nadie habla?»

Nadia contestó con un enlace y una frase: «Dice algo mejor. Dice por qué los dashboards de incidencias nos están mintiendo.»

---

El capítulo se titulaba «El termómetro que mide al revés», y Sofía lo leyó dos veces:

> «En los años noventa, una investigadora llamada Amy Edmondson estudió errores de medicación en unidades hospitalarias. Hipótesis obvia: los mejores equipos cometerían menos errores. Los datos dijeron lo contrario: los equipos con mejor liderazgo y mejores relaciones reportaban MÁS errores. Edmondson tardó en entenderlo, y cuando lo entendió cambió la disciplina entera: no cometían más errores. Los CONTABAN. En los equipos "peores", los errores existían igual — y se escondían.
> Lee tu dashboard de incidencias otra vez con esto en la cabeza. Un equipo con cero incidencias reportadas es un equipo sin incidencias o un equipo con miedo, y el dashboard no distingue. Una retro muda no es un equipo sin problemas: es un equipo donde hablar tiene precio. Edmondson le puso nombre a la variable — seguridad psicológica: la creencia compartida de que este grupo es seguro para el riesgo interpersonal; preguntar, admitir, discrepar, pedir ayuda — y veinte años de estudios la señalan como la variable número uno de los equipos que funcionan. No es buen rollo. Es que decir la verdad no te cueste nada.»

Sofía pensó en los despidos de noviembre. En el LinkedIn a media pantalla. En Paula, cuyo equipo entero había sido disuelto tras una mala racha de incidencias, diciendo «todo bien por mi parte». Pensó, con un frío súbito, en el gráfico que Víctor enseñaba en los all-hands: «incidencias reportadas por equipo, tendencia a la baja». Tendencia a la baja. Desde noviembre.

Y entonces pasó lo de la sincronización.

---

Fue Rosa quien lo pescó, con papel y boli, como pescaba todo.

La residencia Miralbueno estrenaba el piloto del modo quiosco, y con él una sincronización nueva de fichas clínicas. El miércoles por la tarde, Rosa llamó a soporte — y soporte, por el canal nuevo que Duna había abierto tras las visitas, escribió directamente al Petirrojo: «Rosa dice que en la ficha de dos residentes nuevos no le sale la alergia al metamizol que ella apuntó el lunes. Lo tiene en su cuaderno de papel, así que no ha pasado nada, pero dice, cito, que "o el ordenador o yo, uno de los dos se equivoca, y yo llevo treinta años sin equivocarme en esto"».

No había pasado nada. Podía haber pasado *todo*: una alergia que no se muestra es la clase de bug que termina en urgencias. El equipo dejó lo que tenía entre manos. Tres horas después habían encontrado la causa — la sincronización descartaba, en un caso raro de codificación, anotaciones creadas el mismo día que la ficha — y un parche estaba camino de producción con dos pares de ojos encima.

Fue en la revisión del parche cuando Duna dijo, con voz plana, mirando la pantalla:

—Yo vi algo parecido hace dos semanas. En el entorno de pruebas. Una anotación que no llegaba. —Silencio—. Pensé que sería cosa del entorno, y que si era real, alguien de plataforma lo tendría visto. Y no… no dije nada. —Levantó la vista, y lo que había en la cara no era excusa, era inventario—. Acababan de disolver el Jilguero por las incidencias. Yo soy QA reconvertida, la mitad de este equipo es nuevo, y no me apetecía ser la que ve fantasmas. Si llego a decirlo, esto se caza en pruebas y Rosa no tiene que fiarse de su cuaderno.

El silencio que siguió fue distinto de todos los silencios del mes. Marc abrió la boca — Nadia habría jurado que para algo tipo «bueno, no ha pasado nada» — y la cerró. Fue Aitor, el de las cuarenta palabras, quien habló:

—En el Alcaudón —dijo, despacio— teníamos una norma que no estaba escrita: los viernes no se reportaba nada, para no ensuciar la semana. Llevo aquí un mes esperando a ver cuáles son las normas no escritas de este equipo. —Se encogió de hombros—. Es lo que hacemos los nuevos. Miramos qué pasa cuando alguien mete la pata, y calibramos.

—¿Y qué habéis calibrado? —preguntó Sofía, aunque no estaba segura de querer la respuesta.

—Que aquí de la pata que metió noviembre no ha hablado nadie —dijo Aitor—. Todavía.

---

La retro de febrero no se pareció a la de enero, porque Sofía la preparó como quien prepara un despliegue delicado, con el Cuaderno abierto en una pestaña y los papers de Edmondson en otra.

Primero cambió el contrato. Abrió con dos minutos que había ensayado en el coche: la historia del hospital — los buenos equipos reportan más — y luego, mirándolos: «Nuestro dashboard de incidencias baja desde noviembre y me temo que eso no es una buena noticia, es un termómetro roto. Lo que se diga en esta sala se usa para arreglar el sistema, no para evaluar personas. Y lo digo yo, y me vais a ver sostenerlo». Después contó lo suyo: que llevaba semanas presidiendo dailys donde la gente le reportaba a ella como a un tribunal, que eso era en parte culpa de cómo ella escuchaba, y que la primera incidencia del nuevo registro la aportaba ella: «he estado tres semanas sin hacer uno-a-uno con nadie por ir a reuniones de seguimiento de las que no sale nada».

Después cambió la mecánica. Nada de tablero en blanco y a ver quién se lanza: **escritura en silencio** primero — ocho minutos, cada uno sus notas, sin nombres en la pantalla compartida hasta que todas estuvieron escritas — y **ronda** después: todos hablan, en orden, sin interrupciones, los nuevos primero («los que menos historia tienen que proteger», dijo, citando el Cuaderno sin decirlo). El efecto fue el de aflojar una tuerca pasada de rosca. Paula, en su turno, miró sus notas y dijo: «En el Jilguero, la retro era donde te enterabas de quién tenía la culpa. Me ha costado la retro pasada entera creerme que esto no iba de eso. Bueno. Y media de esta.» Y habló ocho minutos, con datos, del proceso de onboarding que no existía.

Salieron cinco temas de los de verdad. El último lo puso Bruno, señalando el calendario:

—Y una cosa más. Marzo. La fecha de Ondara. Estamos a mitad de camino y nadie ha vuelto a mirar si el plan de enero sigue teniendo sentido, porque nadie quiere ser el que abra el melón. Propongo que el melón tenga cita fija: revisión de mitad de trimestre, pase lo que pase, duela lo que duela. Los grupos no revisan el rumbo cuando deberían; lo revisan cuando el calendario los obliga. Eso también sale en los papeles de la jardinera, ¿verdad?

—Gersick, 1988 —dijo Nadia, sin poder evitarlo—. Los equipos cambian de enfoque justo en el punto medio del plazo. Casi nunca antes.

—Pues seamos el caso raro que lo hace a propósito —dijo Bruno.

Al salir, Sofía se quedó recogiendo los post-its de verdad — esta vez había que recogerlos — y se encontró con que Duna la esperaba en la puerta.

—Gracias por lo del termómetro —dijo Duna—. Pero que sepas que lo de hablar hoy no ha sido por la charla. Ha sido porque el martes, cuando conté lo del entorno de pruebas, nadie me dijo «tenías que haberlo reportado». Me dijisteis «¿qué habría hecho falta para que lo contaras?». —Se colgó la mochila—. Esa pregunta la vais a tener que sostener muchas veces, ¿eh? Una charla no es un sistema.

En el jardín, esa noche: *Edmondson: el termómetro mide el miedo, no los errores. Aitor: los nuevos calibran mirando qué pasa cuando alguien mete la pata — noviembre sigue sin conversarse y todo el mundo lo lleva puesto. La escritura en silencio funciona: lo que la gente escribe a la vez no se ancla en lo que dijo el primero. Y Duna, la mejor frase del trimestre: una charla no es un sistema. PENDIENTE: leer el estudio de las tripulaciones aéreas que cita el Cuaderno — dice que el 73% de los incidentes pasan el primer día que la tripulación vuela junta. Enseñárselo a quien inventó lo de la "polinización".*
