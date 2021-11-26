import serial 

def init_serial():
	COM = 1
	global ser
	
	ser = serial.Serial("/dev/ttyUSB0", 9600)
	
	ser.timeout = 10
	w = ser.read
	
	if ser.isOpen():
		print(w)
		
init_serial()
