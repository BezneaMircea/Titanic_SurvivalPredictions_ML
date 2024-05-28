import pandas as pd
import variables as var
import Task2C1
from utils import destroy_outliers_with_z

destroy_outliers_with_z(var.no_outliers_df, "Age")
destroy_outliers_with_z(var.no_outliers_df_and_Z, "Parch")
destroy_outliers_with_z(var.no_outliers_df_and_Z, "SibSp")

print(var.no_outliers_df_and_Z)
