from db_libs.connect_function import *
import pandas as pd

def defect_to_total(conn, table_name):
	result, co = read_query(conn, table_name)
	result = pd.DataFrame(result)
	job_number = result[6]
	test = result[164]
	job_Num_Array = []
	num_Jobs = 0
	num_Tested_Cam = len(test)
	for i in range(num_Tested_Cam - 1):
		job_Num_Current = job_number.iloc[i]
		job_Num_Past = job_number.iloc[i+1]
		if job_Num_Current != job_Num_Past:
			job_Num_Array.append(job_Num_Current)
			num_Jobs = num_Jobs + 1

          #What is the point of NONE for this. 
		if test.iloc[i] == "NONE":
			test_Result_None = test_Result_None + 1
		if test.iloc[i] == "FAIL":
			test_Result_Fail = test_Result_Fail + 1
		if test.iloc[i] == "PASS":
			test_Result_Pass = test_Result_Pass + 1

	test_Result_Fail = test_Result_Fail + test_Result_None
	test_Percent_Pass = round(test_Result_Pass/num_Tested_Cam * 100, 2)
	test_Percent_Fail = round((test_Result_Fail+test_Result_None)/num_Tested_Cam * 100, 2)	

	return test_Result_Fail