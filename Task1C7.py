import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# deschidem fisierul in care adaugam rezultatele de la acest task
data_variables = open('data.txt', 'a+')
print('Task1C7 data:', file=data_variables)

# dataset cu adultii si copiii
children = var.data[var.data['Age'] < 18]
adults = var.data[var.data['Age'] >= 18]

# procentajul de copii
print('Children percentage:', round(children.shape[0] / var.data.shape[0] * 100, 2), file=data_variables)
print(file=data_variables)

# dataset cu supravietuitorii, copii si adulti
survived_children = children[children['Survived'] == 1]
survived_adults = adults[adults['Survived'] == 1]

# grafic cu procentajul de supravietuire pentru copii si adulti
plt.bar('Children', round(survived_children.shape[0] / children.shape[0] * 100, 2))
plt.bar('Adults', round(survived_adults.shape[0] / adults.shape[0] * 100, 2))
plt.ylabel('Percentage survived')
plt.savefig("Supravietuire_copii_adulti.png")
plt.close()

data_variables.close()