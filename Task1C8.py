import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# extragem oamenii care au supravietuit si care au murit
supravietuitori = var.data[var.data['Survived'] == 1]
morti =	var.data[var.data['Survived'] == 0]

# cautam coloanele care au valori lipsa
for coloana in var.data.columns:
	if (var.data[coloana].isna().sum() > 0):
		for row in var.data.iterrows():
			# cautam randurile care au valori lipsa
			if pd.isna(row[1][coloana]):
				# daca persoana a supravietuit, luam media din supravietuitori de pe coloana
				# respectiva si o punem in locul valorii lipsa
				if (row[1]['Survived'] == 1):
					# verificam daca e coloana numerica sau categorica
					if (var.data[coloana].dtypes != 'object'):
						# punem valoarea medie de pe coloana respectiva din supravietuitori
						row[1][coloana] = round(supravietuitori[coloana].mean())
					# daca e coloana categorica (la noi asta inseamna ca exista intre
					# 2 si 5 valori unice in toata coloana), punem valoarea cea mai intalnita
					elif (var.data[coloana].nunique() >= 2 and var.data[coloana].nunique() <= 5):
						row[1][coloana] = supravietuitori[coloana].mode()[0]
				else:
					# aceeasi logica dar pe setul de date pentru morti
					if (var.data[coloana].dtypes != 'object'):
						row[1][coloana] = round(morti[coloana].mean())
					elif (var.data[coloana].nunique() >= 2 and var.data[coloana].nunique() <= 5):
						row[1][coloana] = morti[coloana].mode()[0]
				var.data.loc[row[0], coloana] = row[1][coloana]

# salvez datasetul cu valorile lipsa completate
var.data.to_csv('dataset_umplut.csv')