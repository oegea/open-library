El mapa de la pared fue cambiando de color durante abril. Cada tarde, alguien cogía el rotulador verde y repintaba una caja naranja: el motor de válvulas cayó en la primera semana (Tomás lo destripó con el mismo gusto con que desmontaba bombas de riego), los offsets solares de Joel tuvieron por fin su documento —tres páginas, con el acta de 1974 citada como se cita una ley— y hasta el módulo de informes, que nadie recordaba haber escrito, confesó sus secretos tras dos tardes de arqueología.

Fue un trabajo lento, humilde y raramente satisfactorio, como ordenar un desván. Y tuvo un efecto secundario que nadie había previsto: el equipo empezó a hablar distinto. «Eso no lo sabemos» dejó de ser una vergüenza y pasó a ser una coordenada: una caja naranja más, con su nombre y su turno de ser abierta.

Pero quedaba la caja más naranja de todas, y no estaba en su repositorio.

—Corvus —dijo Élia, un lunes, plantándose delante del mapa—. Seguimos pagando por una plataforma que no usamos desde marzo. Toca decidir: o volvemos a activarla, o la cortamos. Y no pienso decidir a ciegas otra vez.

—No podemos abrir la caja de Corvus —dijo Bruno—. Es suya. Está en su nube, detrás de su candado Enterprise.

—Ya. —Élia se volvió hacia Nadia—. Por eso vamos a abrir otra. Nadia: tú montaste agentes en tu trabajo anterior, ¿no? Pequeños, para procesar tickets o algo así.

—Para clasificar incidencias, sí.

—¿Cuánto código era? El agente en sí. El corazón.

Nadia lo pensó.

—¿El corazón? Cincuenta líneas. Sesenta.

Bruno se rio. Tomás no.

—Sesenta líneas —repitió Tomás—. Lo que hace nuestra centralita de válvulas. —Se levantó y despejó la mesa grande con dos gestos, que era su manera de inaugurar los acontecimientos—. Pues se acabó hablar de estas cosas de oído. Viernes por la tarde, aquí, todos. Nadia nos lo escribe delante. Sin plataformas, sin panel bonito, sin humo. Un modelo, un bucle y nuestras herramientas. Quiero ver a la criatura andar en pelotas antes de decidir si le compro un traje.

---

El viernes, Nadia conectó su portátil al proyector con el mismo cosquilleo con que se ataba las zapatillas antes de una vía difícil del rocódromo. Había preparado el terreno con cuidado, y el cuidado era la mitad de la demostración: una carpeta con una copia de los datos de sensores de Los Alcores —una copia, subrayó, en una máquina sin acceso a nada—, y tres funciones de Python normales y corrientes que había escrito por la mañana: una para listar los sensores, una para leer las medidas de un sensor, y una para escribir una nota en un fichero de diagnóstico.

—Esto es todo lo que el agente va a poder hacer —dijo—. Estas tres funciones. No puede tocar válvulas, no puede tocar la red, no puede tocar nada que yo no le haya dado. Eso no es una limitación técnica del modelo: es una decisión mía. Apuntad esto en algún sitio, porque es lo más importante que voy a decir hoy: **un agente puede exactamente lo que sus herramientas le permiten**. Ni más, ni menos.

—Como un autómata —dijo Tomás desde la primera fila—. Puede lo que sus salidas pueden.

—Espérate, que te va a gustar más todavía. —Nadia abrió un fichero vacío y empezó a escribir, hablando mientras tecleaba—. El programa es un bucle. En cada vuelta le mando al modelo la conversación entera: lo que le he pedido, lo que ha hecho hasta ahora y lo que han devuelto sus herramientas. El modelo responde una de dos cosas: o «quiero usar tal herramienta con tales parámetros», o «he terminado, aquí está mi respuesta». Si pide herramienta, la ejecuto yo —mi código, no él—, le pego el resultado a la conversación, y vuelta a empezar. Eso es un agente. No hay más.

Escribió el bucle. Cupo en la pantalla del proyector con sitio de sobra: el while, la llamada al modelo, el if de las herramientas, el diccionario donde cada nombre de herramienta apuntaba a una de sus tres funciones. Cuando terminó, se quedó mirándolo un segundo y le añadió una línea más, un simple print que volcaba por consola cada petición del modelo antes de ejecutarla.

—Y esto —dijo— es la ventana. La que Corvus nos quería alquilar. En mi casa, la ventana es un print.

Lo lanzó. En la consola, con todos mirando, el agente pensó en voz alta. Pidió la lista de sensores. Pidió las medidas del caudalímetro del sector 7, y luego, sin que nadie se lo sugiriera, las del sector 6, «para comparar con un sector no afectado». Encontró la anomalía de la madrugada del 14 de marzo. Escribió en el fichero de diagnóstico un resumen de tres párrafos que era, palabra arriba palabra abajo, el mismo análisis que a Élia le había costado una mañana entera.

Duró un minuto y cuarenta segundos. Nadie dijo nada hasta que el bucle terminó con su código de salida cero, humilde como un script de backup.

