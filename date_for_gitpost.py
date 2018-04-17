

# this script will help to make a dir base on the date and time of local machine

from datetime import datetime
now = datetime.now()  
#/ now = datetime.now   // no need '() '

current_year = now.year
next_year = current_year + 1
current_month = now.month
current_day = now.day
print (now.year)
print (now.month)
print (now.day)
print (current_year)
print (next_year)

 
import os, time
DEBUG = 0

# you can change the file name as needed , last part is for time information

dir_name = "vol_name" + "_mediafiles_" + time.strftime("%Y-%m-%d_%H-%M", time.localtime())+ ".dir"
print (dir_name) 

