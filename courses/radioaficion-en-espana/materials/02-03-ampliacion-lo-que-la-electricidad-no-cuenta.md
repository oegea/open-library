La teoría te ha dado las cuatro magnitudes y su ley. Esta ampliación añade el contexto, las esquinas curiosas y un par de verdades prácticas que algún día te ahorrarán un susto o una avería.

## Los apellidos de las unidades: una pequeña galería de retratos

Todas las unidades eléctricas son apellidos, y sus dueños se conocieron, se pelearon y se admiraron entre sí:

- **Alessandro Volta** (voltio) presentó en 1800 la primera pila: discos de cinc y cobre separados por paños empapados en salmuera. Napoleón, fascinado, lo cubrió de honores. Antes de la pila de Volta, la electricidad solo existía en chispazos; con ella, por primera vez, hubo *corriente continua* disponible para experimentar.
- **André-Marie Ampère** (amperio) construyó la teoría matemática de la corriente en unas semanas frenéticas de 1820, tras enterarse de que una corriente movía una brújula. Vida trágica y mente prodigiosa: su lema, grabado en su tumba, fue *tandem felix* («feliz, al fin»).
- **Georg Simon Ohm** (ohmio) era un profesor de instituto sin laboratorio ni fortuna. Su ley (1827) fue recibida en Alemania con desdén —un crítico la llamó «una red de fantasías desnudas»— y tardó casi veinte años en ser reconocida. Hoy su apellido se escribe con Ω, la letra griega omega, en todos los circuitos del planeta. Paciencia para los que llegan pronto.
- **James Watt** (vatio) ni siquiera era «eléctrico»: fue el ingeniero escocés de la máquina de vapor. Su unidad se adoptó para la potencia en general, porque la potencia es potencia, venga del vapor o de una batería. Watt inventó también el «caballo de vapor» (735,5 W) para venderles máquinas a dueños de caballos, en lo que quizá sea el primer ejemplo de marketing técnico de la historia.
- **Werner von Siemens** (siemens, la unidad de conductancia) fundó además la empresa que lleva su nombre y tendió algunas de las primeras grandes líneas telegráficas europeas.

## La resistividad, con números de verdad

La teoría te dijo que la resistencia depende del material. El dato preciso es la **resistividad** (ρ, en Ω·mm²/m): la resistencia de un hilo de ese material de un metro de largo y un milímetro cuadrado de sección.

| Material | ρ (Ω·mm²/m) aprox. | Comentario |
|---|---|---|
| Plata | 0,016 | La mejor. Se usa en baños para contactos y bobinas de calidad |
| Cobre | 0,017 | El caballo de batalla: casi tan bueno y mucho más barato |
| Oro | 0,024 | Peor que el cobre... pero no se oxida jamás: por eso baña conectores |
| Aluminio | 0,028 | Ligero y barato; líneas de alta tensión y antenas |
| Hierro | 0,10 | Malo como conductor; en radio, casi solo estructural |
| Nicrom | ~1,1 | Fatal a propósito: es el hilo de las estufas y tostadoras |

Dos sorpresas útiles ahí: el oro **no** es el mejor conductor (se usa por inoxidable, no por conductor), y el aluminio, aunque peor que el cobre a igual sección, conduce *mejor a igual peso*: por eso las antenas grandes y los tendidos eléctricos son de aluminio.

La fórmula completa, por si la ves: `R = ρ × L / S` (longitud entre sección, por la resistividad). Un ejemplo con sentido radioaficionado: 30 metros de cable de cobre de 1,5 mm² para alimentar tu equipo desde una batería lejana suponen R = 0,017 × 30 / 1,5 = 0,34 Ω *por conductor*, 0,68 Ω contando ida y vuelta. A 10 amperios, la ley de Ohm te roba U = 10 × 0,68 = 6,8 V... ¡de tus 12! El equipo se apagaría al transmitir. Moraleja de oro para siempre: **la batería cerca del equipo, y los cables de alimentación cortos y gordos**. Este error (cable fino y largo en 12 V) es posiblemente la avería fantasma más común entre principiantes.

## Superconductores: cuando la resistencia se rinde

