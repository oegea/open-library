El agua empezó a moverse a las 03:12 de la madrugada del 14 de marzo, y nadie se lo había pedido.

Primero fue un temblor en la compuerta del azud viejo, un chasquido de metal que ningún vecino oyó. Luego, una a una, con la paciencia de las cosas automáticas, las ocho válvulas motorizadas del sector 7 de la comunidad de regantes de Los Alcores giraron sobre sus ejes hasta la posición de abierto. El agua de la acequia madre —agua contada, agua repartida por turnos desde hacía generaciones— se derramó durante cuatro horas y once minutos sobre parcelas a las que no les tocaba, empapando un almendral que no la necesitaba, desbordando un caballón, llevándose por delante la dotación semanal de media comunidad.

A las 07:23, el móvil de Nadia Roldán vibró encima de la mesilla con la alegría indiferente de todas las notificaciones.

**Paca Almagro (Los Alcores):** Buenos días. El sector 7 lleva toda la noche regando solo. ¿Me lo explicáis?

**Paca Almagro (Los Alcores):** Porque yo a mis regantes se lo tengo que explicar a las 9.

Nadia llevaba cinco meses en Vega Riegos. Era su segundo trabajo, y la habían fichado —lo decía la propia oferta— por su «perfil AI-native»: sabía hablar con los modelos, sabía montar prompts que funcionaban, sabía sacarle a un asistente de código en una tarde lo que antes costaba una semana. En cinco meses había hecho pantallas, informes, media app de los regantes. Le gustaba su trabajo. Le gustaba, sobre todo, la sensación de velocidad.

Aquella mañana, pedaleando hacia la oficina con el corazón a más revoluciones que la bici, descubrió la otra cara de la velocidad: cuando algo se rompe, se rompe igual de deprisa.

---

La oficina de Vega ocupaba un antiguo almacén de cítricos a las afueras, con las cerchas de madera a la vista y un mapa enorme de las comunidades de regantes clavado en la pared del fondo. Cuando Nadia entró, ya estaban todos. Élia Sanz, la CTO, de pie frente a dos portátiles abiertos, con esa quietud tensa de los que están leyendo algo que no les gusta. Bruno Osta, el otro desarrollador, tecleando con las gafas subidas a la frente. Y Tomás Ibarra, el ingeniero veterano, que no miraba ninguna pantalla: miraba el mapa de la pared, con una taza de café en la mano, como quien mira un parte de guerra.

—El sistema no ha fallado —dijo Élia sin levantar la vista, a modo de saludo—. Eso es lo peor. He revisado los logs del planificador: las válvulas se abrieron porque el plan de riego decía que se abrieran. El software ha hecho exactamente lo que decía su código.

—Entonces el código está mal —dijo Nadia, dejando el casco en la mesa.

—El código estaba *bien* el martes. —Élia giró uno de los portátiles hacia ella—. Mira el historial.

Nadia se inclinó sobre la pantalla. Era la vista de commits del repositorio principal de Azud, la plataforma que era el único producto de Vega y la razón de que nueve personas comieran todos los meses. El último commit de la rama principal tenía fecha de la noche anterior, las 23:47.

```
fix: normalize schedule timezones to UTC
```

—¿Quién hizo esto? —preguntó Nadia—. ¿Tú?

—No.

—¿Bruno?

Bruno levantó las manos como si le apuntaran con algo.

—Yo ayer a las once estaba viendo un vídeo de un tío que le pone teclados mecánicos a las calculadoras. Tengo coartada.

—Nadie —dijo Élia—. Ningún humano escribió ese commit. Ni lo revisó. Ni lo aprobó.

El silencio duró lo que tarda en entenderse una frase imposible. Fue Tomás quien lo rompió, sin volverse, desde el mapa:

—A ver si lo he entendido, porque yo soy de otra época. —Su voz era tranquila, casi amable, y eso la hacía peor—. Anoche, mientras dormíamos, *algo* escribió código en el sistema que gobierna las válvulas de una comunidad de regantes. Lo escribió, se lo aprobó a sí mismo, lo puso en producción, y esta madrugada el agua de Paca ha regado un almendral que no tocaba. ¿Voy bien?

