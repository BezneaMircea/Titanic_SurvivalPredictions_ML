import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

alone_survived = []
alone_not_survived = []
not_alone_survived = []
not_alone_not_survived = []

for line in var.data.iterrows():
	if var.data['SibSp'][line[0]] == 0 and var.data['Parch'][line[0]] == 0:
		if var.data['Survived'][line[0]] == 1:
			alone_survived.append(var.data.loc[line[0]])
		else:
			alone_not_survived.append(var.data.loc[line[0]])
	else:
		if var.data['Survived'][line[0]] == 1:
			not_alone_survived.append(var.data.loc[line[0]])
		else:
			not_alone_not_survived.append(var.data.loc[line[0]])

alone_survived_df = pd.DataFrame(alone_survived)
alone_not_survived_df = pd.DataFrame(alone_not_survived)
not_alone_survived_df = pd.DataFrame(not_alone_survived)
not_alone_not_survived_df = pd.DataFrame(not_alone_not_survived)

data_subset = var.data.head(100)

sns.catplot(data=data_subset, x="Pclass", y="Fare", hue="Survived", kind="swarm", height=4, aspect=2.7)
plt.savefig("swarmplot.png")