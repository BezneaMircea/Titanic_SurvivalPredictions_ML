import pandas as pd
import variables as var
import Task1C1
import matplotlib.pyplot as plt
import numpy as np

# extrag din nume partea din el care contine titlul unui om
# pentru asta stim ca inainte de titlu avem o virgula si un spatiu
# iar dupa avem un punct
# ce ramane intre, reprezinta titlul persoanei
title = var.data['Name'].str.extract(r', ([^\.]+).')
# extrag titlurile unice si de cate ori apar
titles = title[0].value_counts()

# afisez distributia titlurilor
# figsize e modificata deoarece am foarte multe titluri si am mai lungit poza
# pentru a incapea si a fi lizibile pe axa OX
plt.figure(figsize=(15, 10))
plt.bar(titles.index, titles.values)
plt.savefig("Distributia_titlurilor.png")
plt.close()

