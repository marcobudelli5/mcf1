giorni_settimana = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
grs = giorni_settimana*3
giorni_settimana_ottobre = giorni_settimana[2:7]+grs+giorni_settimana[0:5]
#numeri_giorni_lunedì = [6, 13, 20,27]
#numeri_giorni_martedì = [7, 14, 21, 28]
#numeri_giorni_mercoledì = [1, 8, 15, 22, 29]
#numeri_giorni_giovedì = [2, 9, 16, 23, 30]
#numeri_giorni_venerdì = [3, 10, 17, 24, 31]
#numeri_giorni_sabato = [4, 11, 18, 25]
#numeri_giorni_domenica = [5, 12, 19, 26]
print('Ecco i nomi dei giorni della settimana del mese di ottobre 2025', giorni_settimana_ottobre)
#numero_nome_giorni_ottobre = {giorni_settimana[0] :numeri_giorni_lunedì, giorni_settimana[1] :numeri_giorni_martedì, giorni_settimana[2] :numeri_giorni_mercoledì, giorni_settimana[3] :numeri_giorni_giovedì, giorni_settimana[4] :numeri_giorni_venerdì, giorni_settimana[5] :numeri_giorni_sabato, giorni_settimana[6] :numeri_giorni_domenica}
#for k in numero_nome_giorni_ottobre:
#   print(k, '  Giorni corrispondenti: ', numero_nome_giorni_ottobre[k])
numeri_giorni = [1]
for j in range(2, 32):
   numeri_giorni.append(j)
print('Ecco i giorni presenti a Ottobre 2025: ', numeri_giorni)
for k in range(0, 31):
   correlazione_num_giorno_ottobre = {giorni_settimana_ottobre[k] : numeri_giorni[k]}
   for j in correlazione_num_giorno_ottobre:
      print('Il giorno della settimana corrispondente al numero ', correlazione_num_giorno_ottobre[j], ' di Ottobre: ', j)

