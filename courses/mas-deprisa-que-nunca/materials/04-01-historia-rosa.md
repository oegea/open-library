Diciembre llegó a Aurelia con dos anuncios y una avería silenciosa.

El primer anuncio fue el «bonus Prometeo»: doscientos euros brutos al mes para los tres developers con más tickets cerrados vía agente. Lo comunicó Recursos Humanos con una plantilla de colores alegres, y Víctor lo defendió en el all-hands como «una forma de premiar a quienes abrazan el cambio». Marc iba primero en la clasificación provisional y no le daba vergüenza decirlo; llevaba una semana llegando antes que nadie para lanzar tandas de agentes al abrir, como quien madruga para regar.

El segundo anuncio no fue un anuncio: fue algo que Bruno descubrió un miércoles a las 8:50 y que en el Petirrojo se recordaría como *lo del módulo*. El módulo de medicación — el corazón clínico de Nido, el que imprimía las hojas que las auxiliares llevaban en los carritos, el que Bruno había construido casi solo en 2017 y cuidado desde entonces como se cuida un huerto — había sido reescrito durante la noche. Enterito. Un agente de la iniciativa «modernización de deuda técnica», lanzado desde plataforma con una lista de módulos antiguos, lo había migrado al framework nuevo, renombrado la mitad de las funciones y aplanado, de paso, ocho años de comentarios. Los tests pasaban. El PR se había automergeado a las 3:12 con la aprobación de otro agente.

Bruno no gritó. Eso fue lo que más asustó a Nadia. Se quedó mirando el diff — verde y rojo hasta donde alcanzaba el scroll — y luego cerró el portátil con el cuidado exagerado de quien no confía en sus propias manos, y se fue a hacer un café que no se bebió.

—Los tests pasan —dijo Marc, conciliador, desde su mesa—. Y el código nuevo es objetivamente más limpio, Bruno. Míralo así: te han quitado trabajo aburrido.

—Marc, hijo —dijo Bruno, sin volverse—. Cuando alguien te quite algo tuyo y te diga que es por tu bien, avísame, que quiero ver la cara que pones.

Nadia apuntó la frase en el jardín, y debajo: *Los tests pasan y algo se ha roto igual. ¿Qué es lo que se ha roto, exactamente? No tiene nombre de ticket.*

La avería silenciosa era eso: la moral. Desde los despidos, la oficina funcionaba con un ruido de fondo nuevo, hecho de conversaciones que se cortaban al abrirse una puerta y de gente puliendo su LinkedIn con la pantalla medio girada. Duna lo dijo en la daily con su franqueza de QA, mirando al suelo: «Yo ya no sé si estoy trabajando o haciendo méritos para la próxima lista». Y Sofía, que oía todo aquello y cargaba con ello, decidió hacer algo que no estaba en ningún manual de management de los que le habían dado.

Lo había leído en el Cuaderno, en el capítulo que Nadia le había reenviado con el asunto «léete esto cuando puedas, creo que es de lo nuestro»:

> «Hay un experimento que nos obsesiona. En un call center de recaudación de fondos, un investigador llamado Adam Grant hizo que los operadores conocieran, cinco minutos, a un estudiante becado con el dinero que ellos recaudaban. Solo eso. Cinco minutos, una vez. Un mes después, los que lo habían conocido recaudaban casi el triple. El grupo al que solo le *contaron* historias de becados, por escrito, no mejoró nada. Conocer no es que te cuenten.
> Nosotros lo aplicamos a rajatabla: toda persona de Lantana pasa un día al trimestre donde el trabajo aterriza. No es un gasto en moral. Según los datos, es la intervención de rendimiento más barata que existe.»

Sofía leyó los papers enlazados — los leyó de verdad, subrayando, la primera literatura científica que leía desde la carrera — y luego escribió a Encarna Millán, directora de la residencia Miralbueno, la de la lista de tres folios. El asunto del correo fue: «¿Podemos ir a ver cómo se usa Nido? En silencio. Sin vender nada.»

Encarna contestó en veinte minutos: «Veníos el jueves. A las 7:30, que es cuando pasa todo. Y con zapato cómodo.»

---

Fueron cinco: Sofía, Nadia, Bruno, Duna y Renata. Marc dijo que tenía «los agentes a medio lanzar» y se quedó, y nadie insistió, y esa también fue una información.

La residencia Miralbueno era un edificio de los noventa con olor a café, a desinfectante y a colonia infantil — «la colonia es cosa nuestra», explicó Encarna, «a los residentes les gusta oler a domingo» —. A las 7:30, el turno de noche pasaba el parte al de mañana en un office donde no cabían todos, y allí conocieron a Rosa.

Rosa Carvajal, cincuenta y ocho años, enfermera y gobernanta de la segunda planta, treinta y un años de oficio, unas gafas colgadas del cuello y una manera de moverse que hacía parecer que el pasillo era suyo, porque lo era. Fue ella quien los adoptó durante la mañana, con una mezcla de hospitalidad y guasa («los informáticos, chiquets, a ver, que no os caigáis en mi planta que luego el parte lo relleno yo»).

Y el Petirrojo vio.

Vio el carrito de medicación a las 8:05: Rosa empujándolo pasillo adelante con la hoja impresa de Nido sujeta con una pinza, porque la tablet «se apaga cada diez minutos, y yo llevo guantes, cielo, ¿tú has probado a meter un PIN con guantes mientras sujetas un vaso con pastillas?». La sesión que caducaba — línea nueve de la lista de Encarna, ticket enterrado en el backlog desde hacía siete meses con etiqueta `minor` — no era *minor* a las 8:05 de la mañana: era la razón de que la trazabilidad de medicación, el orgullo clínico de Nido, se hiciera de memoria y se pasara a limpio a las doce.

