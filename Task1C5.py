import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

data_variables = open('data.txt', 'a+')

very_young_people = var.data[var.data['Age'] <= 20]

young_people = var.data[(var.data['Age'] > 20) & (var.data['Age'] <= 40)]

middle_aged = var.data[(var.data['Age'] > 40) & (var.data['Age'] <= 60)]

old_people = var.data[var.data['Age'] > 60]

print('Very young people:', very_young_people.shape[0], file=data_variables)
print('Young people:', young_people.shape[0], file=data_variables)
print('Middle aged:', middle_aged.shape[0], file=data_variables)
print('Old people:', old_people.shape[0], file=data_variables)

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


var.data.insert(var.data.shape[1], 'Age Index', age_index)

plt.bar('Very young people', very_young_people.shape[0], label='Very young people')
plt.bar('Young people', young_people.shape[0], label='Young people')
plt.bar('Middle Aged', middle_aged.shape[0], label='Middle Aged')
plt.bar('Old People', old_people.shape[0], label='Old People')
plt.show()

data_variables.close()