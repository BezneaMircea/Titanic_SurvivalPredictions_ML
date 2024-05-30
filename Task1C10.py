import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# tinem minte daca o persoana este singura sau nu la bord si daca a murit sau a supravietuit
alone_survived = []
alone_not_survived = []
not_alone_survived = []
not_alone_not_survived = []

# pentru fiecare persoana din dataset, verificam daca are rude la bord
for line in var.data.iterrows():
	if var.data['SibSp'][line[0]] == 0 and var.data['Parch'][line[0]] == 0:
		# daca nu are rude la bord, verificam daca a supravietuit sau nu
		if var.data['Survived'][line[0]] == 1:
			# adaugam persoana in lista corespunzatoare
			alone_survived.append(var.data.loc[line[0]])
		# daca a murit si era singur la bord
		else:
			alone_not_survived.append(var.data.loc[line[0]])
	# daca are rude la bord
	else:
		# verificam daca a supravietuit sau nu
		if var.data['Survived'][line[0]] == 1:
			not_alone_survived.append(var.data.loc[line[0]])
		else:
			not_alone_not_survived.append(var.data.loc[line[0]])

# transformam listele in DataFrame-uri pentru a putea face operatii pe ele
alone_survived_df = pd.DataFrame(alone_survived)
alone_not_survived_df = pd.DataFrame(alone_not_survived)
not_alone_survived_df = pd.DataFrame(not_alone_survived)
not_alone_not_survived_df = pd.DataFrame(not_alone_not_survived)

# afisam numarul de persoane in functie de numarul de rude la bord si daca au supravietuit sau nu
plt.bar(['Alone Survived', 'Alone Not Survived', 'Not Alone Survived', 'Not Alone Not Survived'], [alone_survived_df.shape[0], alone_not_survived_df.shape[0], not_alone_survived_df.shape[0], not_alone_not_survived_df.shape[0]])
plt.savefig("Morti_per_rude.png")
plt.close()

# extrag primele 100 de date pentru a face un grafic mai usor de citit
data_subset = var.data.head(100)

# facem un grafic care determina relatia dintre clasa in care a calatorit o persoana, pretul biletului si daca a supravietuit sau nu
sns.catplot(data=data_subset, x="Pclass", y="Fare", hue="Survived", kind="swarm", height=4, aspect=2.7)
plt.savefig("Grafic_dependenta_fare_class_survive.png")
plt.close()