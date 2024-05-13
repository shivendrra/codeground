import time
import zipfile
import os
import sys

path = os.chdir('d:/Machine Learning/NLP/CSV Files')

# Define the directory to zip
dir_to_zip = r"D:/Machine Learning/NLP/CSV Files"
zip_file_name = 'myfile.zip'
scheduled_time = time.strftime("%H:%M")   # 24-hour format

# create a file name array
file_names = ['data2.csv', 'test.csv', 'test_ti.csv']

while True:
  # Get the current time
  current_time = time.strftime("%H:%M")
    
  # If the current time matches the scheduled time, create the zip file
  if current_time == scheduled_time:
    dir_list = []
    file_list = []
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip:
      for root, dirs, files in os.walk(dir_to_zip):
        dir_list += dirs
        file_list += files
        print(root, file_list, dir_list)  #this will print the paths and directories
        for file in file_names:
          zip.write(os.path.join(root, file), file)
    break

dict1 = {}
my_list = []
dict2 = {}
title = ['name', 'is', 'bond', 'james', 'bond', 'and', 'yours', 'fuck', 'off', 'please']
for j in range(0,10):
  my_list.append(j)
  for i in range(len(my_list)):
    thumbnail = 'video'+ str(j)
    dict1[thumbnail] = title[i]
    dict2[thumbnail] = dict1

print(dict2)
sys.exit()