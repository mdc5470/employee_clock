from backend_work import *
from Employee_Clock_In_Out import *
import time



while True:
	f = read_data()
	print(f)
	#in_out = clockin_out(f)
	#print(in_out)
	t_f, c, UID = find_employee(f)
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