Vio a una auxiliar, Loli, rellenar un parte de incidencias desde el pasillo con un residente agarrado de su brazo: cuarenta segundos de formulario que en la oficina de Aurelia parecían razonables y que allí, con don Ernesto preguntando por tercera vez si su hija venía hoy, eran una eternidad en la que Loli tecleaba con una mano, tranquilizaba con la otra, y acababa eligiendo entre el software y la persona. Elegía a la persona. El parte se rellenaba luego, de memoria, o no se rellenaba.

Y vio — esto fue lo de Bruno — el módulo de medicación en producción, en las manos para las que existía. Rosa repasando la hoja de la tarde, señalando con el boli: «Esto de aquí, esta columna, esta me salvó una vez de un disgusto gordo con una anticoagulación, porque lo pone bien claro y en grande. No sé quién lo hizo así de claro, pero le debo un café». Bruno miró la columna. La había diseñado él, en 2017, después de una conversación con una enfermera de otra residencia que le contó un susto parecido. No dijo nada. Se quitó las gafas, las limpió con la camiseta, y Nadia, que lo vio, tuvo la elegancia de mirar hacia otra parte.

A las 11:00, en el office, con café de máquina buena («la máquina la elegí yo, es la decisión de más impacto de mi carrera», dijo Encarna), Rosa les resumió la mañana sin saber que estaba dictando un roadmap:

—Nido nos hace falta, eso que quede claro. Cuando entró, se acabaron los cuadernos con letra de médico y los sustos de «esto quién lo apuntó». Pero, chiquets, últimamente cada mes hay pantallas nuevas que nadie ha pedido y las de todos los días siguen igual de duras. Es como si me cambiarais el pasillo de sitio cada mes y los carritos siguieran sin ruedas. Yo no necesito que Nido haga más cosas. Necesito que las cinco cosas que hago cien veces al día cuesten dos toques menos. —Se puso las gafas para mirarlos, uno a uno—. ¿Vosotros sabéis lo que es que a las 8 de la mañana te sobren cuatro segundos? Es la diferencia entre mirar la pastilla o mirar a la señora. Yo quiero mirar a la señora.

Nadie del Petirrojo dijo nada durante unos segundos. Luego Duna, que apenas había hablado en toda la mañana, sacó su libreta y dijo:

—¿Nos enseñas lo de los guantes otra vez? Lo del PIN. Quiero grabarlo, si te parece bien.

---

El viaje de vuelta en el coche de Sofía fue el silencio más productivo de la historia del equipo. Lo rompió Bruno pasado Sollana, mirando por la ventanilla:

—Treinta años en esto. He ido a doscientas reuniones de requisitos. Es la primera vez que veo usar mi software con la persona delante. —Pausa—. La columna de la anticoagulación. Ni me acordaba. Para mí era un ticket de 2017. Para Rosa es que no se le murió una señora.

—¿Y ahora entiendes lo del módulo? —preguntó Nadia, con cuidado—. Lo de que el agente lo reescribiera. Por qué dolió.

Bruno tardó en contestar.

—Dolió porque ese módulo era el sitio donde yo sabía por qué cada cosa estaba donde estaba. Cada rareza tenía una historia, y la mitad de las historias eran una Rosa. El código nuevo es más limpio, el chaval tiene razón. Pero ya no es de nadie. Es como… —buscó la palabra— como si te asfaltaran el huerto y te dijeran que ahora es más fácil de mantener.

Esa semana pasaron cosas pequeñas que no salieron en ningún dashboard. Duna montó, sin que nadie se lo pidiera, un canal interno donde subía un clip semanal de dos minutos de las visitas («Rosa explica los guantes», 340 visualizaciones, récord absoluto de cualquier contenido interno de Aurelia). El ticket de la sesión que caducaba salió del sótano del backlog y se resolvió en tres días, con un modo quiosco para las tablets de planta; el PR llevaba una descripción inusualmente larga que empezaba: «Contexto: a las 8:05, con guantes y un vaso de pastillas en la mano…». Y Marc — que había visto el clip de los guantes como todo el mundo — apareció el viernes en la mesa de Sofía, incómodo, con una pregunta que no parecía suya:

—¿Cuándo es la próxima visita? Es que… a ver. Yo cierro cuarenta tickets a la semana. Y no sabría decirte qué cambia en el mundo cuando los cierro. Antes no me lo preguntaba y ahora me lo pregunto todo el rato. No sé si me habéis hecho un favor o me habéis fastidiado la racha.

—Las dos cosas —dijo Sofía—. Bienvenido.

En cuanto al bonus Prometeo: la clasificación provisional siguió publicándose cada lunes, pero algo se le había desinflado. La semana después de la visita, dos de los tres primeros pidieron en retro, con cierta vergüenza y las palabras justas, que los doscientos euros se los dieran «a otra cosa», que cerrar tickets a peso «se había vuelto raro». Víctor, cuando Sofía se lo transmitió, se lo tomó peor de lo esperado — «¿ahora resulta que premiar está mal?» — y Sofía no supo explicarle con datos por qué un premio podía desmotivar. Todavía no. El Cuaderno tenía un capítulo sobre eso, con un meta-análisis de 128 experimentos, y Nadia lo estaba leyendo esa misma noche.

En el jardín, antes de dormir: *Grant tenía razón y ni siquiera hemos medido: la visita nos ha cambiado más que cualquier charla. La frase de Rosa — «quiero mirar a la señora» — vale un roadmap entero. Bruno y el huerto asfaltado: la propiedad no sale en la telemetría pero existe. Y el bonus: premiar el número ha hecho el trabajo MÁS pequeño, no más grande. ¿Por qué? El Cuaderno dice: Deci, Ryan, 1999. Mañana lo leo.*
