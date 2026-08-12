Bienvenida, bienvenido. Este curso quiere enseñarte tres cosas que suelen contarse por separado y que en realidad son una sola: **código limpio** (escribir código que otros puedan leer), **arquitecturas limpias** (organizar ese código para que pueda cambiar sin romperse) y **Domain-Driven Design** o **DDD** (hacer que el código hable el idioma del problema que resuelve). Si hoy no sabes qué significa ninguno de esos términos, estás exactamente en el punto de partida para el que se diseñó el curso. Si llevas años programando, también hay sitio para ti: hemos procurado que en cada sección haya al menos una idea, un patrón o una historia de las que hacen decir «esto no lo sabía».

## Qué vas a encontrar en cada sección

El curso avanza por secciones temáticas, y cada una repite el mismo ritmo, pensado para que la teoría nunca llegue antes que la necesidad:

1. **Una historia.** El curso narra, capítulo a capítulo, una única historia de ficción: la de Júlia Ferrer, una programadora junior que entra a trabajar en una empresa cuyo producto —un viejo sistema de facturación al que todos llaman «el Monstruo»— está a punto de costarle su cliente más importante. Cada episodio te pone delante de un problema real antes de darle nombre. La historia continúa de sección en sección; los personajes crecen, hay preguntas que no se responden hasta el final, y te recomendamos leerla en orden, como una novela por entregas. Todo lo técnico que ocurre en ella es real: los bugs, los errores de diseño y las soluciones son los que encontrarás en tu carrera.
2. **La teoría.** Después de cada episodio, un capítulo explica con rigor lo que la historia mostró: definiciones precisas, el porqué de cada regla, ejemplos de código en **JavaScript** y **Python**, y citas de las fuentes originales — cuando una idea es de alguien, se dice de quién y de dónde. Cada capítulo de teoría cierra con una lista de puntos «Para llevar» y referencias para profundizar.
3. **Una ampliación** (solo en algunas secciones). Matices, patrones adicionales y rincones menos transitados: material que no es imprescindible para seguir el hilo, pero que es donde más suelen aprender quienes ya conocían el tema.
4. **Un examen.** Preguntas tipo test con una particularidad: lo importante no es la nota, sino la **explicación** que acompaña a cada respuesta. Trata los exámenes como una herramienta de aprendizaje más, no como un juicio.

Ninguna sección asume vocabulario que no se haya definido antes. Si un término aparece por primera vez, se explica en ese momento, en negrita, con una definición sencilla y el matiz necesario.

## Hecho con inteligencia artificial, y dicho claramente

Este curso ha sido redactado con ayuda de inteligencia artificial, bajo dirección y revisión humanas. No queremos que esto se lea en letra pequeña: está marcado como tal en la plataforma, y te lo contamos aquí, en el primer capítulo, porque la transparencia es parte de lo que el curso enseña.

Vivimos un momento extraño y fascinante: **crear nunca ha sido tan fácil, y precisamente por eso la responsabilidad de crear bien nunca ha sido tan grande.** Cuando producir mil páginas cuesta una tarde, la tentación es inundar el mundo de páginas que nadie ha pensado de verdad. Este curso intenta ser lo contrario: cada fuente citada existe y se ha respetado; cada cita textual indica su origen; las ideas de Eric Evans, Robert C. Martin, Martin Fowler, Alistair Cockburn, Kent Beck y tantos otros se presentan como suyas, con nombre y obra, no como si fueran nuestras. La IA se ha usado como lo que es: una herramienta extraordinaria para ordenar, redactar y explicar — no para suplantar el trabajo intelectual de quienes descubrieron estas ideas, ni para ahorrarnos el deber de verificar.

Si encuentras un error, será nuestro, no de las fuentes. Y agradeceremos que nos lo digas.

## La otra mitad de la responsabilidad: software que la IA también entienda

