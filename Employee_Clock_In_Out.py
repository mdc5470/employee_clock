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
    print(len(candidates))
    if not candidates:
    	errormess("No device with signature {device_signature} found")
    if len(candidates) > 1:
        errormess("More than one device with signature {device_signature} found")
    return candidates[0].device
    
#This error handling needs to de done using a dictionary so we are able to relate an error number to a function that needs to be redone.
def errormess(message):
	print(ports)
	#serial.Serial(ports, "9600").close()
	print(message)
	time.sleep(2)
	while len(find_serial_device()) == 0:
		print(message)
	
		
		

board = Arduino(find_serial_device())



def init_serial():

	#i = 0
	COM = 1
	global ser
	global ports
	
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = find_serial_device()
	ports = find_serial_device()
	print(ports)
	ser.timeout = 5000
	ser.open()
	RFID_Data = ser.readline()
	return(ser)
	
			
	
	#if ser.isOpen()
	
#Writes data to arduino through the serial port	
def write_read(x):

    arduino = serial.Serial(port=find_serial_device(), baudrate=9600, timeout = 0.1)
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data
	
def read_data():
	
	while True:
		ser = init_serial()
		time.sleep(20)
		if ser:
			try:
				RFID_Data = ser.readline()
				if RFID_Data:
					RFID_Data = RFID_Data.decode()
					RFID_Data = RFID_Data.strip()
					RFID_Data = str(RFID_Data)
					return(RFID_Data)
			except:
				errormess("j")
