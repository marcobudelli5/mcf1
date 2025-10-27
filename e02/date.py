from datetime import datetime, timedelta
datetime.now()
datenow = datetime.now()
print(datenow.year)
print(datenow.month)
print(datenow.day)
print(datenow.hour)
print(datenow.minute)
print(datenow.second)
anno_di_nascita = input('Inserisci il tuo anno di nascita: ')
mese_di_nascita = input('Inserisci il tuo mese di nascita: ')
giorno_di_nascita = input('Inserisci il tuo giorno di nascita: ')
ora_di_nascita = input('Inserisci l ora in cui sei nato: ')
minuto_nascita = input('inserisci i minuti in cui sei nato: ')
secondi_nascita = input('Inserisci i secondi  a cui sei nato: ')
mydate_str = anno_di_nascita+'-'+mese_di_nascita+'-'+giorno_di_nascita+' '+ora_di_nascita+':'+minuto_nascita+':'+secondi_nascita
mydate = datetime.strptime(mydate_str, "%Y-%m-%d %H:%M:%S")
print('Data di nascita: ', mydate)
print('Anno di nascita: ', mydate.year)
print('Secondi: ', mydate.second)
print('Giorno:', mydate.day)
print('Ora:', mydate.hour)
timediff = datenow - mydate
timediff
tots = timediff.total_seconds()
totd = tots/86400
toty_non_bisestile = 31536000
toty_bisestile = 31622400
a_n = int(anno_di_nascita)
dny = int(datenow.year)
for i in range(a_n, dny):
   if  i%4 == 0 or i%400 == 0:
      i = toty_bisestile
   else:
      i = toty_bisestile
   toty = (tots/i)
print('Età in secondi:' ,tots)
print('Età in anni:', toty)
print('Età in giorni:', totd)
