Las palabras del idioma ya están aprendidas. Esta ampliación cuenta sus etimologías: de dónde salió el circuito resonante, por qué el cuarzo sabe la hora, qué era la misteriosa bombilla en serie de Dani, y un par de esquinas del oficio que convierten teoría en criterio.

## El columpio tiene partida de nacimiento: la botella de Leyden

El circuito resonante no lo inventó un ingeniero de radio: lo descubrió, sin buscarlo, el físico Joseph Henry hacia 1842, al observar que la descarga de una botella de Leyden (el primer condensador, un tarro de vidrio forrado de estaño) a través de una bobina magnetizaba agujas... unas veces en un sentido y otras en el contrario. La descarga no era un chorro: era un vaivén que se amortiguaba, un columpio que se paraba solo. Lord Kelvin puso la matemática en 1853, y medio siglo después aquel columpio olvidado resultó ser el corazón de la radio: los primeros transmisores de chispa de Marconi eran exactamente eso, botellas de Leyden descargándose por bobinas, columpios brutales que sacudían el éter con cada chispazo.

Detalle que une los cabos del curso: aquellas descargas oscilantes y amortiguadas generaban señales anchísimas y sucias que ensuciaban todo el espectro (por Fourier: onda breve y abrupta = frecuencias por todas partes). La telegrafía de chispa fue prohibida internacionalmente en los años veinte por interferente; fue la primera gran «limpieza de bandas» de la historia y el empujón definitivo hacia los osciladores de onda continua... es decir, hacia el mundo cuyo examen estás preparando.

## Por qué el cuarzo sabe la hora

La teoría te dijo que el cristal de cuarzo equivale a un LC de Q altísimo. El porqué merece su párrafo: el cuarzo es **piezoeléctrico** (descubrimiento de los hermanos Curie, 1880): apriétalo y genera tensión; aplícale tensión y se deforma. Una lámina de cuarzo tallada tiene una frecuencia de vibración mecánica propia —como una campana microscópica— y, gracias a la piezoelectricidad, esa vibración mecánica y el circuito eléctrico se hablan. Resultado: un resonador cuya frecuencia depende de las dimensiones físicas de una piedra tallada, estables hasta el aburrimiento. Donde una bobina real logra Q de 100 o 200, un cristal pasa de 10.000 y llega a millones.

El reloj de cuarzo de tu muñeca (y de tu horno, y de tu coche) lleva un diapasón de cuarzo tallado a 32.768 Hz. ¿Por qué ese número feo? Porque es 2 elevado a 15: divide su frecuencia por dos quince veces con contadores binarios baratos y obtienes exactamente 1 Hz, un tic por segundo. Es posiblemente el compromiso ingenieril más elegante que llevarás puesto jamás.

Y la miniatura radioaficionada: durante décadas, «cambiar de frecuencia» significaba literalmente **cambiar de piedra**: los equipos llevaban zócalos donde se enchufaba el cristal de la frecuencia deseada, y los operadores llevaban cajitas con sus cristales como quien lleva llaves. En los mercadillos como el de Xenillet todavía aparecen, en sus cápsulas metálicas con la frecuencia grabada. Si encuentras uno marcado «7030 kc», tienes en la mano una frecuencia fosilizada (y ya sabes leer los kilociclos).

## La bombilla en serie: el instrumento de seguridad más barato del mundo

El truco de Dani merece explicación completa, porque es un clásico universal de taller y un repaso de media ley de Ohm. Se conecta una bombilla incandescente **en serie** con el aparato sospechoso, y ocurre esto:

- Si el aparato está sano, consume su corriente normal, modesta: la bombilla apenas se enciende (cae poca tensión en ella) y el aparato arranca casi normal.
- Si el aparato tiene un **cortocircuito**, la corriente intenta dispararse... pero al crecer la corriente, el filamento de la bombilla se calienta, y el filamento caliente multiplica su resistencia (sección 2: los metales suben de resistencia con la temperatura). La bombilla se convierte en el elemento dominante del circuito, se lleva casi toda la tensión, brilla a plena luz... y el aparato enfermo queda alimentado con una miseria inofensiva.

