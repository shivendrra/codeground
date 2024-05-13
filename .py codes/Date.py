#  practice program

date = input(str("enter the date in format dd/mm/yyyy"))
d_name = input(str("enter the day"))
newDate = date.split('/')
dd = int(newDate[0])
mm = int(newDate[1])
yy = int(newDate[2])
print(newDate)

def checkWeekday(dayname):      #predict the next day of week
  weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  print(weekdays[dayname])

def checkValidity(date, month, year):     #function to check the date validity
  if(month<=12):
    if(month==1 or 3 or 5 or 7 or 8 or 10 or 12):     #month of 31days
      if(date<=31):
        checkWeekday(d_name)       #call the function
      else:
        print("not a vaild date")
    elif(month==4 or 6 or 9 or 11):       #month of 30days
      if(date<=30):
        checkWeekday(d_name)       #call the function
      else:
        print("not a valid date")
    elif(month==2):       #month of feb
      if(year%4==0):        #leap year or not
        if(date<=29):
          checkWeekday(d_name)       #call the function
        else:
          print("enter a valid date")
      else:
        if(date<=28):
          checkWeekday(d_name)       #call the function
        else:
          print("enter a valid date")
    else:
      print("enter a valid date")
  else:
    print("enter a valid date")

checkValidity(dd, mm, yy)       #call the function