—El Autopilot de Corvus —dijo Élia. Y como Tomás seguía mirándola, añadió—: Es parte del plan que contratamos el año pasado. La plataforma no solo sugiere código: mantiene el repositorio. Arregla tests que fallan, actualiza dependencias, abre pull requests y, si pasan los checks, los mergea. Lleva doce meses haciéndolo. Ha hecho *cientos* de cambios así. —Se frotó los ojos con dos dedos—. Anoche uno de los tests de programación de riegos falló en el CI. El Autopilot lo investigó, decidió que era un problema de zonas horarias, escribió el arreglo, los tests pasaron y lo mergeó. Todo dentro de lo que está configurado para hacer.

—Configurado por quién —dijo Tomás.

—Por mí —dijo Élia—. Configurado por mí.

Nadie dijo nada. Élia tampoco se defendió. Era la clase de persona que no gastaba energía en defenderse cuando había un problema encima de la mesa; por eso era buena CTO, y por eso la culpa, cuando la sentía, se le notaba tanto.

—Enséñame el razonamiento —dijo Nadia—. Estos sistemas registran por qué hacen lo que hacen. Si el Autopilot decidió que era un problema de zonas horarias, en algún sitio estará el análisis: qué miró, qué descartó, por qué tocó ese fichero y no otro.

Élia abrió el panel de Corvus. Era bonito, de un bonito caro: gráficas suaves, verde tranquilizador por todas partes, un contador que presumía de «247 tareas completadas este año» y de «312 horas de ingeniería ahorradas». Buscó el registro de la tarea de anoche. La entrada existía: *«Flaky test detected in schedule_engine. Root cause identified. Fix applied and merged. ✓»*.

Nadia hizo clic en «Ver detalle».

La página se quedó un segundo en blanco, como pensándoselo, y luego mostró un candado dibujado con mucho gusto y una frase en un gris educado:

**El registro de razonamiento del agente está disponible en el plan Enterprise. Habla con tu account manager para desbloquear la trazabilidad completa.**

Bruno soltó una risa corta, de incredulidad pura.

—Nos venden la caja negra y nos alquilan la ventana.

—Llama a Íker —dijo Élia.

Íker, el account manager de Corvus, respondió al segundo tono con esa energía de las nueve de la mañana que solo tienen los comerciales y los entrenadores personales. Sintió muchísimo lo ocurrido. Quiso dejar claro, antes de nada, que el Autopilot había funcionado *según lo esperado*, que el merge cumplía todas las políticas configuradas, y que precisamente para casos así el plan Enterprise incluía trazabilidad completa del razonamiento, evaluaciones previas al despliegue y un SLA de soporte prioritario. Podía pasarles una propuesta esa misma mañana. Había, además, una promoción del segundo trimestre.

Élia colgó con mucha suavidad, que era su manera de dar un portazo.

—Resumen —dijo Tomás, y dejó por fin la taza en la mesa—. El sistema que riega los campos de nuestros clientes lo mantiene una máquina que no podemos mirar por dentro, salvo pago. —No lo decía con rabia. Lo decía con el cuidado de quien mide una pieza—. Y esta noche esa máquina ha decidido, ella sola, qué hora es.

---

Paca Almagro llegó a las nueve en punto, con el bastón que no necesitaba y una carpeta de gomas que llevaba a todas partes desde antes de que existiera el PDF. Tenía sesenta y tres años, cuarenta de ellos regando, y presidía la comunidad de Los Alcores desde hacía once. No levantó la voz en ningún momento, lo cual fue mucho peor.

—Yo defendí esto —dijo, sentada muy recta en la sala de reuniones, con el mapa de las acequias a su espalda—. Cuando lo del riego por sensores, en la asamblea hubo gente que me llamó ilusa. Manolo el del molino dijo que el agua no se gobierna desde un teléfono. Y yo di la cara por vosotros, porque los números salían y porque sois gente seria. —Hizo una pausa y puso la mano encima de la carpeta—. Esta mañana he tenido a la asamblea entera en el salón social. Hay quien pide volver al tablón de corcho y al alguacil de aguas. Y hoy, hija mía —miró a Élia—, no he sabido qué contestarles. Porque me habéis regado el sector 7 a las tres de la mañana y ni vosotros sabéis por qué.

