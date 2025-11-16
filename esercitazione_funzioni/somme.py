def somma_n_numeri(n):
     somma=0
     for i in range(n+1):
          somma = somma+i
     return somma
def somma_n_numeri2(n):
     somma1 = (n*(n+1))/2
     somma2 = int(somma1)
     return somma2
print(somma_n_numeri(10))
print(somma_n_numeri2(10))
