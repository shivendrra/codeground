import zipfile
import time
import os

path = os.chdir('d:/Machine Learning/NLP/CSV Files')

# Define the directory to zip
dir_to_zip = 'd:Machine Learning/NLP/CSV Files'

# Define the name of the zip file
zip_file_name = 'myFile.zip'

# create a file name array
file = ['data2.csv', 'test.csv', 'test_ti.csv']

# Define the time to run the script
scheduled_time = time.strftime("%H:%M")   # 24-hour format

# Loop until the scheduled time is reached
while True:
		# Get the current time
	current_time = time.strftime("%H:%M")
		# If the current time matches the scheduled time, create the zip file
	if current_time == scheduled_time:
		with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip:
			for root, dirs, files in os.walk(dir_to_zip):
				print(root)
				for file in files:
					zip.write(os.path.join(root, file))
		break
	# Wait for one minute before checking the time again
	time.sleep(60)