from flask import Flask, render_template, request
import pandas as pd
import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from tools import *
from employee import *
import os

#conn = create_server_connection("192.168.18.36", "sqluser", "", "Production_db")
app=Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

@app.route('/')
def show_index():
	return render_template("home.html")

#Secure app login information to access the website
#@app.route('/', methods=['POST', 'GET'])
#def login():
 #   error = None
 #   if request.method == 'POST':
  #      if valid_login(request.form['username'],
   #                    request.form['password']):
    #        return log_the_user_in(request.form['username'])
   #     else:
  #          error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
   # return render_template('home.html', error=error)

@app.route('/employee/')
def employee():
	return render_template("employee.html")

#@app.route('/edit_emp/')
#def edit_emp():
#	m = os.path.join('static', 'img')
#	print(m)
#	app.config['st'] = m
#	full_filenames = os.path.join(app.config['st'], 'seegridlogo.jpg')
#	return render_template("edit_emp.html", user_image = full_filenames)

@app.route('/export/')
def export():
	return render_template("export.html")

@app.route('/tools/')
def tools():
	return render_template("tools.html")

@app.route('/view/')
def view():
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	return render_template("view.html")

#Tools page routing and the functions that are needed to modify the html files.

@app.route('/addform', methods=["POST"])
def addform():
	
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	UID = request.form.get("UID")
	add_employ(first_name+last_name, UID)
	
	return render_template("form.html", first_name=first_name, last_name=last_name, UID=UID, formtype="add")
	
@app.route('/deleteform', methods=["POST"])
def deleteform():
	
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	UID = request.form.get("UID")
	delete_employ(first_name+last_name)
	
	return render_template("form.html", first_name=first_name, last_name=last_name, UID=UID, formtype="delete")

@app.route('/modifyform', methods=["POST"])
def modifyform():
	
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	UID = request.form.get("UID")
	new_first_name = request.form.get("first_name")
	new_last_name = request.form.get("last_name")
	new_UID = request.form.get("UID")
	modify_employ(first_name+last_name, UID, new_first_name+new_last_name, new_UID)
	
	return render_template("form.html", first_name=first_name, last_name=last_name, UID=UID, formtype="modify")

#Employee page routing and the functions that are needed to modify the html files. 

@app.route('/mod_clock_in', methods=["POST"])
def mod_clock_in():

	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	UID = request.form.get("UID")	
	date_mod = request.form.get("date_mod")
	time_mod = request.form.get("time_mod")
	mod_clock_in(first_name+last_name, UID, date_mod, time_mod)
	return render_template("look_up_try.html", formtype="look_up")
	
def mod_clock_out():

	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	UID = request.form.get("UID")	
	date_mod = request.form.get("date_mod")
	time_mod = request.form.get("time_mod")
	mod_clock_out(first_name+last_name, UID, date_mod, time_mod)
	return render_template("look_up_try.html", formtype="look_up")
	

@app.route('/look_up', methods=["POST"])
def look_up():
	
#Get the info from the form in the HTML file
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	UID = request.form.get("UID")	
	look_up_func(first_name+last_name, UID)
	
	
	return render_template("look_up_try.html", formtype="look_up")

#@app.route('/camera/')
#def camera():
#	return render_template("camera.html")

#@app.route('/pcba/')
#def pcba():
#Call the data from the database storage that already has the information

#	conn = create_server_connection("192.168.18.36", "sqluser", "", "Production_db")
#	cam_data, cam_col = filter_dipswitch(conn, "IQC_Cam_Results_cam_results")
#	test_Result_Fail, test_Percent_Fail, test_Percent_Pass, test_Result_Pass = defect_to_total(cam_data)
#	cam_data = cam_data.to_records(index=False)
	
	

#	return render_template("pcba.html", cam_num_fail=test_Result_Fail, cam_per_fail=test_Percent_Fail, cam_per_pass=test_Percent_Pass, cam_num_pass = test_Result_Pass, result = cam_data) 

@app.route('/clock_in/')
def clock_in():
	return render_template("employee/clock_in.html")

@app.route('/clock_out/')
def clock_out():
	return render_template("employee/clock_out.html")

@app.route('/add/')
def add():
	return render_template("tools/add.html")

@app.route('/modify/')
def modify():
	return render_template("tools/modify.html")

@app.route('/delete/')
def delete():
	return render_template("tools/delete.html")


if __name__=="__main__":
	app.run(debug=True)
