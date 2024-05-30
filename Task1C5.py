import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# deschidem fisierul in care adaugam rezultatele de la acest task
data_variables = open('data.txt', 'a+')
print('Task1C5 data:', file=data_variables)

# extragem seturile de date pentru fiecare grupa de varsta
very_young_people = var.data[var.data['Age'] <= 20]
young_people = var.data[(var.data['Age'] > 20) & (var.data['Age'] <= 40)]
middle_aged = var.data[(var.data['Age'] > 40) & (var.data['Age'] <= 60)]
old_people = var.data[var.data['Age'] > 60]

# adaugam numarul lor in fisierul de date
print('Very young people:', very_young_people.shape[0], file=data_variables)
print('Young people:', young_people.shape[0], file=data_variables)
print('Middle aged:', middle_aged.shape[0], file=data_variables)
print('Old people:', old_people.shape[0], file=data_variables)
print(file=data_variables)

# vrem sa vedem in ce categorie este fiecare om din dataset
# pentru fiecare, adaugam un index in functie de varsta
# 0 - Very young people [0, 20]
# 1 - Young people [21, 40]
# 2 - Middle Aged [41, 60]
# 3 - Old People [61, ...]
# -1 - daca nu se incadreaza in nicio categorie sau nu apare varsta
age_index = []

for age in var.data['Age']:
	if age <= 20:
		age_index.append(0)
	elif age > 20 and age <= 40:
		age_index.append(1)
	elif age > 40 and age <= 60:
		age_index.append(2)
	elif age > 60:
		age_index.append(3)
	else:
		age_index.append(-1)

# adaugam in dataset coloana cu aceste valori
var.data.insert(var.data.shape[1], 'Age Index', age_index)
# cream un nou fisier csv cu aceasta coloana adaugata
var.data.to_csv('train_with_age_index.csv')

# facem un grafic cu numarul de persoane din fiecare grupa de varsta
plt.bar('Very young people', very_young_people.shape[0], label='Very young people')
plt.bar('Young people', young_people.shape[0], label='Young people')
plt.bar('Middle Aged', middle_aged.shape[0], label='Middle Aged')
plt.bar('Old People', old_people.shape[0], label='Old People')
plt.savefig('Grupe_de_varsta.png')
plt.close()

data_variables.close()