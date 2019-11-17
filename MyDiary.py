#I am working on saving and taking user data to save locally to there device to resemble a diary.
#This is still being worked on.
import time
daycount = 1
while(True):
    user = input("Day " + str(daycount) + " Log: ")
    user = str(user)
    print("Saved!")
    time.sleep(1)
    user1 = input("Would you like to see the past logs or write for the next day? (yes or no or next)")
    if (user1 == "yes"):
        print(user)
    if (user1 == "next"):
        time.sleep(1)
        daycount += 1
        continue
    if (user1 != "yes" or "next"):
        break
