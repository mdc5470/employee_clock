import serial 
import time
import pandas as pd
from backend_work import *
from pyfirmata import Arduino, util, STRING_DATA

board = Arduino("/dev/ttyUSB0")

def init_serial():
	i = 0
	COM = 1
	global ser
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = "/dev/ttyUSB0"
	
	ser.timeout = 10
	ser.open()

	return(ser)
	
			
	
	#if ser.isOpen()
	
def send_msg(text):
	if text:
		board.send_sysex( STRING_DATA, util.str_to_two_byte_iter(text))
	
def read_data():
	
	ser = init_serial()
	RFID_Data = ser.readline()
	if RFID_Data:
		RFID_Date = RFID_Data.decode()
		RFID_Date = RFID_Data.strip()
		RFID_Data = str(RFID_Data);
		return(RFID_Data)
	
def write_data():

	ser = init_serial()
	e_name = "Michael"
	ser.write(bytes(e_name, 'utf-8'))
	time.sleep(0.05)
	

while(True):		
	data = write_data()
	print(data)
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

