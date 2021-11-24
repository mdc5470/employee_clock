import serial 
import pandas as pd
from backend_work import *

def init_serial():
	COM = 1
	global ser
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = COM - 1
	
	ser.timeout = 10
	ser.open()
	
	if ser.isOpen():
		print("OPen")
		

#Use the function to find if the UID is already used by another person.
 

def det_in_out():
	
	#Input of the Serial String in DF
	ser_in = pd.DataFrame(init_serial())
	
	#Split the string of the input of the serial.
	ser_in = ser_in.str.split(" ", n = 1, expand = True)
	
	#Remove the first column of the string because this is telling which device it came from.
	
	
	
	#Read the data from the csv file 
	UID_col = info_read("UID")
	e_name = info_read("Employee Name")
	
	#Combined Employee Name and UID numbers DataFrame
	#name_UID = pd.concat(UID_col, e_name)
	
	print(UID_col)
	print(e_name)
	
	#print(name_UID)
	
	#Parse the Serial 
	
	
	#Determine if this person is already clocked in?
	
	