import numpy as np
import pandas as pd
import sys

def generateCapacityFitness():  # Generar fitness a partir de la capacidad de cada objeto
    return data[:, 1]

def generateValueFitness():     # Generar fitness a partir del valor de cada objeto
    return data[:, 0]

if len(sys.argv) == 5:  # python.exe .\main.py .\hardinstances_pisinger\knapPI_11_20_1000.csv 1 10000 1.4
    filepath = str(sys.argv[1])
    seed = int(sys.argv[2])
    iterations = int(sys.argv[3])
    tau = float(sys.argv[4])
    print("Ruta del archivo: ", filepath, "Semilla: ", seed, "Numero de iteraciones: ", iterations, "Tau: ", tau, sep='\n')
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: ruta del archivo, semilla, numero de iteraciones y tau')
    sys.exit(0)
    
np.random.seed(seed)

nnodes = np.genfromtxt(filepath, delimiter=' ', skip_header = 1 , usecols=(1) , max_rows=1, dtype = int)            # Numero de objetos
capacity = np.genfromtxt(filepath, delimiter=' ', skip_header = 2 , usecols=(1) , max_rows=1, dtype = int)          # Capacidad de la mochila
z_best = np.genfromtxt(filepath, delimiter=' ', skip_header = 3 , usecols=(1) , max_rows=1, dtype = int)            # Mejor valor esperado
data = np.genfromtxt(filepath, delimiter=',', skip_header = 5 , usecols=(1, 2, 3) , max_rows=nnodes, dtype = int)   # Informacion de los objetos
x_best = np.random.randint(2, size=nnodes)  # Arreglo inicial de objetos en la mochila

# Creacion de la ruleta con respecto a i^-tau
roulette = np.arange(1, nnodes + 1)**-tau
roulette /= np.sum(roulette)

sorted_capacity_fitness = np.argsort(generateCapacityFitness()) # Indices ordenados del fitness de la capacidad
sorted_value_fitness = np.argsort(generateValueFitness())       # Indices ordenados del fitness del valor

best_factible_x = np.full(nnodes, -1)
best_factible_value_x = 0