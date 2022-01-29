
def create_add_request():

	

def add(e_name, UID):
	
	df = pd.read_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv')
	indice = len(df) + 1
	dates = date.today()
	print(indice)
	print(df)
	df2 = pd.DataFrame([[indice, e_name, dates, UID]], columns=('Employment Count', 'Employee Name', 'Employment Date', 'UID'))
	df = df.append(df2)
	print(df)
	df.to_csv('/home/mdc5470/Documents/employee_clock/employee_id.csv', index=False)
	
	return(e_name + " UID: " + UID)
