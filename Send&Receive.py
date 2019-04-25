#Create a program called Send and Receive
#Import time
import time
#Take users input and save it locally
user = input("")
type(user)
#Display sending with 5 second delay
print("Sending...")
time.sleep(5)
#Show message and that it was sent successfully
print("Message was sent successfully!")
#Receive Message
time.sleep(3)
print("Receiving...")
time.sleep(5)
print(user)