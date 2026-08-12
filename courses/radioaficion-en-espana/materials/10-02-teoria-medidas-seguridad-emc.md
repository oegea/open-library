Esta sección junta tres capítulos del temario oficial que en la práctica son uno: **medir** (saber qué pasa de verdad en tu estación), **protegerte** (de la electricidad, de la RF y del cielo) y **convivir** (no interferir y no ser interferido: la compatibilidad electromagnética). Son los capítulos que convierten a un aprobado en un buen vecino del espectro.

## Los instrumentos de medida

**El polímetro (multímetro).** El fonendoscopio de Vicente: mide tensión (voltímetro), corriente (amperímetro) y resistencia (ohmímetro), y casi todos añaden prueba de diodos y continuidad. Lo que el examen pregunta y la práctica graba a fuego:

- **Voltímetro: en paralelo** con lo que se mide, sin cortar nada. Para no perturbar el circuito debe tener **resistencia interna muy alta** (idealmente infinita): que por él no se desvíe corriente apreciable.
- **Amperímetro: en serie**, cortando el circuito para que la corriente lo atraviese. Debe tener **resistencia interna muy baja** (idealmente nula): que no estorbe. Conectarlo en paralelo por error es crear un cortocircuito con pantalla: clásico funeral de fusibles de polímetro.
- **Ohmímetro: siempre sin tensión.** Mide inyectando su propia corrientecita: sobre un circuito alimentado, miente o muere.

**El medidor de ROE (reflectómetro) y el vatímetro.** Intercalados en la línea de antena, miden potencia directa, reflejada y su relación (la ROE de la sección 8). El vatímetro de RF serio mide en PEP para SSB. Recuerda el matiz: el medidor de ROE puesto junto al transmisor mide el acuerdo *desde ahí*; no ve las pérdidas del cable que tiene delante (un cable con muchas pérdidas «disimula» la ROE de una antena mala: la energía reflejada llega tan debilitada de vuelta que el medidor sonríe; el DX, no).

**El frecuencímetro.** Cuenta ciclos por segundo, literalmente: dígitos que te dicen dónde estás transmitiendo de verdad. Los equipos modernos lo llevan de serie (el sintetizador ES un patrón de frecuencia), pero el concepto cae en examen.

**El osciloscopio.** El que *dibuja* la señal: tensión en vertical, tiempo en horizontal. Con él se ve la senoide, el recorte de una sobremodulación, el rizado de una fuente: todo lo que este curso ha descrito con palabras, en pantalla. Es el instrumento rey del taller (y hoy los hay por el precio de una cena).

**El analizador de antenas.** El aparatito de Dani en la azotea: un mini-transmisor barredor + medidor que dibuja la ROE de la antena a lo largo de la frecuencia: ve la resonancia, el ancho de banda útil y los desastres, sin transmitir potencia. Herramienta moderna por excelencia del antenista aficionado.

**La carga artificial** (vieja conocida): 50 Ω que no radian, donde se ajusta y se mide sin ensuciar el aire.

Y un principio general de metrología que el examen roza y la vida confirma: **todo instrumento perturba lo que mide y tiene su error** (su clase de precisión). Medir dos veces, con dos métodos, cuando el resultado importa.

## Seguridad eléctrica: lo que no perdona

Sin dramatismo y sin anestesia: la radioafición maneja energías que exigen respeto profesional, y el temario de seguridad es de lo más serio del examen. Lo esencial:

**La corriente mata, no los voltios (repaso ampliado).** Desde ~30 mA a través del tórax hay riesgo grave (fibrilación); la resistencia del cuerpo baja drásticamente con piel húmeda. Consecuencias prácticas: manos secas, calzado aislante, y la regla de oro de los electricistas veteranos para trabajar en circuitos con tensión presente (que NO deberías, pero por si acaso): **una mano en el bolsillo**: que no exista camino mano-corazón-mano.

