En la historia, Meridian pierde 4.700,32 € y casi pierde a su mayor cliente por una línea que *funcionaba*. Conviene empezar el curso deteniéndose en esa paradoja, porque es la puerta de entrada a todo lo demás: **el código puede estar bien para la máquina y catastróficamente mal para las personas.** Este capítulo explica por qué eso importa, cuánto cuesta y cuál es la primera herramienta — la más barata y la más infravalorada — para evitarlo: los nombres.

## Código limpio: una definición honesta

Llamamos **código limpio** al código que una persona distinta de su autor puede leer, entender y modificar con seguridad y sin ayuda. La definición tiene truco: no menciona a la máquina. A la máquina le da igual — ejecuta `$aux3` con el mismo entusiasmo que `numeroDeLineasDeFactura`. El código limpio es una disciplina *para humanos*.

¿Y por qué habría de importar tanto el lector? Por una asimetría que todo programador profesional acaba descubriendo: **el código se lee muchas más veces de las que se escribe.** Robert C. Martin lo estima así en su libro *Clean Code* (2008): por cada hora que pasamos escribiendo código nuevo, pasamos del orden de diez leyendo código existente — el nuestro de hace tres meses, el del compañero, el de la dependencia que falla. Escribir rápido y sucio no ahorra tiempo: lo *toma prestado* de todos los lectores futuros, con intereses.

Piensa en la noche del martes de Júlia. La línea 847 tardó en escribirse, quizá, un minuto. Leerla — entenderla de verdad, con su contexto, su `$aux3` camaleónico y su `$modo_calc` — costó una jornada entera de una persona, más una crisis con el cliente, más una reunión de tres horas con dirección. Esa es la contabilidad real del código: no lo que cuesta teclearlo, sino lo que cuesta *volver a entenderlo* cada una de las veces que alguien lo necesita.

## La deuda técnica: qué dijo realmente Ward Cunningham

Para hablar de ese coste acumulado, la industria usa una metáfora que seguramente oirás la primera semana en cualquier empresa: la **deuda técnica**. La acuñó Ward Cunningham — uno de los pioneros de la programación extrema y el inventor de la wiki — en un informe de experiencia de la conferencia OOPSLA de 1992, y merece la pena citar la idea original, porque se usa casi siempre mal:

