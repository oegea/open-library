La primera llamada del simulacro llegó por «el repetidor comarcal». A media mañana, la organización lo dio por caído a propósito («los ejercicios los diseñan con mala idea, como debe ser», había avisado Salva) y el puesto tuvo que arreglárselas sin él. En esas dos escenas está todo lo que hay que saber de un repetidor: lo mucho que ayuda y por qué no conviene depender de él.

Tu primer equipo será, casi seguro, un portátil de FM para las bandas de 2 metros y 70 centímetros. Al terminar esta lección sabrás qué hace un repetidor, qué tres datos hay que programar para usarlo, cómo se llama a través de él y cuándo es mejor no usarlo.

## El problema: en VHF y UHF manda el horizonte

Recuerda de la sección 9 que en VHF y UHF la onda viaja en línea recta, de antena a antena. Un portátil a la altura de la mano alcanza unos pocos kilómetros en terreno llano, y una sierra entre dos estaciones las deja mudas aunque estén cerca.

La solución también la conoces: poner algo muy alto.

> **Repetidor:** estación automática, instalada en un punto elevado, que recibe la señal de una estación y la retransmite en el mismo instante para que llegue más lejos.

Dos portátiles de 5 W separados por setenta kilómetros y una sierra no se oyen entre sí, pero los dos alcanzan el repetidor del monte, y a través de él conversan como si estuvieran al lado.

Los repetidores los instalan y mantienen radioclubes y asociaciones, con su dinero y sus fines de semana. El reglamento español les exige, a cambio de la autorización, que el acceso sea **libre**: cualquier radioaficionado puede usarlos, y si tienen un código de acceso, debe ser público.

## Por qué necesita dos frecuencias

Un repetidor tiene que hacer algo que tu portátil no hace nunca: **recibir y transmitir a la vez**. Si lo hiciera en la misma frecuencia, su propio transmisor, a un metro de su receptor, lo dejaría sordo: se oiría a sí mismo.

Por eso usa dos:

> **Frecuencia de salida:** aquella en la que el repetidor transmite. Es la que tú **escuchas**, y la que figura en las listas como «la frecuencia del repetidor».
>
> **Frecuencia de entrada:** aquella en la que el repetidor recibe. Es en la que tú **transmites**.
>
> **Desplazamiento** (en inglés *shift* u *offset*): la diferencia entre las dos.

Tu equipo, por tanto, tiene que cambiar de frecuencia cada vez que aprietas el PTT. Lo hace solo, si le dices cuánto.

En España, los desplazamientos normales son:

| Banda | Desplazamiento | Quiere decir |
|---|---|---|
| 2 metros (VHF) | **−600 kHz** | Transmites 600 kHz **por debajo** de donde escuchas |
| 70 centímetros (UHF) | **−7,6 MHz** | Transmites 7,6 MHz **por debajo** de donde escuchas |

**Ejemplo.** *Un repetidor de 2 metros figura en la lista con 145,600 MHz. ¿Dónde transmites?*

Para restar, ponlo todo en la misma unidad: 600 kHz son 0,600 MHz.

145,600 − 0,600 = **145,000 MHz**

Escuchas en 145,600 y, al apretar el botón, tu equipo salta a 145,000. Al soltar, vuelve.

**Ejemplo.** *Un repetidor de 70 centímetros figura con 438,800 MHz.*

438,800 − 7,6 = **431,200 MHz**

Que sean negativos es puro convenio; lo que cuenta es que tu equipo y el repetidor usen el mismo. Y son los valores habituales, no una ley universal: el de 2 metros es común a toda Europa, pero en 70 centímetros otros países usan otros, y hay repetidores que se salen de la norma. El dato bueno es siempre el de la ficha del repetidor, que publican el club que lo mantiene y las listas de las asociaciones.

## El subtono: la llave

Falta un tercer dato. El receptor de un repetidor está en un monte, con una antena excelente, y oye muchísimo: ruido eléctrico, y también a estaciones lejanas que en realidad quieren activar *otro* repetidor que usa la misma frecuencia de entrada a doscientos kilómetros. Si retransmitiera todo lo que le llega, estaría emitiendo basura a todas horas.

