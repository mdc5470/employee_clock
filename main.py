from backend_work import *
#from Employee_Clock_In_Out import *
from connect import USB_interface
import time

#git hub key: 
con = USB_interface()
con.connect()
while True:
	if con.isConnected():

		#f = read_data()
		f = con.read_datas()
		print(f)
		#in_out = clockin_out(f)
		#print(in_out)
		t_f, c, UID = find_employee(f, con)
		print(t_f)
		if t_f == "T":
			print("There has been a signal from a RFID card")	
			con.write_data(t_f)
			con.write_data(c)
			#time.sleep(15)
			clock_in_out(UID)
		elif t_f == "F":
			write_read(t_f)
			e_name = input("What is your name?")
			e_nameuid = add(e_name, UID)
			write_read(e_nameuid)
		elif t_f == "In Disconnect State":
			print(t_f)
		else:
			print(t_f)
			
		
		
	else:
		print("Trying to Reconnect")
		time.sleep(1)
		#con.disconnect()
		con = USB_interface()
		con.connect()
		
		
		