**El enchufe y sus tres hilos.** Fase (marrón), neutro (azul), **tierra de protección (verde-amarillo)**: la tierra conecta las carcasas metálicas al suelo, de modo que un fallo interno (fase tocando chasis) dispare las protecciones en vez de esperar a tus dedos. Los cuadros modernos añaden el **interruptor diferencial**, que corta si detecta que se «fuga» corriente (≥30 mA en viviendas: la cifra no es casual) por donde no debe (por ejemplo, por ti), y los **magnetotérmicos** contra sobrecargas y cortos. Jamás anules una tierra ni un diferencial; tu estación se conecta a una instalación con ambos, siempre.

**Los condensadores no olvidan.** Las fuentes (y más las de válvulas, con cientos de voltios) guardan carga letal en sus electrolíticos **días** después de desenchufar. Norma de taller: desenchufar, esperar, y **comprobar con el voltímetro** que los condensadores gordos están descargados antes de meter mano (los equipos decentes llevan resistencias de descarga; los viejos y los reparados, quién sabe). El «respeta los condensadores grandes» de la sección 4, ahora con toda su estatura.

**RF: quema sin avisar.** La radiofrecuencia de potencia produce **quemaduras de RF** (profundas, dolorosas, con contacto mínimo: tocar un hilo de antena transmitiendo, o el famoso «beso» de una punta de antena de coche). Y a niveles altos, el cuerpo absorbe RF como el pollo del microondas (efecto térmico): de ahí los **límites de exposición** (normativa española incluida) que se traducen en sentido común de instalación: antenas lejos de donde vive la gente, nunca transmitir con personas junto a los elementos, potencias altas solo con las distancias que tocan. Tu dipolo en la azotea a 10 metros de las ventanas cumple con margen enorme; una vertical de balcón con un kilovatio, no.

**Rayos y tormentas: el protocolo de Vicente.**

- Tormenta anunciada o audible: **desconectar antenas** y alejar los cables de equipos y personas (el bote de cristal es teatro; la distancia, física). La inducción de rayos cercanos mata equipos a cientos de metros del impacto.
- Instalación fija seria: **descargadores de gas** en las bajadas (se ceban y derivan a tierra el impulso; se sacrifican y se sustituyen), mástil y descargadores unidos a **tierra de RF/tormentas** con conductor corto, grueso y sin curvas cerradas (los impulsos de rayo odian las curvas: alta frecuencia al fin y al cabo).
- Y la distinción de la historia, que cae en examen y en la vida: **tierra de protección eléctrica** (la del enchufe, contra fallos de red) y **tierra de RF/rayos** (pica propia, contra el cielo y para el plano de referencia de RF) se unen en un solo sistema equipotencial correcto en instalaciones bien hechas, pero conceptualmente son funciones distintas: confundir sus papeles produce instalaciones que ni protegen ni funcionan.

**Trabajo en alturas y antenas:** arnés y sentido común en tejados; y la norma absoluta, subrayada en rojo en todos los manuales del mundo: **jamás montar antenas donde puedan caer sobre líneas eléctricas** (ni las líneas sobre ellas). Cada año mueren aficionados por esto en el mundo. Distancia a líneas: más que la altura total de la antena caída en el peor sentido. Sin excepciones, sin prisas de sábado.

## EMC: el arte de convivir en el espectro

**Compatibilidad electromagnética (EMC)**: que cada aparato funcione sin perturbar a los demás ni ser perturbado. El radioaficionado vive los dos lados del mostrador, y el examen pregunta ambos.

**Lado 1: tú interfieres (interferencias emitidas).** Tu señal puede colarse en equipos ajenos por dos vías, y distinguirlas es el 80 % del diagnóstico:

- **Emisiones no deseadas tuyas** (armónicos, espurias: los pecados de la sección 7): la culpa es tuya de verdad. Remedios: filtro paso bajo, equipo sano, potencia justa. Obligación reglamentaria, además: el artículo 32 del Reglamento español obliga a cesar y corregir si causas interferencia perjudicial.
- **Fundamental limpio que se cuela** (*fundamental overload*): tu señal es perfectamente legal y limpia, pero el aparato del vecino —tele con amplificador de oferta, altavoces amplificados, timbre inalámbrico— está mal protegido y la traga por donde no debe (cables que hacen de antena, etapas sin filtrar). La culpa técnica es del aparato receptor... y la solución práctica es la diplomacia con ferritas de la historia: **ferritas** en los cables del aparato afectado (frenan la RF que entra por ellos: la bobina que se opone a la alterna rápida, en acto de servicio comunitario), filtros paso alto en antenas de TV, y método: probar transmitiendo a potencias crecientes, banda a banda, con un observador. El caso Morientes es el caso universal: mitad y mitad, y se arregla en ambos lados con piezas de céntimos.

