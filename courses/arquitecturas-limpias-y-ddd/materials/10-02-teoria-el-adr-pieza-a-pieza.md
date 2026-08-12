Este es el capítulo para el que se escribió el curso entero. Vamos a leer, de arriba abajo y sin saltarnos nada, el documento de arquitectura real de un proyecto real de código abierto — **Open Knowledge**, la plataforma de cursos sobre la que quizá estés leyendo esto ahora mismo — y a comprobar que cada línea, que hace doce secciones habría sonado a jerga, ahora es una vieja conocida con nombre, historia y porqué. El documento es su **ADR 0001: Clean Architecture with DDD-style modules** (github.com/oegea/open-knowledge, en `docs/adr/`). Es corto: una página. Doce secciones de curso caben en una página — esa compresión es exactamente lo que un buen documento de arquitectura hace.

## Primero: qué es un ADR

Un **ADR** (*Architecture Decision Record*, registro de decisión de arquitectura) es un documento breve que captura **una** decisión estructural: su contexto, la decisión misma y sus consecuencias. El formato lo propuso Michael Nygard en un artículo de blog de 2011 (*Documenting Architecture Decisions*, gratuito en cognitect.com) con una motivación que a estas alturas del curso te sonará profundamente familiar:

> Los que llegan después «pueden aceptar la decisión sin entenderla, o rechazarla sin entenderla» — y ambas cosas destruyen proyectos. El ADR existe para que la tercera opción sea posible: entenderla. *(paráfrasis del argumento del artículo)*

Las propiedades que hacen del ADR una herramienta y no una burocracia: es **corto** (una o dos páginas; nadie mantiene catedrales de documentación), es **inmutable** (las decisiones no se editan: se *sustituyen* con un nuevo ADR que referencia al viejo — como las entidades del curso, el historial completo se conserva), **vive con el código** (en `docs/adr/`, versionado en Git, revisado en los mismos PRs) y — la parte que Silvia aprendió tarde y a oscuras — **se escribe a tiempo**, cuando la decisión se toma, no como arqueología. `faro` era un ADR póstumo escrito por una sola persona; la meta de la práctica es que no haga falta ninguno póstumo.

## El recorrido

Vamos con el documento. Cada bloque citado es (traducido) del ADR real; debajo, su genealogía en el curso.

### El contexto y las capas

> «Open Knowledge necesita una base de código que pueda evolucionar de forma sostenible, que mantenga las reglas de negocio independientes de frameworks y tecnología de almacenamiento, y que sea fácil de testear. [...]
> 1. **Capa de dominio** — entidades de negocio, value objects, list classes e interfaces de repositorio. Sin dependencias de otras capas ni de librerías externas.
> 2. **Capa de aplicación** — casos de uso que orquestan objetos del dominio. Depende solo de la capa de dominio.
> 3. **Capa de infraestructura** — implementaciones concretas de las interfaces de repositorio (base de datos, HTTP, servicios externos). Puede depender de dominio y aplicación.
> La regla fundamental: **las dependencias siempre apuntan hacia dentro.**»

Tres frases de contexto que son las tres monedas del curso: evolucionar sin dolor (secciones 1-3: el coste del cambio es EL coste), negocio independiente de la tecnología (sección 4: dentro/fuera), testeable (secciones 2 y 9: la diferencia entre creer y saber). Y las tres capas son la servilleta de Silvia con nombres canónicos: el dominio no importa nada (¡ni librerías! — la cláusula que convierte la pureza en algo auditable con un vistazo a los imports), la aplicación importa solo dominio, la infraestructura importa el mundo y los contratos de dentro. La «regla fundamental» es, palabra por palabra, la regla de la dependencia de Martin (2012) — y nota que el ADR la enuncia en cuatro palabras sin citar a nadie: cuando una idea gana, se vuelve anónima. Ahora tú sabes su genealogía completa: Parnas → DIP → Cockburn → Martin.

### Los módulos

> «El código se estructura en módulos basados en contextos de negocio. Cada módulo contiene sus propias capas: `src/modules/{context}/` con `application/`, `domain/`, `infrastructure/`, `test/`. [...] Contextos previstos: `course`, `identity`, `study` (progreso), `assessment` (exámenes), `certificate`, `notification`, `news`, `settings`.»

La sección 8 entera en una estructura de carpetas: **módulo = bounded context hecho directorio**, cada uno con sus capas completas y su soberanía. Fíjate en que los contextos llevan nombres del dominio de la plataforma (curso, identidad, estudio, evaluación) y no de la tecnología (nada de `api/`, `database/`, `utils/`): screaming architecture — la raíz grita «plataforma de aprendizaje», no «app de Next.js». Y fíjate también en la escala: ocho contextos para una aplicación de tamaño medio, cada uno pequeño. Las fronteras no son un lujo de gigantes; son más baratas cuanto antes se dibujan.

### Los value objects

