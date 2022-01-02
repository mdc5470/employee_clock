from backend_work import *
from Employee_Clock_In_Out import *
from connect import USB_interface
import time

#git hub key: 
con = USB_interface()

if con.connect():


	while True:
		#f = read_data()
		con.isConnected()
		f = con.read_datas()
		print(f)
		#in_out = clockin_out(f)
		#print(in_out)
		t_f, c, UID = find_employee(f)
		print(t_f)
		if t_f == "T":	
			write_read(t_f)
			#time.sleep(0.01)
			write_read(c)
			clock_in_out(UID)
		elif t_f == "F":
			write_read(t_f)
			e_name = input("What is your name?")
			e_nameuid = add(e_name, UID)
			write_read(e_nameuid)
		elif t_f == "In Disconnect State":
			print(t_f)
			time.sleep(10)
			if con.connect == True:
				con.disconnect
				con.connect
		else:
			print(t_f)
		
else:
	print("Hi")
