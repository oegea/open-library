## Coda

Un año y medio después del martes de los 4.700,32 €, el mapa de la cocina de Meridian sigue colgado junto a la máquina de café. Nadie lo ha quitado porque ya no es una denuncia: es una foto antigua, de esas que se guardan para acordarse de dónde se viene. A su lado hay una lámina nueva, plastificada — Marta impone sus formatos —, con el context map del sistema: cuatro cajas, sus flechas, sus aduanas con nombre. Debajo, un pósit descolorido que nadie se atreve a retirar: *«El segundo dibujo siempre es más bonito. Pregunta por qué.»*

El Monstruo sigue vivo, más pequeño cada trimestre, facturando lo que aún le toca mientras la higuera le va tomando las ramas. Nadie le puso fecha de muerte; se la está poniendo él solo, módulo a módulo, sin que ningún viernes por la tarde haya que contener la respiración. Óscar dirige las dos cosas — lo que queda del árbol y lo que crece de la higuera — y ha descubierto, dice, el placer más raro de su carrera: aburrirse en los despliegues.

Y en el repositorio del segundo módulo, en `docs/adr/`, hay once documentos. El primero lo escribió un equipo entero una mañana de reunión. El último lo propuso la semana pasada una desarrolladora que entró hace tres meses y encontró una decisión que no entendía: en lugar de aceptarla sin entenderla o rechazarla sin entenderla, escribió un ADR proponiendo sustituirla, con su contexto, su porqué y sus consecuencias. Se aprobó el jueves. Júlia le escribió en la revisión una sola palabra, que en Meridian se ha convertido en la máxima condecoración técnica que existe:

*«Faro.»*

## Lo que te llevas (si te llevas diez cosas)

1. **El código se escribe para el que viene después.** La máquina entiende cualquier cosa; el compañero cansado de las nueve de la noche, no. Nombres que revelan intención, funciones que hacen una cosa, comentarios solo para el porqué.
2. **Legacy = código sin tests, y se toca con red**: caracterización primero, cambio después. La lista de tests que fallan es el mapa de tus efectos.
3. **Acoplamiento bajo, cohesión alta**: lo que cambia junto vive junto. SOLID son cinco instrumentos de esa única brújula; el DIP — los contratos los define la política — es el que sostiene todo lo demás.
4. **La regla de la dependencia**: dentro el negocio, fuera el mundo, las flechas siempre hacia dentro, y se audita mirando imports. Hexagonal, onion y clean son tres dibujos del mismo teorema.
5. **No reescribas: estrangula.** El código feo contiene el conocimiento real de tu negocio; la higuera crece con el árbol vivo y siempre tiene botón de deshacer.
6. **Que lo inválido no pueda nacer**: value objects autovalidados e inmutables, entidades que defienden sus invariantes, dinero en céntimos enteros dentro de un tipo que no sabe mentir.
7. **La persistencia es un detalle**: contratos en el dominio con vocabulario de negocio, implementaciones intercambiables en infraestructura, y la in-memory como detector de fugas.
8. **Cada operación se escribe una vez**: casos de uso con dependencias inyectadas, puertas tontas, factorías que solo cablean. Los tests de operación son la especificación ejecutable del sistema.
9. **El lenguaje es el sistema**: lenguaje ubicuo sin traductores, bounded contexts donde las palabras cambian de país, aduanas explícitas — o alguien las hará a mano con una lámina plastificada, durante años, gratis.
10. **El sistema acaba pareciéndose a las conversaciones que lo construyeron.** La deuda técnica se paga refactorizando; la deuda de conversaciones, conversando. Empieza por la segunda.

Y la nota de época que prometimos retomar en el primer capítulo, ahora que tienes el curso entero como argumento: todo lo anterior vale el doble en la era de la IA. Los agentes que hoy escriben y modifican código sufren `$aux3` y los ficheros-maraña exactamente igual que Júlia en su semana tres, y rinden — igual que ella — donde hay nombres honestos, fronteras con contrato, operaciones escritas una vez y una red de tests que convierte «creo» en «sé». Escribir sistemas legibles ya no es solo cortesía con el compañero que viene después: es la condición para que las herramientas que multiplican tu trabajo puedan ayudarte sin romper nada, y para que tú sigas sabiendo — responsabilidad indelegable — lo que tu software hace. El que viene después, a veces, ya no es humano. La luz encendida sirve para los dos.

