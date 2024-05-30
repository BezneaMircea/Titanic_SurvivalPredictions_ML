import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# deschidem fisierul in care adaugam rezultatele de la acest task
data_variables = open('data.txt', 'a+')
print('Task1C6 data:', file=data_variables)

# extragem seturile de date pentru fiecare grupa de varsta
very_young_people = var.data[var.data['Age'] <= 20]
young_people = var.data[(var.data['Age'] > 20) & (var.data['Age'] <= 40)]
middle_aged = var.data[(var.data['Age'] > 40) & (var.data['Age'] <= 60)]
old_people = var.data[var.data['Age'] > 60]

# aflam cati oameni din fiecare grupa de varsta au supravietuit
# apoi luam doar barbatii care au supravietuit din fiecare grupa de varsta
survived_very_young_people = very_young_people[very_young_people['Survived'] == 1]
male_survived_very_young_people = survived_very_young_people[survived_very_young_people['Sex'] == 'male']

survived_young_people = young_people[young_people['Survived'] == 1]
male_survived_young_people = survived_young_people[survived_young_people['Sex'] == 'male']

survived_middle_aged = middle_aged[middle_aged['Survived'] == 1]
male_survived_middle_aged = survived_middle_aged[survived_middle_aged['Sex'] == 'male']

survived_old_people = old_people[old_people['Survived'] == 1]
male_survived_old_people = survived_old_people[survived_old_people['Sex'] == 'male']

# numarul acestora va fi pus in fisierul de date
print("very young male survived: ", male_survived_very_young_people.shape[0], file=data_variables)
print("young male survived: ", male_survived_young_people.shape[0], file=data_variables)
print("middle aged male survived:", male_survived_middle_aged.shape[0],file=data_variables)
print("old male survived:", male_survived_old_people.shape[0], file=data_variables)
print(file=data_variables)

# facem un grafic cu numarul de barbati din fiecare grupa de varsta care au supravietuit
plt.bar('Very young male survived', male_survived_very_young_people.shape[0], label='Very young male survived')
plt.bar('Young male survived', male_survived_young_people.shape[0], label='Young male survived')
plt.bar('Middle Aged male survived', male_survived_middle_aged.shape[0], label='Middle Aged male survived')
plt.bar('Old male survived', male_survived_old_people.shape[0], label='Old male survived')
plt.savefig('Supravietuitori_barbati_per_grupa_ani.png')
plt.close()

data_variables.close()