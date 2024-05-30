import pandas as pd
import numpy as np
import variables as var
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss
from sklearn.metrics import confusion_matrix

data = pd.read_csv('No_outliers_df_and_Z.csv')
# Luam dataframeul fara outliere

var.no_outliers_df_and_Z = data

supravietuitori = var.no_outliers_df_and_Z[var.no_outliers_df_and_Z['Survived'] == 1]
morti = var.no_outliers_df_and_Z[var.no_outliers_df_and_Z['Survived'] == 0]

for coloana in var.no_outliers_df_and_Z.columns:
    if (var.no_outliers_df_and_Z[coloana].isna().sum() > 0):
        for row in var.no_outliers_df_and_Z.iterrows():
            if pd.isna(row[1][coloana]):
                if (row[1]['Survived'] == 1):
                    if (var.no_outliers_df_and_Z[coloana].dtypes != 'object'):
                        row[1][coloana] = int(round(supravietuitori[coloana].mean()))
                    elif (var.no_outliers_df_and_Z[coloana].nunique() >= 2 and var.no_outliers_df_and_Z[coloana].nunique() <= 5):
                        row[1][coloana] = supravietuitori[coloana].mode()[0]
                else:
                    if (var.no_outliers_df_and_Z[coloana].dtypes != 'object'):
                        row[1][coloana] = int(round(morti[coloana].mean()))
                    elif (var.no_outliers_df_and_Z[coloana].nunique() >= 2 and var.no_outliers_df_and_Z[coloana].nunique() <= 5):
                        row[1][coloana] = morti[coloana].mode()[0]
                var.no_outliers_df_and_Z.loc[row[0], coloana] = row[1][coloana]
# Inlocuim valorile lipsa cu valorea medie de pe coloana respectiva (in cazul inturilor)
# respectiv cu cea frecventa valore in cazul coloanelor categoriale ("Sex, Class, etc")

var.no_outliers_df_and_Z.loc[:,'Age'] = var.no_outliers_df_and_Z['Age'] / var.no_outliers_df_and_Z['Age'].max()
var.no_outliers_df_and_Z.loc[:,'Fare'] = var.no_outliers_df_and_Z['Fare'] / var.no_outliers_df_and_Z['Fare'].max()
var.no_outliers_df_and_Z.loc[:,'SibSp'] = var.no_outliers_df_and_Z['SibSp'] / var.no_outliers_df_and_Z['SibSp'].max()

var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Sex'] == 'male', 'Sex'] = 1
var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Sex'] == 'female', 'Sex'] = 2
# Codificam prin numere Sexul, 1 = male, 2 = female

var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Embarked'] == 'S', 'Embarked'] = 1
var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Embarked'] == 'C', 'Embarked'] = 2
var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Embarked'] == 'Q', 'Embarked'] = 3
# Similar ca mai sus codificam prin numere Embarked. S = 1, C = 2, Q = 3


var.no_outliers_df_and_Z.to_csv("Final_data_for_training_and_testing.csv")
# Salvam varianta finala pentru dataset obtinuta pentru a antrena modelul

training_parcentage = round(len(data) * 0.8)
testing_parcentage = len(data) - training_parcentage

var.training_set = data.head(training_parcentage)
var.testing_set = data.tail(testing_parcentage)
# Impartim setul in setul de training 80% si setul de test 20%

x_training = var.training_set
y_training = var.training_set['Survived']
x_testing = var.testing_set
y_to_check = var.testing_set['Survived']
# Facem rost de coloanele de raspunsuri
# Vrem sa facem predictii legate de supravietuire
del x_training['PassengerId']
del x_training['Survived']
del x_training['Name']
del x_training['Cabin']
del x_training['Ticket']

del x_testing['PassengerId']
del x_testing['Survived']
del x_testing['Name']
del x_testing['Cabin']
del x_testing['Ticket']
# Eliminam coloanele inutile

clf = DecisionTreeClassifier()
clf = clf.fit(x_training, y_training)
# Antrenam modelul

predictions = clf.predict(x_testing)
# Facem predictia

accuracy = accuracy_score(y_to_check, predictions)
loss = log_loss(y_to_check, predictions)
# Aflam parametrii de acuratete si loss. Am observat ca modelul nostru
# are o acuratete de aproximativ 80%

tn, fp, fn, tp = confusion_matrix(y_to_check, predictions).ravel()
# Aflam negativele adevarate, fals pozitivele, fals negativele si pozitivele adevarate

y = np.array([tn, fp, fn, tp])
labels = ['Negative adevarate', 'Pozitive false', 'Negative false', 'Pozitive adevarate']
plt.pie(y, labels = labels)
plt.savefig('Piechart_tn_fp_fn_tp.png')
# Cream si salvam un piechart cu acestea

print(accuracy)
print(loss)
# Afisam parametrii de acuratete ai modelului