> «Inmutables, igualdad por valor, autovalidados. API estándar: `static create(...)` — crea una instancia nueva, validando. `static fromPrimitive(data: XPrimitive)` — crea una instancia desde un valor plano. `static ensureXIsValid(...)` — valida los parámetros de entrada. `toPrimitive(): XPrimitive` — convierte a valor plano para serialización. `equals(other: X): boolean`. [...] Todo value object o entidad que exponga `fromPrimitive`/`toPrimitive` DEBE declarar una interfaz `XPrimitive` dedicada en el mismo fichero.»

La sección 5, convertida en contrato de equipo. Las tres propiedades canónicas (inmutable, igual por valor, autovalidado — «lo inválido no nace») y la aduana `fromPrimitive`/`toPrimitive` con su `XPrimitive` obligatorio: el tipo del dato desnudo declarado junto al tipo rico, para que la frontera de serialización sea un contrato visible y no una costumbre. El ejemplo del ADR real es un `CourseTitle` que valida no-vacío y máximo 200 caracteres, con errores prefijados `[CourseTitle]` — el mismo patrón, letra por letra, que el `Importe` de Meridian: la clase corta que hace imposible el estado ilegal y grita su nombre en los logs.

Detalle de lectura fina: la API es *estándar*. No «cada value object como su autor prefiera»: los cinco métodos, siempre, con esos nombres. Es la lección del pasillo con las puertas iguales (sección 6) aplicada al dominio — el lector que conoce un value object los conoce todos.

### Las entidades y las list classes

> «Definidas por identidad, inmutables (los modificadores devuelven instancias nuevas), componen value objects. API estándar: `create`, `fromPrimitive`, `ensureXIsValid`, `getId()`, getters, `setX(...)` devolviendo instancia nueva, `toPrimitive()`, `equals(other)`. [...] Las colecciones de entidades/value objects reciben clases de lista inmutables dedicadas (`CourseList`) con accesores que devuelven copias y modificadores que devuelven listas nuevas.»

Sección 5 otra vez: identidad sobre atributos (el `equals` de una entidad compara por id), inmutabilidad funcional (`setX` devuelve una entidad nueva — el tiempo explícito, los invariantes comprobados en un solo lugar), composición de value objects (la entidad no guarda un string: guarda un `CourseTitle`). Y las list classes de la ampliación 5: colecciones con reglas y domicilio, copias defensivas incluidas («accesores que devuelven copias» — la escotilla cerrada).

### Los repositorios

> «Definidos en la capa de dominio; devuelven objetos de dominio, nunca DTOs ni filas de base de datos. Toda clase que se comunica con un sistema externo (base de datos, API, almacenamiento, broker de mensajes...) se nombra con el sufijo `Repository` — sin alternativas `Manager`, `Connector`, `Client` o `Service`. El dominio define el contrato genérico (`CourseRepository`) y la infraestructura aporta implementaciones nombradas (`SqliteCourseRepository`, `HttpCourseRepository`).»

La sección 6 completa en cuatro frases: interfaz en el dominio (el contrato lo posee quien manda), objetos de dominio a través de la aduana (nunca filas: la promesa «toda entidad en memoria es válida» exige revalidar todas las puertas), implementaciones por tecnología en infraestructura, y la regla de nomenclatura radical — todo lo externo es `Repository`, sinónimos prohibidos — con la justificación que ya conoces: los patrones valen por repetidos, y un pasillo con las puertas iguales se recorre a oscuras. Ahora también sabes qué te está *prometiendo* ese sufijo cuando lo leas en cualquier fichero del proyecto: toca el exterior, tiene contrato fingible, no esconde negocio.

### Los casos de uso y la factoría

> «Una operación de negocio por fichero, implementada como una función que recibe sus dependencias (repositorios, otros casos de uso como puertos) en un único objeto de props. [...] Los errores lanzados por los casos de uso se prefijan con el nombre del caso de uso: `[createCourse] ...`.
> Cada módulo expone un `application/factory.ts` que es **solo cableado**: instancia repositorios y llama a **un** caso de uso por método. Una factoría NO debe: 1. Declarar interfaces/tipos — los contratos pertenecen al caso de uso o al dominio. 2. Coordinar dos o más casos de uso — una cadena de casos de uso en la factoría es un caso de uso que falta. Crea un caso de uso que posea el flujo e inyecta el otro caso de uso como puerto.»

La sección 7, incluida su regla más citada, en versión original. Merece subrayarse el paréntesis «otros casos de uso *como puertos*»: la composición de operaciones se hace inyectando la operación pequeña en la grande, por la misma puerta que los repositorios — la solución exacta al «caso de uso que falta». Y la factoría con sus dos prohibiciones, que ya sabes por qué existen: el único lugar que conoce aplicación e infraestructura a la vez es el lugar que la gravedad empuja a pensar, y la fontanería que piensa es un segundo cerebro sin tests.

### Los entrypoints y el frontend

