En la azotea, Dani no ajustó la antena de Marina a ojo. Conectó un aparatito con pantalla, miró un dibujo, cortó un trozo de hilo y volvió a mirar. Abajo, en el cuarto de radio de Vicente, hay otras dos cajas que tienen que ver con lo mismo: una con dos mandos grandes que él llama «el acoplador» y un bote metálico con aletas que nunca se conecta a ninguna antena.

Esta lección presenta esos aparatos. Al terminar sabrás cómo se mide la ROE y qué precauciones pide la medida, cómo se lee la curva de un analizador de antenas, qué hace un acoplador y qué no hace, y para qué sirve una carga artificial. Son cuatro preguntas directas de examen.

## El medidor de ROE

También llamado *reflectómetro*, o «medidor de estacionarias» en el habla de radioclub. Es una cajita que se intercala en el cable, entre el transmisor y la antena, y que mide por separado la potencia que va y la que vuelve. Con esas dos cifras indica la ROE. (Por dentro hace, al revés, la cuenta de los dos pasos de la lección anterior, y le sale el mismo número que saldría de comparar las tensiones a lo largo del cable.) Muchos equipos modernos lo llevan incorporado.

Recuerda que en el cable la onda estacionaria no es deseable: es la señal de que la antena devuelve parte de lo que le llega, y este aparato sirve para vigilarla.

Para medir con él hay que **transmitir**, y transmitir es salir al aire. Así que la medida se hace con poca potencia, durante unos segundos, en una frecuencia libre y después de escuchar que no molestas a nadie.

## El analizador de antenas

Es el aparatito con pantalla que Dani subió a la azotea. Lleva dentro un transmisor minúsculo, de milésimas de vatio, que va recorriendo las frecuencias una tras otra mientras mide la ROE en cada una. El resultado es una curva en la pantalla: la ROE de la antena a lo largo de toda la banda.

Esa curva tiene forma de valle, y enseña de un vistazo todo lo que importa:

- **El fondo del valle** es la frecuencia de resonancia de la antena.
- **La profundidad del valle** dice lo buena que es la adaptación en ese punto.
- **La anchura del valle** es el ancho de banda: el tramo de frecuencias en el que la ROE se mantiene aceptable, por ejemplo por debajo de 2.

![La curva de ROE de una antena a lo largo de la frecuencia, con forma de valle. El punto más bajo, con ROE 1,2, está en 7,10 megahercios: es la frecuencia de resonancia. Una línea horizontal en ROE 2 corta la curva en dos puntos; el tramo de frecuencias entre ellos es el ancho de banda utilizable.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s08-curva-de-roe.svg)

Así fue como ajustaron el dipolo de Marina. El primer valle apareció por debajo de la banda: la antena estaba larga. Recortaron un poco de cada punta y el valle se desplazó hacia arriba; otro pellizco, y quedó donde lo querían, con el fondo en 1,2.

### Un engaño que conviene conocer

El medidor se coloca casi siempre junto al equipo, y desde ahí lo que ve es la onda reflejada *después* de que haya recorrido el cable de vuelta. Si el cable tiene muchas pérdidas, esa onda llega muy debilitada, y el medidor marca una ROE mejor que la real. Un cable malo puede esconder una antena mala. Un cable con muchísimas pérdidas y sin antena alguna puede marcar una ROE estupenda… porque toda la potencia se está quedando en el cable.

## El acoplador: un diplomático, no un cirujano

Queda un aparato muy popular y muy malentendido: el **acoplador de antena**, también llamado *sintonizador* o, en inglés, *tuner*.

Es una caja con bobinas y condensadores ajustables que se coloca entre el transmisor y el cable. Ajustándola, se consigue que el transmisor «vea» 50 Ω aunque la antena presente otra cosa. Por dentro son una bobina y dos condensadores (o dos bobinas y un condensador) dispuestos en forma de **π** o de **T**, según cómo se dibujan en el esquema; son los dos nombres que pregunta el examen. Muchos equipos llevan un acoplador automático en su interior.

Lo que hace y lo que no hace:

- **Lo que hace:** contenta al transmisor. El equipo ve sus 50 Ω, no se protege y entrega toda su potencia.
- **Lo que no hace:** arreglar la antena. El acoplador está en un extremo del cable y la antena en el otro. Entre el cable y la antena el desacuerdo sigue exactamente igual que antes, con sus idas y venidas y sus pérdidas añadidas en el cable.

De ahí el dicho: el acoplador es un diplomático, no un cirujano. Convence al transmisor de que todo va bien, pero no opera al paciente.

¿Sirve entonces para algo? Para mucho, bien usado:

- Para aprovechar los extremos de una banda, donde una antena buena tiene una ROE de 2 o 2,5.
- Para usar un mismo hilo en varias bandas, con un cable corto y de pocas pérdidas.
- Colocado **junto a la antena**, en vez de junto al equipo. Ahí sí corrige el desacuerdo en su origen, y el cable trabaja adaptado en toda su longitud. Las antenas de hilo largo se montan así.

Lo que no debe hacerse es usarlo para tapar una antena rota o un conector en mal estado. Si una antena que daba ROE 1,3 pasa un día a dar 4, lo que toca es subir a la azotea, no girar los mandos del acoplador.

