import pandas as pd
from openpyxl import load_workbook
from datetime import date
from datetime import timedelta
from io import StringIO
from hours_worked import *
import numpy as np
from connect import USB_interface
import time

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
def find_employee(UID, con):
#Try to make it  so that we are reading from the same location so that we can centerlize errors
	df = pd.read_csv('employee_id.csv', index_col=False)
	name_df = df["UID"]
	length = len(name_df)
#Adds people when they are not already in the system.
	try:
		#print(len(UID))
		for l in range(len(name_df)):
			plce = df.iloc[l]["UID"]
		
			if plce == UID:
	 			name = df.iloc[l]["Employee Name"]
		t_f = "T"
		return (t_f, name, UID)
	except:
#*****This is a strange spot to check the connectivity of teh device this should be move to somewhere else
		
		#t = con.connect()
		#print("Is it COnnected:" + str(t))
		#print(UID)
		if UID == None and con.isConnected() == True:
			#print("if")
			t_f = "Waiting on Data"
			name = "Waiting on Data"
			
		elif UID == None and con.isConnected() == False:
			#print("Elif")
			t_f = "In Disconnect State"
			name = "Please reconnect USB"
			
		else:
			t_f = "F"
			name = "You are not in the system. Please enter in computer!"

	return (t_f, name, UID)
	
def clock_in_out(UID):
	
	cur_date_time = datetime.now()
	
	cur_date_time = datetime.strftime(cur_date_time, "%m/%d/%Y, %H:%M:%S")
	
	df = pd.read_csv('employee_id.csv', index_col=False)
	df = df.fillna(0.0)
	name_df = df["UID"]
	
	for l in range(len(name_df)):
		plce = df.iloc[l]["UID"]
		
		if plce == UID:
			indexloc = l
			print(indexloc)
	count_col = df.shape[1] - 1
	
	
	print("This is count Col:" + str(count_col))

	
	i = 0
	count = 0		
	for i in range(count_col):
		indexlo = df.iloc[indexloc][i]
		print("THis is index" + str(indexlo))
		
		if str(indexlo) == "0.0" or str(indexlo) == "0":
			print(str(actualloc) + "if")
			count = count + 1
			actualloc = i - count + 1
		else:
			actualloc = i + 1
			print(actualloc)
	#count_col = count_col - 1
	if actualloc == count_col:
		print("wr")
		df["New " + str(actualloc + 1)] = np.nan
		actualloc = actualloc + 1
		df = df.fillna(0)	
	
	df.iat[indexloc, actualloc] = cur_date_time
	df.to_csv('employee_id.csv', index=False)	
	
		
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