> **Subtono** (en inglés **CTCSS**, *Continuous Tone-Coded Squelch System*): un tono grave y continuo que tu equipo añade a tu voz mientras transmites. El repetidor solo se abre si detecta **su** tono.

Funciona como una llave: cada repetidor tiene el suyo, elegido de una lista normalizada que va de 67,0 a 250,3 Hz. Uno de ellos, por ejemplo, es 88,5 Hz; hay más de treinta.

—Si mi equipo mete un pitido continuo mientras hablo, ¿no lo oye todo el mundo? —preguntó Marina.

—No, y por eso se llama *sub*tono. Acuérdate de que la voz, por radio, se recorta: solo se transmite más o menos de 300 a 3.000 Hz. El subtono va por debajo de 300, en una zona que los receptores filtran y los altavoces pequeños ni reproducen. Viaja con tu voz, el repetidor lo detecta, y nadie lo oye.

Algunos repetidores antiguos se abren con un pitido de **1.750 Hz** al empezar; la recomendación actual de la IARU es el subtono.

![Un repetidor en lo alto de una montaña entre dos valles. En el valle izquierdo, un portátil transmite en 145,000 megahercios, la frecuencia de entrada, añadiendo a la voz un subtono de 88,5 hercios. El repetidor recibe esa señal y la retransmite al mismo tiempo en 145,600 megahercios, la frecuencia de salida, 600 kilohercios más arriba. En el valle derecho, otro portátil la escucha en 145,600. La línea recta entre los dos portátiles está cortada por la montaña.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s11-repetidor.svg)

## Los tres datos, y cómo saber cuál falla

Para usar un repetidor programas en una memoria de tu equipo:

1. **La frecuencia de salida** (la que escuchas).
2. **El desplazamiento**: cuánto y hacia dónde.
3. **El subtono.**

Si algo falla, los síntomas te dicen qué:

| Lo que pasa | Lo más probable |
|---|---|
| Oyes hablar a otros por el repetidor, pero cuando transmites tú no pasa nada | Subtono equivocado o sin activar, o desplazamiento mal puesto |
| Aprietas, sueltas, y oyes un instante de portadora y quizá un pitido, pero nadie te contesta | Has abierto el repetidor: todo está bien. Simplemente no hay nadie |
| Te dicen que llegas «con mucho ruido» o entrecortado | Llegas justo al repetidor: muévete un metro, sube la antena, busca una ventana |
| Te dicen que distorsionas y que «te sales del canal» | Llevas la FM ancha en un repetidor de canal estrecho: la sobredesviación de la sección 7 |

Ese instante de portadora después de que alguien suelte se llama **cola** del repetidor, y muchos emiten al final un pitido de cortesía: marcan el momento en que puede hablar el siguiente.

La ficha de cada repetidor (salida, desplazamiento y subtono) está en el listado de repetidores de la URE y en la web del radioclub que lo mantiene. En el equipo, los tres ajustes suelen llamarse *frecuencia*, *SHIFT* u *OFFSET* (con su signo) y *TONE* o *CTCSS*. Programa uno, guarda la memoria y pruébalo escuchando antes de transmitir.

## Cómo se habla por un repetidor

Un repetidor es un recurso único que comparten cientos de personas en toda una comarca. De ahí salen sus costumbres, algo distintas de las de la onda corta. Unas las recoge el manual de la IARU (pausas, brevedad, «break», símplex); otras las ha añadido el uso.

**Para llamar no hace falta CQ.** Escuchas un rato. Si está en silencio, dices tu indicativo y que estás a la escucha:

«EA5RKV, a la escucha por el repetidor.»

Quien esté atento y quiera, contesta. Si buscas a alguien: «EA5XYZ, aquí EA5RKV».

Un contacto entero suena así. Imagina a Marina dentro de unos meses, ya con licencia (pongamos que su indicativo es EA5XYZ), y a Dani en la estación del club:

