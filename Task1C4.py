import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

supravietuitori = var.data[var.data['Survived'] == 1]
morti =	var.data[var.data['Survived'] == 0]

info_missing = []

for coloana in var.data.columns:
	nr_valori_lipsa = var.data[coloana].isna().sum()
	if (nr_valori_lipsa > 0):
		procentaj_total = round(nr_valori_lipsa / var.nr_lines * 100, 2)
		procentaj_supravietuitori = round(supravietuitori[coloana].isna().sum() / supravietuitori.shape[0] * 100, 2)
		procentaj_morti = round(morti[coloana].isna().sum() / morti.shape[0] * 100, 2)

		info_missing.append({
			'Coloana': coloana,
			'Valori_lipsa': nr_valori_lipsa,
			'Procentaj_total': procentaj_total,
			'Procentaj_din_supravietuitori': procentaj_supravietuitori,
			'Procentaj_din_morti': procentaj_morti
		})

data_missing = pd.DataFrame(info_missing)
var.data_missing = data_missing