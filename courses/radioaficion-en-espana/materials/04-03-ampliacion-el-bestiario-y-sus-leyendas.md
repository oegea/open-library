Ya te sabes las cuatro familias y media. Esta ampliación abre el cajón de las historias: la radio de galena que escuchaba sin pilas, el invento que valió tres premios Nobel y cabía en la palma de la mano, por qué las ferritas de la lata de Amparo están hoy pegadas a la mitad de tus cables, y algún truco de taller que no viene en los libros.

## La radio que funcionaba sin pilas: la galena

Las primeras radios domésticas de los años veinte no tenían pilas, ni enchufe, ni amplificador. Un cable largo de antena, una bobina, un cristal de **galena** (sulfuro de plomo natural) con un hilillo metálico apoyado encima —el famoso «bigote de gato»— y unos auriculares sensibles. La energía que movía el auricular era *la propia onda de radio capturada por la antena*: la emisora, a decenas de kilómetros, alimentaba tu receptor. El cristal con su bigote hacía de diodo detector (un semiconductor natural, décadas antes de entender por qué funcionaba), y encontrar «el punto bueno» del cristal era un arte de sobremesa familiar.

Generaciones enteras de radioaficionados —incluida la de los maestros de Vicente— empezaron construyéndose una. Y el concepto no ha muerto: esas etiquetas antirrobo de las tiendas y las tarjetas NFC de tu cartera también viven de la energía de la onda que las interroga. La galena fue la primera *energy harvester* de la historia doméstica.

Si algún día montas una (hay kits y planos por todas partes, y es tarde bien gastada), entenderás de golpe tres secciones de este curso: antena, circuito resonante y detección, sin un solo componente activo.

## El transistor: tres Nobel en la palma de la mano

En diciembre de 1947, en los laboratorios Bell, John Bardeen y Walter Brattain consiguieron que un artilugio de germanio, láminas de oro y un muelle de plástico amplificara una señal. Su jefe de grupo, William Shockley, furioso por haberse perdido el momento (y por que la patente no llevara su nombre en solitario), se encerró un mes en un hotel y salió con el diseño del transistor de unión, el que se pudo fabricar en masa. Los tres compartieron el Nobel de 1956; la relación personal quedó, digamos, en circuito abierto. Bardeen, por cierto, ganó *otro* Nobel de física en 1972 (superconductividad): sigue siendo la única persona con dos Nobel de física.

La palabra «transistor» la eligió por votación interna el ingeniero John Pierce (contracción de *transfer resistor*). Las primeras aplicaciones masivas fueron audífonos (1952) y la radio de bolsillo Regency TR-1 (1954): la radio, otra vez, estrenando cada revolución electrónica. Dato para la perspectiva: aquel primer transistor medía centímetros; hoy se fabrican más transistores cada año que granos de arroz se han cosechado en la historia de la humanidad, y el precio unitario ha caído por debajo del de una letra impresa en un periódico.

## Por qué media humanidad lleva una ferrita pegada al cable (y no lo sabe)

Abre el cajón de cables de tu casa: varios tendrán cerca del conector un cilindro rígido moldeado en el plástico. Eso es un **núcleo de ferrita**, y ahora puedes entender qué hace: el cable, además de llevar su señal *por dentro*, puede actuar de antena involuntaria *por fuera*, trayendo o llevando radiofrecuencia que causa interferencias. La ferrita abraza el cable y convierte su superficie exterior en una bobina con pérdidas para esas corrientes de RF: recuerda, la bobina se opone a la alterna rápida. La señal útil del interior ni se entera; la RF parásita del exterior se frena y se disipa.

Para el radioaficionado las ferritas son munición básica: unas vueltas de cable alrededor de un toroide de ferrita resuelven la mitad de los casos de «cuando transmito, se oye en el mando de la tele del vecino» (asunto serio que trataremos en la sección 10; en la historia de esta sección, ya te imaginas quién acabará poniendo ferritas en Vallverd). Las «ferritas varias» de la lata de Amparo no eran calderilla: eran el botiquín diplomático de la casa.

## El código de colores tiene su leyenda (y una polémica de verdad)

