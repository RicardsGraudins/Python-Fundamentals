#Import the datetime library https://docs.python.org/2/library/datetime.html
import datetime

#Prints the current date and the current time
print(datetime.datetime.now())
#Prints the current time
print(datetime.datetime.now().time())
#Prints the current date
print(datetime.datetime.now().date())

#Prints formated date and time
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

#Alternatively you can do the following:
#from datetime import datetime
#print(datetime.now())
#print(datetime.now().time())
#print(datetime.now().date())
#print (datetime.now().strftime("%Y-%m-%d %H:%M"))

#Ref. https://docs.python.org/2/library/datetime.html and http://strftime.org/