## La carga artificial: transmitir sin salir al aire

El bote con aletas de la mesa de Vicente es el tercer aparato.

Hay muchos momentos en que necesitas poner el transmisor en marcha sin que nadie te oiga: para comprobar que funciona después de una reparación, para medir su potencia, para ajustarlo. Hacer todo eso con la antena conectada significa ocupar una frecuencia y molestar a quien esté en ella.

> **Carga artificial** (también *antena fantasma* o, en inglés, *dummy load*): una resistencia de 50 Ω capaz de absorber toda la potencia del transmisor y convertirla en calor, sin radiarla. Se conecta en lugar de la antena para hacer pruebas y ajustes.

Tiene tres propiedades que explican su utilidad:

- **Es de 50 Ω y puramente resistiva.** El transmisor ve una adaptación perfecta, con ROE 1, y trabaja como si tuviera conectada la mejor antena del mundo.
- **No radia** (prácticamente nada). Toda la potencia se convierte en calor.
- **Aguanta la potencia** del equipo, al menos durante un tiempo. Una carga para 100 W es una pieza con aletas metálicas, o un bote lleno de aceite que reparte el calor. Las cargas pequeñas solo soportan su potencia máxima durante unos segundos; conviene mirar la etiqueta.

Vicente lo decía a su manera: ajustar un transmisor por la antena es ensayar la trompeta en el rellano.

La carga artificial tiene además un uso de diagnóstico muy práctico. Si la ROE de tu instalación sale alta, desconecta la antena y pon la carga artificial al final del cable. Si ahora la ROE es 1, el cable está bien y el problema está en la antena. Si sigue alta, el problema está en el cable o en sus conectores.

## Donde la gente se lía

- **«El acoplador mejora la antena.»** Mejora la vida del transmisor. La antena y el cable siguen como estaban.
- **«Si el medidor marca bien, todo va bien.»** Un cable con muchas pérdidas disimula la ROE. Una ROE sospechosamente buena al final de un cable largo y fino no es una buena noticia.
- **«El fondo del valle del analizador es donde mejor radia la antena.»** Es donde mejor adaptada está. Casi siempre coincide con su resonancia, pero la curva no dice nada de hacia dónde radia ni de cuánto.
- **«La carga artificial es una antena pequeñita para pruebas.»** Es lo contrario de una antena: está hecha para **no** radiar.
- **«Con la carga artificial sale ROE 1, así que mi antena está bien.»** Con la carga artificial conectada, la antena no interviene. Ese resultado solo dice que el equipo y el cable están bien.

## Compruébalo tú

1. Un medidor intercalado entre el equipo y la antena marca 100 W directos y 4 W reflejados. ¿Qué ROE hay? Usa la tabla de la lección anterior.
2. El analizador muestra el valle de tu antena en 14,05 MHz y tú quieres trabajar en 14,25 MHz. ¿Qué haces con el hilo?
3. La curva de tu antena está por debajo de ROE 2 entre 7,02 y 7,18 MHz. ¿Cuál es su ancho de banda, en kilohercios?
4. Un compañero tiene una antena con ROE 6. Pone un acoplador junto al equipo, lo ajusta y el equipo marca ROE 1. Dice que ya ha arreglado la antena. ¿Qué le explicas?
5. ¿Con qué dos letras se nombran las disposiciones habituales de los componentes de un acoplador?
6. Quieres comprobar la potencia de tu equipo sin molestar a nadie. ¿Qué conectas en lugar de la antena y qué ROE esperas ver?
7. La ROE de tu instalación ha pasado de 1,3 a 5 de un día para otro. Pones la carga artificial al final del cable, en lugar de la antena, y la ROE sale 1. ¿Dónde está la avería?

**Soluciones**

1. Se reflejan 4 de cada 100 vatios, el 4 %. En la tabla, eso corresponde a una ROE de **1,5**: muy buena.
2. El valle está por debajo de donde lo quieres, así que la antena está **larga**: se **recorta** un poco de cada punta y se vuelve a medir.
3. 7,18 − 7,02 = 0,16 MHz, que son **160 kHz**.
4. Que ha contentado al transmisor, que ahora ve 50 Ω y entrega su potencia, pero que entre el cable y la antena la ROE sigue siendo 6, con las pérdidas añadidas que eso supone en el cable. El acoplador no ha tocado la antena. Con una ROE tan alta, lo que toca es averiguar qué le pasa.
5. **π** y **T**.
6. Una **carga artificial** de 50 Ω que aguante la potencia del equipo. Se espera una ROE de **1**.
7. En la **antena** (o en su conexión con el cable). Con la carga artificial al final, el cable y sus conectores han demostrado estar bien.

## En una frase

El medidor de ROE compara la potencia que va con la que vuelve, el analizador dibuja la ROE de la antena a lo largo de la frecuencia, el acoplador hace que el transmisor vea 50 Ω sin arreglar la antena, y la carga artificial son 50 Ω que se tragan la potencia sin radiarla, para probar sin molestar.

Queda la pieza que une todo lo demás y que hemos tratado hasta ahora como si fuera perfecta. No lo es: el cable se queda con una parte de tu potencia, y a veces se pone a hacer de antena por su cuenta.
