La presentación de ATLAS NG duró cuarenta minutos y fue, Júlia tuvo que admitirlo, hermosa.

La consultora había hecho un buen trabajo: diagramas de cajas ordenadas, un stack moderno, microservicios con nombres en inglés, una demo con una interfaz limpia como un quirófano. Óscar cerró con la diapositiva del calendario: nueve meses de desarrollo en paralelo — «el equipo actual mantiene ATLAS; un equipo nuevo construye NG» —, migración de clientes en el mes diez, apagado del Monstruo en el doce. Aplauso tibio. Marta preguntó cuánto costaba. La cifra hizo ese silencio que hacen las cifras con muchos ceros.

—¿Preguntas técnicas? —dijo Óscar.

Júlia levantó la mano. Notó su propio pulso en el cuello. Dos meses antes no habría abierto la boca en una reunión general ni bajo tortura.

—¿Qué hacemos con las peticiones de los clientes durante los nueve meses? Vesta pide cambios cada semana.

—Se implementan en ATLAS, como siempre, y el equipo de NG las incorpora a su plan.

—Entonces NG persigue un blanco móvil —dijo Júlia. No lo dijo como un desafío; lo dijo como quien lee un número en un termómetro—. Cada semana que pasa, la distancia entre los dos sistemas crece. Para alcanzar a ATLAS, NG tiene que correr más rápido de lo que ATLAS cambia, durante nueve meses, sin equivocarse en nada que ATLAS ya resuelve. Incluido el tipo 7, que no sabemos qué es.

Se hizo un silencio distinto al de la cifra. Varias cabezas veteranas se giraron hacia Júlia con una expresión extraña, casi supersticiosa, y ella comprendió — un segundo tarde, como se comprenden estas cosas — que acababa de describir, sin saberlo, algo que ya había ocurrido.

Óscar tardó en contestar. Cuando lo hizo, su voz era perfectamente plana.

—Por eso esta vez lo hará un equipo dedicado, con presupuesto propio. Siguiente pregunta.

*Esta vez.*

---

Esa tarde, Júlia fue a la mesa de Gabriel, y no le preguntó por servidores.

—Cuéntame qué fue el proyecto Fénix.

Gabriel se quedó muy quieto, de esa quietud suya de servidor antiguo. Luego se levantó sin decir nada, cogió su chaqueta y señaló la puerta con la cabeza. Bajaron al bar de la esquina, uno de camareros mayores y máquina tragaperras, y no habló hasta que tuvo el café delante.

—¿Qué sabes ya?

—Que hace unos diez años se intentó reescribir ATLAS desde cero. Que duró dos años y casi se lleva la empresa. Que la arquitecta se llamaba Silvia Roca y que después se marchó. Que nadie habla de ello. —Júlia dudó y decidió jugarlo todo—: Y sé que existe `faro`. Lo encontré la noche del bug de Vesta. Llevo dos meses leyéndolo. Y sé que tú también lo conoces, porque el pósit de la cocina lo escribiste tú imitando su manera de hablar. «Pregunta por qué.» Estoy preguntando.

Gabriel sonrió a su café, una sonrisa breve, con más años que humor.

—Le dije a Silvia que algún día alguien lo encontraría. Ella decía que no, que la gente ya no lee. —Removió el azúcar con una lentitud deliberada—. Está bien. La historia. La historia de verdad, no la versión de pasillo.

»Dos mil quince, más o menos. ATLAS tenía la mitad de años que ahora, pero ya era el Monstruo: cada cambio costaba el triple, los clientes se quejaban, todos estábamos hartos. Y entonces alguien — no importa quién — dijo la frase. La frase que tú ya has oído esta mañana con otro nombre: *sería más rápido hacerlo de nuevo.* —Levantó la vista—. Entiéndeme: no es una frase estúpida. Es una frase *lógica*. Todo programador la siente delante de código viejo, igual que todo el que entra en una casa desordenada siente ganas de quemarla y construir otra. Leer es más difícil que escribir, siempre. El código de otros parece peor de lo que es, siempre. Y uno se cree mejor de lo que es. Siempre.

—¿Silvia estaba a favor?

