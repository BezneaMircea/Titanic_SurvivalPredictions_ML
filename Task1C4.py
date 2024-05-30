import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# deschidem fisierul in care adaugam rezultatele de la acest task
data_variables = open('data.txt', 'a+')
print('Task1C4 data:', file=data_variables)

# extragem seturile de date pentru supravietuitori si morti
supravietuitori = var.data[var.data['Survived'] == 1]
morti =	var.data[var.data['Survived'] == 0]

# cautam coloanele care au valori lipsa
# cand gasim o coloana cu valori lipsa, calculam procentajul de valori lipsa
# din totalul de valori, si din totalul de valori lipsa, pentru supravietuitori si morti
for coloana in var.data.columns:
	nr_valori_lipsa = var.data[coloana].isna().sum()
	if (nr_valori_lipsa > 0):
		procentaj_total = round(nr_valori_lipsa / var.nr_lines * 100, 2)
		procentaj_supravietuitori = round(supravietuitori[coloana].isna().sum() / supravietuitori.shape[0] * 100, 2)
		procentaj_morti = round(morti[coloana].isna().sum() / morti.shape[0] * 100, 2)
		# adaugam aceste valori in fisierul de date
		print(f'{coloana} are {nr_valori_lipsa} valori lipsa, {procentaj_total}% din totalul celor lipsa', file=data_variables)
		print(f'{procentaj_supravietuitori}% din supravietuitori au valori lipsa la {coloana}', file=data_variables)
		print(f'{procentaj_morti}% din morti au valori lipsa la {coloana}', file=data_variables)
		# \n in fisier
		print(file=data_variables)

data_variables.close()