El nombre lo puso Paca, sin querer.

Fue un martes de mayo, en la visita mensual que Élia había instituido después del riego fantasma —«caras humanas una temporada», había pedido Paca, y Élia lo había convertido en costumbre—. Estaban en la acequia madre viendo trabajar a la cuadrilla de limpieza: seis hombres y mujeres con palas y capazos, sacando lodo y cañas del cauce antes de la campaña de verano, cada uno a su tramo, un capataz recorriendo la fila.

—Mira que sois raros los informáticos —dijo Paca, observando a Tomás, que fotografiaba una compuerta—. Tenéis máquinas que escriben solas y os dan miedo. Esto de aquí lleva funcionando quinientos años. —Señaló la fila con la barbilla—. Cada peón a su tramo, con su herramienta, y ninguno decide por su cuenta dónde se rompe un caño. Para decidir está el capataz, y para el capataz está la comunidad. El día que montéis vuestras máquinas así, me avisáis.

Tomás bajó el móvil muy despacio.

—Paca —dijo—, me acaba usted de ahorrar tres reuniones.

Así que cuando aquella semana montaron el primer agente de trabajo real de Vega —uno solo, para empezar, aunque el plan era una flota—, en el repositorio nuevo el README abría con una foto de la acequia y una palabra: **CUADRILLA**.

---

Construir el arnés les llevó tres semanas, y lo primero que descubrieron fue que casi todo lo que necesitaban ya lo sabían hacer. Era, como había dicho Tomás, un lunes cualquiera: entornos, permisos, registros, pruebas. Lo nuevo no eran las piezas; era a quién se le aplicaban.

La primera pieza fue la jaula. Ningún agente de la Cuadrilla trabajaba sobre el sistema real: cada tarea arrancaba en un contenedor desechable, con una copia del repositorio, sin credenciales de producción y sin salida a la red salvo la lista blanca imprescindible. Tomás diseñó aquello con un placer casi artesanal, y con un principio que repetía como un martillo: «la seta de emergencia no se negocia». Si algo olía raro, se tiraba el contenedor entero y no había nada que limpiar.

La segunda pieza fueron los permisos, y ahí la discusión fue larga y buena. Bruno defendía darle al agente el máximo («si le atamos las manos, ¿para qué lo queremos?»); Tomás, el mínimo («empezamos en cero y vamos soltando cuerda cuando se la gane»). Ganó Tomás, pero fue Nadia quien encontró la formulación que acabó escrita en la pared, junto al mapa:

**Leer, casi todo. Proponer, todo. Ejecutar, lo listado. Mergear, jamás.**

La Cuadrilla podía leer el código, los tests, la documentación, las incidencias. Podía proponer lo que quisiera: sus propuestas eran pull requests, como las de cualquier compañero. Podía ejecutar las herramientas de su lista —compilar, correr tests, linters, levantar el entorno de pruebas— y ninguna más. Y el botón de merge, sencillamente, no existía en su mundo: eso quedaba al otro lado de la frontera, en el lado de los humanos. La diferencia con Corvus cabía en una frase y Élia la dijo en la retro: «El Autopilot tenía nuestros permisos. La Cuadrilla tiene los suyos.»

La tercera pieza fue la más humilde y la que más les cambió el trabajo: un fichero de texto. Se llamaba `AGENTS.md`, estaba en la raíz del repositorio, y era —Nadia lo explicó así— «el README que siempre debimos escribir, solo que ahora lo lee alguien que hace caso». Ahí fue a parar, destilado, todo lo que habían aprendido en la reconquista del desván: que las horas del planificador son horas de acequia y no se normalizan jamás (con el enlace al documento de los offsets y al acta del 74); que los tests de válvulas se ejecutan siempre contra el simulador y nunca contra hardware; que el módulo de informes tiene tres consumidores que no aparecen en el código; cómo se ejecuta la suite, qué comandos existen, qué está prohibido tocar sin abrir discusión.

—¿Os dais cuenta? —dijo Élia una tarde, releyéndolo—. Llevábamos años sin escribir esto *para personas*. Ha tenido que venir una máquina a leernos para que documentemos la casa.

—Es que la máquina nos ha quitado la excusa —dijo Nadia—. Con un compañero nuevo siempre piensas «ya se lo contaré cuando pregunte». Esta no pregunta en la máquina de café. O está escrito, o no existe.

