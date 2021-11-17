import serial 

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
		
init_serial()