Hay una segunda cara de esa responsabilidad, menos comentada y mucho más importante para ti como desarrollador o desarrolladora, y queremos dejarla plantada desde el primer capítulo porque atraviesa todo el curso: **en la era de la IA, todo lo que aquí vas a aprender vale el doble.**

Hoy tu código ya no lo leen solo tus compañeros: lo leen — y lo modifican — asistentes y agentes de inteligencia artificial. Y resulta que a la IA le pasa exactamente lo mismo que a nosotros. Una variable ilegible que significa tres cosas según la línea la confunde igual que a ti. Un fichero donde se entrelazan las interacciones de treinta sistemas distintos la degrada igual que al junior de su primer día — y si hablamos de sistemas que tocan hardware, donde el error no se revierte con un despliegue, el coste de esa confusión se multiplica. En cambio, unos nombres honestos, unas funciones que hacen una sola cosa, unas fronteras claras con contratos explícitos y un lenguaje compartido con el negocio le permiten trabajar con la misma seguridad que a un humano — y, sobre todo, te permiten a ti **verificar lo que produce**, que es la otra mitad del trato.

De ahí la doble responsabilidad de esta época. Primero, **seguir sabiendo lo que hacemos**: la IA nos permite producir más código del que entendemos, y el código que su propio equipo no entiende es la forma definitiva de deuda técnica — da igual quién lo haya tecleado. Y segundo, **construir sistemas que tanto humanos como máquinas puedan leer, navegar y cambiar con seguridad**: el código limpio y las arquitecturas de este curso ya no son solo cortesía con el compañero cansado de las nueve de la noche; son también la interfaz con las herramientas que multiplican tu trabajo. Un sistema legible es un sistema en el que la IA puede ayudarte de verdad. Un sistema-maraña es un sitio donde ni la mejor IA puede pisar sin romper algo — y donde nadie podrá comprobar si lo ha roto.

No hace falta que te creas esto hoy: el curso entero es el argumento. Cuando llegues al final, vuelve a leer este apartado.

## Créditos y agradecimientos

Este curso se apoya, con gratitud, en material abierto o de libre acceso:

- **Eric Evans**, *Domain-Driven Design Reference* (2015), publicado bajo licencia Creative Commons Attribution 4.0 — las definiciones canónicas de DDD que usamos vienen de ahí.
- **Robert C. Martin**, por sus artículos abiertos *The Clean Architecture* (2012) y *The Principles of OOD*, además del legado de sus libros.
- **Alistair Cockburn**, por el artículo original de la arquitectura hexagonal (*Ports and Adapters*, 2005), disponible gratuitamente en su web.
- **Martin Fowler**, cuyo *bliki* (martinfowler.com) es una biblioteca abierta de la que este curso cita con frecuencia.
- La comunidad de **97 Things Every Programmer Should Know** (Creative Commons BY-NC-SA 3.0).
- **InfoQ**, por el minilibro gratuito *Domain Driven Design Quickly*.
- **CodelyTV**, por sus repositorios de ejemplo de DDD y arquitectura hexagonal publicados como código abierto (AGPL-3.0), referencia práctica en español.
- El proyecto **Open Knowledge**, cuyo ADR de arquitectura real usaremos como destino del viaje en la sección 10.

La bibliografía completa, con enlaces y licencias, está en el capítulo de cierre.

## Un regalo

Este curso es gratuito y quiere ser, sencillamente, un regalo: una puerta de entrada digna a un oficio hermoso. El conocimiento que contiene no es nuestro — pertenece a la comunidad que lo construyó durante décadas, ensayo y error mediante, y a ti que lo recoges ahora. Si te sirve, el mejor pago posible es el de siempre: cuida tu código, cuida a quien lo leerá después de ti, y cuando sepas algo que otro necesita, regálalo también.

Empezamos. Hay una empresa de provincia, un sistema de facturación con quince años de cicatrices y una factura que salió mal por 4.700,32 €. Y hay una programadora a la que nadie ha explicado todavía que el código se escribe, sobre todo, para ser leído.
