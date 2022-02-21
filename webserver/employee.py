import pandas as pd
import time
from datetime import datetime
import sys
from IPython.display import HTML
from mod_html_temp import *

def mod_clock_in(e_name, UID, ):
	
	df = pd.read_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv')
	indice = len(df) + 1
	dates = datetime.today()
	print(indice)
	print(df)
	df2 = pd.DataFrame([[indice, e_name, dates, UID]], columns=('Employment Count', 'Employee Name', 'Employment Date', 'UID'))
	df = df.append(df2)
	print(df)
	df.to_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv', index=False)
	
	return(e_name + " UID: " + UID)
	
def mod_clock_out(e_name, UID, ):
	
	df = pd.read_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv')
	indice = len(df) + 1
	dates = datetime.today()
	print(indice)
	print(df)
	df2 = pd.DataFrame([[indice, e_name, dates, UID]], columns=('Employment Count', 'Employee Name', 'Employment Date', 'UID'))
	df = df.append(df2)
	print(df)
	df.to_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv', index=False)
	
	return(e_name + " UID: " + UID)
	
def look_up_func(e_name, UID):

	df = pd.read_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv')
	name_df = df["UID"]
	length = len(name_df)
	
	for l in range(len(name_df)):
		plce = df.iloc[l]["UID"]
	
		if plce == UID:
			indice = l
			print (plce + "   " + str(l))
			
	if df.iloc[indice]["Employee Name"] == e_name:
		print("Matches")
		
	else:
		print("Fail")
	
	employ_df = df.iloc[[indice]]
	
	filter_employ_df = employ_df.dropna(axis='columns')
	
	modify_html(filter_employ_df)
	
		
