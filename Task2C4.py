import pandas as pd
import numpy as np
import variables as var
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('No_outliers_df_and_Z.csv')

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


var.no_outliers_df_and_Z.loc[:,'Age'] = var.no_outliers_df_and_Z['Age'] / var.no_outliers_df_and_Z['Age'].max()
var.no_outliers_df_and_Z.loc[:,'Fare'] = var.no_outliers_df_and_Z['Fare'] / var.no_outliers_df_and_Z['Fare'].max()
var.no_outliers_df_and_Z.loc[:,'SibSp'] = var.no_outliers_df_and_Z['SibSp'] / var.no_outliers_df_and_Z['SibSp'].max()

var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Sex'] == 'male', 'Sex'] = 1
var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Sex'] == 'female', 'Sex'] = 2

var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Embarked'] == 'S', 'Embarked'] = 1
var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Embarked'] == 'C', 'Embarked'] = 2
var.no_outliers_df_and_Z.loc[var.no_outliers_df_and_Z['Embarked'] == 'Q', 'Embarked'] = 3

#print(var.no_outliers_df_and_Z['Parch'])

training_parcentage = round(len(data) * 0.8)
testing_parcentage = len(data) - training_parcentage

var.training_set = data.head(training_parcentage)
var.testing_set = data.tail(testing_parcentage)
# we got the training and the testing sets

x_training = var.training_set
y_training = var.training_set['Survived']
x_testing = var.testing_set
y_to_check = var.testing_set['Survived']

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


clf = DecisionTreeClassifier()
clf = clf.fit(x_training, y_training)

predictions = clf.predict(x_testing)

print(accuracy_score(y_to_check, predictions))

# print(var.training_set)

# Example usage for classification
