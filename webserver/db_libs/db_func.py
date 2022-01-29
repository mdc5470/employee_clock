import mysql.connector as mysql
import pandas as pd
from mysql.connector import Error



#Connection with the database and tables

def create_server_connection(host, user, password, db_name):
#Maybe make a check to make sure that this is a valid server that the person is connecting to!!!!!
	try:
		conn = mysql.connect(host = host, user = user, password = password, db = db_name)
		print("Connection Successful")

	except Error as e:
		print("Error while connecting to MySQL", e)

	return conn

#Creating Databases and Tables 

def create_database(conn, db_name):

	cursor = conn.cursor()
	try:
		query = "CREATE DATABASE " + db_name
		cursor.execute(query)
		status = "Database created successfully"
	except Error as e:
		status = "Database was not created sorry"

	return status

def create_table(conn, table_name):

	cursor = conn.cursor()
	try:
		query = "CREATE TABLE " + table_name
		cursor.execute(query)
		conn.commit()
		status = "Query successful"
	except Error as e:
		status = "Query was not successfully written"

	return status

def populate_table(conn, db_name, table_name):

	status = []

	cursor = conn.cursor()
	for i,row in empdata.iterrows():
		try:
			sql = "INSERT INTO " + db + "." + table + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(sql, tuple(row))
			print("Recorded")
			conn.commit()
			status[i] = "Recorded"
		except Error as e: 
			status[i] = "Already Written"   

	return status
	
def modify_table(conn, table_name, mod_type, mod_col):

	query = "ALTER TABLE " + table_name + " " + mod_type + " " + mod_col + ";"
	cursor = conn.cursor()
	try: 
		cursor.execute(query)
		result = "The column, " + mod_col + " was successfully " + mod_type + " from " + table_name
	except Error as e:
		result = "There was an error"

	return result

def read_query(conn, table_name):

	
	query = "SELECT * FROM " + table_name + ";"
	cursor = conn.cursor()
	result = None
	query_col = "SHOW COLUMNS FROM " + table_name + ";"
	try:
		cursor.execute(query)
		result = cursor.fetchall()
	except Error as e:
		result = ("Failed to read the data", e)
	
	try:
		column_names = cursor.execute(query_col)
	except Error as e:
		column_names = ("Failed to get column names", e)
	print(column_names)

	return result, column_names



 	