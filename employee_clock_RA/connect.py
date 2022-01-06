import serial
import serial.tools.list_ports as list_ports


class USB_interface:

	def __init__(self):
		self.ser = None
		
	def find_serial_device():
	
		device_signature = "1a86:7523"
		
		candidates = list(list_ports.grep(device_signature))
		print(candidates)
		if not candidates:
			errormess = "No device with signature " + device_signature + " found"
		if len(candidates) > 1:
			errormess = "More than one device with signature " + device_signature + " found"
		return candidates[0].device
	
	def connect(self):
	
		try:
			if self.ser == None:
				port = USB_interface.find_serial_device()
				self.ser = serial.Serial(port,  baudrate=9600, timeout = 0.1)
				print(port)
				return True
			else: 
				if self.ser.isOpen():
					self.ser.close()
					return False
				else:
					self.ser.open()
					return True
		except Exception as e:
			return False
	
#This function is to let us know if the serial port is open and ready to receive data.			
	def isConnected(self):
	
		try:
			conn = USB_interface.find_serial_device()
			print("The device is connected on port: " + str(conn))
			return True
		except:
			return False
					
	def write_data(self, data):
	
		try:
			self.ser.write(bytes(data, 'utf-8'))
			data = self.ser.readline()
		except Exception as e:
			tkMessageBox.showerror('Serial connection error', 'Error sending message')
			
	def read_datas(self):
	
		try:
			RFID_Data = self.ser.readline()
			print("This is the RFID Data: " + str(RFID_Data))
			if len(RFID_Data) > 1:
				RFID_Data = RFID_Data.decode()
				RFID_Data = RFID_Data.strip()
				RFID_Datas = str(RFID_Data)
			return RFID_Datas
		except Exception as e:
			print("Nothing to read for the read_datas of USB_interface")
			#tkMessageBox.showerror('Serial connection error', 'Error sending message')
		
	def disconnect(self):
	
		self.ser.close()
		
		


	
				
				
