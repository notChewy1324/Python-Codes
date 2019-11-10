#Create a program called password cracker 
#Create the secret code
secret = "1234"
#Create a password
pword = "123"
#Display the output if input is the secret code or pword
print("Enter the Password!")
x = input("")
type(x)
if (x == secret) :
	print("You just hacked 'eM!")
elif (x == pword) :
	print("You just got HACKED!")
else : 
	print("error")