Es decir: una resistencia *autorregulable* que da diagnóstico visual (brillo fuerte y fijo = corto dentro) y protección simultáneos, por el precio de una bombilla de filamento. Los restauradores la llaman «lámpara serie» y es el primer aparato que se construye cualquiera que repare equipos antiguos. Con los LED esto no funciona, por cierto: hacía falta el filamento y su física. Motivo sentimental adicional para el aprecio: es tecnología de 1880 protegiendo tecnología de 1970 bajo supervisión de un polímetro de 2020. Tres siglos de electricidad en un enchufe.

## Q de «quality»... y de quejarse: el lado oscuro de la selectividad

El factor Q parece siempre deseable: más Q, más selectividad, más pureza. Ahora, el matiz de ingeniero: un circuito de Q altísimo también es **lento**. Un columpio finísimo tarda muchos ciclos en arrancar y muchos en pararse (la energía entra y sale despacio de un resonador poco amortiguado). Traducción a radio: un filtro estrechísimo «suena» — las señales de morse rápidas se emborronan, los clics se alargan como campanadas. Los telegrafistas lo llaman *ringing*, campaneo. Por eso los filtros de los receptores son conmutables: ancho para fonía, medio para morse cómodo, estrechísimo solo para pescar señales agónicas entre interferencias, aceptando el campaneo. No existe el filtro perfecto; existe el filtro adecuado a cada momento. Guarda esta idea: reaparecerá en la sección 7 con la selectividad, y es de las que distinguen al operador que entiende de quien solo aprieta botones.

## Rizado con banda sonora: cómo suena una fuente enferma

El rizado de las fuentes tiene diagnóstico acústico, y reconocerlo de oído es un pequeño superpoder de club. Si en una transmisión de fonía se oye un zumbido grave mezclado con la voz, hay alterna colándose donde no debe. Y el tono delata al culpable: un zumbido a **50 Hz** (el grave profundo de los transformadores) apunta a inducción directa de la red o rectificación de media onda; a **100 Hz** (una octava más arriba), a filtrado insuficiente tras un puente rectificador —el electrolítico seco de manual—. Los veteranos de oído fino te dicen «llevas cien hercios de rizado, revisa la fuente» por radio, gratis, como quien te avisa de que llevas una rueda floja. En tiempos de las válvulas y sus fuentes de alta tensión esto era epidemia; hoy ha vuelto por la puerta de los cargadores conmutados baratos, que en vez de zumbar *rascan*. Cada época tiene la banda sonora de sus averías.

## Regla del pulgar: dónde está la frecuencia en un esquema

Truco de lectura rápida heredado de generaciones de reparadores, para cuando mires tus primeros esquemas de verdad: en un aparato de radio, **la frecuencia baja va con condensadores gordos y la alta con condensadores diminutos**. Ves electrolíticos de miles de µF: estás en la fuente (50-100 Hz). Ves µF y nF de plástico: audio (cientos a miles de Hz). Ves picofaradios cerámicos y bobinas al aire: radiofrecuencia. Es la reactancia trabajando al revés: cada etapa usa los tamaños que le dan impedancias cómodas a su frecuencia. Con este pulgar y las «palabras» de la teoría, un esquema desconocido se deja cartografiar en un minuto: fuente aquí, audio allá, RF en aquella esquina. Amparo lo habría explicado más corto: «dime el tamaño de tus condensadores y te diré a qué frecuencia trabajas».

## Para seguir tirando del hilo

- Wikipedia (CC BY-SA): «Botella de Leyden», «Transmisor de chispa», «Cristal piezoeléctrico» y «Lámpara en serie» (en la edición inglesa, *dim-bulb tester*): las historias completas con referencias.
- En falstad.com/circuit, monta el circuito «LRC» y ve subiendo la resistencia: verás el columpio amortiguarse exactamente como la descarga de Henry de 1842. Luego busca «full-wave rectifier» y observa nacer el rizado en vivo.
- Si te ha gustado la bombilla en serie: busca «dim bulb tester» y tendrás tu primer proyecto de taller documentado en mil versiones. Materiales: cinco euros. Lecciones: incontables.