*Marina:* «EA5XYZ, a la escucha por el repetidor.»

*Dani:* «EA5XYZ, aquí EA5RCT. Buenas tardes. Entras limpia, sin soplido. ¿Desde dónde sales? Cambio.»

(Pausa. Suena el pitido del repetidor.)

*Marina:* «EA5RCT, de EA5XYZ. Buenas tardes, Dani. Te recibo perfecto. Estoy en casa, en Vallverd, con un portátil y cinco vatios. Cambio.»

(Pausa.)

*Dani:* «Pues con cinco vatios entras muy bien. Prueba a bajar a uno y me cuentas. No ocupo más el repetidor: setenta y tres. EA5XYZ, de EA5RCT.»

*Marina:* «Gracias por el contacto, Dani. Setenta y tres. EA5RCT, de EA5XYZ, que deja libre el repetidor.»

| Igual que en onda corta | Distinto |
|---|---|
| Primero el indicativo del otro, luego el tuyo | No se llama CQ |
| «Cambio» para ceder el turno | Pausa tras cada turno, hasta el pitido |
| Identificación al empezar, al terminar y cada diez minutos | El informe se da de palabra: cómo entras en el repetidor (lección 4) |
| Despedida con setenta y tres | Contactos breves: es un recurso de todos |

**Deja pausas entre turnos.** Cuando tu corresponsal suelte, espera a que acabe la cola o suene el pitido, y un segundo más. Sirve para tres cosas:

- Para que pueda entrar una tercera estación, sobre todo una que tenga algo urgente.
- Para poner a cero el temporizador: casi todos los repetidores cortan la transmisión si alguien habla más de unos minutos seguidos, por protección.
- Para no comerte la primera sílaba: el repetidor tarda un instante en abrirse.

**Para entrar en una conversación**, di tu indicativo en una pausa. Te darán paso.

**«Break» se reserva para las emergencias.** Si necesitas interrumpir por algo grave: «break, break, break, tráfico de emergencia». (*Tráfico* es como se llama en radio al conjunto de mensajes que se cursan.) Y si lo oyes tú, callas y cedes el repetidor de inmediato.

**Identifícate**, como siempre: al empezar, al terminar y al menos cada diez minutos. El repetidor emite su propio indicativo de vez en cuando, en voz o en morse; eso lo identifica a él, no a ti. Abrir un repetidor apretando el botón sin decir nada es una emisión sin identificar.

**La potencia, la mínima con la que entres bien.** Si con 1 W abres el repetidor sin ruido, los 5 W solo sirven para gastar batería y para molestar a otro repetidor lejano que comparta frecuencia.

## Símplex: cuando no hace falta

> **Símplex:** contacto directo entre dos estaciones, que transmiten y reciben en la misma frecuencia, sin repetidor.

La recomendación del manual de la IARU es clara: **símplex siempre que se pueda**. Dos estaciones que se alcanzan directamente no necesitan el repetidor, y usándolo se lo quitan a quien sí.

¿Cómo saber si te alcanzas con tu corresponsal? Sintoniza la frecuencia de **entrada** del repetidor mientras él habla (muchos equipos tienen una tecla, «REV», que lo hace). Si le oyes ahí, le estás recibiendo directamente, sin pasar por el monte. Proponle una frecuencia símplex y dejad libre el repetidor.

El punto de encuentro en símplex, ya lo sabes, es la frecuencia de llamada de FM, 145,500 MHz en 2 metros (433,500 MHz en 70 centímetros): se contacta allí y se pasa a otra.

Y hay una razón más para practicar el símplex, que es la de la historia. Un repetidor es una máquina en un monte: necesita corriente, y aunque el reglamento le exige alimentación de reserva para al menos seis horas, las emergencias duran más. El día que falte, quien solo sepa hablar por el repetidor se quedará sin radio. En el simulacro, cuando lo dieron por caído, el puesto pasó a onda corta «sin drama» porque lo tenían previsto.

## Donde la gente se lía

