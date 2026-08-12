La teoría dejó dos hilos anunciados: qué es exactamente un «agregado» (la unidad de la que los repositorios son colección) y qué pasa en las fronteras raras — transacciones, consultas de pantalla, eventos. Esta ampliación los desarrolla. Es el material más avanzado del curso hasta ahora; si es tu primera pasada, puedes seguir a la sección 7 y volver aquí cuando el módulo de Meridian te haya crecido en la cabeza.

## Agregados: la frontera de consistencia

Definición del *DDD Reference* (Evans, CC BY 4.0, traducción propia):

> «Agrupa las entidades y value objects en agregados y define fronteras alrededor de cada uno. Elige una entidad como raíz de cada agregado y permite que los objetos externos referencien solo la raíz. [...] Como la raíz controla el acceso, los invariantes que involucran a los miembros del agregado pueden garantizarse.»

La intuición con el caso de Meridian: `Factura` y sus `LineaFactura` forman **un agregado** con la factura como **raíz**. Las reglas que las atan — «el total es la suma de las líneas», «una emitida no cambia» — solo pueden garantizarse si *nadie* toca una línea por su cuenta: todo pasa por la puerta de la raíz (`factura.anadirLinea(...)`). De ahí las dos reglas prácticas que ya usaste sin nombre:

- **Repositorios solo de raíces.** Existe `RepositorioDeFacturas`; no existe `RepositorioDeLineasFactura`. A una línea se llega a través de su factura. Un repositorio de no-raíces es una puerta trasera a los invariantes.
- **El agregado se carga y se guarda entero.** La raíz es la unidad de consistencia, luego es la unidad de persistencia: guardar una factura guarda sus líneas; cargarla, las trae.

¿Y de qué tamaño se hace un agregado? La pregunta de los mil hilos de foro. La referencia moderna son los ensayos *Effective Aggregate Design* de Vaughn Vernon (2011, gratuitos en su web, luego integrados en su libro *Implementing Domain-Driven Design*): **agregados pequeños** — la regla empírica: la mayoría, una entidad raíz y sus value objects —, que protejan **invariantes verdaderos** (reglas que deben ser ciertas *en la misma transacción*) y nada más. El error típico del entusiasmo: el mega-agregado `Cliente` que contiene todas sus facturas, que contiene todos sus pedidos — cargarlo cuesta un segundo, guardarlo colisiona con todo el mundo, y protege «invariantes» que el negocio jamás pidió. Entre agregados distintos: **referencias por id** (`factura.clienteId`, no `factura.cliente` con el objeto entero) y consistencia *eventual* — ya llegará, no en esta transacción — cuando la regla cruce fronteras.

Regla de servilleta para decidir si X entra en el agregado de Y: «si cambio X y Y *a la vez* y una regla exige que el resultado sea coherente en ese mismo instante, van juntos; si la coherencia puede esperar un segundo, van separados».

## La transacción y la unidad de trabajo

Pregunta incómoda que el patrón repository despierta en cuanto hay dos repositorios en el mismo caso de uso: «guardo la factura Y marco el pedido como facturado — ¿y si falla el segundo?». La respuesta clásica es el patrón **Unit of Work** (Fowler, *PoEAA*): un objeto que registra los cambios de una operación de negocio y los confirma o revierte *juntos*.

En la práctica de arquitectura limpia hay tres posturas, de más simple a más sofisticada:

1. **Transacción = agregado** (la postura de Vernon y la del curso): si diseñaste bien los agregados, cada caso de uso modifica *uno*; la transacción coincide con `repositorio.guardar(raiz)` y no necesitas nada más. Las coordinaciones entre agregados van por consistencia eventual (eventos, procesos). Esta postura convierte el problema técnico en una pregunta de diseño — «¿por qué este caso de uso toca dos agregados?» — que muchas veces revela un agregado mal cortado o un concepto que falta.
2. **La unidad de trabajo como puerto**: un contrato de dominio (`UnidadDeTrabajo.ejecutar(fn)`) implementado en infraestructura con la transacción del motor. Legítimo cuando el negocio *de verdad* exige atomicidad entre agregados y no puedes rediseñar.
3. **La transacción en el adaptador de entrada** (el controlador abre/cierra): la opción pragmática de muchos frameworks; funciona, pero riega conocimiento transaccional por la capa que menos sabe del negocio.

Lo importante para tu criterio: la transacción es **una decisión de negocio disfrazada de detalle técnico** — «¿qué tiene que ser cierto a la vez?» es una pregunta para Marta, no para el driver.

## Lecturas de pantalla: cuando el repositorio no es la herramienta

Segunda incomodidad práctica: el listado de administración quiere «número de factura, nombre del cliente, total y días de retraso, paginado de 50 en 50, ordenable por seis columnas». ¿Metemos eso en `RepositorioDeFacturas`? Ya viste el olor (el repositorio gordo con métodos-de-pantalla). La salida honesta es reconocer que **leer para mostrar y ejecutar reglas de negocio son problemas distintos**: la separación se conoce como **CQRS** (*Command Query Responsibility Segregation*, popularizada por Greg Young; Fowler tiene entrada gratuita en su bliki, con la advertencia sensata de no usarla en todas partes). En su forma modesta — la única que este curso recomienda por defecto —: los **comandos** (emitir, anular) pasan por casos de uso + agregados + repositorios; las **consultas de pantalla** pueden tener su propio camino de solo-lectura (una consulta SQL directa que devuelve DTOs planos para la vista), sin pasar por el modelo de dominio, porque no ejecutan ninguna regla. Eso no «rompe la arquitectura»: los dos caminos siguen la regla de dependencia; simplemente el de lectura no necesita el peaje del modelo. Peca de pragmático a sabiendas: el peligro señalizado es que alguien cuele una *escritura* por el camino de lectura — ahí sí se rompió todo.

## Eventos de dominio: la caja que avisa

Tercer hilo, apuntado para el futuro: cuando una factura se emite, contabilidad quiere saberlo, el correo quiere enviarse, las métricas quieren subir. ¿Llama el caso de uso a los tres? Eso lo acopla a conocimientos ajenos. El patrón maduro: la entidad registra **eventos de dominio** (`FacturaEmitida`, con sus datos), y tras guardar, se publican a quien esté suscrito. Del *DDD Reference*: «modela como evento de dominio aquello que ocurre en el dominio y que los expertos quieren rastrear». Los eventos son el pegamento de la consistencia eventual entre agregados (postura 1 de las transacciones) y la semilla de los context maps de la sección 8. En el piloto de Meridian aún no existen; en el ADR de la sección 10 verás que tampoco — un sistema pequeño hace bien en no pagar ese peaje hasta que el negocio lo pida. Saber que existe la puerta ya es la mitad del criterio.

## Para llevar

- Agregado: frontera de consistencia con una raíz que controla el acceso; los invariantes de dentro se garantizan en la misma transacción (Evans). Repositorios solo de raíces; se carga y guarda entero.
- Agregados pequeños (Vernon): protegen invariantes verdaderos y nada más; entre agregados, referencias por id y consistencia eventual. El mega-agregado es el error del entusiasta.
- Transacciones: la postura por defecto es transacción = un agregado por caso de uso; si necesitas más, quizá el corte está mal. «¿Qué debe ser cierto a la vez?» es pregunta de negocio.
- CQRS modesto: las pantallas pueden leer por un camino directo de solo-lectura sin modelo de dominio; las escrituras, jamás.
- Eventos de dominio: la forma madura de avisar sin acoplar; conocer la puerta antes de necesitarla.
