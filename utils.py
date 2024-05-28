import numpy as np
import variables as var

def destroy_outliers(df, coloana):
	percentile_Q1 = df[coloana].quantile(0.25)
	percentile_Q2 = df[coloana].quantile(0.50)
	percentile_Q3 = df[coloana].quantile(0.75)
	IQR = percentile_Q3 - percentile_Q1
	inf_lim = percentile_Q1 - 1.5 * IQR
	sup_lim = percentile_Q3 + 1.5 * IQR

	no_outliers = df[(df[coloana] >= inf_lim) & (df[coloana] <= sup_lim)]
	
	var.no_outliers_df = no_outliers