Y la cuarta pieza fue la que Tomás bautizó, inevitablemente, como *los sentidos*: la batería de comprobaciones automáticas que le decía al agente, en cada vuelta del bucle, si iba bien o mal. Los tests, el linter, los tipos, el simulador de la red de riego. Aquello ya existía a medias —era el CI de siempre—, pero trabajar con la Cuadrilla les obligó a algo que el CI de siempre perdonaba: que fuera *rápido* y que fuera *honesto*. Un test flaky, descubrieron, no era ya una molestia: era un sentido que miente, y un agente con un sentido que miente es exactamente la historia del 14 de marzo. La caza de tests intermitentes que Bruno llevaba meses posponiendo se convirtió en la primera tarea de la temporada, y —justicia poética— se la asignaron a la propia Cuadrilla, con Bruno de revisor.

—Me está arreglando mis flakys —informó Bruno a la semana, entre la admiración y la ofensa—. Y me ha dejado un comentario diciendo que uno de mis tests «no verifica nada al asertar sobre un mock». Tiene razón. La odio.

---

La prueba de fuego llegó en junio, y no la diseñó nadie: la trajo el azar, como las buenas pruebas.

Un sábado por la mañana, el sensor de presión del hidrante 12 empezó a mandar lecturas absurdas —picos de veinte bares en una red que trabajaba a cuatro— y el sistema de alertas, correctamente, se puso a gritar. La Cuadrilla, que tenía entre sus tareas «investigar alertas de telemetría y proponer diagnóstico», arrancó su contenedor, miró los datos, miró el código y abrió un pull request en veinte minutos. El diagnóstico era impecable: el driver del sensor interpretaba mal un valor centinela que el fabricante usaba para señalar «lectura inválida»; proponía filtrar el centinela y añadía la explicación con enlaces a la hoja de datos del fabricante, que había encontrado ella sola en la documentación del repositorio.

Y el arnés dijo que no.

No al contenido: al procedimiento. La política de la Cuadrilla exigía que todo cambio en drivers de hardware llegara acompañado de un test que reprodujera el fallo, y el PR no lo traía —el agente había verificado el arreglo a mano, contra los datos del sábado, pero no había dejado la trampa puesta para que el bug no volviera—. El check se puso rojo, el PR quedó marcado como borrador, y el lunes por la mañana el equipo se encontró la escena completa en el registro: el diagnóstico, la propuesta, el rechazo automático y la nota del agente en el hilo del PR: *«Bloqueado por política: falta test de regresión para cambio en driver. Preparando test con los datos capturados del incidente.»* Segundo commit, test incluido, checks en verde. A las 9:40, Tomás lo revisó —leyó el diff entero, línea a línea, como leía todo— y mergeó.

En la retro de aquella semana, Élia proyectó el hilo del PR al lado de una captura vieja: el panel de Corvus del 14 de marzo, el candado elegante, el «Root cause identified ✓».

—Mismo tipo de bicho dentro —dijo—. Puede que hasta el mismo modelo, quién sabe. Mirad la diferencia. No está en la inteligencia: está en la casa que le hemos construido. Uno trabajaba a oscuras con nuestras llaves en el bolsillo. La otra trabaja en una jaula de cristal, con sus herramientas contadas, y cuando se salta una norma de la casa, la casa se lo dice *antes* de que el error llegue al agua. —Se volvió hacia el equipo—. ¿Alguien echa de menos el panel verde?

Nadie lo echaba de menos. Aunque fue Bruno, cómo no, quien le puso la posdata a la temporada:

—Solo digo una cosa. Todo esto es precioso, jaulas, sentidos, el fichero mágico… pero el noventa por ciento del carácter de la Cuadrilla sigue estando en los prompts que le escribimos. Y los prompts los redacto yo un poco como me sale, la verdad. El del resumen diario de incidencias lo retoqué el jueves y quedó fino, fino.

—¿Lo retocaste dónde? —preguntó Nadia, con un principio de escalofrío profesional—. ¿En qué commit?

—¿Commit? —Bruno parpadeó—. Está en un Google Doc.

El silencio que se hizo en la sala fue de los que preceden a las secciones nuevas de un curso.

*Día 95*, escribió Nadia aquella noche. *El arnés funciona. Hoy hemos descubierto que la pieza más influyente del sistema vive en un Google Doc, sin historial, sin revisión y sin tests. Tomás dice que eso en su gremio se llama «llevar la máquina con un destornillador metido en el relé». Mañana hablamos.*

---

*En la teoría de esta sección: qué es exactamente un arnés — todo lo que no es el modelo — y cómo se diseña uno con criterio de ingeniero: entornos desechables, permisos mínimos, AGENTS.md como documentación operativa, y los feedback loops (tests, linters, simuladores) como los sentidos del agente. Con las fuentes de quienes están definiendo esta disciplina ahora mismo — y con la tradición de treinta años de bancos de pruebas que Tomás reconoció a la primera.*
