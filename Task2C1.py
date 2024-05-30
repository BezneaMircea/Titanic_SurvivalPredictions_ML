import variables as var
import numpy as np
import Task1C1
import pandas as pd
from utils import destroy_outliers


destroy_outliers(var.data, 'Age')
# Eliminam outlierele de la Age
destroy_outliers(var.no_outliers_df, 'Parch')
# Eliminam outlierele de la Parch
destroy_outliers(var.no_outliers_df, 'Fare')
# Eliminam outlierele de la Fare

var.no_outliers_df.to_csv("No_outliers_df.csv")
