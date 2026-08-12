Antes de entrar en materia conviene saber una cosa que casi nunca se cuenta a quien empieza: **nada de lo que vas a aprender aquí se inventó de golpe, ni lo inventó una sola persona.** «Código limpio», «arquitectura hexagonal», «DDD»… suenan a marcas, pero son capas de sedimento: medio siglo de gente quemándose con los mismos problemas y dejando notas para los siguientes. Este capítulo es el mapa de ese sedimento. No hace falta memorizarlo; hace falta saber que existe, para que cuando el curso cite a alguien sepas dónde colocarlo.

## 1968: la palabra «crisis»

En 1968, la OTAN organizó en Garmisch (Alemania) una conferencia con un título deliberadamente provocador: *Software Engineering*. Allí se puso nombre a algo que todos los presentes sufrían: los proyectos de software llegaban tarde, costaban el doble y fallaban en producción. Lo llamaron la **crisis del software**. Más de cincuenta años después, la crisis no se ha «resuelto»: se ha ido domesticando con ideas. Las de este curso son, probablemente, las que mejor han envejecido.

La primera lección de la historia es humilde: **el problema nunca fue escribir código; fue cambiarlo.** Un programa que funciona hoy y no puede modificarse mañana es un problema con fecha de caducidad. Casi todo lo que estudiarás aquí — nombres claros, capas, dependencias que apuntan hacia dentro, código que habla el idioma del negocio — son estrategias para una sola cosa: que el cambio no duela.

## Los setenta y ochenta: cohesión, acoplamiento y objetos

En los años setenta, Larry Constantine y Edward Yourdon formalizaron dos palabras que usaremos constantemente: **acoplamiento** (cuánto depende una pieza de otras) y **cohesión** (cuánto tienen que ver entre sí las cosas que viven dentro de una misma pieza). Su libro *Structured Design* (1979) estableció el criterio que sigue vigente: acoplamiento bajo, cohesión alta. David Parnas, en 1972, había publicado el artículo que fundamenta todo lo demás: *On the Criteria To Be Used in Decomposing Systems into Modules*, donde propuso dividir los sistemas ocultando decisiones — cada módulo esconde un secreto que puede cambiar sin afectar al resto. Guarda esa idea: la verás reaparecer, con otros nombres, en cada sección de este curso.

En los ochenta llegó la programación orientada a objetos al gran público (Smalltalk, C++), y con ella la promesa de modelar el mundo en el código. La promesa se cumplió a medias — veremos por qué —, pero dejó el vocabulario sobre el que todo lo demás se construye.

## Los noventa: los pragmáticos

Los noventa son la década en que la comunidad empezó a escribir para la comunidad. Tres nombres que citaremos mucho:

- **Kent Beck** — creador de Extreme Programming y del testing automatizado moderno (JUnit, junto a Erich Gamma). Suyas son las «cuatro reglas del diseño simple» que veremos en la sección 2, y suya es la práctica que hace posible todo lo demás: si el código tiene tests, se puede cambiar sin miedo.
- **Martin Fowler** — el gran cronista de la disciplina. Su libro *Refactoring* (1999) dio nombre y catálogo a la actividad de mejorar código sin cambiar su comportamiento, y su web, martinfowler.com, es la enciclopedia abierta que este curso cita una y otra vez.
- **Robert C. Martin** («Uncle Bob») — durante los noventa recopiló y bautizó los principios de diseño orientado a objetos que hoy conocemos por el acrónimo **SOLID** (sección 3), y años después popularizó las ideas de *Clean Code* (2008) y *Clean Architecture* (2012/2017).

En 2001, varios de ellos firmaron el *Manifesto for Agile Software Development*. Conviene recordar una cosa que se olvida a menudo: el manifiesto ágil lo escribieron, en su mayoría, personas obsesionadas con la calidad técnica. La agilidad sin código sano es solo prisa.

## 2003-2005: el dominio en el centro

Dos publicaciones casi simultáneas forman el corazón de este curso:

- En 2003, **Eric Evans** publicó *Domain-Driven Design: Tackling Complexity in the Heart of Software*, conocido cariñosamente como «el libro azul». Su tesis: la mayor complejidad del software no está en la tecnología, sino en el **dominio** — el negocio, el problema real —, y por tanto el modelo del dominio debe ser el centro del diseño, expresado en un **lenguaje ubicuo** compartido entre programadores y expertos del negocio. Evans liberó después las definiciones esenciales en el *DDD Reference* bajo licencia Creative Commons; son las que usaremos.
- En 2005, **Alistair Cockburn** publicó el artículo *Hexagonal Architecture (Ports and Adapters)*: la aplicación debe poder funcionar igual con una interfaz gráfica, con tests automáticos o con un fichero por lotes, porque su lógica no sabe nada del mundo exterior — se comunica con él a través de «puertos» a los que se enchufan «adaptadores».

En 2012, Robert C. Martin sintetizó éstas y otras propuestas (la *Onion Architecture* de Jeffrey Palermo, entre ellas) en un artículo breve y muy influyente, *The Clean Architecture*, cuyo diagrama de círculos concéntricos probablemente hayas visto alguna vez: las dependencias apuntan siempre hacia el centro, donde viven las reglas de negocio.

## Hoy: la síntesis

Nada de lo anterior compite entre sí. El estado del arte actual — el que practican los equipos que citaremos y el que describe el documento de arquitectura real que leeremos entero en la sección 10 — es una síntesis: **código limpio** en lo pequeño, **capas con dependencias hacia dentro** en lo mediano, y **el dominio como centro y el lenguaje como guía** en lo grande. Ese es el viaje del curso, y este es su mapa:

| Secciones | Escala | Pregunta que responden |
|---|---|---|
| 1-2 | Una línea, una función | ¿Cómo escribo código que otro pueda leer y tocar? |
| 3 | Una clase, un módulo | ¿Cómo evito que todo dependa de todo? |
| 4 | Una aplicación | ¿Dónde pongo cada cosa y por qué? |
| 5-7 | Los ladrillos | ¿Qué son entidades, value objects, repositorios y casos de uso? |
| 8 | Un sistema y su gente | ¿Cómo hago que el código hable el idioma del negocio? |
| 9 | La red de seguridad | ¿Qué tests sostienen todo esto? |
| 10 | El plano completo | ¿Cómo se ve todo junto en un proyecto real? |

Una advertencia final, la más importante del capítulo: **ninguna de estas ideas es un dogma.** Todas nacieron de dolores concretos, y solo se entienden desde el dolor que resuelven. Por eso este curso empieza cada sección con una historia: para que sientas el problema antes de aprender la solución. Los mejores ingenieros que conocemos no son los que aplican patrones; son los que saben *por qué* existen — y por eso saben también cuándo no aplicarlos.

En el próximo capítulo empieza la historia. Es lunes, hay una junior con la mochila aún puesta, y en la bandeja de entrada de soporte hay 214 correos con el mismo asunto.
