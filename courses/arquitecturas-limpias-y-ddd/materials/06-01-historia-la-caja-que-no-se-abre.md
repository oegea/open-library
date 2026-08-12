La bomba llegó, como casi todas las bombas, en un correo con asunto amable: «Actualización requisitos técnicos — Plan de modernización».

Vesta había contratado un director de sistemas nuevo, un tal Ferrán, que venía de una multinacional y traía las ideas claras y plastificadas. Entre ellas, una que afectaba de lleno al piloto: los datos de facturación de Vesta debían residir «en infraestructura auditada por Vesta» — su propio PostgreSQL, en su propia nube — «con acceso de lectura para los sistemas del proveedor». Traducción: la base de datos MySQL de ATLAS, donde Meridian llevaba quince años guardándolo todo, dejaba de ser el centro del universo. Plazo para presentar plan técnico: tres semanas.

Óscar convocó al equipo del piloto con el correo proyectado en la pared, y Júlia le notó en la cara una emoción compleja: la mitad era preocupación sincera; la otra mitad, y eso era lo interesante, parecía *alivio*. Como si la bomba confirmara algo.

—Esto —dijo, golpeando la pared con el dorso de la mano— es exactamente para lo que NG está diseñado. Multi-tenant, agnóstico de base de datos, cada cliente en su nube. Lo tengo en las diapositivas desde el primer día. —Se volvió hacia Júlia—. Y es exactamente lo que un módulo cosido a mano contra el MySQL de ATLAS no puede hacer. Tu piloto lee los pedidos del Monstruo, ¿me equivoco? ¿Cuánto SQL de ATLAS tenéis ya dentro?

Júlia abrió su portátil sin prisa. Había esperado esta conversación — no así, no tan pronto, pero la había esperado — porque el capítulo seis del faro la había preparado con una precisión que ya no le parecía casualidad:

> *La pregunta que va a matar o salvar este sistema no es qué base de datos usamos. Es: ¿cuántos ficheros saben qué base de datos usamos? En ATLAS la respuesta es «todos». El SQL está en las pantallas, en los informes, en los PDFs. La base de datos no es una pieza de ATLAS: es su esqueleto, y por eso no se puede cambiar sin matar al animal.*
> *En el sistema que quiero, la respuesta sería «uno por concepto». Un solo lugar sabe cómo se guardan las facturas. El resto del sistema le habla a ese lugar en el idioma del negocio — guárdame esta factura, dame las vencidas de este cliente — y no tiene ni idea de si detrás hay MySQL, un fichero o una paloma mensajera bien entrenada. A ese lugar los libros lo llaman repositorio. Yo lo llamo la caja que no se abre: todo el mundo sabe pedirle cosas, nadie sabe qué hay dentro.*

—Te equivocas en una cosa —dijo Júlia, girando el portátil hacia la sala—. El piloto no lee «del MySQL de ATLAS». Lee de esto.

En la pantalla, un fichero de la carpeta `domain/`, corto como un poema:

```javascript
export class RepositorioDePedidos {
  async buscarPendientesDeFacturar(clienteId) { throw new Error("implementar"); }
  async buscarPorId(pedidoId) { throw new Error("implementar"); }
}
```

—Esto es todo lo que el negocio sabe sobre de dónde salen los pedidos. Un contrato. Cuatro frases en el idioma de facturación. —Pasó a otro fichero—. El MySQL de ATLAS existe, claro, pero vive aquí, en `infrastructure`, en una clase que se llama `MySQLRepositorioDePedidos`, y es la única de todo el módulo que sabe SQL. Ciento veinte líneas. Si Vesta quiere PostgreSQL en su nube, escribimos `PostgreSQLRepositorioDePedidos`, la enchufamos, y el negocio — el cálculo, los descuentos, los impuestos, los tests — no se entera. Ni una línea.

Óscar se quedó mirando la pantalla. Se acercó. Leyó el fichero del contrato entero, que tardaba ocho segundos en leerse.

—¿Y esto lo tenéis así… por qué? ¿Sabíais lo de Vesta?

—No. —Júlia dudó un instante y decidió que la verdad completa era mejor—. Lo tenemos así porque sin esto no hay tests. Para probar el cálculo de una remesa no podemos levantar el MySQL de ATLAS cada vez: los tests usan un `InMemoryRepositorioDePedidos`, treinta líneas, un array. Mil doscientos tests en cuatro segundos. La portabilidad no la buscamos. Vino sola. Es la misma puerta: si el negocio no sabe qué hay detrás del contrato, da igual que detrás haya un array de test o el PostgreSQL de Ferrán.

—Enséñame el de los tests —dijo Óscar. Era la primera vez que pedía ver código en meses.

Denís, que esperaba ese momento como se espera un cumpleaños, lo puso en pantalla:

