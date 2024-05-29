import pandas as pd
import variables as var
import matplotlib.pyplot as plt
import Task2C2

var.data = var.no_outliers_df

very_young_people = var.data[var.data['Age'] <= 20]

young_people = var.data[(var.data['Age'] > 20) & (var.data['Age'] <= 40)]

middle_aged = var.data[(var.data['Age'] > 40) & (var.data['Age'] <= 60)]

old_people = var.data[var.data['Age'] > 60]

plt.bar('Very young people', very_young_people.shape[0], label='Very young people')
plt.bar('Young people', young_people.shape[0], label='Young people')
plt.bar('Middle Aged', middle_aged.shape[0], label='Middle Aged')
plt.bar('Old People', old_people.shape[0], label='Old People')
plt.show()
percentage_survived = var.data['Survived'].value_counts() / (var.nr_lines - var.Survived_missing_count)* 100
percentage_class = var.data['Pclass'].value_counts() / (var.nr_lines - var.Pclass_missing_count)* 100
percentage_gender = var.data['Sex'].value_counts() / (var.nr_lines - var.Sex_missing_count) * 100

plt.bar('Survived', percentage_survived[1], label='Survived')
plt.bar('Not Survived', percentage_survived[0], label='Not Survived')

plt.bar('Class 1', percentage_class[1], label='Class 1')
plt.bar('Class 2', percentage_class[2], label='Class 2')
plt.bar('Class 3', percentage_class[3], label='Class 3')

plt.bar('Male', percentage_gender['male'], label='Male')
plt.bar('Female', percentage_gender['female'], label='Female')

plt.ylabel('Percentage')
plt.show()