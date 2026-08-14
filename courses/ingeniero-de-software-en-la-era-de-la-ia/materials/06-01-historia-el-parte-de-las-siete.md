Todas las mañanas a las siete, la Cuadrilla escribía el parte.

Era, según Paca, lo mejor que Vega había hecho nunca, incluida la app entera: un mensaje corto, en cristiano, que resumía la noche de la red de riego. *Presiones normales en toda la red. El sector 4 completó su tanda a las 5:50. El caudalímetro del hidrante 9 dio lecturas dudosas entre las 2 y las 3; ya lo estamos mirando. Hoy riegan los sectores 2 y 5.* Los regantes lo leían en el desayuno; el grupo de la comunidad, antes un avispero de fotos borrosas de compuertas y teorías cruzadas, se había vuelto un lugar casi apacible. El parte de las siete había hecho por la confianza más que tres años de gráficas.

Lo escribía un flujo sencillo: un script juntaba la telemetría de la noche, las alertas y el estado de las tandas, y un prompt cuidadosamente redactado le pedía al modelo el resumen en el tono de la casa: claro, sin alarmismo, sin tecnicismos, sin ocultar nada. Aquel prompt había ido puliéndose durante meses. Vivía —el equipo entero lo sabía ya, con incomodidad retrospectiva— en un Google Doc titulado «Prompt parte diario (BUENO) v3 FINAL este».

El jueves 11 de junio, Bruno lo había retocado. Nada dramático: un párrafo nuevo para que el parte destacara «solo lo relevante para el regante, evitando ruido técnico que no afecte al riego del día». El resultado de aquella tarde le pareció más limpio, más profesional. Lo dio por bueno y lo pegó en el documento, encima de la versión anterior, que dejó de existir en ese momento porque los documentos de Google no entierran: incineran.

Los partes siguieron saliendo a las siete, impecables de tono. Y durante dos semanas, nadie —ni humano ni máquina— notó lo que faltaba.

---

Se enteraron por Paca, claro.

—Oye, hija —le dijo a Nadia por teléfono, un lunes de julio—, ¿vosotros habéis arreglado lo de la presión del ramal del norte? Lo digo porque Andrés, el de los caquis, dice que el riego le llega flojo desde hace lo menos dos semanas, y en los partes no sale nada de nada. Y me extraña, porque antes salía hasta cuando estornudaba un manómetro.

Nadia miró la telemetría con el teléfono aún en la mano. Ahí estaba: caídas de presión intermitentes en el ramal norte, modestas pero constantes, desde finales de junio. El sistema de alertas las había registrado todas, obediente. Y el parte de las siete no había mencionado ni una.

Reunió el histórico y lo repasó parte a parte, con el estómago encogido. La cosa era peor que un fallo: era una *media verdad estadística*. Algunos días la incidencia de presión aparecía, breve, al final. Otros días —la mayoría— el modelo la clasificaba, con su nuevo criterio de «evitar ruido técnico que no afecte al riego del día», como omisible: la presión baja no impedía regar, solo regaba peor. Ningún parte mentía. Todos juntos, sí.

—A ver si lo entiendo —dijo Tomás en la reunión de urgencia, con la calma peligrosa del 14 de marzo—. ¿Quién aprobó el cambio del prompt?

—Nadie —dijo Bruno, gris—. No hay… no tenemos aprobación para eso. Es un documento. Lo edité y ya.

—¿Y la versión de antes?

—No está. Escribí encima.

—¿Y cómo comprobaste que el cambio no rompía nada?

—Lo probé. —Bruno oyó cómo sonaba aquello y se corrigió—: Lo probé *una vez*. Generé el parte de esa tarde, me gustó, lo di por bueno. —Se frotó la cara con las dos manos—. Con una ejecución. De un sistema que cada vez sale por un camino. Me sé la teoría, Tomás, me la sé desde el día del folio de flechas. Es que no… no me pareció *código*. Era un texto en un documento. Los textos no se despliegan.

—Ese texto —dijo Élia, sin crueldad, pero sin anestesia— decide cada mañana qué saben y qué no saben ochocientos regantes sobre el agua de la que viven. Es la pieza de más impacto por línea de todo el sistema. Y la hemos tratado con menos cuidado que el CSS del pie de página, que al menos pasa por un pull request.

El silencio lo rompió Tomás, y lo que dijo se quedó, como tantas cosas suyas, clavado en la pared de la memoria del equipo:

—En el fondo es la misma lección del almendral, ¿no os dais cuenta? En marzo aprendimos que el código sin teoría es peligroso. Hoy aprendemos que la teoría sin ingeniería también. —Contó con los dedos—: Una pieza operativa crítica. Sin control de versiones. Sin revisión. Sin pruebas. Sin vuelta atrás. Si esto se lo hago yo a un PLC de una embotelladora en 1995, me mandan a casa, y con razón. La pregunta no es cómo se nos ha colado. La pregunta es por qué creímos que esta pieza era especial y estaba exenta de las normas de todo lo demás.

—Porque es texto —dijo Nadia despacio, pensándolo mientras lo decía—. Parece una redacción, no una pieza. Y como el resultado varía cada vez, ni siquiera está claro qué significaría «probarla»… —Se detuvo. Ahí estaba, otra vez, la sensación de la pieza encajando—. Espera. Sí que está claro. Es lo que hacemos con todo lo no determinista, desde siempre. No compruebas *la* salida. Compruebas *propiedades* de la salida, muchas veces, y mides. Como los tests de carga. Como el simulador de la red con ruido. Nadie espera que el caudal simulado dé el mismo litro exacto: esperas que se mantenga dentro de la banda.

—Habla en cristiano —pidió Paca… es decir, Bruno.

—Que el parte de las siete necesita su propia suite de tests. Distinta, pero suite. —Nadia ya estaba escribiendo en la pizarra—. Cogemos treinta noches reales del histórico, de todos los sabores: noches tranquilas, noches con avería gorda, noches con avería *pequeña y aburrida* como las del ramal norte, noches con datos corruptos. Para cada una escribimos qué tiene que cumplir su parte, sí o sí, salga por donde salga el modelo: si hubo incidencia de presión, se menciona; si un dato es dudoso, se dice que es dudoso; nunca se promete arreglo sin ticket; largo máximo; tono. Cada vez que alguien toque el prompt —o cambiemos de modelo, apunta esto también— la suite genera los treinta partes, unas cuantas veces cada uno, y comprueba las reglas. Si el nuevo prompt hace desaparecer las incidencias de presión, no hace falta que lo note Andrés el de los caquis dos semanas tarde: lo nota un check rojo en el pull request, dos minutos después de proponer el cambio.

—¿Y el prompt vive…? —preguntó Élia, aunque sabía la respuesta.

—En el repositorio. Junto al código que lo usa, con su historial, su revisión y su suite. Se acabaron los documentos con «FINAL» en el título.

Élia asintió y miró a Bruno, que seguía gris.

—Tuya —dijo.

—¿El qué?

—La suite. El sistema entero de evaluación. Tuya y de Nadia. El que la lía la desface, y de paso se convierte en el que mejor entiende del tema en toda la empresa. —Le sostuvo la mirada, y por debajo de la severidad había algo parecido al afecto—. Es lo que Tomás lleva diciéndonos desde marzo, Bruno. No eres malo. Ninguno lo somos. Es peor: somos buenos con las piezas que *parecen* software y descuidados con las que no lo parecen. Y esta época nuestra consiste exactamente en que cada vez más piezas decisivas no lo parecen.

Bruno estuvo dos semanas insoportablemente callado, que en él era el ruido del trabajo serio. La suite quedó preciosa: los treinta escenarios se convirtieron en cuarenta y dos, las reglas deterministas se complementaron con un segundo modelo que puntuaba lo que las reglas no sabían medir —claridad, tono— con instrucciones de puntuación escritas y versionadas a su vez, y el día que la primera regresión de verdad fue cazada por un check rojo (un retoque inocente que hacía prometer al parte «lo revisaremos hoy mismo», cosa que nadie había autorizado a prometer), Bruno imprimió la captura y la clavó en el corcho, donde otros clavan la primera factura.

Encima escribió, con rotulador grueso: **«NO ES UNA REDACCIÓN. ES UNA PIEZA.»**

*Día 117*, apuntó Nadia. *Hoy el parte de las siete ha vuelto a contar las averías aburridas. Paca dice que Andrés dice que ya llega bien el agua. He pensado una cosa leyendo el diff del prompt: hace cuatro meses ni se nos habría ocurrido pedirle perdón a un regante por un párrafo. El software ya no se acaba donde se acaba el código, y me parece que esa frontera nueva es donde va a vivir nuestro oficio a partir de ahora.*

---

*En la teoría de esta sección: los principios atemporales aplicados a las piezas que no parecen software — el prompt como artefacto versionado y revisado, las specs como contrato, y las evals: cómo se prueba con rigor un componente que nunca responde dos veces igual, qué merece esa inversión y qué no, y qué puede (y qué no puede) hacer un modelo evaluando a otro.*