> «Los handlers de rutas, páginas y jobs son finos: ejecutan autenticación/guardas básicas y delegan en UN caso de uso a través de la factoría del módulo. Incrustar flujo de negocio en un entrypoint es una violación de arquitectura.
> Los mismos principios aplican en el frontend: módulos con implementaciones `HttpXRepository` que llaman a la API, separación contenedor/presentador en componentes, y hooks personalizados que encapsulan la interacción con los casos de uso.»

Las puertas tontas de la sección 7, elevadas a ley con nombre de delito («violación de arquitectura»). Y el párrafo del frontend, que es el regalo final del documento: **las mismas ideas funcionan al otro lado del cable.** Para el frontend, «el exterior» es la propia API del backend — así que el patrón se repite entero: un `HttpCourseRepository` (el adaptador que sabe de fetch y endpoints) implementa el contrato que los hooks (los casos de uso del cliente) consumen, y los componentes se parten en contenedor (coreografía) y presentador (pintar props — puertas tontas). La arquitectura limpia no es una doctrina de backend: es una manera de tratar cualquier frontera.

### Las consecuencias

> «La lógica de negocio es testeable de forma aislada con interfaces de repositorio simuladas. La tecnología de almacenamiento puede cambiar sin tocar los casos de uso. La estructura consistente reduce la fatiga de decisión; los módulos nuevos siguen la plantilla.»

Nygard exige esta sección por una razón de honestidad: toda decisión tiene consecuencias, y escribirlas es la diferencia entre una elección y una moda. Las tres del ADR son los tres finales de la historia de Meridian: los mil ochocientos tests verdes de la víspera (testeable aislado), el plan de tres semanas para el PostgreSQL de Ferrán (almacenamiento intercambiable), y el segundo módulo arrancando con cuatro personas sin discutir la estructura (la fatiga de decisión, gastada una vez, en el ADR, y nunca más). Un ADR maduro lista también los costes — más ficheros, más indirección, un peaje de aprendizaje — y este los da por asumidos en su contexto; tú ya tienes el criterio (sección 3, la crítica a SOLID) para exigirle esa honestidad al tuyo.

## Escribir el tuyo

El capítulo — y la parte técnica del curso — termina donde terminó la historia: con el cursor parpadeando bajo el título de un ADR en blanco. La plantilla de Nygard cabe aquí entera:

```markdown
# ADR NNNN — [decisión en una frase]
**Estado:** propuesto | aceptado | sustituido por ADR-MMMM
**Fecha:** AAAA-MM-DD

## Contexto
Qué fuerzas están en juego: el problema, las restricciones, lo que duele.
Escrito para alguien que llegará en tres años sin contexto ninguno.

## Decisión
Qué se decide, en presente activo. («Organizamos el código en módulos por
contexto de negocio con tres capas...»)

## Consecuencias
Lo bueno, lo malo y lo pendiente. Todas las decisiones tienen las tres.
```

Y las tres reglas de la práctica sana, condensadas de todo el recorrido: se escribe **a tiempo** (el día de la decisión, no en la autopsia), se escribe **entre todos** (un ADR de una sola cabeza documenta una opinión; la deuda de conversaciones no la paga el código — sección 8), y se escribe **para el que viene después** — que es la frase con la que empezó el cuaderno de faro y con la que puede cerrarse el curso, porque es el mismo principio en todas las escalas: los nombres (sección 1), los tests (sección 9) y los ADRs son tres tamaños del mismo acto: **dejar la luz encendida.**

## Para llevar

- ADR (Nygard, 2011): una decisión estructural por documento — contexto, decisión, consecuencias. Corto, inmutable (se sustituye, no se edita), vive con el código, se escribe a tiempo y entre todos.
- El ADR 0001 de Open Knowledge comprime el curso: capas con dependencias hacia dentro (secc. 4), módulos = bounded contexts (secc. 8), value objects y entidades inmutables con API estándar y aduana `XPrimitive` (secc. 5), repositorios con contrato en dominio y sufijo único (secc. 6), casos de uso con props object + factoría solo-cableado con sus dos prohibiciones (secc. 7), entrypoints finos y los mismos principios en frontend.
- Las APIs *estándar* (los cinco métodos de un value object, el sufijo Repository) son la lección del pasillo de puertas iguales: la consistencia elimina fatiga de decisión y compra lectura a oscuras.
- La sección de consecuencias es el detector de honestidad de un ADR: toda decisión tiene costes; escribirlos la convierte en elección.
- Nombres, tests, ADRs: tres escalas del mismo oficio — escribir para el que viene después.

## Para profundizar

- Michael Nygard, *Documenting Architecture Decisions* (2011) — el artículo original, gratuito; diez minutos de lectura.
- El ADR 0001 completo (con su código TypeScript) y sus catorce hermanos: github.com/oegea/open-knowledge, `docs/adr/` — un catálogo real y navegable de decisiones con su porqué, incluida la estrategia de tests (ADR 0002) que reconocerás de la sección 9.
- adr.github.io — el índice comunitario de formatos y herramientas ADR.
