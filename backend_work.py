import pandas as pd
from openpyxl import load_workbook
from datetime import date
from datetime import timedelta
from io import StringIO
from hours_worked import *


#All functions of the program work.
#Needs checks and balnces and errors


#Export Data to Pandas DF
def read_df():
	df = pd.read_csv('employee_id.csv')
	df = df.dropna()
	return(df)

def info_read(col):
	df = read_df()
	df_info = df[col]
	return(str(df_info))

#Function should be good to go
def find_employee(UID):
	df = pd.read_csv('employee_id.csv', index_col=False)
	name_df = df["UID"]
	length = len(name_df)
#Adds people when they are not already in the system.
	try:
		for l in range(len(name_df)):
			plce = df.iloc[l]["UID"]
		
			if plce == UID:
	 			name = df.iloc[l]["Employee Name"]
		t_f = "T"
		return (t_f, name, UID)
	except:
		t_f = "F"
		name = "You are not in the system. Please enter in computer!"

	return (t_f, name, UID)

def add(e_name, UID):
	
	df = pd.read_csv('employee_id.csv')
	indice = len(df) + 1
	dates = date.today()
	print(indice)
	print(df)
	df2 = pd.DataFrame([[indice, e_name, dates, UID]], columns=('Employment Count', 'Employee Name', 'Employment Date', 'UID'))
	df = df.append(df2)
	print(df)
	df.to_csv('employee_id.csv', index=False)
	
	return(e_name + " UID: " + UID)
	
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
