import os


def modify_html(filter_employ_df):
	
	os.remove("templates/look_up_try.html")
	
	filter_employ_df = filter_employ_df.to_html()
	
	
	text_file = open("templates/look_up_try.html", "w")
	head = """<html>
<head>
	<link rel="stylesheet" href="/static/css/home.css">
	<title>Using </title>
	<div id="logo">
		<img src="{{ url_for('static', filename='img/rossell_auto.jpg') }}"
			width="300"
			height="225" />
	</div>
</head>
<body>
	<div class="topnav">
		<a class="active" href="/">Home</a>
		<a href="/employee">Employee</a>
		<a href="/tools">Tools</a>
		<a href="/view">View</a>
		<a href="/export">Export</a>
	</div>

</body>"""
	text_file.write(head)
	text_file.write(filter_employ_df)
	text_file.close()
				
