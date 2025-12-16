from scipy import constants, fft
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft, istft

name = "data1.txt"
samplerate = 44100

with open('./'+name, 'r') as data:
    datax =[]
    datay = []
    for line in data:
        p=line.split()
        datax.append(float(p[0]))
        datay.append(float(p[1]))

print(samplerate)
#print(datax)
print(len(datax))
#print(datay)
print(len(datay))

'''
plt.figure(figsize=(10, 10))
plt.title("Waveform")
plt.plot(datax, datay, color='red')
plt.xlabel("Tempo[s]")
plt.ylabel("Ampiezza[u.a]")
plt.show()
'''
#FFT dell'array ottenuto

datafft = fft.rfft(datay)
datafft_mod=[np.abs(x) for x in datafft]
datafft_mod2=[x**2 for x in datafft_mod]
datafft_real = [z.real for z in datafft]
datafft_imag = [z.imag for z in datafft]
datafft_mod2_real = [(np.abs(z))**2 for z in datafft_real]
datafft_mod2_imag = [(np.abs(z))**2 for z in datafft_imag]
datafft_phase= [np.arctan2(w.imag,w.real) for w in datafft]
#datafft_ril=[(p > ((1/10)**8)*np.max(datafft_mod)) for p in datafft_mod]
#datafft2=fft.rfft(datay2)
#datafft_abs = fft.rfft(np.abs(datay))
#datafft2_abs=np.abs(datafft2)
#print(datafft.size)
#print(len(datay))
#fftfreq = 0.5*fft.rfftfreq(datafft.size, 1.0/samplerate)
fftfreq = fft.rfftfreq(len(datax), 1.0/samplerate)

#print(datafft)
#print(len(datafft))
#print(fftfreq)
#print(len(fftfreq))
'''
Plot parte reale dei coefficienti
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("FFT")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Ampiezza(Parte Reale)(u.a)')
plt.plot(fftfreq[:len(datafft)], datafft[:len(datafft)].real, color='pink')
plt.show()

#Plot della parte immaginaria dei coefficienti
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("FFT")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Ampiezza(Parte Immaginaria)(u.a)')
plt.plot(fftfreq[:len(datafft)], datafft[:len(datafft)].imag, color='red')
plt.show()

#Plot della potenza
#datay_float=[float(elemento) for elemento in datay]
#datay2=[x**2 for x in datay_float]
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("POTENZA DELLA FFT")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Potenza(W)')
plt.plot(fftfreq[:len(datafft)], datafft_mod2[:len(datafft_mod)] , color='black')
plt.show()

#Plot potenza parte immaginaria dei coefficienti
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("POTENZA Parte immaginaria")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Potenza(W)')
plt.plot(fftfreq[:len(datafft)], datafft_mod2_imag[:len(datafft_mod)] , color='orange')
plt.show()

#Plot potenza parte reale dei cefficienti
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("POTENZA DELLA Parte reale")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Potenza(W)')
plt.plot(fftfreq[:len(datafft)], datafft_mod2_real[:len(datafft_mod)] , color='purple')
plt.show()

#Plot fase FFT
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("FASE FFT")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('FASE')
plt.plot(fftfreq[:len(datafft)], datafft_phase[:len(datafft)] , color='purple')
plt.show()

plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("FASE FFT IMAG")
plt.xlabel('Frequenza(Hz)')
plt.ylabel('FASE IMAG')
plt.plot(fftfreq[:len(datafft_phase)], datafft_phase[:len(datafft_phase)])
plt.show()

#ri-sintesi del segnale

syndata = fft.irfft(datafft, n=len(datax))
plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("Ri-sintesi del segnale")
plt.xlabel('Tempo[s]')
plt.ylabel('Ampiezza[u.a]')
plt.plot(datax[:len(datax)], syndata[:len(syndata)])
plt.show()
'''
#mascheramento del rumore

# Stima del rumore (robusta)
'''
noise_level = np.median(datafft_mod2)

# Maschera: tieni solo ciò che emerge dal rumore
#mask = np.empty(0)
'''
mask = []
for i in datafft_mod2 :
    if i>10*noise_level :
        mask.append(1)
    else :
        mask.append(0)
mask_float= [float(s) for s in mask]
m = np.mean(mask_float)
print(m)
X_filt= datafft*mask
        

# Torna nel tempo
x_filt = np.fft.irfft(X_filt) 


plt.figure(20)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.title("Ri-sintesi del segnale mascherato")
plt.xlabel('Tempo[s]')
plt.ylabel('Ampiezza[u.a]')
plt.plot(datax[:len(x_filt)], x_filt[:len(x_filt)])
plt.show()


plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.title("Segnale originale")
plt.plot(datax, datay, color='pink')
plt.xlabel("Tempo [s]"); plt.ylabel("Ampiezza")

plt.subplot(2,1,2)
plt.title("Segnale filtrato con STFT")
plt.plot(datax, x_filt, color='black')
plt.xlabel("Tempo [s]"); plt.ylabel("Ampiezza")
plt.tight_layout()
plt.show()