—Silvia estaba *al mando*. Y al principio estaba a favor, sí. Era la mejor programadora que ha pisado esa oficina, con diferencia, y esa fue exactamente la trampa: era tan buena que se creyó capaz. Y dirección le dio la mejor gente, y a los demás nos dejaron el mantenimiento del viejo. —Bebió—. ¿Sabes lo que pasa cuando pones a tu mejor gente a construir el sistema nuevo y dejas el viejo con lo justo? Que el viejo empeora más rápido, los clientes gritan más fuerte, y las urgencias van saliendo del presupuesto del nuevo. Empezamos siendo seis en Fénix. A los seis meses éramos cuatro. Al año, tres.

»Y aun así lo peor no fue eso. Lo peor fue lo que tú has dicho hoy en la reunión con veinticuatro años y dos meses de empresa, y que nosotros con toda nuestra experiencia no quisimos ver: el blanco móvil. Fénix empezó con una foto de ATLAS de 2015. Mientras lo construíamos, ATLAS siguió cambiando, porque el negocio no espera. Cada acuerdo nuevo de Marta, cada peculiaridad nueva de cada cliente, había que hacerla dos veces: en el viejo, porque facturaba, y en el nuevo, para no quedarse atrás. Nunca íbamos por delante. Dos años corriendo para llegar, con suerte, a *empatar* con un sistema que odiábamos.

—¿Y el negocio? —preguntó Júlia—. ¿Fénix al menos entendía mejor el dominio? ¿La facturación, los abonos, todo eso?

Gabriel la miró un momento con una expresión indescifrable, como si la pregunta le hubiera tocado un nervio concreto.

—Esa —dijo lentamente— es exactamente la pregunta correcta, y la respuesta es la parte de la historia que no te voy a contar hoy. No por secretismo. Porque no la vas a entender todavía. Cuando llegues al capítulo ocho del faro, vuelve y me la haces otra vez. —Apuró el café—. Te cuento el final. Mes veintidós. Fénix facturaba en paralelo, en pruebas, con datos reales copiados. Y los números no cuadraban. No mucho. Céntimos. —Sonrió sin sonreír al ver la cara de Júlia—. Sí. Céntimos. El Monstruo tenía quince mil pequeñas verdades aprendidas a golpes, y Fénix, que era limpio y moderno y precioso, no sabía ninguna. Cada descuadre era una regla de negocio que nadie recordaba haber decidido y que solo existía en el código viejo, escrita por alguien que ya no estaba, por un motivo que nadie apuntó. Dirección hizo cuentas: alcanzar la paridad real costaba otro año, y la caja daba para tres meses. Vesta, que ya entonces era el cliente gordo, se enteró de que llevábamos dos años invirtiendo en un sistema que no existía mientras su ATLAS acumulaba parches. Estuvieron a esto de irse. —Separó dos dedos un centímetro—. Fénix se canceló un viernes por la tarde. La empresa despidió a nueve personas para sobrevivir. Y a mí me tocó ejecutar la orden.

—¿Qué orden?

—Borrar los repositorios. —Lo dijo sin dramatismo, mirando la mesa—. Dirección no quería que quedara «tentación de retomarlo». Yo era el admin. Obedecí. Veintidós meses de trabajo de la mejor gente que he conocido: `rm`, y a otra cosa. —Pausa larga—. Lo de Silvia no fue por la cancelación. Fue por cómo se repartió el después. Alguien tenía que cargar con Fénix, y el nombre de Silvia estaba en el diseño, así que la historia oficial fue sencilla: la arquitecta se equivocó. Nadie recordó quién había aprobado qué, ni con qué prisas, ni con qué avisos. Ella no se defendió. Escribió `faro` en sus últimas semanas, aquí, de noche — mira la fecha de los commits algún día —, me pidió que no lo borrara, y se fue. No la despidieron. Se fue ella. Me dijo una cosa el último día que no he olvidado: «Gabriel, el fuego no fue el error. El error fue creer que el fénix nace del fuego. De un incendio no nace nada. Las cosas renacen de otra manera: rama a rama, mientras el árbol viejo sigue en pie.»

Júlia estuvo un rato callada, dándole vueltas al posavasos. La tragaperras del fondo soltó su musiquilla idiota.

—Y ahora Óscar va a hacerlo otra vez.

