import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# extragem doar datele numerice din dataset
numeric_data = var.data.select_dtypes(include=np.number)

# pentru fiecare coloana numerica, generam o histograma
for coloana in numeric_data.columns:
	if (coloana != 'PassengerId'):
		plt.hist(numeric_data[coloana])
		plt.xlabel(coloana)
		plt.ylabel('Numar exemple')
		plt.savefig('histograma_' + coloana + '.png')
		# o inchidem pentru a nu se suprapune cu urmatoarea histograma si sa apara erori
		plt.close()