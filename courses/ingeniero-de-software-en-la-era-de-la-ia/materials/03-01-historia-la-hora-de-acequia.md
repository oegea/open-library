La casa de Paca olía a leña y a naranja, y en el pasillo había una foto en blanco y negro de un hombre con azada junto a una compuerta que Nadia ya sabía reconocer: el azud viejo, el mismo cuya válvula había girado sola tres semanas atrás.

—Mi padre —dijo Paca, siguiendo su mirada—. Cuarenta años de alguacil de aguas. Sentaos, que esto no se cuenta de pie.

Sobre la mesa camilla, junto a la cafetera, estaba la carpeta de gomas. Paca la abrió con un cuidado que no era ceremonia sino costumbre, y fue sacando papeles: actas mecanografiadas, un plano de las acequias dibujado a mano con tinta de dos colores, listados de partícipes con enmiendas al margen. Se detuvo en un documento amarillento, con sello de la comunidad y fecha de julio de 1974.

—El acta de la concordia —dijo—. Aquí está lo que venís a buscar, aunque todavía no lo sepáis.

Tomás la leyó primero, despacio. Luego se la pasó a Nadia sin decir nada, con esa cara de quien confirma una sospecha que habría preferido no confirmar. El párrafo clave estaba en la tercera página, redactado con esa prosa de secretario antiguo que no usaba una palabra de menos:

*«…acuerdan los partícipes que las tandas del estío se contarán desde la primera luz, comenzando el turno primero media hora antes de la salida del sol sobre el cerro de la Atalaya, y corriendo los demás turnos de seguido, cada uno su dotación, hasta cumplirse la rueda; y que así se guardará cada día, adelantándose o retrasándose el comienzo conforme se adelante o retrase el sol, para que ningún partícipe riegue con más calor que otro.»*

Nadia lo leyó dos veces. Levantó la vista.

—Los turnos no empiezan a una hora fija.

—Claro que no, hija. —Paca sirvió café—. Empiezan con el sol. En agosto la rueda arranca casi una hora antes que en junio, y así todo el verano, corriéndose un poquito cada día. Se hizo así en el 74 porque los del final de la tanda regaban siempre a mediodía, con el sol pegando, y el agua se les evaporaba en el surco. Hubo pleitos, hubo hasta una pedrada. La concordia fue eso: que la rueda girase con el sol, para que el calor se repartiera igual que el agua. Y lo que empezó siendo cosa del verano se quedó de costumbre para todo el año, que así nadie anda cambiando de cuenta. —Dio un sorbo—. Aquí lo llamamos regar por la hora de la acequia. Mi padre la llevaba en la cabeza. Yo la llevo en la cabeza. Y cuando vinisteis con los sensores, se lo expliqué a vuestro programador, al que estaba entonces… Joel, ¿no se llamaba? Un chico muy atento. Lo apuntó todo en su ordenador.

Nadia y Tomás se miraron. Joel había sido el primer empleado de Vega. Se marchó a una scale-up alemana dos años atrás. Su código seguía allí; sus apuntes, nadie sabía.

—Señora Paca —dijo Nadia, eligiendo las palabras—, ¿usted sabe cómo hacía nuestro sistema para seguir la hora de la acequia?

—¿Yo? Hija, yo sé que la seguía. Los turnos caían cuando tenían que caer. Por eso me fie.

En el coche de vuelta, Tomás condujo callado un buen rato, con el acta fotografiada en el móvil de Nadia y el original devuelto a su carpeta como una reliquia.

—Ya sé qué pasó la madrugada del catorce —dijo al fin—. Y no te va a gustar, porque no falló nadie. Falló *que no había nadie*.

---

De vuelta en el almacén, Nadia tiró del hilo hasta el fondo. Con el acta delante, el código del planificador se leía de otra manera. Y allí estaba, en un módulo con un nombre anodino —`schedule_offsets.py`—, escrito por Joel en 2023: una función que calculaba, para cada comunidad, un desplazamiento diario a partir de la salida del sol, y lo aplicaba a las horas «naive» del plan de tandas. Sin zona horaria, a propósito: aquellas horas no eran horas civiles. Eran horas de acequia, ancladas al sol del cerro de la Atalaya, y el desplazamiento las convertía en tiempo real cada madrugada.

No había ni un comentario que lo explicara. Ni un test que lo protegiera. Ni una línea de documentación. El único sitio del mundo donde aquella lógica estaba explicada era la cabeza de Joel, a dos mil kilómetros, y un acta de 1974 en una carpeta de gomas.

—Y entonces llega el Autopilot —dijo Nadia en la reunión del miércoles, con todo el equipo delante y el acta proyectada en la pared junto al commit—. Ve fechas sin zona horaria mezcladas con UTC. Ve un test que falla de vez en cuando. Ha leído diez mil manuales que dicen, con razón, que las fechas naive son un error clásico y que la solución canónica es normalizar a UTC. No puede saber que *precisamente aquí* esas fechas son la representación correcta de un acuerdo de 1974 anclado al sol, porque eso no está escrito en ningún sitio donde una máquina —o un humano nuevo— pueda leerlo. Hace el arreglo de manual. Los tests pasan, porque el único test que protegía esa lógica era flaky y su versión «arreglada» ya no la protegía sino que la contradecía. Y la madrugada siguiente, la rueda de tandas arranca a la hora civil en punto: tres horas antes que el sol. —Hizo una pausa—. Las válvulas no se volvieron locas. Obedecieron un calendario que por primera vez en dos años estaba *equivocado con total corrección*.

