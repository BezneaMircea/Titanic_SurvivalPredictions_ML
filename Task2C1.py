import variables as var
import numpy as np
import Task1C1
import pandas as pd
from utils import destroy_outliers


destroy_outliers(var.data, 'Age')
destroy_outliers(var.no_outliers_df, 'Parch')
destroy_outliers(var.no_outliers_df, 'Fare')

var.no_outliers_df.to_csv("No_outliers_df.csv")
