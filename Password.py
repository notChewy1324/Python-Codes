#Create a program named Password
#Take user input and save it localy to a varible
pword = input("Give me a password!")
type(pword)
print("Password Saved! \nEnter Password!")
password = input("")
preset = pword
#Take users input to match the correct password or inncorrt password and display in or out
if (password == preset) :
	print("Your In")
	print("Password is correct")
else :
	print("Your Out")
	print("Password is incorrect")