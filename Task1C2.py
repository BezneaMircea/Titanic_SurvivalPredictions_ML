import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt

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
plt.ylim(0, 70)
plt.savefig('General_statistics.png')