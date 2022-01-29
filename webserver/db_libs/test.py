from connect_function import create_server_connection
from connect_function import read_query

conn = create_server_connection("192.168.18.36", "sqluser", "", "Production_db")

results = read_query(conn, "IQC_Cam_Results_cam_results")

for result in results:
	print(result)