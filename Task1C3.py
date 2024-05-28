import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

numeric_data = var.data.select_dtypes(include=np.number)

for coloana in numeric_data.columns:
	plt.hist(numeric_data[coloana])
	plt.xlabel(coloana)
	plt.ylabel('Numar exemple')
	plt.show()