import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

supravietuitori = var.data[var.data['Survived'] == 1]
morti =	var.data[var.data['Survived'] == 0]

for coloana in var.data.columns:
	if (var.data[coloana].isna().sum() > 0):
		for row in var.data.iterrows():
			if pd.isna(row[1][coloana]):
				if (row[1]['Survived'] == 1):
					if (var.data[coloana].dtypes != 'object'):
						row[1][coloana] = int(round(supravietuitori[coloana].mean()))
					elif (var.data[coloana].nunique() >= 2 and var.data[coloana].nunique() <= 5):
						row[1][coloana] = supravietuitori[coloana].mode()[0]
				else:
					if (var.data[coloana].dtypes != 'object'):
						row[1][coloana] = int(round(morti[coloana].mean()))
					elif (var.data[coloana].nunique() >= 2 and var.data[coloana].nunique() <= 5):
						row[1][coloana] = morti[coloana].mode()[0]
				var.data.loc[row[0], coloana] = row[1][coloana]

var.data.to_csv('train_cleaned.csv')