## Bibliografía: las fuentes de este curso

Todo lo enseñado aquí tiene autores. Estas son las fuentes usadas, con su licencia o condición de acceso — las abiertas primero, porque puedes leerlas hoy mismo sin gastar un euro.

### Abiertas o de libre acceso (verificadas)

- **Eric Evans — *Domain-Driven Design Reference*** (2015). Las definiciones canónicas de DDD (entidad, value object, agregado, repositorio, bounded context, lenguaje ubicuo, context map). **Licencia Creative Commons BY 4.0**; PDF gratuito en domainlanguage.com/ddd/reference.
- **Robert C. Martin — *The Clean Architecture*** (2012), ***Screaming Architecture*** (2011) y ***The Principles of OOD***. Artículos gratuitos en blog.cleancoder.com y butunclebob.com. El artículo *Design Principles and Design Patterns* (2000) circula libremente y es el origen escrito de la recopilación SOLID.
- **Alistair Cockburn — *Hexagonal Architecture (Ports and Adapters)*** (2005). El artículo original, gratuito, en alistair.cockburn.us/hexagonal-architecture.
- **Martin Fowler — bliki** (martinfowler.com), gratuito. Entradas citadas: *TechnicalDebt* y *TechnicalDebtQuadrant*, *BeckDesignRules*, *TellDontAsk*, *AnemicDomainModel*, *ValueObject*, *BoundedContext*, *UbiquitousLanguage*, *StranglerFigApplication*, *ObjectMother*, *TestDouble*, *Mocks Aren't Stubs*, *UnitTest*, *CQRS*, *Inversion of Control Containers and the Dependency Injection pattern*, y los resúmenes del catálogo de *Patterns of Enterprise Application Architecture* (Repository, Gateway, Money, Unit of Work). Además, el ensayo *The Practical Test Pyramid* de Ham Vocke, alojado en el mismo sitio.
- **Ward Cunningham — *The WyCash Portfolio Management System*** (OOPSLA '92). El texto original de la deuda técnica, dos páginas, en c2.com.
- **Brian Foote & Joseph Yoder — *Big Ball of Mud*** (1997). Gratuito en laputan.org.
- **David Parnas — *On the Criteria To Be Used in Decomposing Systems into Modules*** (1972). El artículo abuelo de la modularidad; disponible en abierto.
- **Joel Spolsky — *Things You Should Never Do, Part I*** (2000). El caso contra las reescrituras, gratuito en joelonsoftware.com. Del mismo autor: *Making Wrong Code Look Wrong* (2005).
- **Michael Nygard — *Documenting Architecture Decisions*** (2011). El artículo que definió los ADRs; gratuito en cognitect.com. Índice comunitario: adr.github.io.
- ***97 Things Every Programmer Should Know*** (O'Reilly, 2010; ed. Kevlin Henney). **Licencia CC BY-NC-SA 3.0**; texto completo en github.com/97-things. Citado: *The Boy Scout Rule* (R. C. Martin), *Comment Only What the Code Cannot Say* (K. Henney).
- **Abel Avram & Floyd Marinescu — *Domain Driven Design Quickly*** (InfoQ). Minilibro gratuito; el mejor resumen corto del libro azul.
- **Herberto Graça — serie *DDD, Hexagonal, Onion, Clean, CQRS: how I put it all together*** (herbertograca.com). Gratuita; la mejor cartografía comparada de las arquitecturas.
- **CodelyTV — *typescript-ddd-example* y *typescript-ddd-skeleton*** (github.com/CodelyTV). **AGPL-3.0**, código abierto; proyectos de referencia navegables, de la comunidad hispanohablante.
- **ddd-crew** (github.com/ddd-crew). Plantillas con licencia abierta: Bounded Context Canvas, Core Domain Charts, context mapping.
- **Vaughn Vernon — *Effective Aggregate Design*** (2011). Los tres ensayos, gratuitos, en kalele.io.
- **Melvin Conway — *How Do Committees Invent?*** (1968). El paper de la ley de Conway, libre en melconway.com.
- **Open Knowledge — ADRs** (github.com/oegea/open-knowledge, `docs/adr/`). El documento destino de este curso (ADR 0001) y sus hermanos, en un proyecto open source real.
- **PEP 8** (peps.python.org/pep-0008) y **David Goldberg — *What Every Computer Scientist Should Know About Floating-Point Arithmetic*** (1991), en abierto.

### Libros de pago que recomendamos honestamente

Ninguno es obligatorio para lo aprendido aquí; todos amplían. Orden sugerido de compra según lo que te haya enganchado:

- **Eric Evans — *Domain-Driven Design: Tackling Complexity in the Heart of Software*** (2003). «El libro azul.» Denso, fundacional; la parte IV (estratégica) es la que releen los veteranos.
- **Michael Feathers — *Working Effectively with Legacy Code*** (2004). Si trabajas con un Monstruo, es el manual de supervivencia. El libro de Gabriel.
- **Martin Fowler — *Refactoring*** (2ª ed., 2018, con ejemplos en JavaScript). El catálogo de movimientos con red.
- **Robert C. Martin — *Clean Code*** (2008) y ***Clean Architecture*** (2017). Influyentes y legibles; léelos con el criterio crítico que este curso te ha dado (los ejemplos de *Clean Code* acusan la edad).
- **Vaughn Vernon — *Implementing Domain-Driven Design*** (2013). El DDD táctico y estratégico aterrizado a código, con más detalle del que el libro azul quiso dar.
- **Vlad Khononov — *Learning Domain-Driven Design*** (2021). Probablemente la mejor introducción moderna y compacta a DDD; excelente segundo libro.
- **Kent Beck — *Test-Driven Development: By Example*** (2002). Breve, fresco, transformador.
- **Fred Brooks — *The Mythical Man-Month*** (1975/1995). Por el efecto segundo sistema y porque medio siglo después sigue doliendo de actual.
- **Sam Newman — *Monolith to Microservices*** (2019). Si algún día la higuera tiene que cruzar la red: patrones de estrangulamiento a escala de servicios.

### Para seguir en comunidad

- **virtualddd.com** — comunidad abierta de DDD, sesiones grabadas y gratuitas.
- **EventStorming** — empieza por eventstorming.com (Alberto Brandolini) y su libro en progreso en Leanpub.
- Las charlas grabadas de **Eric Evans**, **Barbara Liskov** (su lección del Turing Award) y **Alberto Brandolini** en YouTube: gratuitas y mejores que la mayoría de cursos de pago.

## Agradecimientos

A Eric Evans, Robert C. Martin, Martin Fowler, Alistair Cockburn, Kent Beck, Michael Feathers, Ward Cunningham, Barbara Liskov, Bertrand Meyer, David Parnas, Vaughn Vernon, Alberto Brandolini y tantos otros que no solo descubrieron estas ideas sino que las escribieron para el que viniera después — este curso es, en el fondo, una visita guiada a su generosidad. A las comunidades que liberan conocimiento con licencias abiertas: sin el *DDD Reference* en Creative Commons, sin el bliki de Fowler, sin los repositorios de ejemplo abiertos, un curso como este no podría citar con la cabeza alta. Al proyecto Open Knowledge, por publicar sus decisiones de arquitectura a la vista de todos, que es la manera más valiente de documentar.

Y a ti, que has llegado hasta aquí. Este curso fue escrito con ayuda de inteligencia artificial y con respeto artesanal por las fuentes, como se explicó en el primer capítulo, y se regala con una sola esperanza, que a estas alturas puede decirse con las palabras de la historia: que en algún sistema futuro, dentro de años, alguien encuentre algo tuyo — un nombre claro, un test con nombre de caso real, un ADR con su porqué — y entienda, y siga construyendo, y deje a su vez la luz encendida.

Quien venga detrás, que la encienda.
