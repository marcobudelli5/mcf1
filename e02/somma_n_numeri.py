import pandas as pd
import numpy as np
import matplotlib as mtl

numero_naturale = input('Inserisci un numero naturale a piacere maggiore di 1: ')
nm = int(numero_naturale)
print('Ecco il numero naturale scelto', nm)
somma = 0
for i in range(1, nm+1):
   somma = somma+i
print('La somma dei primi', numero_naturale, 'numeri naturali è', somma) 
