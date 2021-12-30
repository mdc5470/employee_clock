import serial 
import time
import pandas as pd
from backend_work import *
from pyfirmata import Arduino, util, STRING_DATA
import serial.tools.list_ports as list_ports

device_signature = '1a86:7523'

def find_serial_device():
    """Return the device path based on vender & product ID.
    
    The device is something like (like COM4, /dev/ttyUSB0 or /dev/cu.usbserial-1430)
    """
    candidates = list(list_ports.grep(device_signature))
    if not candidates:
        raise ValueError(f'No device with signature {device_signature} found')
    if len(candidates) > 1:
        raise ValueError(f'More than one device with signature {device_signature} found')
    return candidates[0].device


board = Arduino(find_serial_device())

def init_serial():

	#i = 0
	COM = 1
	global ser
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = find_serial_device()
	
	ser.timeout = None
	ser.open()

	return(ser)
	
			
	
	#if ser.isOpen()
	
#Writes data to arduino through the serial port	
def write_read(x):

    arduino = serial.Serial(port=find_serial_device(), baudrate=9600, timeout=.1)
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data
	
def read_data():
	
	ser = init_serial()
	#ser.clear()
	RFID_Data = ser.readline()
	if RFID_Data:
		RFID_Data = RFID_Data.decode()
		RFID_Data = RFID_Data.strip()
		RFID_Data = str(RFID_Data)
		return(RFID_Data)

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
	
	
	#Determine if this person is already clocked in?\
