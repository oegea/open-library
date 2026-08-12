La reunión general del lunes duró once minutos y dejó más preguntas que respuestas.

Óscar la abrió sin sentarse, con la consultora externa proyectada en una diapositiva llena de logotipos: doce meses, plan de modernización, «decisiones estructurales» que se anunciarían «en las próximas semanas». Ninguna concreción. Al acabar, mientras la gente salía de la pecera con murmullo de fondo, Júlia le preguntó a Denís qué significaba «decisiones estructurales» en el idioma de las diapositivas.

—Significa que están decidiendo si ATLAS se arregla o se tira a la basura y se hace de nuevo. —Denís se dejó caer en su silla—. Y te doy un consejo gratis, novata: cuando eso se discuta, tú no digas la palabra «reescritura» delante de Gabriel.

—¿Por qué?

Denís abrió la boca, la cerró, y por primera vez desde que Júlia lo conocía pareció elegir las palabras con cuidado.

—Porque aquí ya se hizo una vez. Antes de mi época. Salió… mal. Mal de verdad, de las de casi cerrar la empresa. Es lo único que sé, porque es lo único que se cuenta. Bueno, eso, y que no se cuenta. —Se encogió de hombros—. Pregúntale al póster de Star Wars, que lleva aquí más años que nadie.

Júlia pensó en el repositorio `faro`, en su última fecha de commit, ocho años atrás, y sintió que dos piezas sueltas se rozaban sin llegar a encajar. No dijo nada. En Meridian, estaba aprendiendo, había una segunda memoria: la que no estaba en ningún repositorio.

---

La petición de Vesta llegó el miércoles por correo, y era, según la propia Vesta, «un cambio menor»: a partir de octubre, las facturas de sus franquiciados debían desglosar el **recargo de equivalencia** — un régimen especial de IVA para minoristas — en una línea separada, con su porcentaje y su base. Marta, la directora comercial, lo trajo personalmente a la mesa de Óscar con la sonrisa de quien trae buenas noticias: «Es solo enseñar un numerito más en la factura, ¿no? Les he dicho que en dos semanas lo tienen».

Óscar miró a Júlia. Júlia, que ya había aprendido a no fiarse de la palabra «solo», abrió el editor y empezó a tirar del hilo. Lo hizo con método, como quien mapea una mazmorra: una hoja de papel, el nombre de cada fichero que había que tocar, y una flecha por cada motivo.

A las siete de la tarde, la hoja se había convertido en tres hojas pegadas con celo, y el recuento daba **veintitrés ficheros**.

No era broma ni exageración. Para enseñar «un numerito más» había que tocar: `calc2()`, claro, que calculaba el recargo *mezclado* con el IVA en una sola cifra imposible de separar después; la tabla `facturas`, cuyo campo `impuestos` guardaba la suma ya fundida — el dato individual se destruía en el momento de nacer —; la plantilla PDF; la plantilla HTML del portal; el export contable a formato SEPA; el *otro* export contable «formato Vesta 2019» que nadie recordaba por qué existía; el informe de descuentos; los cuatro listados donde aparecían totales de impuestos; y una cascada de ficheros intermedios que copiaban datos de un formato a otro añadiendo o quitando campos como en el juego del teléfono estropeado. En la hoja de Júlia, las flechas formaban una tela de araña con un nudo gordo en el centro: todos los caminos pasaban por `calc2()` y por la tabla `facturas`.

Y había algo más, algo que le costó una hora ver porque era demasiado absurdo: el PDF **no recibía los impuestos de la base de datos**. Los *recalculaba*. Otra copia de la lógica, la cuarta que encontraba, esta vez incrustada en la plantilla, «porque en 2019 hubo un problema de rendimiento y era más rápido así», según un comentario que mentía a medias.

Júlia se echó atrás en la silla y contempló la tela de araña completa. Y entonces le vino, con una claridad casi física, la imagen que buscaba desde hacía semanas: ATLAS no era un dragón. Era **una máquina de Rube Goldberg construida por quince años de gente con prisa**: para tostar el pan, una bola rueda por un canalón, tira una ficha de dominó, la ficha despierta a un gato, y el gato, al huir, tensa la cuerda de la tostadora. Funcionaba — llevaba quince años tostando pan —, pero pedirle «ahora tuesta dos rebanadas» significaba renegociar con la bola, la ficha, el gato y la cuerda. *Un cambio pequeño en el problema* se convertía en *un cambio enorme en el sistema*, porque cada concepto del negocio — «impuesto», «descuento», «total» — estaba desparramado por veinte sitios, y cada fichero sabía demasiado sobre los asuntos de los demás.

