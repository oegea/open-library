«Las dependencias entran por la puerta» es la frase más repetida del curso, y merece una ampliación propia: qué es exactamente la inyección de dependencias, por qué no necesita frameworks, qué aportan y cobran los contenedores, y un par de matices (composición root, ciclo de vida) que distinguen una fontanería sana de un pantano. Material especialmente útil si vienes de un framework que «te lo hace solo» y nunca has visto el truco desnudo.

## El patrón, desnudo

**Inyección de dependencias** (DI) significa, en su totalidad: *un objeto no construye sus colaboradores; los recibe*. Eso es todo. La forma más simple es la que usa el curso — parámetros:

```python
# Sin DI: el caso de uso fabrica su despensa (y queda soldado a ella)
async def emitir_factura(pedido_id):
    repositorio = PostgreSQLRepositorioDeFacturas(config.DB_URL)   # soldadura
    ...

# Con DI: la recibe
async def emitir_factura(*, pedido_id, repositorio_de_facturas):
    ...
```

Martin Fowler documentó el patrón y sus variantes en el artículo que fijó el vocabulario (*Inversion of Control Containers and the Dependency Injection pattern*, 2004, gratuito en martinfowler.com): inyección por constructor, por setter, por interfaz. En lenguajes con funciones de primera clase, «por parámetro» es la variante natural y la más honesta: la firma declara el contrato completo.

Conviene deshacer un nudo terminológico que confunde a todo el mundo una vez: **DI no es DIP**. El principio (DIP, sección 3) dice que la política define contratos y los detalles los implementan — es una afirmación sobre *quién posee las abstracciones*. La inyección (DI) es una *técnica de construcción*: pasar colaboradores desde fuera. Se puede inyectar sin invertir nada (pasarle a una función el driver concreto de MySQL sigue siendo DI… y sigue acoplando), y la inversión sin inyección es letra muerta (un contrato precioso que cada clase esquiva construyendo su implementación dentro). La arquitectura sana usa las dos: contratos del dominio (DIP), servidos por fuera (DI).

## La composition root: un solo lugar que lo sabe todo

Si nadie construye sus colaboradores, la construcción entera se acumula en algún sitio. Ese sitio tiene nombre en la literatura — **composition root** (término acuñado por Mark Seemann en *Dependency Injection in .NET*, 2011) — y una regla: existe **uno por aplicación**, tan cerca del `main` como sea posible. La factoría por módulo del curso es la versión federada de esta idea: cada módulo cablea lo suyo, y el entrypoint de la aplicación compone módulos.

La regla operativa que evita el 90% de los líos: **`new` (construcción de infraestructura) solo aparece en la composition root / factorías.** Si un caso de uso, una entidad o — peor — un adaptador construye por su cuenta otro adaptador, has plantado un segundo cerebro de cableado que nadie vigilará. Buscar `new PostgreSQL` por el código fuera de las factorías es una auditoría de arquitectura de treinta segundos, prima hermana de «mira los imports» (sección 4).

## Contenedores: qué compran y qué cobran

Los **contenedores de DI** (Spring, NestJS, Angular; `dependency-injector` o `punq` en Python; `inversify` o `awilix` en JavaScript) automatizan la composition root: registras qué implementa qué, y el contenedor resuelve el grafo, a menudo vía decoradores/anotaciones y reflexión.

Qué compran: en aplicaciones con *cientos* de piezas, el cableado manual se vuelve un fichero tedioso; el contenedor lo genera. Gestión de ciclo de vida declarativa. Integración con el framework anfitrión.

Qué cobran, y no es calderilla:

- **El grafo se vuelve invisible.** Con factoría manual, «¿quién usa el repositorio de abonos?» se responde leyendo un fichero. Con contenedor, se responde entendiendo la configuración, los decoradores repartidos por cuarenta ficheros y las convenciones de resolución — el conocimiento pasa del código a la magia.
- **Errores en tiempo de arranque (o de petición) en lugar de errores de lectura.** El cableado manual que falta no compila o revienta en la primera línea; la anotación que falta revienta cuando el contenedor intenta resolver, con un stack trace del contenedor, no del programa.
- **El framework se infiltra.** Decoradores del contenedor en los casos de uso — `@Injectable()` sobre `emitirFactura` — son un import de infraestructura en la capa de aplicación: una gotera de la regla de dependencia, pequeña y oficial. Hay maneras de evitarla (registrar sin anotar), pero exigen nadar contra la corriente del framework.

El criterio del curso, sin fanatismo: **empieza con factorías manuales**; su coste crece linealmente con el proyecto y su legibilidad es total. Considera un contenedor cuando el cableado manual duela de verdad — y si lo adoptas, mantén los decoradores fuera de `domain/` y `application/`: que el contenedor sea un detalle de infraestructura más, sustituible como todos.

## Ciclo de vida: la dependencia con memoria

Detalle que muerde en producción y casi ningún tutorial cuenta: no todas las dependencias son iguales ante el tiempo.

- **Sin estado** (la mayoría de repositorios: reciben pool de conexiones, no guardan nada): constrúyelas una vez, compártelas siempre. Es el caso de la factoría del curso.
- **Con estado por petición** (una transacción abierta, el usuario autenticado, un identificador de correlación para logs): NO pueden ser un singleton del módulo — dos peticiones concurrentes se pisarían. Se crean por invocación y viajan… por parámetro, como todo. Si un día ves un bug donde «a veces la factura sale con el usuario de otro», busca una dependencia por-petición ascendida a singleton.
- **Caras de crear** (pools, clientes con handshake): una vez, en el arranque, y compartidas; crearlas por petición es un incendio de latencia.

Los contenedores llaman a esto *scopes* (singleton, request, transient). La factoría manual lo resuelve con la herramienta más vieja del mundo: dónde pones el `new` — arriba del fichero (una vez) o dentro de la función (cada vez). Otra virtud de la fontanería visible: el ciclo de vida se *ve*.

## Los dobles de test entran por la misma puerta

Última pieza del cuadro, anticipo de la sección 9: la razón por la que los tests del curso no usan librerías de mocks para las dependencias es que **no las necesitan**. Cuando la dependencia entra por parámetro y su contrato es pequeño, el doble de test es una clase normal (`InMemoryRepositorioDeFacturas`) — legible, reutilizable, sin sintaxis de framework. Las librerías de mocking nacieron, en gran parte, para colarse en código que *no* recibía sus dependencias; en código bien inyectado quedan para los bordes (verificar «se llamó al puerto de notificación una vez»), no para el pan de cada día. La necesidad compulsiva de mocks sofisticados suele ser el olor de una inyección deficiente.

## Para llevar

- DI = los colaboradores se reciben, no se construyen. La variante por parámetro/props object es la más honesta: la firma es el contrato. (Fowler, 2004.)
- DI ≠ DIP: la técnica de pasar cosas ≠ el principio de quién posee los contratos. Se necesitan mutuamente para valer algo.
- Composition root (Seemann): un solo lugar — factorías — donde vive todo `new` de infraestructura. Auditoría exprés: buscar `new` fuera de las factorías.
- Contenedores: compran comodidad en grafos enormes; cobran invisibilidad, errores tardíos y decoradores infiltrados en capas puras. Empezar manual; migrar cuando duela; mantener el contenedor fuera del dominio.
- Ciclo de vida: singleton para lo sin-estado, por-petición para lo que recuerda, una-vez para lo caro. Con factoría manual, el scope se ve a simple vista.
- En código bien inyectado, los dobles son clases normales; la sed de mocks mágicos delata inyección pobre.
