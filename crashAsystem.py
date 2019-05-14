#Create a program called crashAsystem
#import time
import time
#Ask user if they want to crash a System
yes = "y"
no = "n"
print("Would you like to crash a system. y/n")
time.sleep(3)
user = input("")
#Create if statement depending on users input
if (user == yes) :
	print("System is crashing!")
	time.sleep(5)
	print("System crashed")
	time.sleep(1)
	print("Now Run. The government is after you!!!")
	
if (user == no) :
	print("Good Choice.")