En 1911, Heike Kamerlingh Onnes enfrió mercurio a −269 °C y observó que su resistencia desaparecía. No «casi cero»: **cero**. Una corriente lanzada en un anillo superconductor sigue girando sola años después, sin batería, sin pérdidas. Los superconductores hacen posibles los imanes de las máquinas de resonancia magnética y de los aceleradores de partículas. Para la radio doméstica no tienen aplicación (de momento: hay filtros superconductores en algunas estaciones base), pero conocer su existencia redondea la idea de resistencia: es una propiedad del material *y de sus condiciones*, no un absoluto.

Y la anécdota inversa: a temperaturas normales, el mejor conductor práctico conocido no es un metal exótico, sino el grafeno, una lámina de carbono de un átomo de grosor, cuyo estudio dio el Nobel de 2010. El carbono, según cómo se ordene, es un aislante decente (diamante), un conductor regular (grafito de lápiz: pruébalo con el polímetro sobre una raya bien gruesa de lápiz blando) o un superconductor en potencia. El material importa, y la estructura del material, más.

## Cuánta electricidad aguanta una persona

Conviene decirlo pronto y claro, porque vas a montar instalaciones: **lo que mata no son los voltios, son los miliamperios atravesando el cuerpo** (y en particular el corazón). Ordenes de magnitud aceptados en seguridad eléctrica:

- ~1 mA: umbral de percepción (cosquilleo).
- 10-20 mA: contracción muscular; puede impedir soltar el cable («umbral de no soltar»).
- ~30 mA: el valor al que disparan los diferenciales domésticos. No es casual.
- 50-100 mA a través del tórax: riesgo grave de fibrilación cardíaca.

¿Y los voltios? Los voltios son el empujón que decide cuántos miliamperios pasan por tu resistencia corporal (decenas o cientos de kΩ con piel seca; muchísima menos mojada — ley de Ohm otra vez). Por eso 12 V de batería no se sienten al tocarlos (I = 12/50.000 = 0,24 mA), pero esa misma batería puede soldarte una llave inglesa a los bornes con cientos de amperios si la cortocircuitas: tensión inofensiva al tacto + resistencia interna bajísima = corrientes de soldadura. Las dos caras del peligro eléctrico, y ninguna es «los voltios» a secas. En la sección 10 haremos la seguridad completa (condensadores cargados, alta tensión de válvulas, RF, rayos); esta miniatura era solo para que empieces a mirar la ley de Ohm como lo que también es: una norma de seguridad.

## El mito del sentido de la corriente (y por qué no importa)

A cualquier persona que estudie electricidad le llega el momento incómodo: «entonces, ¿la corriente va del + al − o del − al +?». Respuesta completa: los electrones van del − al +; el convenio dice del + al −; y **ninguna fórmula cambia** por ello, porque una carga negativa moviéndose hacia la izquierda es matemáticamente idéntica a una positiva moviéndose hacia la derecha. Benjamin Franklin eligió los nombres «positivo» y «negativo» en el siglo XVIII, con una moneda al aire conceptual, un siglo antes de que J.J. Thomson descubriera el electrón (1897) y se viera que había salido cruz. Cambiar el convenio habría exigido reescribir toda la ciencia publicada; se decidió que no valía la pena, y se sigue decidiendo. En algunos campos (física de semiconductores, que verás en la sección 4) hasta resulta útil: allí se habla con toda seriedad de «huecos» positivos que se mueven de verdad.

## Tres hábitos de electricista viejo, de regalo

1. **Duda de todo cable.** La mitad de las averías de estación son un cable, un conector o una soldadura. Antes de sospechar del carísimo transceptor, mide continuidad en el cable de 3 €.
2. **Fusible en el positivo, junto a la batería.** No a medio camino, no «ya lo pondré»: junto al borne. El fusible protege el cable; un cable que roza chapa con 60 Ah detrás es un soplete.
3. **Apunta los consumos.** Un adhesivo en cada equipo: «RX 0,8 A / TX 10 A». El día que dependas de una batería, esa etiqueta es tu autonomía calculada de un vistazo. Es la libreta cuadriculada de Vicente en versión pegatina.

## Para seguir tirando del hilo

- OpenStax, *Física universitaria* vol. 2 (CC BY 4.0): resistividad y superconductividad con el detalle matemático completo.
- Los artículos de Wikipedia sobre Volta, Ampère, Ohm y la historia de la pila voltaica (CC BY-SA) están muy bien referenciados si te ha picado la parte biográfica.
- Busca en vídeo «battery short circuit wrench» para respetar para siempre a las baterías de 12 V. Mejor verlo que protagonizarlo.
