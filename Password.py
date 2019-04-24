#Create a program named Password
#Take user input and save it localy to a varible
print("Give me a password!")
pword = input("")
type(pword)
print("Password Saved!")
print("Enter Password!")
password = input("")
preset = pword
#Take users input to match the correct password or inncorrt password and display in or out
if (password == preset) :
	print("Your In")
	print("Password is correct")
else :
	print("Your Out")
	print("Password is incorrect")