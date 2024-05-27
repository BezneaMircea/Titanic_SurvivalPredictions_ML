import csv
from utils import det_list_type
from utils import are_there_duplicates

PassengerId = []
Survived = []
Pclass = []
Name = []
Sex = []
Age = []
SibSp = []
Parch = []
Ticket = []
Fare = []
Cabin = []
Embarked = []
with open("train.csv", 'r') as file:
	reader = csv.reader(file, delimiter=",")
	header = next(reader)
	column_nr = len(header)
	nr_lines = 0
	# Avem nr de coloane
	for row in reader:
		PassengerId.append(row[0])
		Survived.append(row[1])
		Pclass.append(row[2])
		Name.append(row[3])
		Sex.append(row[4])
		Age.append(row[5])
		SibSp.append(row[6])
		Parch.append(row[7])
		Ticket.append(row[8])
		Fare.append(row[9])
		Cabin.append(row[10])
		Embarked.append(row[11])
		nr_lines += 1
	# Avem numarul de linii

	PassengerId_missing_count = len([item for item in PassengerId if item == ''])
	Survived_missing_count = len([item for item in Survived if item == ''])
	Pclass_missing_count = len([item for item in Pclass if item == ''])
	Name_missing_count = len([item for item in Name if item == ''])
	Sex_missing_count = len([item for item in Sex if item == ''])
	Age_missing_count = len([item for item in Age if item == ''])
	SibSp_missing_count = len([item for item in SibSp if item == ''])
	Parch_missing_count = len([item for item in Parch if item == ''])
	Ticket_missing_count = len([item for item in Ticket if item == ''])
	Fare_missing_count = len([item for item in Fare if item == ''])
	Cabin_missing_count = len([item for item in Cabin if item == ''])
	Embarked_missing_count = len([item for item in Embarked if item == ''])
	# Aflam cate elemente lipsesc din fiecare coloana

	PassengerId_type = det_list_type(PassengerId)
	Survived_type = det_list_type(Survived)
	Pclass_type = det_list_type(Pclass)
	Name_type = det_list_type(Name)
	Sex_type = det_list_type(Sex)
	Age_type = det_list_type(Age)
	SibSp_type = det_list_type(SibSp)
	Parch_type = det_list_type(Parch)
	Ticket_type = det_list_type(Ticket)
	Fare_type = det_list_type(Fare)
	Cabin_type = det_list_type(Cabin)
	Embarked_type = det_list_type(Embarked)
	# Avem tipul listelor
	
	# Deoarece Id-ul pasagerului este unic, este suficient pentru a verifica
	# daca exista duplicate sa vedem daca exista duplicate in lista id-urilor
	found_duplicates = are_there_duplicates(PassengerId)