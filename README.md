# Documentación Tarea / Práctica 2

Primero nos colocamos en la raíz de la práctica ó en el directorio del problema que queremos probar (Graph/Codify)

##Para Graph

Tenemos 3 archivos `Reader.py`, `Solution.py` y `Main.py` 


<ul>
    <li>Reader: lee el .col y crea la matriz de adyacencias, la representa y guarda el resultado de la ejecución</li>
    <li>Solution: representa la solución, también tiene muchas funciones auxiliares que nos ayudan a encontrar la solución</li>
    <li>Main: ejecutable principal</li>
</ul>

**Main.py**

Este script se ejecuta desde terminal de la siguiente manera:

Si estamos en la raíz del repositorio:

`python3 src/Graph/Main.py <nombre_archivo.col>`

Si estamos en el directorio `src/Graph`

`python3 Main.py <nombre_archivo.col>`

Esto no generará ningún output en terminal(a menos que haya errores de ejecución) para verificar el output debemos ir al directorio `src/output` y abrir el 
archivo `coloring_output.txt`

(El archivo de prueba dado se llama `graph1.col`, se puede modificar o crear otro archivo para probar otra gráfica)


##Para Codify
Tenemos 4 archivos `codificador.py`, `decodificador.py`, `codificador_vectores.py` y `decodificador_vectores.py` 
<ul>
    <li>codificador: Codifica un número real a número binario, con la cantidad de bits deseados en un rango de números establecido. </li>
    <li>decodificador: Deodifica un número binario a número base 10, con la cantidad de bits determinada, en un rango de números establecido.</li>
    <li>codificador_vectores: Utiliza el codificador para codificar un vector de números reales de la longitud que se requiera.</li>
    <li>decodificador_vectores: Utiliza el decodificador para decodificar un vector de números binarios de la longitud que se requiera.</li>

</ul>

**codificador.py**

Este script se ejecuta desde terminal de la siguiente manera (en el mismo directorio que esté el archivo):
>python3 codificador.py x nBits vmin vmax
donde:
x representa el número que se va a codificar, puede ser en el siguiente formato
nBits es el número de bits 
vmin es a, extremo inferior del intervalo
vmax es b, extremo superior del intervalo

ejemplo:
`>python3 codificador.py 5 6 0 5`

**decodificador.py**

Este script se ejecuta desde terminal de la siguiente manera (en el mismo directorio que esté el archivo):
>python3 decodificador.py x nBits vmin vmax
donde:
x representa el número binario que se va a decodificar
nBits es el número de bits 
vmin es a, extremo inferior del intervalo
vmax es b, extremo superior del intervalo

ejemplo:
`>python3 decodificador.py 100 3 0 4`

**codificador_vectores.py**

Este script se ejecuta desde terminal de la siguiente manera (en el mismo directorio que esté el archivo):
>python3 codificador_vectores.py nBits, vmin, vmax, x
donde:
nBits es el número de bits
vmin es a, extremo inferior del intervalo
vmax es b, extremo superior del intervalo
x representa los números que se van a codificar separados por un espacio

ejemplo:
`>python3 codificador_vectores.py 3 0 5 1 2 3 4 5`

**decodificador_vectores.py**

Este script se ejecuta desde terminal de la siguiente manera (en el mismo directorio que esté el archivo):
>python3 decodificador_vectores.py nBits, vmin, vmax, x
donde:
nBits es el número de bits
vmin es a, extremo inferior del intervalo
vmax es b, extremo superior del intervalo
x representa los números que se van a decodificar separados por un espacio

ejemplo:
`>python3 decodificador_vectores.py 3 0 5 000 001 010 011 100 101 110 111`
