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
	
	if type == "week":
	
		hours = week_time(day, df)
		
	elif type == "day":
	
		hours = day_time(day, df)
	
	print(hours)
	
	
	

def export_cv(defin):

	df = info_read(defin)
	df.to_csv('Rossell Clock ' + defin + '.csv', index=False)


hours_work("11/09/2021", "week")