```javascript
export class InMemoryRepositorioDePedidos extends RepositorioDePedidos {
  #pedidos = [];
  async guardar(pedido) { this.#pedidos.push(pedido); }
  async buscarPendientesDeFacturar(clienteId) {
    return this.#pedidos.filter((p) => p.esDe(clienteId) && !p.estaFacturado());
  }
  async buscarPorId(pedidoId) {
    return this.#pedidos.find((p) => p.getId() === pedidoId) ?? null;
  }
}
```

—Treinta líneas —dijo Denís—. Es la misma caja con otro relleno. Al negocio le da exactamente igual. Esta semana le hemos enchufado tres rellenos distintos: el MySQL real, este de memoria, y uno de mentira que falla a propósito para probar qué pasa cuando la base de datos se cae un martes a las tres.

Se hizo uno de esos silencios que Júlia había aprendido a no interrumpir. Óscar seguía mirando la pantalla, y lo que le pasaba por la cara ya no era escepticismo: era aritmética. Estaba, se dio cuenta Júlia, comparando aquello con algo — con un recuerdo, con un presupuesto, con nueve meses de diapositivas, quién sabe.

—Fénix tenía una capa de datos común —dijo por fin, en voz rara, casi para sí—. Un framework entero. Genérico, configurable, para cualquier motor. Nos costó cuatro meses. —Tamborileó en la mesa—. Cuatro meses el framework, y luego cada pantalla hacía sus consultas por su cuenta igualmente, porque el framework era lento para los listados. Al final teníamos las dos cosas: la catedral y los atajos.

—¿Y esto en qué se diferencia? —preguntó, y por una vez la pregunta no era retórica ni hostil. Era una pregunta.

—En que esto no es un framework —dijo Júlia—. Es un contrato por concepto. `RepositorioDePedidos` no sabe leer «cualquier cosa de cualquier motor»: sabe responder cuatro preguntas sobre pedidos, las cuatro que facturación necesita, y ni una más. El día que facturación necesite una quinta pregunta, se añade la quinta. No hay catedral. Solo puertas del tamaño exacto de quien las cruza.

Óscar asintió muy despacio. Recogió su portátil, y en la puerta se detuvo.

—Preparad el plan para Ferrán. PostgreSQL, su nube, lectura para nosotros. Tres semanas. —Y añadió, sin mirar a nadie en concreto—: Presupuesto para el piloto: un mes más. Lo saco de la partida de NG.

Cuando la puerta se cerró, Denís levantó los dos puños al techo en silencio absoluto, como un futbolista que celebra en fuera de juego.

---

Gabriel escuchó el relato por la tarde, mientras cambiaba un disco del servidor de backups, y emitió su veredicto con la parquedad de costumbre:

—La partida de NG. Vaya, vaya. —Atornilló la bandeja—. ¿Sabéis qué es lo mejor que habéis hecho esta semana? Y no es la demo.

—¿El qué?

—El nombre. —Cerró el armario rack—. `Repositorio`. Todo lo que habla con el exterior, en vuestro módulo, se llama repositorio-de-algo. No hay `Manager`, ni `Handler`, ni `DataService`, ni `Helper`. Cuando yo leo `MySQLRepositorioDePedidos` sé exactamente qué es, qué hace y dónde vive, sin abrirlo. En ATLAS hay ciento y pico clases que hablan con algo de fuera y tienen setenta y tres nombres distintos. Cada una fue la ocurrencia de alguien un martes. —Se guardó el destornillador en el bolsillo—. Los patrones no valen por listos. Valen por *repetidos*. Un pasillo con todas las puertas iguales se recorre a oscuras.

Júlia lo apuntó esa noche en sus notas, casi textual, junto a otra cosa que no le contó a nadie: que al enseñarle la arquitectura a Óscar, en la pizarra, había dibujado sin darse cuenta el mismo diagrama — círculo dentro, cajas fuera, flechas entrando — que aparecía en el capítulo seis del faro, trazado en ASCII art por una mujer a la que nunca había visto.

Le quedaba una duda, sin embargo, una que el capítulo seis mencionaba de pasada y prometía desarrollar en el ocho, y que se estaba convirtiendo en la pregunta de fondo de todo: el contrato del repositorio hablaba «el idioma del negocio». Pedidos «pendientes de facturar». Facturas «vencidas». ¿Quién decidía ese idioma? ¿Los programadores? ¿Marta? ¿El código de quién era ese diccionario?

Porque esa misma mañana, en la cocina, había oído a Marta decirle por teléfono a alguien de Vesta que «el abono se lo aplicamos en la próxima remesa», y Denís, que estaba delante, había asentido convencido — y Júlia sabía con certeza absoluta que Denís creía que «abono» era una cosa y Marta estaba diciendo otra.

Lo apuntó también. *Preguntar qué es un abono. A Marta, no a Denís.*

Iba a ser la pregunta más rentable de su carrera, pero eso todavía no lo sabía.