- **Programar la frecuencia de entrada como «la del repetidor».** La de las listas es la de salida, la que escuchas. La de entrada la calcula el equipo con el desplazamiento.
- **Equivocarse de signo.** En 2 metros y en 70 centímetros, el desplazamiento habitual es negativo: transmites *por debajo*. Con el signo contrario transmites donde el repetidor no escucha.
- **Creer que el subtono da privacidad.** Solo decide si el repetidor se abre. Lo que dices lo oye todo el que escuche la salida, con subtono o sin él.
- **Usar el repetidor como un teléfono.** Media hora de charla entre dos vecinos que se alcanzarían en símplex deja sin servicio a toda la comarca.

## Compruébalo tú

1. Un repetidor de 2 metros tiene la salida en 145,750 MHz y desplazamiento de −600 kHz. ¿En qué frecuencia debe transmitir tu equipo?
2. Un repetidor de 70 centímetros tiene la salida en 439,300 MHz y desplazamiento de −7,6 MHz. ¿Cuál es su frecuencia de entrada?
3. Programas un repetidor y oyes perfectamente a dos estaciones conversando por él. Cuando aprietas el PTT en una pausa, nadie te contesta ni se oye la cola. Di dos causas posibles.
4. Te dan esta ficha: salida 438,950 MHz, desplazamiento −7,6 MHz, subtono 77,0 Hz. Escribe los tres datos que programas, la frecuencia en la que transmitirá tu equipo y la frase con la que te anuncias si tu indicativo es EA5XYZ.
5. Estás escuchando a un amigo por el repetidor. Pulsas la tecla que te deja oír la frecuencia de entrada y le oyes igual de bien. ¿Qué te indica, y qué le propones?
6. Dos estaciones charlan por el repetidor pasándose el turno sin dejar ni medio segundo. Tú estás en la montaña, con un compañero que se ha torcido un tobillo, y necesitas avisar. ¿Qué falla en su manera de operar, y qué dices tú en cuanto encuentres un hueco?
7. Hablas por un repetidor con un compañero que va en coche. Te dice: «¿qué informe me das?». La barra de tu medidor está al máximo, pero su voz llega con soplido y se corta a ratos. ¿Qué le contestas, y por qué no «cinco nueve»?

**Soluciones**

1. 145,750 − 0,600 = **145,150 MHz**.
2. 439,300 − 7,6 = **431,700 MHz**.
3. El subtono (no está activado, o no es el de ese repetidor) o el desplazamiento (no está activado, o tiene el signo o el valor equivocados). En los dos casos el repetidor no se entera de que le llamas. Una tercera: que no llegues, por estar en una zona sin cobertura hacia el monte.
4. Programas: frecuencia 438,950 MHz, desplazamiento −7,6 MHz y subtono 77,0 Hz. El equipo transmitirá en 438,950 − 7,6 = **431,350 MHz**. Tras escuchar un rato: «EA5XYZ, a la escucha por el repetidor».
5. Que le recibes directamente, sin necesidad del repetidor. Le propones pasar a una frecuencia símplex libre y dejar el repetidor para quien lo necesite.
6. No dejan pausas, que existen precisamente para que pueda entrar quien tiene algo urgente. En el primer hueco: «Break, break, break, tráfico de emergencia. Aquí…» y tu indicativo.
7. «Entras con soplido y se te corta a ratos.» La barra al máximo mide la señal del repetidor, que tienes cerca, no la de tu compañero; lo que a él le sirve es saber cómo entra *él* en el repetidor. Es lo que viste en la lección 4.

## En una frase

Un repetidor recibe en una frecuencia y retransmite a la vez en otra desde un punto alto; para usarlo se programan su frecuencia de salida, el desplazamiento (−600 kHz en 2 metros, −7,6 MHz en 70 centímetros) y el subtono que lo abre, y se usa con pausas, brevedad y solo cuando el contacto directo no alcanza.

Has visto que hay frecuencias para llamar, tramos para hablar, entradas y salidas de repetidor. Alguien ha tenido que repartir todo eso. La lección siguiente es el plano.