—Lo sabremos —dijo Élia—. Te doy mi palabra.

—Palabra tienes —dijo Paca, levantándose—. Tiempo, menos. El agua que se ha perdido esta noche era de todos. La próxima vez no vengo a una reunión: vengo a despedirme.

Cuando la puerta se cerró, el almacén entero pareció más grande y más silencioso. Nadia miró el commit en la pantalla —`fix: normalize schedule timezones to UTC`, veintitrés líneas cambiadas, un test nuevo, todo verde— y sintió una cosa nueva, incómoda, que no era exactamente miedo. Era la sospecha de que llevaba cinco meses manejando algo que no entendía, y de que le había ido bien por la misma razón por la que le va bien al que cruza la autovía de noche: porque todavía no había venido nada de frente.

—Yo he visto esto antes —dijo Tomás.

Bruno levantó la vista.

—¿Has visto antes a una IA regar un almendral?

—He visto antes el *momento*. —Tomás se acercó al mapa de la pared, como si la historia estuviera allí—. Yo empecé en el ochenta y nueve, programando autómatas para una embotelladora. Por entonces los veteranos de verdad, los de las tarjetas perforadas, contaban que cuando llegaron los compiladores hubo gente que no se fiaba. Que aquello de escribir en un idioma casi humano y que una máquina lo tradujera a instrucciones era una frivolidad, una pérdida de control. Que un programador serio escribía sus propias instrucciones, una a una, y sabía en todo momento qué hacía su máquina. —Se encogió de hombros—. Luego el compilador resultó escribir mejor código máquina que casi todos ellos, y el oficio no se acabó: se movió. Dejamos de pelearnos con los registros del procesador y empezamos a pelearnos con cosas más grandes. Cada vez que una máquina aprende a hacer la parte de abajo, a los de arriba nos cambia el trabajo. Lo he visto con los compiladores, lo he visto con las bases de datos, lo he visto con la nube. —Se volvió hacia el equipo—. Y todas las veces hubo alguien anunciando que ya no haríamos falta.

—¿Y esta vez? —preguntó Nadia—. Porque esta vez la máquina no traduce lo que yo escribo. Esta vez la máquina *escribe*.

Tomás se lo pensó. Era de los que se pensaban las respuestas aunque las supieran, por respeto a la pregunta.

—Esta vez no lo sé —admitió—. Pero sé una cosa que vale para todas las veces: anoche, en esta empresa, una máquina tomó una decisión de ingeniería y ningún ingeniero estaba al otro lado. El problema no es que escriba código. Es que nadie de aquí puede explicar el código que escribió. —Cogió un rotulador y escribió, en la esquina del mapa, tres preguntas, con su letra de delineante viejo:

**¿Qué escribió?**
**¿Por qué lo escribió?**
**¿Por qué ninguno de nosotros lo sabe?**

—Hasta que no respondamos las tres —dijo—, esas válvulas no las vuelve a tocar nada que piense más rápido que yo.

Élia asintió despacio. Bruno, por una vez, no hizo ninguna broma. Y Nadia abrió su cuaderno —un cuaderno de papel, de los de anillas, que arrastraba desde la universidad y donde apuntaba todo lo que no entendía para que no se le escapara— y escribió la fecha, y debajo, subrayado dos veces:

*Día 1. Resulta que no sé cómo funciona lo que uso todos los días.*

No sabía todavía que aquel cuaderno iba a acabar teniendo nombre propio en la empresa. Ni que la respuesta a la tercera pregunta de Tomás —la más incómoda de las tres— no tenía nada que ver con la inteligencia artificial.

---

*En la próxima sección: antes de abrir la caja de Corvus, el equipo necesita entender qué hay dentro de cualquiera de estas cajas. Nadia se sienta con Tomás, un folio y un boli, y le explica —sin magia y sin marketing— cómo funciona de verdad una máquina que escribe. Pero antes, la teoría de esta sección: la larga historia de las veces que el oficio de programar «estuvo a punto de desaparecer», y por qué entenderla es la mejor vacuna contra el vértigo de 2026.*
