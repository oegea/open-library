Cuando Tomás, delante del mapa de la pared, dijo aquello de «todas las veces hubo alguien anunciando que ya no haríamos falta», no estaba consolando a nadie: estaba citando, sin saberlo, setenta años de historia documentada. Esta primera teoría existe para que tú tengas esa historia tan a mano como él. No por erudición: porque es la mejor vacuna contra los dos errores simétricos de 2026 — el pánico («el oficio se acaba») y la negación («esto es una moda más»). Ninguno de los dos sobrevive a los archivos.

## 1954: la máquina que iba a «eliminar la programación»

Empecemos por el documento fundacional del género. En noviembre de 1954, IBM publicó el informe preliminar del **FORTRAN** — el primer lenguaje de programación de alto nivel con éxito masivo, el que permitió escribir fórmulas matemáticas en lugar de instrucciones de máquina. En su página 2, el informe promete:

> «Since FORTRAN should virtually eliminate coding and debugging…»
> («Dado que FORTRAN debería eliminar virtualmente la codificación y la depuración…» — traducción propia. *Preliminary Report: Specifications for the IBM Mathematical FORmula TRANslating System*, IBM, 10 de noviembre de 1954.)

Léelo otra vez: *eliminar la codificación*. En 1954, «programar» significaba escribir a mano, una a una, las instrucciones numéricas del procesador. Desde esa definición, FORTRAN efectivamente eliminó la programación… tal y como se entendía entonces. Lo que nadie previó es que escribir fórmulas que una máquina traduce *también* acabaría llamándose programar, que haría falta muchísima más gente para hacerlo, y que esa gente cobraría más que sus predecesores, no menos.

Este es el patrón completo del curso en miniatura, y conviene darle nombre desde ya. Una **abstracción**, en ingeniería de software, es una capa que te permite trabajar con un concepto («una fórmula», «una tabla», «un fichero») sin manejar los detalles que hay debajo (registros del procesador, sectores del disco). Cada gran ola de herramientas de nuestra historia ha consistido en subir el nivel de abstracción: dejar que la máquina se encargue de la capa de abajo. Y cada subida ha producido el mismo anuncio — «ya no harán falta programadores» — seguido del mismo desenlace: los programadores no desaparecen; su criterio se muda un piso más arriba.

## Hopper y los que no se fiaban del compilador

La otra cara de la moneda de 1954 es menos contada y más útil para nosotros. Grace Hopper — pionera de la computación, creadora del primer **compilador**, el programa que traduce código de alto nivel a instrucciones de máquina — no encontró un mundo ansioso por adoptar su invento. Encontró lo contrario. Ella misma lo contó así:

> «I had a running compiler and nobody would touch it. They told me computers could only do arithmetic.»
> («Tenía un compilador funcionando y nadie quería tocarlo. Me decían que los ordenadores solo podían hacer aritmética.» — traducción propia. *The Wit and Wisdom of Grace Hopper*, OCLC Newsletter n.º 167, 1987.)

Los programadores veteranos de los años cincuenta desconfiaban del código generado por máquina por razones que hoy nos sonarán: ¿cómo va a escribir una máquina algo tan delicado como código? ¿Cómo confiar en instrucciones que no has escrito tú? Los veteranos de las tarjetas perforadas de los que hablaba Tomás en el capítulo existieron, y sus objeciones eran serias, no supersticiosas: los primeros compiladores generaban código peor que un buen programador humano. Hasta que dejaron de hacerlo. La lección no es «los escépticos siempre pierden»; es más fina: **la desconfianza inicial ante el código generado es una constante histórica, y se resuelve siempre igual — no con fe, sino con herramientas de verificación que hacen innecesario fiarse**. Nadie «confía» hoy en su compilador por cariño: confiamos porque hay tests, porque hay décadas de uso, porque el comportamiento es determinista y auditable. Guarda esta idea: reaparecerá cuando hablemos de agentes, donde una de esas tres condiciones se rompe.

## 1968: la palabra «ingeniería» como provocación

