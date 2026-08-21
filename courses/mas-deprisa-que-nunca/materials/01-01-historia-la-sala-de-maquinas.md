El jueves que despidieron a Teo, Aurelia batió su récord histórico de velocidad de entrega, y las dos cosas se anunciaron con cuarenta minutos de diferencia.

El récord se anunció primero, en el all-hands de las diez. Toda la empresa en la cafetería de la segunda planta — ciento y pico personas entre presentes y ventanas de videollamada — mirando la pantalla grande donde Víctor Sanz, CTO, cuarenta y un años, camisa impecable y ese entusiasmo suyo de ingeniero converso, pasaba diapositivas del programa Prometeo. Ocho meses antes, Prometeo era una frase en un consejo de administración: «Aurelia será una empresa IA-first». Ahora era esto: un dashboard con curvas subiendo.

—Velocidad de entrega: por cuatro —dijo Víctor, y dejó que la cifra respirara—. No es una estimación. Son datos. Cuatrocientos doce pull requests mergeados la semana pasada. Hace un año eran ciento y pico. El código ha dejado de ser el cuello de botella, señoras y señores. Somos más rápidos que nunca.

Hubo aplausos. Sinceros, además. Nadia Cherkaoui aplaudió también, desde la tercera fila, aunque llevaba semanas con una sensación rara que no sabía nombrar y que aquella diapositiva, por algún motivo, empeoró.

A las once menos veinte, Recursos Humanos citó a cuatro personas en la sala pequeña de la primera planta, la que no tiene ventanas. Una de ellas era Teo Ibarra, veinticuatro años, el otro junior del equipo Petirrojo. El comunicado interno habló de «ajuste selectivo para alinear la estructura con la nueva realidad productiva». Bruno Otero, que llevaba en Aurelia casi desde el principio y en la profesión desde antes de que naciera Teo, lo tradujo sin levantar la vista del teclado:

—La nueva realidad productiva es que a los juniors los escribe una API.

Nadia ayudó a Teo a recoger la mesa. No había mucho: una taza del Levante, un cactus, una libreta cuadriculada con la letra apretada de quien todavía toma apuntes de todo. Teo era de esos. Hacía las preguntas que nadie se atrevía a hacer en las reuniones y luego apuntaba las respuestas.

—Oye, que no pasa nada —dijo Teo, que era el que se iba, consolándola a ella—. Ya encontraré algo. Es solo que… —se quedó un momento con el cactus en la mano—. Llevaba seis meses pidiendo que alguien revisara conmigo el módulo de medicación, para aprenderlo. Todo el mundo estaba siempre a tope. Y ahora resulta que sobro por no saber lo que nadie tuvo tiempo de enseñarme.

Nadia no encontró nada útil que decir. Le dio un abrazo y el cactus se les clavó a los dos.

---

Para entender la sensación rara de Nadia hay que describir su jornada de aquellos meses, porque no se parecía a la jornada para la que había estudiado.

A las 9:04 abría el panel de revisión. Los agentes — «los prometeos», los llamaba Bruno, y el nombre había cuajado — trabajaban de noche. Cada mañana, la cola: catorce, dieciocho, veintidós pull requests generados automáticamente contra el monolito de Nido, el producto de Aurelia, un sistema de gestión para residencias de mayores que usaban cientos de centros en toda España. Planes de cuidado, hojas de medicación, turnos del personal, el portal de las familias. Software del que dependía, en último término, que la señora del 214 tomara lo suyo a su hora.

El trabajo de Nadia consistía en mirar esos PRs y pulsar botones. Approve. Approve. Request changes, cuando algo le chirriaba y tenía fuerzas para justificarlo. Los diffs eran plausibles, estaban bien escritos, mejor comentados que los suyos. También eran quinientas, ochocientas líneas cada uno, sobre partes del sistema que ella no conocía, generados a partir de tickets que había redactado un product manager con otro agente. A las cinco de la tarde había «revisado» más código del que antes leía en un mes, y no habría podido explicarle a nadie qué hacía la mitad.

Lo intentó explicar una vez, en la daily:

—Siento que ya no hago software. Hago control de calidad de una cinta transportadora.

—Aprobadora profesional —dijo Marc, sin malicia. Marc Vives, veintinueve años, era el converso entusiasta del equipo: encadenaba agentes como quien encadena dominó y presumía, con razón, de cerrar más tickets que nadie—. Yo lo veo distinto, ¿eh? Yo nunca había tenido esta potencia. Es como tener un equipo entero a mis órdenes.

—Ya —dijo Bruno—. Eso decía el folleto de la última transformación. Y el de la anterior. Yo he sobrevivido a tres transformaciones ágiles y a un ERP, chaval. Lo único que se transforma seguro es el PowerPoint.

Sofía Griñán, la Engineering Manager, cerró la daily como la cerraba siempre últimamente: mirando el reloj, con seis reuniones por delante, prometiendo «hablarlo con calma» en un uno-a-uno que llevaba tres semanas moviéndose de sitio en el calendario como un mueble incómodo.

Y sin embargo — esto era lo que Nadia no conseguía cuadrar — los números de Víctor eran verdad. Se entregaba más que nunca. Los agentes no se cansaban, no se quejaban, no pedían contexto. Producción recibía despliegues a un ritmo que dos años atrás habría parecido ciencia ficción. Si aquello era el futuro, ¿por qué olía a quemado?

