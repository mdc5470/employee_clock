import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
from datetime import timedelta

def day_calc(day, df, num_days):

# These will be grabbed values, but for now they are values that are used 
	num_employ = 4

	total = pd.DataFrame()

	
	for j in range(num_days):
		
		day1_time_in = df[day + " IN"]
		day1_time_out = df[day + " OUT"]
		duration_time = []
				
		for i in range(num_employ):
			time_in = datetime.strptime(day1_time_in[i], '%H:%M').time()
			time_out = datetime.strptime(day1_time_out[i], '%H:%M').time()
		
			t1 = timedelta(hours=time_in.hour, minutes=time_in.minute, seconds=time_in.second)
			t2 = timedelta(hours=time_out.hour, minutes=time_out.minute, seconds=time_out.second)

			duration = str(t2-t1)
			duration_time.append(duration)
	
		daytime = pd.DataFrame(duration_time, columns=[day])

		day_start = datetime.strptime(day, '%m/%d/%Y')
		day = day_start + timedelta(days=1)
		day = day.strftime('%m/%d/%Y')
		
		total = pd.concat([total, daytime], axis=1)
	
	return(total)
		

