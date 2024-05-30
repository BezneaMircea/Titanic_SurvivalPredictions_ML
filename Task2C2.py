import pandas as pd
import variables as var
import Task2C1
from utils import destroy_outliers_with_z

destroy_outliers_with_z(var.no_outliers_df, "Age")
# Eliminam outlierele de la Age
destroy_outliers_with_z(var.no_outliers_df_and_Z, "Parch")
# Eliminam outlierele de la Parch
destroy_outliers_with_z(var.no_outliers_df_and_Z, "Fare")
# Eliminam outlierele de la Fare

var.no_outliers_df_and_Z.to_csv("No_outliers_df_and_Z.csv")
