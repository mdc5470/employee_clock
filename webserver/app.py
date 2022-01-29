from flask import Flask, render_template, request
from db_libs.db_func import *
import pandas as pd
from cam_analysis import *
import os



#conn = create_server_connection("192.168.18.36", "sqluser", "", "Production_db")
app=Flask(__name__)

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
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	return render_template("view.html")

#@app.route('/export_data/')
#def export_data():
#	return render_template("export_data.html")

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

@app.route('/lookup/')
def lookup():
	return render_template("employee/lookup.html")

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
	app.run(host='localhost', port=9875)
