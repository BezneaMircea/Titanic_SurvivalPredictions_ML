import csv
from utils import det_list_type
from utils import are_there_duplicates
import variables

# PassengerId = []
# Survived = []
# Pclass = []
# Name = []
# Sex = []
# Age = []
# SibSp = []
# Parch = []
# Ticket = []
# Fare = []
# Cabin = []
# Embarked = []
with open("train.csv", 'r') as file:
	reader = csv.reader(file, delimiter=",")
	header = next(reader)
	variables.column_nr = len(header)
	variables.nr_lines = 0
	# Avem nr de coloane
	for row in reader:
		variables.PassengerId.append(row[0])
		variables.Survived.append(row[1])
		variables.Pclass.append(row[2])
		variables.Name.append(row[3])
		variables.Sex.append(row[4])
		variables.Age.append(row[5])
		variables.SibSp.append(row[6])
		variables.Parch.append(row[7])
		variables.Ticket.append(row[8])
		variables.Fare.append(row[9])
		variables.Cabin.append(row[10])
		variables.Embarked.append(row[11])
		variables.nr_lines += 1
	# Avem numarul de linii

	variables.PassengerId_missing_count = len([item for item in variables.PassengerId if item == ''])
	variables.Survived_missing_count = len([item for item in variables.Survived if item == ''])
	variables.Pclass_missing_count = len([item for item in variables.Pclass if item == ''])
	variables.Name_missing_count = len([item for item in variables.Name if item == ''])
	variables.Sex_missing_count = len([item for item in variables.Sex if item == ''])
	variables.Age_missing_count = len([item for item in variables.Age if item == ''])
	variables.SibSp_missing_count = len([item for item in variables.SibSp if item == ''])
	variables.Parch_missing_count = len([item for item in variables.Parch if item == ''])
	variables.Ticket_missing_count = len([item for item in variables.Ticket if item == ''])
	variables.Fare_missing_count = len([item for item in variables.Fare if item == ''])
	variables.Cabin_missing_count = len([item for item in variables.Cabin if item == ''])
	variables.Embarked_missing_count = len([item for item in variables.Embarked if item == ''])
	# Aflam cate elemente lipsesc din fiecare coloana

	variables.PassengerId_type = det_list_type(variables.PassengerId)
	variables.Survived_type = det_list_type(variables.Survived)
	variables.Pclass_type = det_list_type(variables.Pclass)
	variables.Name_type = det_list_type(variables.Name)
	variables.Sex_type = det_list_type(variables.Sex)
	variables.Age_type = det_list_type(variables.Age)
	variables.SibSp_type = det_list_type(variables.SibSp)
	variables.Parch_type = det_list_type(variables.Parch)
	variables.Ticket_type = det_list_type(variables.Ticket)
	variables.Fare_type = det_list_type(variables.Fare)
	variables.Cabin_type = det_list_type(variables.Cabin)
	variables.Embarked_type = det_list_type(variables.Embarked)
	# Avem tipul listelor
	
	# Deoarece Id-ul pasagerului este unic, este suficient pentru a verifica
	# daca exista duplicate sa vedem daca exista duplicate in lista id-urilor
	variables.found_duplicates = are_there_duplicates(variables.PassengerId)
	