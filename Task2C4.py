import pandas as pd
import numpy as np
import variables as var

data = pd.read_csv('No_outliers_df_and_Z.csv')
var.no_outliers_df_and_Z = data

training_parcentage = round(len(data) * 0.8)
testing_parcentage = len(data) - training_parcentage

var.training_set = data.head(training_parcentage)
var.testing_set = data.tail(testing_parcentage)
# we got the training and the testing sets

supravietuitori = var.training_set[var.training_set['Survived'] == 1]
morti = var.training_set[var.training_set['Survived'] == 0]


for coloana in var.training_set.columns:
    if (var.training_set[coloana].isna().sum() > 0):
        for row in var.training_set.iterrows():
            if pd.isna(row[1][coloana]):
                if (row[1]['Survived'] == 1):
                    if (var.training_set[coloana].dtypes != 'object'):
                        row[1][coloana] = int(round(supravietuitori[coloana].mean()))
                    elif (var.training_set[coloana].nunique() >= 2 and var.training_set[coloana].nunique() <= 5):
                        row[1][coloana] = supravietuitori[coloana].mode()[0]
                else:
                    if (var.training_set[coloana].dtypes != 'object'):
                        row[1][coloana] = int(round(morti[coloana].mean()))
                    elif (var.training_set[coloana].nunique() >= 2 and var.training_set[coloana].nunique() <= 5):
                        row[1][coloana] = morti[coloana].mode()[0]
                var.training_set.loc[row[0], coloana] = row[1][coloana]


var.training_set.loc[:,'Age'] = var.training_set['Age'] / var.training_set['Age'].max()
var.training_set.loc[:,'Fare'] = var.training_set['Fare'] / var.training_set['Fare'].max()
var.training_set.loc[:,'SibSp'] = var.training_set['SibSp'] / var.training_set['SibSp'].max()

print(var.training_set)