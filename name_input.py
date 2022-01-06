from tkinter import *

root = Tk()
root.title("Rossell Automation")

def main_page():
	global label1
	label1=Label(root, text="Rossell Automation")
	label1.pack()

	def exit():
		root.destroy()
	
	def menun():
		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command=exit)
		menubar.add_cascade(label="File", menu=filemenu)
		root.config(menu=menubar)
	
	menun()
main_page()
#root.attributes('-fullscreen', True)
root.mainloop()
