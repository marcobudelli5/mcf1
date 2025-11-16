import math as mt
def somma__n_numeri(n):
     somma=0
     for i in range(1, n+1):
          somma = somma+i
     return somma

def somma_prodotto_n_numeri(n):
     somma=0
     prodotto=1
     for i in range(1, n+1):
          somma = somma+i
          prodotto=prodotto*i
     return somma, prodotto

def somma_radici(n):
     somma_r=0
     for i in range(n+1):
          radice = mt.sqrt(i)
          somma_r=somma_r+radice
     return somma_r

def sommatoria_potenze_alfa(n,a=1):
     sommatoria=0
     for i in range(0, n+1):
          sommatoria=sommatoria+mt.pow(i, a)
     return sommatoria
     
#def somma_n_numeri2(n):
     #somma1 = (n*(n+1))/2
    # somma2 = int(somma1)
     #return somma2
#print('Ecco la somma dei numeri naturali: ',  somma_n_numeri(10))
#print('Ecco la somma delle radici dei numeri naturali: ', somma_radici(2))
#print(somma_n_numeri2(10))
