import pandas as pd
import time
from datetime import datetime

def add_employ(e_name, UID):
	
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
	
def delete(e_name):

	df = pd.read_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv')
	df = df[df["Employee Name"] != e_name]
	print(df)
	df.to_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv', index=False)
