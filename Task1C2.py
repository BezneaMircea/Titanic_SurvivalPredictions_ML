import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt

# in data_variables sunt toate rezultatele cerute in taskul 1
data_variables = open('data.txt', 'a+')
print('Task1C2 data:', file=data_variables)

# extragem cati oameni au supravietuit si cati au murit value_counts() returneaza un dictionar cu cheia valoarea si valoarea numarul de aparitii
percentage_survived = var.data['Survived'].value_counts() / (var.nr_lines - var.Survived_missing_count) * 100
# extragem cate persoane sunt in fiecare clasa
percentage_class = var.data['Pclass'].value_counts() / (var.nr_lines - var.Pclass_missing_count) * 100
# extragem cate persoane sunt per sex
percentage_gender = var.data['Sex'].value_counts() / (var.nr_lines - var.Sex_missing_count) * 100

# adaug aceste valori in fisierul unde retin datele relevante pentru acest DataFrame
print('Percentage dead and survived:', percentage_survived, file=data_variables)
# aceste linii imi adauga un \n ca sa arate mai aerisit in fisier datele
print(file=data_variables)
print('Percentage per class:', percentage_class, file=data_variables)
print(file=data_variables)
print('Percentage per gender:', percentage_gender, file=data_variables)
print(file=data_variables)

# fac un grafic cu aceste date, fiecare coloana reprezinta un rezultat aflat mai sus
plt.bar('Survived', percentage_survived[1], label='Survived')
plt.bar('Not Survived', percentage_survived[0], label='Not Survived')

plt.bar('Class 1', percentage_class[1], label='Class 1')
plt.bar('Class 2', percentage_class[2], label='Class 2')
plt.bar('Class 3', percentage_class[3], label='Class 3')

plt.bar('Male', percentage_gender['male'], label='Male')
plt.bar('Female', percentage_gender['female'], label='Female')

plt.ylabel('Percentage')
# la final o sa compar acest grafic cu cel facut de colegul meu la Taskul 2
# el elimina outliere-le din acest set de date si vrem sa compara rezultatele
# pentru a fi mai usor de vizualizat vrem sa avem aceeasi scara pentru axa OY
plt.ylim(0, 70)
# salvam graficul drept poza
plt.savefig('Statistici_generale.png')
plt.close()

data_variables.close()