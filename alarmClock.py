from datetime import datetime
from playsound import playsound


def validateTime(alarmTime):
    if len(alarmTime) != 11:
        return "Invalid time format! Please try again... "
    else:
        if int(alarmTime[0:2]) > 12:
            return "Invalid hour format! Please try again... "
        elif int(alarmTime[3:5]) > 59:
            return "Invalid minute format! Please try again... "
        elif int(alarmTime[6:8]) > 59:
            return "Invalid second format! Please try again... "
        else:
            return "ok"
        
while True:
    alarmTime = input("Enter the time in 'HH:MM:SS AM/PM' format: ")
    
    validate = validateTime(alarmTime.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting your alarm for: {alarmTime}")
        break
    

while True:
    
    alarm_hr = alarmTime[0:2]
    alarm_min = alarmTime[3:5]
    alarm_sec = alarmTime[6:8]
    alarmPeriod = alarmTime[9:].upper()
    
    now = datetime.now()

    current_hr = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    currentPeriod = now.strftime("%p")
    
    if alarmPeriod == currentPeriod:
        if alarm_hr == current_hr:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("WAKE UP!")
                    playsound('/Users/chewy1324/Downloads/amazing_wake_up_sound.mp3')
                    break