#Create a program called crashAsystem
#import time
import time
#Ask user if they want to crash a System
user = input("Would you like to crash a system. (1/0): ")
user = int(user)
#Create if statement depending on users input
if (user == 1) :
	print("System is crashing!")
	time.sleep(5)
	print("System crashed")
	time.sleep(1)
	print("Now Run. The government is after you!!!")
	
if (user == 0) :
	print("Good Choice.")