Salto de una década. A finales de los sesenta, el software vivía su primera gran crisis de crecimiento: los proyectos se retrasaban, se disparaban de coste, fallaban en producción. El hardware había crecido más deprisa que nuestra capacidad de organizarnos para programarlo. En octubre de 1968, el Comité de Ciencia de la OTAN reunió en Garmisch (Alemania) a medio centenar de expertos en una conferencia que es, para nuestro oficio, algo así como el acta fundacional. El informe resultante (Naur y Randell, eds., 1969 — sí, el mismo Naur que reaparecerá en la sección 3) registra:

> «There was a considerable amount of debate on what some members chose to call the 'software crisis' or the 'software gap'.»
> («Hubo un debate considerable sobre lo que algunos miembros optaron por llamar la "crisis del software" o la "brecha del software".» — traducción propia, §7.1.2.)

Y deja constancia de que el propio nombre de la conferencia era una declaración de intenciones:

> «The phrase 'software engineering' was deliberately chosen as being provocative…»
> («La expresión "ingeniería del software" fue elegida deliberadamente por ser provocadora…» — traducción propia.)

Provocadora porque en 1968 llamar «ingeniería» a aquello era un aspiración, no una descripción: implicaba que construir software debía parecerse a construir puentes — con disciplina, con teoría, con responsabilidad — y todavía no se parecía. Una participante de esa historia merece mención aparte: **Margaret Hamilton**, directora del equipo que programó el ordenador de a bordo del Apolo, contaba que empezó a usar el término «software engineering» para reivindicar que su disciplina merecía el mismo respeto que las demás ingenierías del proyecto — y que al principio «se consideraba muy gracioso; fue una broma recurrente durante mucho tiempo» (IEEE Computer Society, 2018 — traducción propia; el informe OTAN, por su parte, atribuye la expresión al comité de estudio que preparó la conferencia en 1967: ambas historias conviven en las fuentes, y te las presentamos las dos).

En Garmisch se dijeron cosas que podrían publicarse hoy sin cambiar una coma. Un asistente, Ron Graham, describió así el estado del arte:

> «We build systems like the Wright brothers built airplanes — build the whole thing, push it off the cliff, let it crash, and start over again.»
> («Construimos sistemas como los hermanos Wright construían aviones: montas el aparato entero, lo empujas por el acantilado, dejas que se estrelle y vuelves a empezar.» — traducción propia.)

Y el informe advertía de que «un mal funcionamiento en un sistema avanzado de hardware y software puede ser cuestión de vida o muerte» (David y Fraser — traducción propia). En 1968 eso era casi teórico. En la sección 9 de este curso veremos el día en que dejó de serlo. Y fíjate en la resonancia con nuestra historia: el software de Vega Riegos no mueve vida o muerte, pero mueve el agua de la que vive una comunidad. La ingeniería nació como aspiración a estar a la altura de esa clase de consecuencias.

## 1986: Brooks y la bala de plata

Nuestra tercera parada es el ensayo más citado — y peor citado — de la historia de la disciplina. En 1986, Fred Brooks (el gestor del proyecto OS/360 de IBM, escarmentado como pocos) publicó *No Silver Bullet*, donde sostiene que ninguna tecnología produciría, por sí sola, una mejora de un orden de magnitud en productividad, fiabilidad o simplicidad en la década siguiente. Su argumento central distingue entre la dificultad **esencial** del software — entender el problema, diseñar el constructo conceptual, decidir qué debe hacer exactamente el sistema — y las dificultades **accidentales** — la fricción de expresarlo: sintaxis, herramientas, entornos. Las herramientas atacan lo accidental; lo esencial resiste:

> «I believe the hard part of building software to be the specification, design, and testing of this conceptual construct, not the labor of representing it…»
> («Creo que la parte difícil de construir software es la especificación, el diseño y la prueba de ese constructo conceptual, no el trabajo de representarlo…» — traducción propia. Brooks, *No Silver Bullet — Essence and Accident in Software Engineering*, 1986/1987.)

Lo que casi nadie recuerda es que Brooks dedicó una sección explícita a la inteligencia artificial, que en los ochenta prometía —vía sistemas expertos— automatizar la programación:

> «Many people expect advances in artificial intelligence to provide the revolutionary breakthrough… I do not.»
> («Mucha gente espera que los avances en inteligencia artificial proporcionen el gran salto revolucionario… Yo no.» — traducción propia, misma obra.)

¿Se equivocó? Es la pregunta interesante de 2026, y merece respuesta honesta y no eslogan. Sobre la IA de su época, acertó de pleno: los sistemas expertos no revolucionaron nada. Sobre la nuestra, el jurado delibera — los modelos de lenguaje son la primera tecnología de la historia que ataca directamente *el coste de escribir el código*, y hay quien sostiene que empieza a rozar lo esencial. Pero fíjate en lo que viste en el capítulo 1: el Autopilot de Corvus ejecutó a la perfección la parte accidental (escribir un fix canónico, limpio, con su test) y falló catastróficamente en la esencial — saber *qué debía hacer el sistema*: algo que, como el equipo aún tardará en descubrir, no estaba escrito en ningún lugar donde máquina alguna pudiera leerlo. El commit del riego fantasma es el ensayo de Brooks convertido en incidente de producción. Y su frase final sigue siendo el mejor resumen del temario que tienes por delante: «There is no royal road, but there is a road» — no hay atajo real, pero hay camino.

## Los ochenta y noventa: 4GL, CASE y el fin del programador (otra vez)

La historia insiste con una regularidad casi cómica. En 1981, James Martin — el consultor más influyente de su generación — publicó un libro cuyo título lo dice todo: *Application Development Without Programmers* («Desarrollo de aplicaciones sin programadores»). La ola de entonces eran los **4GL** (lenguajes de cuarta generación: lenguajes declarativos de muy alto nivel, pensados para que un analista de negocio generara aplicaciones sin «programar»), seguida por las herramientas **CASE** (*Computer-Aided Software Engineering*: entornos que prometían generar el sistema entero a partir de diagramas y especificaciones). Miles de millones de dólares, portadas de revistas, y el mismo guion: los 4GL encontraron su nicho (los descendientes de aquella idea siguen vivos: SQL es, en espíritu, un 4GL que triunfó), las CASE colapsaron bajo su propia promesa, y la demanda de programadores siguió creciendo. La ola **no-code/low-code** de los años 2010-2020 es el mismo fenómeno con interfaz más bonita — útil para una clase de problemas, mudo ante la pregunta esencial de Brooks. Si quieres el panorama completo de este medio siglo contado por un testigo directo, Brian Randell — coeditor del informe de Garmisch — lo repasa en *Fifty Years of Software Engineering* (arXiv:1805.02742, 2018, acceso abierto).

## El patrón de fondo: la abstracción desplaza el criterio

¿Por qué el «fin del programador» no llega nunca, si las herramientas mejoran de verdad? La mejor respuesta teórica la dio Edsger Dijkstra en su discurso del premio Turing de 1972, *The Humble Programmer* — un texto que deberías leer entero alguna vez, está libre en el archivo de la Universidad de Texas. Dos ideas suyas sostienen esta sección. La primera redefine qué es abstraer:

> «The purpose of abstracting is not to be vague, but to create a new semantic level in which one can be absolutely precise.»
> («El propósito de abstraer no es ser impreciso, sino crear un nuevo nivel semántico en el que se puede ser absolutamente preciso.» — traducción propia. Dijkstra, EWD340, 1972.)

Subir de abstracción no es saber menos: es ser preciso sobre *otras cosas*. El programador de FORTRAN era preciso sobre fórmulas en vez de sobre registros; el de SQL, sobre relaciones en vez de sobre índices de disco; tú, cuando diriges un agente, tienes que ser preciso sobre intenciones, restricciones y criterios de verificación en vez de sobre bucles `for`. La precisión no desaparece con la abstracción: se muda. Quien cree que la nueva capa le exime de ser preciso — quien escribe prompts vagos y acepta lo que salga — no está trabajando en un nivel de abstracción más alto; simplemente ha dejado de trabajar. Y la segunda idea de Dijkstra explica por qué las herramientas importan tanto:

> «The tools we are trying to use and the language or notation we are using to express or record our thoughts, are the major factors determining what we can think or express at all!»
> («¡Las herramientas que intentamos usar y el lenguaje o notación con que expresamos o registramos nuestros pensamientos son los factores principales que determinan qué podemos pensar o expresar en absoluto!» — traducción propia, misma obra.)

Las herramientas no son neutras: moldean el pensamiento de quien las usa. Una generación que aprenda a programar *solo* conversando con modelos pensará distinto — para bien y para mal — que una que depuró punteros. Por eso este curso insiste tanto en abrir las cajas: no por nostalgia del nivel de abajo, sino porque, como veremos en la sección 3, hay una diferencia enorme entre *no necesitar* mirar debajo de la abstracción y *no poder* hacerlo.

## Qué tiene de distinto esta ola (y qué no)

Seamos rigurosos por ambos lados, que es lo que distingue un curso de un panfleto. Lo que esta ola tiene en común con todas las anteriores: promete eliminar la programación atacando el coste de producir código; genera desconfianza en los veteranos y entusiasmo sin frenos en los recién llegados; y desplaza el criterio hacia arriba en vez de eliminarlo. Lo que tiene de genuinamente distinto — y negarlo sería tan poco riguroso como el pánico —: primero, es la primera herramienta de la historia **no determinista** (el mismo encargo puede producir resultados distintos, como verás hacer al agente de Nadia dos veces seguidas en la sección 4; los compiladores jamás hicieron eso, y esta propiedad lo cambia casi todo, de los tests a la confianza); segundo, opera en lenguaje natural, con lo que la frontera entre «especificar» y «programar» se difumina; y tercero, no se limita a traducir lo que tú decides — puede *decidir* pasos intermedios, como decidió el Autopilot que aquel test flaky era un problema de zonas horarias. Las olas anteriores automatizaron la traducción del criterio. Esta es la primera que imita el criterio mismo. Por eso el resto del curso no va de cómo escribir prompts: va de dónde debe vivir el criterio cuando la máquina aparenta tenerlo.

## Para llevar

- Desde 1954, cada gran salto de herramientas (compiladores, 4GL, CASE, no-code, LLM) ha venido acompañado del anuncio del «fin del programador». Todas las veces anteriores, el oficio no desapareció: subió de nivel de abstracción y el criterio se desplazó.
- La desconfianza ante el código generado por máquina es tan vieja como Hopper y su compilador, y nunca se resolvió con fe: se resolvió con verificación.
- Brooks (*No Silver Bullet*): lo difícil del software es lo esencial — especificar, diseñar, verificar el constructo conceptual —, no lo accidental — teclearlo. El riego fantasma fue un fallo esencial ejecutado con perfección accidental.
- Dijkstra: abstraer no es ser vago, es ser preciso en un nivel nuevo. Dirigir agentes exige tanta precisión como programar; solo cambia sobre qué.
- Esta ola comparte el patrón histórico, pero añade tres novedades reales: no determinismo, lenguaje natural como interfaz, e imitación del criterio (no solo de la traducción). Tomarse en serio ambas mitades — el patrón y la novedad — es la posición del ingeniero.

## Para profundizar

- *Software Engineering: Report on a conference sponsored by the NATO Science Committee* (Garmisch, 1968), eds. Naur & Randell — PDF libre en el archivo de Brian Randell (Universidad de Newcastle). El acta fundacional del oficio; se lee sorprendentemente bien.
- E. W. Dijkstra, *The Humble Programmer* (EWD340, 1972) — libre en el archivo EWD de la Universidad de Texas. Veinte páginas que valen un máster.
- F. P. Brooks, *No Silver Bullet* (1986) — búscalo junto con su secuela *«No Silver Bullet» Refired* (en *The Mythical Man-Month*, ed. aniversario), donde el propio Brooks revisa sus predicciones.
- B. Randell, *Fifty Years of Software Engineering* (arXiv:1805.02742, 2018) — acceso abierto; el medio siglo contado por un testigo de Garmisch.
- *Preliminary Report: FORTRAN* (IBM, 1954) — en softwarepreservation.org (Computer History Museum), por el placer arqueológico de leer la promesa original.
