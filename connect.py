import serial
import serial.tools.list_ports as list_ports


class USB_interface:

	def __init__(self):
		self.ser = None
		
	def find_serial_device():
	
		device_signature = "1a86:7523"
		
		candidates = list(list_ports.grep(device_signature))
	
		if not candidates:
			errormess = "No device with signature " + device_signature + " found"
		if len(candidates) > 1:
			errormess = "More than one device with signature " + device_signature + " found"
		return candidates[0].device
	
	def connect(self):
	
		try:
			if self.ser == None:
				self.ser = serial.Serial(port = USB_interface.find_serial_device(),  baudrate=9600, timeout = 0.1)
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
					
	def isConnected(self):
	
		try:
			th = self.ser.isOpen()
			print(th)
			return True
		except:
			return False
					
	def wirte_data(self, data):
	
		try:
			self.ser.write(bytes(data, 'utf-8'))
		except Exception as e:
			tkMessageBox.showerror('Serial connection error', 'Error sending message')
			
	def read_datas(self):
	
		try:
			RFID_Data = self.ser.readline()
			print(RFID_Data)
			if len(RFID_Data) > 1:
				RFID_Data = RFID_Data.decode()
				RFID_Data = RFID_Data.strip()
				RFID_Datas = str(RFID_Data)
			return RFID_Datas
		except Exception as e:
			print("Hey")
			#tkMessageBox.showerror('Serial connection error', 'Error sending message')
		
	def disconnect():
	
		self.ser = disconnect()
		
		


	
				
				
