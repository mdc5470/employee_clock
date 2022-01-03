# employee_clock
Developing a clock in and clock out system.

Hardware Specs:
- Arduino Uno
- 2 UID Readers
- USB-A to USB-C 
- 4 Line LCD LED








Create Automatic Boot of Python file on start up (Linux):

##*****Note: MAKe sure that all the files that are needed are included in the same path as the python script that yopu want to run. Also make sure that all libs are downloaded with sudo pip not just pip so that they are also in this location. 

#Find Python path:
	"which python"
	
#Create Service File:
	"sudo systemctl --force --full edit <YOUR NAME>.service"
	
#Paste into file: 
	[Unit]
	Description=<(Optional) Description of your project>
	After=network.target

	[Service]
	ExecStart=<YOUR-PYTHON-PATH> <PATH-TO-YOUR-SCRIPT>.py

	[Install]
	WantedBy=multi-user.target

#Reload the Demons:
	"sudo systemctl daemon-reload"
	
#Enable Start:
	"sudo systemctl enable <YOUR-NAME>.service"
	
#Status of the script when it starts:
	"sudo systemctl status <YOUR-NAME>.service"
	
