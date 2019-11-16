#I am working on saving and taking user data to save locally to there device to resemble a diary.
#This is still being worked on.
import time
daycount = 1
while(True):
    user = input("Day " + str(daycount) + " Log: ")
    user = str(user)
    time.sleep(1)
    print("Saved!")
    user1 = input("Would you like to see the past logs or write for the next day? (y or n or next)")
    if (user1 == "y"):
        print(user)
    if (user1 == "next"):
        time.sleep(1)
        daycount += 1
        continue
    if (user1 != "y" or "next"):
        break
#The current goal is to have a diary that logs information when you save data to it.