> «Enviar código por primera vez es como endeudarse. Un poco de deuda acelera el desarrollo siempre que se devuelva pronto mediante una reescritura. [...] El peligro aparece cuando la deuda no se devuelve. Cada minuto que se pasa sobre código no-del-todo-correcto cuenta como interés de esa deuda.»
> — Ward Cunningham, *The WyCash Portfolio Management System* (OOPSLA '92, informe de experiencia; traducción propia)

Fíjate en los matices, porque aquí hay dos ideas que mucha gente con años de carrera no conoce:

1. **La deuda, en la metáfora original, no es «código mal hecho por vagancia».** Es una decisión *consciente*: entrego hoy algo imperfecto para aprender antes del mercado, y devuelvo la deuda en cuanto sé más. Cunningham insistió años después en que él nunca quiso justificar escribir código malo, sino describir el desfase entre lo que el código dice y lo que el equipo ha aprendido del problema. Martin Fowler, en su bliki (martinfowler.com, entrada *Technical Debt Quadrant*), distingue por eso entre deuda **prudente o imprudente** y **deliberada o inadvertida**: la deuda prudente y deliberada es una herramienta; la imprudente e inadvertida — la de `$aux3` — es simplemente ruina.
2. **El interés se paga en la moneda más cara: tiempo de personas.** Cada tarea sobre ATLAS cuesta el triple «porque nadie se fía de nada», escribía Silvia en su cuaderno. Eso es el interés compuesto: no un gran desastre, sino un sobrecoste pequeño y constante en *cada* cambio, para siempre, hasta que alguien amortice.

La consecuencia práctica: un equipo que nunca dedica tiempo a devolver deuda no es un equipo rápido; es un equipo que aún no ha recibido la carta del banco. Vesta, en nuestra historia, es la carta del banco.

## Los nombres: la unidad mínima de diseño

Silvia empezaba su cuaderno por los nombres, y no por modestia: **nombrar es la decisión de diseño más frecuente que tomarás.** Variables, funciones, clases, ficheros, tablas, endpoints: todo necesita nombre, decenas de veces al día, durante toda tu carrera. Un nombre es, en palabras del cuaderno de faro, *una promesa*: le dice al lector qué puede esperar sin obligarle a mirar dentro. El código sucio es, ante todo, un código lleno de promesas rotas o de promesas que nadie hizo.

Veamos la línea del desastre, reescrita solo con nombres. El original (en PHP, como el Monstruo; los ejemplos del curso serán normalmente en JavaScript y Python):

```php
if ($cliente_dto > 0 && $aux3 > 1) { $imp = round($imp, 2); }
```

Y una traducción a JavaScript donde lo único que ha cambiado son los nombres:

```javascript
const debeRedondearPorLinea = clienteTieneDescuento && numeroDeLineas > 1;
if (debeRedondearPorLinea) {
  importe = redondearADosDecimales(importe);
}
```

No hemos arreglado el bug. El bug — dos políticas de redondeo distintas conviviendo en silencio — sigue ahí. Pero ahora **se ve**: cualquier lector, incluido un recién llegado, puede preguntar en voz alta «¿por qué redondeamos por línea solo cuando hay descuento y más de una línea?», y esa pregunta, formulada a tiempo, vale 4.700,32 €. Esa es la función real de los buenos nombres: no decorar el código, sino **hacer visibles las decisiones** para que puedan discutirse.

### Qué hace bueno a un nombre

Los criterios esenciales, destilados del capítulo 2 de *Clean Code* y de la práctica común:

- **Revela la intención.** La prueba del algodón: si el nombre necesita un comentario al lado para explicarse, el nombre está mal. `d` no; `diasDesdeUltimoPago` sí. En Python:

  ```python
  # Mal: ¿qué es esto?
  d = (hoy - f).days

  # Bien: no hace falta preguntar
  dias_desde_ultimo_pago = (hoy - fecha_ultimo_pago).days
  ```

- **Una palabra, un concepto — siempre el mismo.** Si en tu sistema «cliente» a veces se llama `cliente`, a veces `customer`, a veces `account` y a veces `$c`, el lector debe hacer tres traducciones mentales por línea. Elegid una palabra por concepto *en equipo* y usadla en todas partes. (Guarda esta idea: en la sección 8 descubrirás que es la semilla de una de las ideas más profundas de DDD, el lenguaje ubicuo.)
- **Pronunciable y buscable.** `genymdhms` no puede decirse en una conversación ni encontrarse con un buscador. `fechaDeGeneracion` sí. Las variables de una letra solo se justifican en ámbitos minúsculos (el índice de un bucle de tres líneas).
- **Sin desinformar.** Peor que un nombre vacío es un nombre que miente. Una función llamada `getCliente()` que además *crea* el cliente si no existe está mintiendo; el día que alguien la llame «solo para consultar» tendrá un efecto que no esperaba. La mentira más común del mundo real es el nombre que *fue* verdad: `facturacion_v2.php` que ya no es la versión nueva, `tmp_pruebas_karim` que lleva nueve años en producción.
- **La longitud del nombre, proporcional a la distancia de uso.** Regla menos conocida y muy útil: cuanto mayor sea el ámbito donde vive el nombre, más descriptivo debe ser. Un `i` en un bucle de tres líneas es perfecto; una variable global llamada `imp` es un crimen con agravante de alevosía.

### El caso `$aux3`, o los nombres como síntoma

Merece autopsia, porque su patología es instructiva. `$aux3`, recordemos, contenía «a veces un importe, a veces un cliente, durante doscientas líneas una fecha». El problema no es solo estético. Un nombre que no puede concretarse casi siempre delata que **la pieza hace demasiadas cosas**: si no puedes nombrar una variable, es que en realidad son tres variables; si no puedes nombrar una función sin usar «y» (`validarYGuardarYNotificar`), es que son tres funciones. Los nombres son el primer sistema de alarma del diseño: cuando cuesten, no busques un sinónimo — busca qué está pidiendo dividirse. La sección 2 (funciones) y la sección 3 (cohesión) desarrollan exactamente esto.

## La regla del boy scout

¿Y qué se hace con quince años de promesas rotas? La respuesta *incorrecta* es «parar el mundo seis meses y limpiarlo todo» — la sección 4 contará por qué esa vía suele acabar en tragedia, y en Meridian tiene nombre propio. La respuesta que funciona la formuló Robert C. Martin, invocando el lema de los boy scouts («deja el campamento más limpio de lo que lo encontraste»), en su capítulo *The Boy Scout Rule* del libro colectivo *97 Things Every Programmer Should Know* (O'Reilly, 2010; el libro está publicado bajo licencia Creative Commons BY-NC-SA 3.0):

> «Deja siempre el código un poco mejor de lo que lo encontraste.» *(traducción propia)*

Cada vez que toques un fichero para tu tarea, mejora *algo* pequeño: renombra una variable críptica, extrae tres líneas repetidas, borra código muerto. No pidas permiso para esto ni lo anuncies en la planificación: es parte de programar, como lavarse las manos es parte de cocinar. La aritmética juega a tu favor: el código que más se toca es exactamente el que más se lee, así que las mejoras se concentran solas donde más rentan. Un sistema no se pudre de golpe y tampoco se sanea de golpe: se sanea *por el camino*.

Dos advertencias de uso, nacidas de cicatrices ajenas:

1. **Mejora pequeña no es rediseño oportunista.** Cambiar un nombre en el fichero que ya estás tocando: sí. Reestructurar medio módulo «ya que estoy»: no — eso mezcla en un mismo cambio tu tarea y tu limpieza, y cuando algo falle nadie sabrá cuál de las dos fue. Commits separados, cambios modestos.
2. **En código sin tests, hasta renombrar tiene riesgo.** Júlia lo va a aprender dolorosamente en la próxima sección. La regla del boy scout alcanza su potencia real cuando existe una red de seguridad — y construir esa red en código legacy es, precisamente, el tema que viene.

## Para llevar

- El código limpio es el que otra persona puede leer, entender y cambiar con seguridad. La máquina no es el público; el público es el compañero cansado de las nueve de la noche.
- El código se lee un orden de magnitud más veces de las que se escribe: optimizar para la escritura es optimizar la parte pequeña del coste.
- La deuda técnica (Ward Cunningham, 1992) es una metáfora sobre *aprendizaje no incorporado al código*, no una excusa para trabajar mal. Se paga interés en cada cambio; la deuda inadvertida e imprudente es la que arruina.
- Un nombre es una promesa. Buenos nombres: revelan intención, un concepto = una palabra, pronunciables, buscables, sin mentiras, longitud proporcional al ámbito.
- Un nombre imposible de poner es un síntoma de diseño: la pieza hace demasiado. Los nombres son el primer sistema de alarma.
- Regla del boy scout: deja cada fichero que toques un poco mejor. Pequeño, constante, sin pedir permiso — y con red de tests en cuanto la tengas.

## Para profundizar

- Ward Cunningham, *The WyCash Portfolio Management System* (OOPSLA '92) — el texto original de la deuda técnica, disponible en c2.com.
- Martin Fowler, entradas *TechnicalDebt* y *TechnicalDebtQuadrant* en martinfowler.com (gratuitas).
- Robert C. Martin, *The Boy Scout Rule*, en *97 Things Every Programmer Should Know* — texto completo abierto (CC BY-NC-SA 3.0) en github.com/97-things.
- Los capítulos 1 y 2 de *Clean Code* (R. C. Martin, 2008) desarrollan la definición de limpieza y el arte de nombrar. Es un libro de pago; lo recomendamos honestamente, con la advertencia de que sus ejemplos en Java acusan la edad.
