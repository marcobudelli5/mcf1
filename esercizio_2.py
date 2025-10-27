import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

df_extrasolare = pd.read_csv("ExoplanetsPars_2025.csv", comment = '#')
print(df_extrasolare.columns)
print(df_extrasolare["pl_orbper"], df_extrasolare["pl_bmassj"], df_extrasolare["pl_orbsmax"], df_extrasolare["st_mass"], df_extrasolare["discoverymethod"])

