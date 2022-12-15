import numpy as np
import pandas as pd
import sys

np.random.seed(seed)

nnodes = np.genfromtxt(filepath, delimiter=' ', skip_header = 1 , usecols=(1) , max_rows=1, dtype = int)            # Numero de objetos
capacity = np.genfromtxt(filepath, delimiter=' ', skip_header = 2 , usecols=(1) , max_rows=1, dtype = int)          # Capacidad de la mochila
z_best = np.genfromtxt(filepath, delimiter=' ', skip_header = 3 , usecols=(1) , max_rows=1, dtype = int)            # Mejor valor esperado
data = np.genfromtxt(filepath, delimiter=',', skip_header = 5 , usecols=(1, 2, 3) , max_rows=nnodes, dtype = int)   # Informacion de los objetos
x_best = np.random.randint(2, size=nnodes)  # Arreglo inicial de objetos en la mochila