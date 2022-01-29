from db_libs.db_func import *
import pandas as pd


def filter_dipswitch(conn, table_name):
	cam_data, cam_col = read_query(conn, table_name)
	cam_data = pd.DataFrame(cam_data)
	print(cam_data)
	num_tested_cam = len(cam_data[1])
	daughter = cam_data[16]
	print(daughter)
	for i in range(num_tested_cam - 1):
		if daughter.iloc[i] == "FAIL":
			cam_data = cam_data.drop(i)
			print(i)
	print(cam_data)
#Need to reset the index so that the numbers come up correctlyt 
	return cam_data, num_tested_cam

def defect_to_total(result):
	num_tested_cam = len(result[1])
	job_number = result[6]
	test = result[164]
	job_Num_Array = []
	num_Jobs = 0
	test_Result_None = 0
	test_Result_Fail = 0
	test_Result_Pass = 0
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

	test_Result_Fail = int(test_Result_Fail + test_Result_None)
	test_Percent_Pass = int(round(test_Result_Pass/num_Tested_Cam * 100, 6))
	test_Percent_Fail = int(round((test_Result_Fail+test_Result_None)/num_Tested_Cam * 100, 6))	

	return test_Result_Fail, test_Percent_Fail, test_Percent_Pass, test_Result_Pass