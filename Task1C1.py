import pandas as pd
import variables as var

data_variables = open('data.txt', 'a+')

# Citirea datelor
data = pd.read_csv('train.csv')

var.data = data

var.nr_lines = data.shape[0]
var.column_nr = data.shape[1]

var.PassengerId_type = data['PassengerId'].dtypes
var.Survived_type = data['Survived'].dtypes
var.Pclass_type = data['Pclass'].dtypes
var.Name_type = data['Name'].dtypes
var.Sex_type = data['Sex'].dtypes
var.Age_type = data['Age'].dtypes
var.SibSp_type = data['SibSp'].dtypes
var.Parch_type = data['Parch'].dtypes
var.Ticket_type = data['Ticket'].dtypes
var.Fare_type = data['Fare'].dtypes
var.Cabin_type = data['Cabin'].dtypes
var.Embarked_type = data['Embarked'].dtypes

var.PassengerId_missing_count = data['PassengerId'].isna().sum()
var.Survived_missing_count = data['Survived'].isna().sum()
var.Pclass_missing_count = data['Pclass'].isna().sum()
var.Name_missing_count = data['Name'].isna().sum()
var.Sex_missing_count = data['Sex'].isna().sum()
var.Age_missing_count = data['Age'].isna().sum()
var.SibSp_missing_count = data['SibSp'].isna().sum()
var.Parch_missing_count = data['Parch'].isna().sum()
var.Ticket_missing_count = data['Ticket'].isna().sum()
var.Fare_missing_count = data['Fare'].isna().sum()
var.Cabin_missing_count = data['Cabin'].isna().sum()
var.Embarked_missing_count = data['Embarked'].isna().sum()

var.found_duplicates = data.duplicated().sum()

data_variables.close()