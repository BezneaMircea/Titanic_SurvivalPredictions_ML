import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

data_variables = open('data.txt', 'a+')

children = var.data[var.data['Age'] < 18]
adults = var.data[var.data['Age'] >= 18]

print('Children percentage:', round(children.shape[0] / var.data.shape[0] * 100, 2), file=data_variables)

survived_children = children[children['Survived'] == 1]
survived_adults = adults[adults['Survived'] == 1]

plt.bar('Children', round(survived_children.shape[0] / children.shape[0] * 100, 2))
plt.bar('Adults', round(survived_adults.shape[0] / adults.shape[0] * 100, 2))
plt.ylabel('Percentage survived')
plt.savefig("supravietuire_copii_adulti.png")

data_variables.close()