Esa noche, el capítulo `03-el-acoplamiento.md` del cuaderno de faro empezaba así:

> *Hay dos números que explican este sistema mejor que cualquier diagrama. Primero: cuántos sitios hay que tocar para cambiar una cosa. Aquí, para cambiar cómo se muestra un impuesto: más de veinte. Se llama acoplamiento, y es la medida de cuánto sabe cada pieza sobre las demás. Segundo: cuántas cosas distintas viven en un mismo sitio. `calc2()` calcula, valida, formatea, registra y decide. Se llama falta de cohesión, y es la medida de cuánto cajón de sastre hay.*
> *La regla que lo resume todo la aprendí tarde y la escribo para no olvidarla: las cosas que cambian juntas deben vivir juntas; las que cambian por motivos distintos deben vivir separadas. Cada pieza debería tener una sola razón para cambiar, un solo jefe al que rendir cuentas. Cuando una pieza tiene cinco jefes, cada uno tira de ella hacia un lado, y acaba como acaba todo lo que tiene cinco jefes.*
> *Mañana intentaré explicárselo a O. con el ejemplo del enchufe: la lámpara no está soldada a la pared. Hay un contrato en medio — el enchufe — y por eso puedes cambiar la lámpara sin llamar a un electricista. En este sistema está todo soldado. Todo. Y luego nos extraña que cualquier cambio necesite un electricista, tres semanas y una novena a Santa Bárbara.*

*Intentaré explicárselo a O.* Júlia se quedó mirando la inicial. Ocho años después, «O.» dirigía el departamento técnico de Meridian y estaba a punto de tomar una «decisión estructural». Fuera lo que fuera lo que Silvia intentó explicarle entonces, no parecía haber funcionado.

---

El jueves, Júlia hizo algo impropio de una junior con dos meses de empresa, y lo hizo precisamente porque nadie le había explicado todavía que era impropio: pasó a limpio la tela de araña — veintitrés cajas, flechas rojas para «recalcula por su cuenta», flechas negras para «lee datos de» — y la colgó en la pared de la cocina, al lado de la máquina de café, con un pósit que decía: *«Esto es lo que cuesta añadir una línea a una factura. No es culpa de nadie. Es el mapa de la casa.»*

El efecto superó cualquier cálculo. A las once, había corrillo. A las doce, alguien de soporte había añadido una flecha que faltaba — «el portal del cliente también recalcula, lo sé porque lo sufro» — con un rotulador de otro color. A la una, Marta la estudiaba muy seria mientras el café se le enfriaba en la mano, y murmuró la frase de la semana: «Ahora entiendo por qué "dos semanas" les hace reír».

Y a las cuatro, Óscar se plantó delante del mapa con los brazos cruzados y estuvo cinco minutos sin decir nada.

—¿Lo has hecho tú? —preguntó por fin.

—Sí. Es la petición del recargo de equivalencia. Veintitrés ficheros.

—Ya. —Óscar asintió despacio, sin dejar de mirar la telaraña. Cuando se volvió hacia Júlia había en su cara algo nuevo, una mezcla de respeto y de decisión tomada que a ella le inquietó sin saber por qué—. Es el mejor argumento que he visto en años. Guárdalo. Lo vas a volver a ver pronto.

Se fue pasillo abajo, hacia la pecera, sacando el móvil del bolsillo. Júlia miró el mapa, miró la espalda de Óscar, y tuvo la sensación exacta de haber fabricado un arma sin saber para qué bando.

El lunes siguiente apareció, clavada con chinchetas junto a su telaraña, una segunda lámina: un diagrama limpio, de cajas ordenadas y flechas paralelas, con un título en letra de imprenta — **«ATLAS NG: propuesta de nueva plataforma»** — y un logo de la consultora externa en la esquina.

Debajo, en el hueco entre las dos láminas, alguien había pegado un pósit amarillo sin firma:

*«El segundo dibujo siempre es más bonito. Pregunta por qué.»*

Júlia lo leyó tres veces. La frase sonaba exactamente al cuaderno de faro: la misma manera seca y cariñosa de avisar de un peligro. Pero el cuaderno era un repositorio Git abandonado hacía ocho años, y los repositorios no escriben pósits.

Alguien más, en aquella oficina, conocía el faro.
