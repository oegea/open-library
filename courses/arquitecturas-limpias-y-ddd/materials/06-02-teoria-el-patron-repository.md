«La caja que no se abre»: todos saben pedirle cosas, nadie sabe qué hay dentro. La historia acaba de mostrar el patrón más rentable de la arquitectura limpia en su momento estelar — el día que el mundo exterior cambia y el negocio no se entera. Este capítulo lo define con rigor, muestra sus reglas de construcción y sus trampas, y explica una decisión de nomenclatura de la arquitectura destino que desconcierta a los recién llegados y enamora a los equipos que la sufren en positivo: aquí, *todo* lo que habla con el exterior se llama `Repository`.

## Definición y genealogía

La definición canónica, del *DDD Reference* de Eric Evans (CC BY 4.0, traducción propia):

> «Para cada tipo de objeto que necesite acceso global, crea un objeto que dé la ilusión de una colección en memoria de todos los objetos de ese tipo. [...] Proporciona repositorios solo para las raíces de agregado que realmente necesiten acceso directo. Mantén al cliente centrado en el modelo, delegando todo el almacenamiento y acceso a objetos en los repositorios.»

La palabra clave es **ilusión**: el repositorio presenta la persistencia *como si* fuera una colección de objetos del dominio — «dame las facturas vencidas de este cliente», «guarda esta» — y esconde absolutamente todo lo demás: el motor, el SQL, las tablas, las filas, los índices, la conexión. Fowler lo cataloga en *Patterns of Enterprise Application Architecture* (2002) en términos casi idénticos: «media entre el dominio y las capas de mapeo de datos usando una interfaz similar a una colección».

El patrón tiene dos mitades, y la arquitectura de este curso las reparte entre capas con toda la intención:

- **La interfaz (el puerto) vive en el dominio.** Es la mitad que manda: define qué conversaciones existen, en vocabulario de negocio. `RepositorioDePedidos` con `buscarPendientesDeFacturar()` es dominio puro — cero imports, cero tecnología.
- **Las implementaciones (los adaptadores) viven en infraestructura**, nombradas por su tecnología: `MySQLRepositorioDePedidos`, `PostgreSQLRepositorioDePedidos`, `InMemoryRepositorioDePedidos`, `HttpRepositorioDePedidos`. Cada una importa su driver y honra el contrato.

Es el DIP de la sección 3 con nombre propio, y el puerto/adaptador de la sección 4 en su caso de uso más frecuente. Si solo puedes llevarte un patrón de este curso a tu trabajo mañana, llévate este.

## Las reglas de construcción

### 1. El repositorio habla dominio, no almacenamiento

La regla más violada del patrón. El contrato se redacta con las preguntas *del negocio*, no con las operaciones *de la base de datos*:

```python
# MAL: el contrato huele a SQL — el dominio acaba sabiendo de filas
class RepositorioDeFacturas(Protocol):
    def query(self, sql: str, params: list) -> list[dict]: ...
    def insert_row(self, table: str, row: dict) -> int: ...

# BIEN: el contrato habla facturación
class RepositorioDeFacturas(Protocol):
    def guardar(self, factura: Factura) -> Factura: ...
    def buscar_por_id(self, factura_id: FacturaId) -> Factura | None: ...
    def buscar_vencidas_de(self, cliente_id: ClienteId) -> FacturaList: ...
```

El primer «repositorio» es una fuga con disfraz: quien lo use escribirá SQL desde el dominio, y la caja habrá quedado abierta. Prueba rápida: lee el contrato en voz alta. Si suena a reunión de facturación, bien; si suena a manual de MySQL, mal.

### 2. Recibe y devuelve objetos de dominio, nunca filas

El repositorio devuelve `Factura` y `FacturaList` — reconstruidas con `fromPrimitive`, es decir, *revalidadas en la aduana* —, jamás diccionarios crudos, filas de ORM o DTOs de transporte. Aquí se cierra el círculo con la sección 5: la promesa «si tienes una Factura entre manos, es válida» solo se sostiene si *todas* las puertas de entrada validan, y la base de datos es una puerta de entrada — quizá esos datos los escribió una versión antigua del código, una migración manual o un compañero con un cliente SQL y prisa.

```python
class PostgreSQLRepositorioDeFacturas:
    def buscar_por_id(self, factura_id: FacturaId) -> Factura | None:
        fila = self._conexion.fetchone(
            "SELECT datos FROM facturas WHERE id = %s", [factura_id.to_primitive()]
        )
        if fila is None:
            return None
        return Factura.from_primitive(fila["datos"])   # la aduana, siempre
```

### 3. Un contrato por concepto, del tamaño de sus clientes

El repositorio no es una «capa de acceso a datos genérica». Fénix construyó una — cuatro meses, «para cualquier motor» — y acabó esquivada por atajos. El repositorio es lo contrario de esa catedral: un contrato *pequeño*, por raíz de agregado (una `Factura` con sus líneas: un repositorio; las líneas solas: jamás — se llega a ellas a través de su factura), con exactamente los métodos que sus casos de uso necesitan hoy. ¿Que aparece una pregunta nueva? Se añade un método nuevo. El ISP de la sección 3, aplicado: puertas del tamaño exacto de quien las cruza.