—Óscar. —Gabriel se pasó la mano por la barba—. Óscar estuvo en Fénix, ¿sabes? De los seis primeros. Era joven, era brillante y era el que más creía. Para él no fue un proyecto fallido: fue *el* proyecto, el que le enseñó lo que duele. Y hay dos maneras de digerir un dolor así. Una es entender por qué pasó. La otra es decidir que la idea era buena y la ejecución fue mala, y que *esta vez*, con más dinero y más consultores, saldrá. —Se encogió de hombros—. Diez años lleva masticándolo. La diapositiva de esta mañana es su segunda oportunidad. No es tonto ni malo, Júlia. Es un hombre pagando una deuda con la persona equivocada.

—¿Y qué hago yo? —La pregunta le salió más desnuda de lo que quería—. Yo soy la última mona. He leído cuatro capítulos de un repositorio muerto y he tenido *una* buena semana con un arnés de tests. No puedo plantarme delante de dirección a decir que el plan de nueve meses del CTO es el mismo error de hace diez años con logos nuevos.

Gabriel se levantó, dejó dos monedas sobre la mesa y se puso la chaqueta con calma de hombre que ya ha visto arder una cosa y no piensa ver arder otra.

—No. Tú no puedes decir eso. —Se anudó la bufanda—. Pero puedes hacer lo que hizo la del pósit: en vez de discutir el dibujo bonito, enseñar uno *verdadero*. Tienes un módulo de facturación con trescientos doce tests que no tenía nadie, un mapa en la cocina que entiende hasta Marta, y el capítulo cuatro del faro sin leer. Silvia no escribió ese capítulo para desahogarse. Lo escribió como plan. Léelo esta noche. Y mañana pídele a Óscar tres meses.

---

El capítulo `04-las-capas.md` era el más largo del cuaderno, y se notaba que Silvia lo había escrito ya de salida, con la libertad de quien no tiene nada que perder:

> *Si algún día alguien intenta salvar este sistema — de verdad, no con otro incendio —, que empiece por entender por qué es insalvable a trozos grandes y perfectamente salvable a trozos pequeños.*
> *El Monstruo no es malo porque sea viejo. Es malo porque no tiene dentro y fuera. La regla de negocio que calcula un descuento, la consulta que lo lee de la base de datos y el HTML que lo pinta viven en las mismas funciones, agarrados unos a otros. No puedes cambiar una pieza sin levantar el edificio, porque el edificio no tiene piezas: es un bloque de hormigón con ventanas pintadas.*
> *La salida tiene tres reglas y caben en una servilleta:*
> *Uno. Dentro, el negocio; fuera, el mundo. El cálculo de una factura es negocio. MySQL, el PDF, el HTTP, son mundo. El negocio no debe saber que el mundo existe.*
> *Dos. Las dependencias apuntan hacia dentro. El mundo puede conocer al negocio; el negocio, al mundo, jamás. Cada import que cruza esa frontera hacia fuera es una gotera.*
> *Tres. La frontera se cruza por puertas con contrato. El negocio declara qué necesita — «guárdame esto», «dame aquello» — y el mundo lo sirve como pueda: hoy MySQL, mañana lo que sea. Mientras el contrato se respete, cambiar el mundo no toca el negocio.*
> *Y si alguien pregunta por dónde empezar, la respuesta no es «por todas partes». Es: por UNA habitación. Se elige el módulo que más duela — aquí, facturación, siempre facturación —, se le construye al lado su versión con dentro y fuera, se desvía el tráfico poco a poco, con el sistema viejo funcionando, y solo cuando la habitación nueva lleva meses aguantando el peso se tapia la vieja. Los ingleses tienen un nombre bonito para esto, por una higuera que crece abrazada a un árbol hasta sustituirlo. Nosotros lo intentamos al revés: talamos el bosque para plantar uno nuevo, y nos quedamos dos años sin sombra.*
> *P.D. para quien seas: no reescribas. Estrangula. Y no le pongas a nada el nombre de un pájaro que arde.*

Júlia leyó la posdata dos veces, cerró el portátil y estuvo un buen rato mirando el techo de su habitación.

Luego abrió un documento nuevo y escribió, arriba del todo: **«Propuesta: facturación, tres meses, sin apagar nada.»**

Le costó dormirse. No era miedo. Era la sensación, nueva y eléctrica, de estar a punto de continuar el trabajo de otra persona.
