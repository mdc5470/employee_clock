import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
from datetime import timedelta
from io import StringIO
from hours_worked import *

#All functions of the program work.
#Needs checks and balnces and errors


#Export Data to Pandas DF
def read_df():
	df = pd.read_csv('employee_id.csv', index_col=False)
	df = df.dropna()
	return(df)

def info_read(col):
	df = read_df()
	df_info = df[col]
	return(df_info)

def add(e_name, UID):
	
	df = read_df()
	indice = len(df) + 1
	date = datetime.date.today()
	print(indice)
	print(df)
	df2 = pd.DataFrame([[indice, e_name, date, UID]], columns=('Employment Count', 'Employee Name', 'Employment Date', 'UID'))
	df = df.append(df2)
	print(df)
	df.to_csv('employee_id.csv', index=False)
	
def delete(e_name):

	df = read_df()
	df = df[df["Employee Name"] != e_name]
	print(df)
	df.to_csv('employee_id.csv', index=False)
	
def hours_work(day, type):
	
	df = read_df()
	num_employ = len(df)
	
	if type == "week":
	
		num_days = 7
		hours = day_calc(day, df, num_days, num_employ)
		
	elif type == "day":
	
		num_days = 1
		hours = day_calc(day, df, num_days, num_employ)
	
	export_cv(hours, type)
	
	return(hours)
	
	
	

def export_cv(df, name):

	df.to_csv('Rossell Clock ' + name + '.csv', index=False)

hours_work("11/09/2021", "day")