**Lado 2: te interfieren (inmunidad).** El azote moderno: el **ruido eléctrico doméstico**. Fuentes conmutadas baratas (cargadores, tiras LED, lámparas), motores, termostatos, PLC (¡internet por la red eléctrica: el enemigo público del HF urbano!), regulan y trocean corriente a frecuencias que siembran de porquería las bandas. Se manifiesta como soplido, zumbido o «ta-ta-tá» que sube el ruido de fondo y entierra las señales débiles. Armas del defensor: localizar (apagando magnetotérmicos de casa uno a uno con un receptor portátil: el 60 % de las veces el ruido es TUYO, de tus propios cacharros), ferritas en los culpables, sustituir la fuente infame de la tira LED por una decente, y antenas lejos de la casa (el dipolo alto de la azotea también escucha menos ruido doméstico que el hilo del balcón: doble dividendo).

**El marco legal del asunto**, para cerrar el círculo con la sección 12: los equipos vendidos en Europa deben cumplir directivas de EMC (marcado CE); el radioaficionado tiene derecho a protección frente a interferencias en sus bandas atribuidas y el deber simétrico de no causarlas fuera de ellas; y la Administración (las Jefaturas de Inspección de Telecomunicaciones, las mismas del examen) es el árbitro formal cuando la diplomacia de ferritas fracasa. Spoiler estadístico de veterano: la diplomacia de ferritas casi nunca fracasa.

## Para llevar

- Voltímetro en paralelo (resistencia interna altísima); amperímetro en serie (bajísima); ohmímetro solo sin tensión.
- Medidor de ROE en la línea; osciloscopio dibuja la señal; analizador de antenas dibuja la ROE vs frecuencia; carga artificial para medir sin radiar.
- La corriente mata desde decenas de mA: tierra de protección + diferencial (30 mA) intocables; condensadores se comprueban descargados; una mano en el bolsillo.
- RF quema y tiene límites de exposición: antenas lejos de personas, potencia con cabeza.
- Rayos: desconectar y alejar cables; descargadores + tierra de tormentas corta y gruesa; tierra de protección ≠ tierra de RF/rayos (funciones distintas, sistema unido).
- EMC: si interfieres, distingue armónicos tuyos (filtro paso bajo) de fundamental que el aparato ajeno traga (ferritas allí); si te interfieren, busca primero en tu propia casa. Medir antes de opinar; ferritas antes que juicios.

## Para el examen

- Conexión y resistencia interna ideal de voltímetro/amperímetro: pregunta fija.
- Qué mide y dónde se intercala el medidor de ROE; para qué sirve la carga artificial (repite desde la sección 8: les gusta).
- Qué instrumento muestra la forma de onda (osciloscopio) y cuál cuenta la frecuencia (frecuencímetro).
- Seguridad: valor del diferencial doméstico (30 mA), función de la tierra de protección, peligro de condensadores cargados y de trabajar cerca de líneas eléctricas.
- EMC: qué es el fundamental overload frente al armónico (quién tiene la culpa técnica en cada caso), para qué sirven las ferritas y el filtro paso bajo, y la obligación de corregir interferencias perjudiciales (art. 32).

## Para profundizar

- El documento IARU *Ética y procedimientos operativos* dedica páginas sabias a la actitud ante las interferencias (la técnica es la mitad; el tono, la otra).
- Busca «EMC for radio amateurs RSGB»: la sociedad británica publica guías abiertas excelentes de diagnóstico y remedios caseros.
- Ejercicio doméstico revelador (sin licencia): con un receptor portátil de AM barato, recorre tu casa pegándolo a cargadores, routers, tiras LED. El mapa de ruido de tu propia vivienda te explicará tu futura banda de 40 mejor que tres artículos.