El viernes llegó la respuesta con nombre y apellidos. Se filtró — en Aurelia se filtraba todo — que el Grupo Ondara, veintiocho residencias, casi un tercio de los ingresos recurrentes de la casa, había pedido una reunión urgente con dirección. Alguien había visto la presentación preliminar. Una frase circulaba por los corrillos como una esquirla: *«Nido cada vez hace más cosas y cada vez nos sirve menos.»*

Más deprisa que nunca, pensó Nadia. Y perdidos como siempre. O más.

---

Fue esa misma tarde, con la oficina medio vacía, cuando cometió el acto de curiosidad que iba a reordenarle la carrera.

Quería entender a la competencia. En el all-hands, entre línea y línea de triunfo, Víctor había dejado caer que «un actor menor» les había arrebatado dos clientes ese trimestre. El actor menor se llamaba Lantana. Nadia esperaba encontrar una startup con cuarenta ingenieros y una ronda de financiación reciente. Encontró una web sobria donde una página titulada «Equipo» enumeraba siete nombres de pila con siete ilustraciones a tinta en lugar de fotos («las fotos se las dejamos al producto», decía el pie). Siete personas. Con un producto más pequeño que Nido, más lento en features y, a juzgar por los dos clientes robados, más querido.

Y encontró algo más. En el pie de la web, un enlace: **«Cuaderno de a bordo — cómo trabajamos (y por qué)»**. Era un manual público. Abierto del todo: licencia Creative Commons, historial de cambios visible, cualquiera podía leerlo e incluso proponer modificaciones, como si fuera código. Los capítulos no tenían el tono de los manuales corporativos que Nadia conocía — nada de «nuestros valores nos definen» — sino notas al pie. Muchas notas al pie. Papers. Años. Nombres de revistas.

No había autor. Solo, al final del prólogo, una inicial: **M.**

El primer capítulo se titulaba «Primero, las personas (no es un eslogan: es el resultado de un experimento que salió mal)». Empezaba con una cita de un libro de 1911, *The Principles of Scientific Management*, de un ingeniero llamado Frederick Winslow Taylor:

> «En el pasado, el hombre era lo primero; en el futuro, el sistema debe ser lo primero.»

Y seguía:

> «Taylor fue el hombre más influyente en la historia de la organización del trabajo, y su idea central era esta: separar el pensar del ejecutar. La dirección piensa, mide y prescribe; el trabajador ejecuta la tarea óptima que otros diseñaron. Funcionó — durante un tiempo, para cierto tipo de trabajo — y su fantasma se reencarna en cada generación de herramientas. Cada vez que alguien diseña un sistema donde unos deciden y otros solo ejecutan (o solo *aprueban*), Taylor sonríe desde 1911.
> En 1951, dos investigadores llamados Trist y Bamforth bajaron a unas minas de carbón inglesas a estudiar por qué la nueva maquinaria, técnicamente superior, estaba produciendo peores resultados, más absentismo y más conflicto. Lo que encontraron cambió la historia del trabajo en equipo, y casi nadie que trabaja en software lo ha leído. Nosotros montamos Lantana sobre ese paper. En serio. Sigue leyendo.»

Nadia leyó el capítulo entero de pie, sin quitarse el abrigo, junto a la ventana que daba al aparcamiento. Reconoció su semana en un texto sobre mineros muertos hacía décadas. Ella era la parte del sistema que ejecutaba — no, ni siquiera: la que *aprobaba* — dentro de una máquina que otros habían diseñado, y la máquina era técnicamente superior, y algo esencial se estaba rompiendo, y en 1951 dos señores ya sabían el qué.

Abrió su repo personal de notas — lo llamaba «el jardín», para vergüenza suya y regocijo de Bruno — y creó un fichero: `cuaderno-de-a-bordo.md`. Apuntó: *Taylor 1911. Trist & Bamforth 1951, minas de Durham. Buscar los papers ORIGINALES, no el resumen. ¿Quién es M.?*

Luego, porque la honestidad era en ella una forma de compulsión, añadió: *¿Por qué la competencia publica gratis cómo trabaja? ¿Qué sabe esta gente que nosotros no?*

---

El lunes hizo una última comprobación, de esas que no llevan a ninguna parte salvo cuando llevan.

Quería saber desde cuándo existía Lantana. En la Wayback Machine de archive.org, buscando fechas, tecleó por inercia el dominio de Aurelia y retrocedió: 2022, 2019, 2016. La web antigua era entrañable: fotos de una oficina diminuta, el primer logo de Nido con un pajarito mal vectorizado. Y en la página «Quiénes somos» de 2016, donde la web actual muestra a un solo fundador, había dos personas.

Una era conocida: sonriente, más joven, el fundador de siempre, el que salía en las notas de prensa.

La otra era una mujer de treinta y muchos, brazos cruzados, mirada tranquila, medio borrada por la compresión JPEG de la época. El pie de foto decía «Cofundadora». Sin nombre. En la versión de 2017, la foto seguía. En la de 2019, ya no estaba. Nadia buscó en la web actual, en las notas de prensa, en la página de historia corporativa que celebraba «diez años de Aurelia». Nada. Ni una mención. Como si la hubieran despegado del álbum.

Se quedó un rato mirando la foto pixelada. Luego miró la inicial al pie del prólogo del Cuaderno. Era una tontería. No tenía ninguna base. Lo apuntó de todos modos, porque el jardín era suyo y en él podía plantar lo que quisiera:

*¿M.?*