### 4. In-memory no es un truco de test: es la prueba del patrón

La implementación en memoria — el array de treinta líneas de Denís — merece estatus de primera clase. Sirve para los tests (miles de tests de negocio en segundos, sin levantar nada), sirve de documentación ejecutable del contrato, y sirve de **detector de fugas**: si tu `InMemoryRepositorioDeX` es difícil de escribir, es que el contrato ha dejado escapar detalles de almacenamiento (un método que recibe SQL, una paginación con cursores del motor, un `flush()` que solo tiene sentido en un ORM). La facilidad de fingir la caja es la medida de que la caja no se abre.

## La regla de nomenclatura: todo lo externo es `Repository`

Y aquí, la decisión más opinable y más deliberada de la arquitectura destino de este curso, tal como la formula su documento de arquitectura real (lo leeremos entero en la sección 10): **toda clase que se comunica con un sistema externo — base de datos, API ajena, almacenamiento, cola de mensajes — se llama `Repository`. Sin excepciones: nada de `Manager`, `Connector`, `Client` ni `Service`.**

Un purista objetará, con razón técnica, que el patrón de Evans reserva «repositorio» para colecciones de agregados, y que un `HttpRepositorioDeTiposDeCambio` que consulta una API de divisas sería en la literatura otro patrón (un *gateway*, en el catálogo de Fowler). ¿Por qué aplanar la distinción? Por el argumento de Gabriel, que es un argumento de *economía de lectura*: los patrones no valen por listos, valen por repetidos. En un código con una sola palabra para «frontera con el exterior», el lector adquiere tres certezas gratis con solo ver el nombre: (1) esta clase toca el mundo exterior, (2) por tanto tiene un contrato en el dominio y puede fingirse en tests, (3) por tanto detrás de ella no hay lógica de negocio que buscar. Setenta y tres sinónimos — el censo de ATLAS — son setenta y tres veces esa deducción hecha a mano. La consistencia compra más que la taxonomía; un pasillo con todas las puertas iguales se recorre a oscuras.

(Que el nombre-comodín sea precisamente `Repository` y no otro tampoco es azar: fuerza a redactar cada contrato como colección de cosas del dominio — `buscarX`, `guardarX` — lo que arrastra la regla 1 de serie.)

## Las trampas conocidas

- **El repositorio gordo.** Cuarenta métodos, la mitad con nombre de pantalla (`buscarParaElListadoDeAdministracion`). Señal de que varios contextos distintos comparten contrato — la solución llega en la sección 8 con los bounded contexts.
- **La fuga del query builder.** El contrato expone el constructor de consultas del ORM (`findWhere(criteria)` con criterios del motor): técnicamente hay una interfaz; en la práctica, el dominio compone SQL con guantes. La caja debe recibir *preguntas de negocio*, no piezas de consulta.
- **Lógica de negocio en el adaptador.** El `WHERE estado = 'vencida' AND dias > 30` que decide qué es «vencida» es una regla de dominio escrita en SQL: el día que cambie, se cambiará en el adaptador de PostgreSQL y se olvidará en el de MySQL. La regla vive en el dominio; el adaptador *traduce* la pregunta, no la *interpreta*. (Matiz honesto: por rendimiento a veces se empuja el filtro al SQL — hazlo dejando la definición canónica de la regla en el dominio y tratando el SQL como una optimización documentada de esa regla.)
- **El ORM como modelo de dominio.** Anotar la entidad de dominio con decoradores de tabla («la clase `Factura` *es* la tabla `facturas`») vuelve a soldar lo que el patrón separa: tu modelo queda esposado al esquema, y cada migración de columna sacude el negocio. El adaptador puede usar ORM por dentro — es su cocina —; la entidad de dominio ni lo huele.

## Para llevar

- Repositorio: la ilusión de una colección en memoria de objetos del dominio (Evans, *DDD Reference*); esconde motor, esquema y consultas.
- Interfaz en el dominio (vocabulario de negocio, un contrato por raíz de agregado, tamaño = sus clientes); implementaciones en infraestructura, nombradas por tecnología.
- Entra y sale dominio: reconstrucción con `fromPrimitive` — la base de datos también es una frontera que pasa aduana.
- La implementación in-memory es documentación ejecutable y detector de fugas: si cuesta fingir la caja, la caja se está abriendo.
- Regla de la arquitectura destino: todo lo que toca el exterior se llama `Repository` — consistencia de lectura por encima de taxonomía de patrones.
- Trampas: repositorio gordo, query builder en el contrato, reglas de negocio en SQL, ORM como modelo. Todas son la misma: la caja abierta.

## Para profundizar

- Eric Evans, *DDD Reference* — entrada *Repositories* (CC BY 4.0, domainlanguage.com).
- Martin Fowler, catálogo de *PoEAA*: entradas *Repository* y *Gateway* (resúmenes gratuitos en martinfowler.com) — útil para conocer la taxonomía completa que la regla de nomenclatura decide aplanar.
- CodelyTV, *typescript-ddd-example* (AGPL-3.0, github.com/CodelyTV) — repositorios de dominio + implementaciones por tecnología en un proyecto ejemplar navegable; en español.
