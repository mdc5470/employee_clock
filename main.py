from backend_work import *
#from Employee_Clock_In_Out import *
from connect import USB_interface
import time
from tkinter import *


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
			con.write_data(t_f)
			pop_up()
			print(employ_name_get)
			e_nameuid = add(employ_name_get, UID)
			con.write_data(employ_name_get)
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


def pop_up(): 
	root = Tk()
	root.title("Rossell Automation")
	root..geometry("500x200")
	
	employ_name = StringVar()
	global label1
	label1=Label(root, text="Rossell Automation")
	label1.pack()

	
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Exit", command=exit)
	menubar.add_cascade(label="File", menu=filemenu)
	root.config(menu=menubar)
	
	employ_names = Entry(root, textvariable = employ_name).pack()
	button = Button(root, text="Enter", command=lambda : exit(root, employ_name)).pack()

	
#root.attributes('-fullscreen', True)
	root.mainloop()


def exit(root, employ_name):
	global employ_name_get
	employ_name_get = employ_name.get()
	root.destroy()

def exit():
		root.destroy()

