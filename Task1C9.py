import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

title = var.data['Name'].str.extract(r', ([^\.]+).')
titles = title[0].value_counts()
	
plt.figure(figsize=(15, 10))
plt.bar(titles.index, titles.values)
plt.savefig("distributia_titlurilor_pe_sex.png")

