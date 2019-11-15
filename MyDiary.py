#I am working on saving and taking user data to save locally to there device to resemble a diary.
#This is still being worked on.
import time
daycount = 1
#Need to put into a while(True) loop 
            #Need to change string to increment by 1
user = input("Day 1 Log:")
user = str(user)
time.sleep(2)
print("Saved!")
user1 = input("Would you like to see the past logs? (y or n)")
if (user1 == "y"):
    print(user)
time.sleep(1)
daycount += 1
#The current goal is to have a diary that logs information when you save data to it.