Nadie dijo nada durante unos segundos. Fue Bruno quien resumió, sin rastro de broma:

—La máquina hizo bien lo que nadie debió pedirle.

—No. —Tomás se levantó y fue hasta el mapa—. La máquina hizo lo que *cualquiera* habría hecho sin la teoría. Si el año pasado entra un senior nuevo, ve ese módulo sin comentarios, ve el test flaky, ve las fechas naive… hace exactamente el mismo commit. Puede que más despacio, puede que preguntando antes en el canal de Slack, y ahí está toda la diferencia: *preguntando*. —Golpeó suavemente el mapa con el dorso de la mano—. El problema no es que Corvus escribiera código. Es que este sistema llevaba dos años funcionando sin que nadie de esta sala supiera *por qué* funcionaba. El conocimiento se fue con Joel. El código se quedó, pero el código no es el conocimiento: es la sombra que el conocimiento proyecta. Nosotros llevábamos dos años regando con la sombra.

Élia había escuchado todo aquello de pie, muy quieta, con los brazos cruzados. Cuando habló, le salió una voz que Nadia no le conocía.

—Yo fundé esta empresa —dijo—. Diseñé la mitad de lo que hay en ese repositorio. Y os tengo que decir una cosa que me cuesta más que lo del otro día con Paca: hace tiempo que no sé explicar mi propio producto. Sé lo que hace. Sé venderlo, sé priorizarlo, sé qué módulo toca cada cosa. Pero si me preguntáis *por qué* el planificador hace lo que hace, línea a línea, decisión a decisión… hay habitaciones enteras de esta casa en las que no he entrado nunca. Algunas las construyó Joel. Otras las construyó Corvus el año pasado, a cientos de commits al año, mientras yo miraba el contador de horas ahorradas y me sentía lista. —Descruzó los brazos—. El catorce de marzo no perdimos el control del sistema. Perdimos el control mucho antes. El catorce de marzo solo nos enteramos.

Se acercó a la pared, cogió el rotulador de Tomás y, bajo las tres preguntas del primer día, escribió la cuarta:

**¿Quién posee la teoría de este sistema?**

—Nadie —dijo, respondiéndose—. Ahora mismo, nadie. Trocitos Tomás, trocitos yo, trocitos Paca, trocitos un chico que vive en Berlín, y trocitos una máquina que no puede contarnos lo que sabe. Pues este es el plan, y no es un plan de software: vamos a reconstruir la teoría de Azud. No reescribir el código —el código funciona; reescribirlo sería otra huida hacia delante—. Reconstruir la *comprensión*: qué hace cada pieza, por qué existe, qué acuerdos del mundo real sostiene, y dejarlo escrito donde lo pueda leer un humano nuevo… o una máquina nueva. Y hasta donde no lleguemos con lo escrito, llegaremos con tests que hagan de memoria.

—¿Y los agentes? —preguntó Bruno—. ¿Los enterramos?

—Al contrario. —Élia tapó el rotulador—. Cuando tengamos la teoría, los agentes van a ser mil veces más útiles, porque podremos darles lo que a Corvus nunca le dimos: el contexto que no está en ningún manual. Pero primero lo primero. No se le puede dictar una teoría a una máquina si no la tienes tú.

Aquella tarde empezaron el mapa. No el de las acequias: el otro, el del sistema. Un rollo de papel continuo de tres metros, pegado con cinta a la pared libre del almacén, donde fueron dibujando cajas y flechas: el planificador, los offsets solares de Joel, el motor de válvulas, la app de los regantes, los informes, las quince integraciones. Cada caja con dos colores posibles: verde si alguien de la sala podía explicarla de arriba abajo, naranja si no. Al acabar la primera pasada, retrocedieron unos pasos y miraron el resultado en silencio.

Había mucho más naranja que verde.

—Bueno —dijo Tomás, y por primera vez en tres semanas sonrió de verdad—. Por lo menos ya tenemos un mapa donde se ve dónde están los dragones.

Nadia sacó el cuaderno y apuntó, bajo la fecha:

*Día 26. El código no es el conocimiento; es la sombra que el conocimiento proyecta. Hoy hemos empezado a buscar el cuerpo.*

Y debajo, más pequeño, porque le daba pudor lo mucho que le importaba:

*Paca se fio de nosotros porque los turnos caían cuando tenían que caer. Que no se me olvide nunca que la confianza de fuera se apoya en la teoría de dentro.*

---

*En la teoría de esta sección, la idea más importante del curso — y probablemente la menos conocida: en 1985 un informático danés escribió que programar no es producir código, sino construir una teoría; que la teoría vive en las personas y muere con ellas; y que un programa cuya teoría ha muerto solo puede decaer. Cuarenta años después, esa página explica el riego fantasma mejor que ningún log — y explica también qué parte de este oficio no se puede delegar en una máquina que escribe.*
