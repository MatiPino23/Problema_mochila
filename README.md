# Problema_mochila
## Introducción


La presente tarea 3, correspondiente a la asignatura de Algoritmos Metaheurísticos inspirados en la naturaleza, se desarrolló en el lenguaje de programación Python 3, para la solución del problema de la Mochila a travéz del método de Extremal Optimisation. Los integrantes responsables de la realización de dicha tarea fueron:
Matías Pino V. y María Suloaga V.

## Instalación de entorno


Para utilizar esta aplicación, se necesita instalar Visual Studio Code en la versión compatible con su sistema operativo. Dicho programa se puede descargar en el siguiente enlace: [Enlace](https://code.visualstudio.com/download)

## Clonación de repositorio


Luego de tener instalado el programa anterior, se debe descargar el repositorio que contiene la aplicación en Python 3, en el enlace: [Enlace](https://github.com/MatiPino23/Problema_mochila/archive/refs/heads/main.zip)


## Compilación y ejecución de la aplicación


Iniciamos Visual Studio Code, y abrimos la aplicación. Una vez realizado el paso anterior, se debe instalar la libreria numpy, ingresando a la terminal de Visual Studio Code y digitando el siguiente comando para realizar la instalación:

***
```
pip install numpy
pip install matplotlib
```
***

Luego de lo anterior, se debe ejecutar la aplicación desde la terminal utilizando el comando, teniendo en cuenta la siguiente nomenclatura:

```
"a" Cantidad de semillas
"b" Numero de iteraciones maximas.
"c" Variable Tau.
 

```
```
 a b c
```
python.exe .\main.py .\hardinstances_pisinger\knapPI_11_20_1000.csv a b c 

***
## Caso de prueba de la mejor solucion
```
 python.exe .\main.py .\hardinstances_pisinger\knapPI_11_20_1000.csv 40 5000 1.1
```
***
