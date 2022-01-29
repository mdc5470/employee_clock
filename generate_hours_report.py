from hours_worked import *
import pandas as pd
import numpy as np

def report_gen():

	df = pd.read_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv')
	name_df = df["UID"]
	row_count = df.shape[0]
	print(row_count)
	col_count = df.shape[1]
	print(col_count)
	
	#df = df.iloc[1]
	print(df)
	count = 0
	
#Make a for loop that cycles through the columns at the row of the employee to create a dataframe of the employees times. 
	
	for column_row in range(row_count):
		print("Colen" + str(column_row))
		#name = []
		name = df.loc[column_row]
		print(name)
		#name = pd.DataFrame(name)
		#print(name.columns)
		name = pd.DataFrame(name, columns = ["dd", str(column_row)])
		print(name.columns)
		print(name)
		#print(name_df)
		#name = name.dropna()
		print(count)
		name = name.astype(str)
		List = pd.DataFrame(name[df.columns.get_iloc(0)].str.split(', ', 1).tolist(), columns = ['Date', 'Time'])
		print(List)
		count=count+1
report_gen()		