El código de colores de las resistencias se estandarizó en los años veinte (asociación de fabricantes RMA, luego EIA). Las nemotecnias para recordar el orden de los colores son legión en todos los idiomas; muchas de las tradicionales eran impublicables, y su sustitución por versiones civilizadas es un pequeño caso de estudio de cómo evoluciona la cultura técnica. Una española inocua: «**N**egritos **M**arrones **R**íen **N**aranjas **Am**arillas, **V**erdes **A**zules **V**iolinistas **G**rises **B**lancos» — o invéntate la tuya, que para eso están.

Detalle práctico que ahorra disgustos: en resistencias de 5 franjas (precisión), las *tres* primeras son cifras. Y el sentido de lectura se decide buscando la franja de tolerancia (dorada/plateada), que va al final y suele estar más separada. Si una resistencia parece de 82 MΩ en un circuito de lógica, dale la vuelta: probablemente es de 28 kΩ leída al revés. El polímetro es el juez de paz de todas estas dudas.

## Supercondensadores: el condensador que quiso ser batería

La teoría te dijo que el faradio es una unidad descomunal. Pues se venden condensadores de **3.000 faradios**. Los *supercondensadores* logran capacidades monstruosas con trucos de química de superficie (carbón activo con hectáreas internas de superficie en gramos de material). No sustituyen a las baterías —almacenan mucha menos energía por kilo—, pero se cargan y descargan en segundos, millones de veces, sin desgaste. Alimentan desde el flash de cámaras hasta frenadas regenerativas de autobuses. En el mundo del radioaficionado asoman en fuentes de respaldo para memorias y relojes de equipos. Sirven aquí, sobre todo, para recalibrar tu asombro: entre el picofaradio del condensador de sintonía y el kilofaradio del super hay *quince órdenes de magnitud*, los mismos que median entre un milímetro y la distancia Tierra-Sol.

## El MOSFET, el objeto más fabricado por el ser humano

Ningún artefacto humano se ha producido en más unidades que el transistor MOSFET: se estima que se han fabricado más de 10^22 (un uno seguido de veintidós ceros). Cada chip de tu móvil contiene miles de millones. Y sin embargo su principio cabe en una frase de esta misma sección: una tensión en la puerta abre o cierra el paso de corriente. Cuando en la sección 7 veas que el amplificador de potencia de un transceptor moderno son «un par de MOSFET grandes», sabrás que lo más exótico de tu equipo es, a la vez, el objeto más común del planeta.

## Trucos de taller heredados (sección no oficial)

- **Los electrolíticos tienen fecha de caducidad aunque estén sin usar.** Un aparato guardado 30 años en un desván no está «como nuevo»: está como un yogur de 1995. Encenderlo directamente a la red puede ser su ejecución. Los restauradores los reforman (subida lenta de tensión) o los sustituyen en bloque. El «huele a condensador reventado» de Vicente en el rastro era diagnóstico olfativo real: el electrolito derramado tiene un olor dulzón inconfundible, dicen que a pescado en los peores casos.
- **Un diodo se comprueba en segundos**: casi todos los polímetros tienen posición «diodo» que muestra la caída directa (~0,5-0,7 V en silicio) y nada en inversa. Igual en ambos sentidos = muerto en corto; nada en ambos = muerto en abierto.
- **Los transistores también se prueban como dos diodos** (base-emisor y base-colector) para un diagnóstico de urgencia. No es un test completo, pero descarta cadáveres.
- **Respeta los condensadores grandes**: los de las fuentes pueden guardar carga letal días después de desenchufar. Es tema de la sección 10, pero el hábito —descargar antes de tocar— empieza hoy.

## Para seguir tirando del hilo

- Wikipedia (CC BY-SA): «Radio de galena», «Historia del transistor», «MOSFET» y «Condensador electrolítico»: artículos sólidos y bien referenciados.
- El documental/ensayo clásico *The Idea Factory* (Jon Gertner) sobre los laboratorios Bell, si te ha intrigado la fábrica de milagros donde nació el transistor (y el dBm, y la teoría de la información).
- Kits de radio de galena («crystal radio kit»): por poco dinero, la experiencia fundacional completa. Con auriculares de alta impedancia y paciencia, escucharás onda media con energía cero. Pocas cosas enseñan más física por euro invertido.