—Otra vez —pidió Tomás.

Nadia lo lanzó otra vez. Y aquí vino la segunda lección de la tarde, la que no estaba en el guion: el agente resolvió el problema igual de bien… pero por otro camino. Esta vez empezó por el sector 6, tardó una vuelta más, y el resumen final, correcto también, estaba organizado de otra manera.

—¿Por qué ha hecho distinto? —preguntó Bruno—. Mismo código, mismos datos, misma pregunta.

—Porque el modelo no es una función determinista, es una distribución —dijo Nadia—. Cada respuesta es un muestreo. ¿Os acordáis del folio de flechas? Elige la siguiente palabra entre varias probables, y esa pequeña lotería, repetida mil veces, da caminos distintos. Casi siempre llegan al mismo sitio. Casi. —Dejó que la palabra flotara—. Por eso los tests de toda la vida no bastan con estas cosas, y por eso el «pasó una vez» del Autopilot no significaba nada. Pero eso es tema para dentro de unas semanas. Hoy quedaos con esto: no es magia ni es un misterio insondable. Es una pieza nueva, con propiedades nuevas, y las propiedades se pueden conocer, medir y acotar. Como cuando metimos las electroválvulas, Tomás: hubo que aprenderse sus tiempos de respuesta y sus modos de fallo. Pues esto igual.

Tomás se había levantado y miraba la consola por encima del hombro de Nadia, con las gafas en la punta de la nariz, siguiendo el rastro de peticiones del agente como quien sigue un esquema eléctrico.

—Un autómata con un operario dentro —dijo al fin, a media voz, casi con ternura—. El bucle es el autómata. Lo de dentro es… otra cosa. Un operario muy leído, muy rápido, un poco fantasioso, que no conoce la finca. —Se enderezó—. Y ahora la pregunta del millón, Nadia: el Autopilot de Corvus, el que nos regó el almendral. ¿Qué es, comparado con esto?

—Esto mismo —dijo Nadia—. Con mejor letra. Un bucle como el mío, un modelo como el mío probablemente, y herramientas. Solo que sus herramientas eran nuestro repositorio entero, el CI y el botón de merge. Y la ventana… la ventana era de pago.

El silencio que siguió fue de los que trabajan. Élia lo rompió con la voz de tomar decisiones:

—O sea, que la diferencia entre esta cosita inofensiva y aquello que nos abrió las válvulas no está en la inteligencia. Está en todo lo de alrededor: qué herramientas le das, qué permisos, qué le dejas tocar sin preguntar, qué ventanas tienes para mirarlo.

—El arnés —dijo Nadia.

—¿El qué?

—Es como lo llamo yo. —Se encogió de hombros, un poco cohibida—. En el rocódromo nadie discute si el escalador es bueno. Da igual lo bueno que sea: nadie escala sin arnés. El arnés no escala por ti, no te hace mejor. Hace que caerte no sea morirte. —Señaló la pantalla—. Todo lo que no es el modelo: el bucle, las herramientas, los permisos, el sandbox, el print. Eso es el arnés. Corvus tenía un modelo estupendo con un arnés que no era nuestro y no podíamos ver. Mi propuesta es la contraria: modelos los que sean, los mejores de cada momento, se alquilan y se cambian. El arnés, nuestro. Diseñado aquí, con nuestras reglas, inspeccionable línea a línea.

Élia miró a Tomás. Tomás miró el bucle en la pantalla, sesenta líneas contando los comentarios, y luego el mapa de la pared, donde la caja de Corvus seguía en naranja chillón.

—Yo llevo treinta años haciendo bancos de pruebas para máquinas que no piensan —dijo—. Jaulas, finales de carrera, setas de emergencia, registros de todo. Jamás dejé que un autómata moviera un motor sin saber exactamente qué podía y qué no podía hacer. —Cogió el rotulador verde y lo hizo girar entre los dedos—. Si me estás diciendo que a esta criatura se le puede construir el banco de pruebas… entonces esto ya no es un debate sobre inteligencias artificiales. Es un lunes cualquiera de mi vida laboral.

—Eso te estoy diciendo.

—Pues vamos a construirlo. —Se volvió hacia el equipo—. Y lo vamos a hacer con más cuidado que nadie, porque nuestras herramientas acaban tocando agua. Se llama… ¿cómo se llama esto, oficialmente?

—Hay gente llamándolo *harness engineering* —dijo Nadia—. Ingeniería del arnés.

—Pues mira —dijo Tomás, destapando el rotulador—, por fin una moda de estas con un nombre de cosa seria.

En el cuaderno de asombros, esa noche, Nadia escribió una sola línea, y la subrayó:

*Día 56. La inteligencia se alquila. El arnés se posee.*

---

*En la teoría de esta sección desmontamos la caja del todo: qué es exactamente un agente (spoiler: un bucle, un modelo, herramientas y contexto), escribimos uno funcional en unas decenas de líneas de Python y JavaScript, y aprendemos las palabras de la tribu — herramientas, ventana de contexto, workflows contra agentes, MCP — sin niebla y con las fuentes originales en la mano.*
