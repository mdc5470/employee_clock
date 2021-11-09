import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
from datetime import timedelta
from io import StringIO

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
	
def week_time(day):

	df = read_df()
	
	for j in range(3):
		
		day1_time_in = df[day + " IN"]
		day1_time_out = df[day + " OUT"]
		duration_time = []
	
		for i in range(4):
			time_in = datetime.strptime(day1_time_in[i], '%H:%M').time()
			time_out = datetime.strptime(day1_time_out[i], '%H:%M').time()
		
			t1 = timedelta(hours=time_in.hour, minutes=time_in.minute, seconds=time_in.second)
			t2 = timedelta(hours=time_out.hour, minutes=time_out.minute, seconds=time_out.second)

			duration = str(t2-t1)
			duration_time.append(duration)
	
		daytime = pd.DataFrame(duration_time, columns=['Work Time'])
		print(daytime)	
		day_start = datetime.strptime(day, '%m/%d/%Y')
		day = day_start + timedelta(days=1)
		day = day.strftime('%m/%d/%Y')
		
		
def day_time(day):

	df = read_df()
	day_time_in = df[day + " IN"]
	day_time_out = df[day + " OUT"]

def export_cv(defin):

	df = info_read(defin)
	df.to_csv('Rossell Clock ' + defin + '.csv', index=False)


week_time("11/09/2021")
