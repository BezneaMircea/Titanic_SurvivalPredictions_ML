# CopyRight(c):
# Codul acesta este preluat de la colegul meu de proiect
# dupa cum se cere in cerinta si foarte putin modificat de mine

import pandas as pd
import variables as var
import matplotlib.pyplot as plt
import Task2C2
import numpy as np
import seaborn as sns

var.data = pd.read_csv('No_outliers_df_and_Z.csv')

Survived_missing_count = var.data["Survived"].isna().sum()
Pclass_missing_count = var.data["Pclass"].isna().sum()
Sex_missing_count = var.data["Sex"].isna().sum()

percentage_survived = var.data['Survived'].value_counts() / (var.data.shape[0] - Survived_missing_count)* 100
percentage_class = var.data['Pclass'].value_counts() / (var.data.shape[0] - Pclass_missing_count)* 100
percentage_gender = var.data['Sex'].value_counts() / (var.data.shape[0] - Sex_missing_count) * 100

plt.bar('Survived', percentage_survived[1], label='Survived')
plt.bar('Not Survived', percentage_survived[0], label='Not Survived')

plt.bar('Class 1', percentage_class[1], label='Class 1')
plt.bar('Class 2', percentage_class[2], label='Class 2')
plt.bar('Class 3', percentage_class[3], label='Class 3')

plt.bar('Male', percentage_gender['male'], label='Male')
plt.bar('Female', percentage_gender['female'], label='Female')

plt.ylabel('Percentage')

plt.ylim(0, 70)

plt.savefig('General_statistics_without_outliers.png')

# Grafic nou
alone_survived = []
alone_not_survived = []

for line in var.data.iterrows():
    if var.data['SibSp'][line[0]] == 0 and var.data['Parch'][line[0]] == 0:
        if var.data['Survived'][line[0]] == 1:
            alone_survived.append(var.data.loc[line[0]])
        else:
            alone_not_survived.append(var.data.loc[line[0]])

alone_survived_df = pd.DataFrame(alone_survived)
alone_not_survived_df = pd.DataFrame(alone_not_survived)

data_subset = var.data.head(100)

sns.catplot(data=data_subset, x="Pclass", y="Fare", hue="Survived", kind="swarm", height=4, aspect=4)
plt.savefig("swarmplot_without_outliers.png")


#Grafic nou
very_young_people = var.data[var.data['Age'] <= 20]
young_people = var.data[(var.data['Age'] > 20) & (var.data['Age'] <= 40)]
middle_aged = var.data[(var.data['Age'] > 40) & (var.data['Age'] <= 60)]
old_people = var.data[var.data['Age'] > 60]

survived_very_young_people = very_young_people[very_young_people['Survived'] == 1]
male_survived_very_young_people = survived_very_young_people[survived_very_young_people['Sex'] == 'male']

survived_young_people = young_people[young_people['Survived'] == 1]
male_survived_young_people = survived_young_people[survived_young_people['Sex'] == 'male']

survived_middle_aged = middle_aged[middle_aged['Survived'] == 1]
male_survived_middle_aged = survived_middle_aged[survived_middle_aged['Sex'] == 'male']

survived_old_people = old_people[old_people['Survived'] == 1]
male_survived_old_people = survived_old_people[survived_old_people['Sex'] == 'male']

plt.figure(figsize=[15, 15])

plt.bar('Very young male survived', male_survived_very_young_people.shape[0], label='Very young male survived')
plt.bar('Young male survived', male_survived_young_people.shape[0], label='Young male survived')
plt.bar('Middle Aged male survived', male_survived_middle_aged.shape[0], label='Middle Aged male survived')
plt.bar('Old male survived', male_survived_old_people.shape[0], label='Old male survived')

plt.savefig('Survivers_by_age_no_outliers.png')