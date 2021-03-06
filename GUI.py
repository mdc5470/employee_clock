#https://pythonprogramming.net/change-show-new-frame-tkinter/

import tkinter as tk
from tkinter import *
from backend_work import *


root = Tk()
root.title("Rossell Automation")

def main_page():
	global label1
	label1=Label(root, text="Rossell Automation")
	label1.pack()
	def add_employ():
		menun()
		global label2
		global button2
		global button1s
		label1.destroy()
		label2=Label(root, text="Add Employee")
		label2.pack()
		e_name=Entry(root, bd = 5).pack()
		#Needs to wait for a new UID to be scanned so that it does not assign a already used UID to the person.
		#UID = add_people().pack()
		#print(UID)
		button2=Button(root, text="Add Employee", command=lambda : det_in_out())
		
		button1=Button(root, text="Back to Main Page", command=back)
		button1.pack()
		button2.pack(side=BOTTOM)

	def delete_employ():
		menun()
		global label2
		global button2
		global button1
		label1.destroy()
		label2=Label(root, text="Delete Employee")
		label2.pack()
		employ_name=Entry(root, bd = 5).pack()
		button2=Button(root, text="Delete Employee", command=lambda : delete(employ_name))
		button1=Button(root, text="Back to Main Page", command=back)
		button1.pack()
		button2.pack(side=BOTTOM)

	def export_csv():
		menun()
		global label2
		global button2
		global button1
		label1.destroy()
		label2=Label(root, text="Export to CSV")
		label2.pack()
		month_button=Button(root, text="Obtain Month data to CSV", command=lambda : hours_work("11/09/2021", "month")).pack()
		week_button=Button(root, text="Obtain Week data to CSV", command=lambda : hours_work("11/09/2021", "week")).pack()
		day_button=Button(root, text="Obtain Day data to CSV", command=lambda : hours_work("11/09/2021", "day")).pack()
		employ_name=Button(root, text="Export to CSV", command=lambda : export_cv("Employee Name")).pack()
		main_page=Button(root, text="Back to Main Page", command=back).pack()

	def back():
		for widgets in root.winfo_children():
			widgets.destroy()
		main_page()

	def t_add():
		for widgets in root.winfo_children():
			widgets.destroy()
		add_employ()

	def t_delete():
		for widgets in root.winfo_children():
			widgets.destroy()
		delete_employ()

	def t_export():
		for widgets in root.winfo_children():
			widgets.destroy()
		export_csv()
	
	def exit():
		root.destroy()
	
	def menun():
		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Main Page", command=back)
		filemenu.add_command(label="Add Employee", command=t_add)
		filemenu.add_command(label="Delete Employee", command=t_delete)
		filemenu.add_command(label="Export to csv", command=t_export)
		filemenu.add_command(label="Exit", command=exit)
		menubar.add_cascade(label="File", menu=filemenu)
		root.config(menu=menubar)

	menun()

main_page()
root.attributes('-fullscreen', True)
root.mainloop()
