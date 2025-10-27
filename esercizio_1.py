import numpy as np
import pandas as pd
import scipy
import  matplotlib.pyplot as plt

df_pianeta = pd.read_csv('kplr010666592-2011240104155_slc.csv')
print(df_pianeta.columns)
#print(df_pianeta)

plt.plot(df_pianeta["TIME"], df_pianeta["PDCSAP_FLUX"])
plt.xlabel('Tempo')
plt.ylabel('Flusso')
plt.show()

plt.plot(df_pianeta["TIME"], df_pianeta["PDCSAP_FLUX"], 'o', color='red')
plt.xlabel('TEMPO')
plt.ylabel('FLUSSO') 
plt.show()

plt.errorbar(df_pianeta["TIME"], df_pianeta["PDCSAP_FLUX"], yerr = df_pianeta["PDCSAP_FLUX_ERR"], fmt='o', color='green')
plt.xlabel('t')
plt.ylabel('flusso')
plt.show()
plt.savefig('grafico_flusso_tempo.pdf')

seldf_pianeta = df_pianeta.loc[(df_pianeta['TIME'] > 949) & (df_pianeta['TIME'] < 951)]
plt.errorbar(seldf_pianeta["TIME"],seldf_pianeta["PDCSAP_FLUX"],yerr=seldf_pianeta["PDCSAP_FLUX_ERR"], fmt= 'o', color='black')
plt.xlabel('t')
plt.ylabel('flusso')
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(df_pianeta["TIME"], df_pianeta["PDCSAP_FLUX"],'o', color='pink')
ins_ax = ax.inset_axes([0.7, 0.7, 0.3, 0.3])
ins_ax.errorbar(seldf_pianeta["TIME"], seldf_pianeta["PDCSAP_FLUX"], yerr = seldf_pianeta["PDCSAP_FLUX_ERR"], fmt='o', color='blue')
plt.show()
