Ya sabes qué es una onda y quién la genera. Esta sección responde a las dos preguntas que faltan para completar el viaje de la voz: cómo viaja la onda por el espacio vacío, y cómo se le sube una voz encima. La segunda pregunta —la **modulación**— es de las más preguntadas del examen y de las más rentables para tu vida de operador: cuando la domines, la cascada del SDR se te volverá un texto en claro, como le pasó a Marina.

## La onda electromagnética: dos campos bailando agarrados

Cuando la corriente alterna de RF recorre una antena, alrededor del conductor nacen dos cosas que ya conoces por separado: un **campo eléctrico** (E, el de los condensadores) y un **campo magnético** (H, el de las bobinas), ambos oscilando al ritmo de la corriente. Maxwell demostró en 1865 la maravilla: un campo eléctrico variable *genera* un campo magnético, y un campo magnético variable *genera* un campo eléctrico. Cada uno crea al otro. A frecuencias suficientes, la pareja se emancipa del conductor y se va: una **onda electromagnética**, los dos campos regenerándose mutuamente mientras avanzan por el espacio —vacío incluido: no necesitan medio alguno— a la **velocidad de la luz** (c ≈ 300.000 km/s; la luz *es* una onda electromagnética de frecuencia altísima).

Datos con consecuencia práctica:

- Los campos E y H oscilan **perpendiculares entre sí y perpendiculares a la dirección de avance** (onda transversal).
- La **polarización** de la onda es la orientación de su campo eléctrico: una antena vertical emite polarización **vertical**; una horizontal, **horizontal**. Importa porque receptor y emisor con polarizaciones cruzadas pierden muchísima señal en comunicación directa (hasta 20 dB): por eso los walkies (antena vertical) se hablan bien entre sí, y las yagis de los concursos de VHF van todas horizontales, por convenio. (En HF a larga distancia la ionosfera revuelve la polarización y el asunto pierde dramatismo.)
- En el espacio libre, la señal se debilita con el cuadrado de la distancia (doble distancia = un cuarto de potencia = −6 dB): la energía se reparte sobre una esfera cada vez mayor. La onda no «se gasta»: se diluye.

## Modular: subir la voz a la onda

Tu voz es una onda de entre 300 y 3.000 Hz aproximadamente (la **banda vocal** útil para comunicaciones). No puede radiarse directamente: a esas frecuencias las antenas eficaces medirían decenas de kilómetros (λ = 300/0,001 MHz = 300 km para 1 kHz...), y además todas las conversaciones del mundo se pisarían en las mismas frecuencias.

La solución universal: usar una onda de RF como vehículo. Esa onda se llama **portadora** (*carrier*): una senoide pura y estable, nacida de un oscilador, en la frecuencia que elijas del dial. **Modular** es alterar alguna propiedad de la portadora (su amplitud, su frecuencia o su fase) al ritmo de la información que quieres enviar. El receptor hace la operación inversa —**demodular** o **detectar**— y recupera la información.

Toda modulación paga un precio en espacio: la portadora pura ocupaba un punto del espectro; la portadora modulada ocupa una franja, el **ancho de banda**. La regla profunda (es Fourier otra vez): cuanta más información por segundo, más ancho de banda. No hay truco que lo esquive, solo maneras más o menos elegantes de gastar.

## CW: la modulación mínima

El modo más antiguo y sencillo: **encender y apagar la portadora** siguiendo el código morse. Se llama **CW** (*Continuous Wave*, onda continua, nombre paradójico que heredó de la lucha contra las chispas: la portadora es continua *mientras está encendida*, a diferencia de los chispazos amortiguados).

- **Ancho de banda: ~100-200 Hz.** Un alfiler. Quince conversaciones de CW caben donde una de voz.
- Toda la potencia se concentra en ese alfiler: por eso el CW «llega» donde la voz muere. Con 5 W de CW se cruza el Atlántico un día normal.
- El receptor necesita un truco para oírlo: una portadora apagándose y encendiéndose no suena a nada (no hay audio que extraer). El receptor añade un oscilador propio (**BFO**, oscilador de frecuencia de batido) que se mezcla con la señal y genera un tono audible con la diferencia. De ahí el «piiii-pi-pi» musical: el tono lo pone tu receptor, no el transmisor.

## AM: la portadora y sus dos copias

La **modulación de amplitud (AM)** hace variar la **amplitud** de la portadora al ritmo de la voz: la envolvente de la onda de RF dibuja la forma de la onda de audio. Es el modo de la radio de onda media de toda la vida y el de las primeras décadas de la radioafición.

Al modular en amplitud, el espectro resultante tiene exactamente la anatomía que Dani dibujó con tres jorobas:

- La **portadora** en el centro, intacta, cargando con la mayor parte de la potencia sin llevar información alguna.
- Dos **bandas laterales** (*sidebands*), una por encima y otra por debajo, cada una conteniendo una copia completa de la voz (una en espejo). Si tu voz llega hasta 3 kHz, cada banda lateral ocupa 3 kHz.

**Ancho de banda AM = 2 × frecuencia máxima de la modulación.** Voz de 3 kHz → 6 kHz de ancho. (Cae en el examen con estos números exactos.)

Balance energético desolador: con modulación al máximo, la portadora se lleva un 67 % de la potencia y cada banda lateral un 17 %. Más de dos tercios del vatio, en cargar; y de lo restante, la mitad duplicada. «Pagar tres billetes para viajar uno.»

Su virtud, que explica su supervivencia en radiodifusión y aviación: el receptor es trivial (un diodo detector basta: la radio de galena) y las estaciones se escuchan sin sintonía fina.

## SSB: la sombra sin cuerpo

La **banda lateral única** (**SSB**, *Single SideBand*) es AM sometida a dieta radical: se **suprime la portadora** (no informa) y se **suprime una de las dos bandas laterales** (redundante). Al aire sale solo una banda lateral: la «sombra» de la voz.

- **Ancho de banda: ~2,4-2,7 kHz.** Menos de la mitad que AM.
- **Toda** la potencia del transmisor va a la información: combinando el ahorro de portadora y de banda duplicada, una SSB rinde como una AM de varias veces más potencia.
- El precio: el receptor debe **reinsertar la portadora** que falta, con un oscilador local, para reconstruir el audio. Si esa portadora reinsertada está desviada aunque sea 100 Hz, la voz se reconstruye desplazada en frecuencia: **el pato de Marina**. Sintonizar SSB es ajustar hasta que la voz «encaja». (Con la práctica, dos segundos.)

Convenio universal que debes memorizar (examen y práctica diaria): de las dos bandas laterales posibles, se usa la **inferior (LSB)** en las bandas por debajo de 10 MHz (160, 80 y 40 metros) y la **superior (USB)** en las bandas por encima (20, 17, 15, 12, 10 metros... y todo VHF/UHF). Es pura tradición estandarizada —herencia de cómo se generaba SSB en los años cincuenta—, pero es LA tradición: tu equipo la aplica solo, y saberla te dice qué botón tocar cuando no.

SSB es, desde los años sesenta, **el modo de fonía estándar en HF**. Cuando en la sección 11 hagas tu primer contacto de voz en onda corta, será en SSB.

## FM: mover la frecuencia, no la amplitud

La **modulación de frecuencia (FM)** deja la amplitud constante y hace variar la **frecuencia instantánea** de la portadora al ritmo de la voz: la voz «empuja» la frecuencia arriba y abajo alrededor del valor central. Cuánto la empuja como máximo es la **desviación** (en radioafición, típicamente ±5 kHz en FM «estrecha»).

- **Ancho de banda: ~10-16 kHz** en la FM estrecha de radioaficionado (regla práctica de Carson: 2 × (desviación + frecuencia máxima de audio) = 2 × (5+3) = 16 kHz). Un derroche en HF; calderilla en VHF/UHF.
- **Su superpoder: la inmunidad al ruido.** Casi todo el ruido natural y doméstico (tormentas, motores, chisporroteos) perturba la *amplitud* de las señales. El receptor de FM ignora la amplitud por diseño (la recorta con un limitador antes de demodular): el ruido se queda fuera. Resultado: audio limpio y cómodo, calidad «de emisora comercial».
- Rasgo curioso con nombre propio: el **efecto captura**: si dos señales de FM coinciden en frecuencia, el receptor se queda solo con la más fuerte y la débil desaparece por completo (en AM/SSB se oirían ambas mezcladas). Bendición contra interferencias débiles; maldición si la débil eras tú.

FM es el modo de **VHF/UHF local**: walkies, equipos de coche, repetidores (sección 11). El primer equipo de casi todo radioaficionado nuevo —el tuyo, probablemente— será un portátil de FM.

## Los modos digitales: cuando modula el ordenador

Un **modo digital** transmite datos (texto, telemetría, imágenes) modulando la portadora con las técnicas anteriores gestionadas por un ordenador o un chip. Los que conviene conocer:

- **RTTY** (radioteletipo, 1930s-hoy): el abuelo; dos tonos alternando (marca/espacio) a 45 baudios. Aún se usa en concursos.
- **PSK31** (1998): modulación de *fase*, 31 Hz de ancho —más fino que el morse—, pensado para conversación tecleada en directo con potencias mínimas.
- **FT8** (2017): el fenómeno. Mensajes estructurados de 77 bits en ráfagas de 15 segundos sincronizadas por reloj, 50 Hz de ancho, y decodificación por debajo del ruido audible (hasta unos −20 dB respecto al ruido: el ordenador saca señales que el oído humano jamás detectaría). Ha revolucionado el DX con antenas modestas —los 143 países de Dani desde un balcón— al precio que Vicente le reprocha: el intercambio es mínimo y automatizable (indicativos, localización, reporte), sin conversación humana. Técnicamente prodigioso, socialmente notarial: los dos tienen razón.
- **Digitales de voz** (DMR, D-STAR, C4FM): voz convertida en datos en VHF/UHF, con enlaces por Internet entre repetidores. Cada marca empujó el suyo; convivencia babélica pero funcional.
- **Packet/APRS:** datos por radio con historia gloriosa: posiciones GPS, telemetría de globos, mensajería. APRS sigue vivo dibujando mapas de estaciones en movimiento.

No hace falta dominarlos para el examen (les basta con «existen y usan poco ancho de banda o técnicas digitales»); sí conviene reconocer sus nombres, porque el dial está lleno de ellos.

## Tabla resumen: los modos y su hábitat

| Modo | Qué varía | Ancho típico | Hábitat natural | Fortaleza |
|---|---|---|---|---|
| CW (morse) | Portadora on/off | 100-200 Hz | HF (y donde haga falta) | Eficacia extrema, sencillez |
| AM | Amplitud | 6 kHz | Radiodifusión OM, aviación | Receptor trivial |
| SSB | Amplitud (sin portadora ni banda espejo) | 2,4-2,7 kHz | Fonía en HF (LSB<10 MHz<USB) | Toda la potencia a la información |
| FM | Frecuencia | 10-16 kHz | VHF/UHF local, repetidores | Inmunidad al ruido |
| FT8 y cía. | Según modo (gestión digital) | 50 Hz-2 kHz | HF débil / según modo | Decodifica bajo el ruido |

## Para llevar

- La onda electromagnética son los campos E y H regenerándose mutuamente a la velocidad de la luz; la **polarización** es la orientación del campo E (= la de la antena) e importa mantenerla en comunicaciones directas.
- **Modular** = alterar amplitud, frecuencia o fase de una **portadora** al ritmo de la información. Más información/segundo = más **ancho de banda**, siempre.
- **CW**: portadora a golpes de morse, ~150 Hz, máxima concentración de energía; el tono lo pone el BFO del receptor.
- **AM**: portadora + dos bandas laterales; ancho = 2 × audio máximo; potencia malgastada en la portadora (~2/3).
- **SSB**: AM sin portadora y sin banda espejo; ~2,7 kHz; el estándar de fonía en HF; **LSB por debajo de 10 MHz, USB por encima**; mal sintonizada = pato.
- **FM**: amplitud constante, frecuencia bailando (desviación ±5 kHz); 10-16 kHz; inmune al ruido de amplitud; efecto captura; el modo de VHF/UHF local.
- Digitales: del RTTY al FT8 (50 Hz, decodifica bajo el ruido); el ordenador como modulador.

## Para el examen

- Anatomía del AM (portadora + 2 bandas laterales) y su ancho de banda (2 × f máx de audio): pregunta muy frecuente, con números.
- Qué suprime la SSB (portadora y una banda lateral) y sus ventajas (ancho mitad, potencia íntegra a la información): clásico absoluto.
- Convenio LSB/USB según banda (el umbral de los 10 MHz).
- Anchos de banda relativos: CW < SSB < AM < FM (ordenar modos por ancho cae a menudo).
- FM: qué es la desviación y por qué es inmune al ruido (el ruido es de amplitud y la FM la ignora).
- Qué modo concentra su energía en menos espectro (CW) y para qué sirve el BFO.

## Para profundizar

- **websdr.org** y las redes KiwiSDR: receptores reales controlables desde el navegador, gratis. Ejercicio concreto: en 40 metros, sintoniza una SSB a propósito «en pato» y encájala tú; luego mide a ojo en la cascada el ancho de una AM de radiodifusión frente a un hilo de CW. Media hora ahí vale por esta sección entera.
- *Ética y procedimientos operativos para el radioaficionado* (Devoldere & Demeuleneere, IARU, ed. española, libre distribución): su capítulo de modos y procedimientos te adelanta la sección 11 con los usos y costumbres de cada modo.
- Wikipedia (CC BY-SA): «Banda lateral única» y «Frecuencia modulada» desarrollan la matemática (índices de modulación, regla de Carson) que aquí queda esbozada; suficiente para el examen español lo que has leído.
