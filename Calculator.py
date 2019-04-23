#Create a program called Calculator
#Create the varibles
multiplaction = "Multi"
Subtraction = "Sub"
Addition = "Add"
Divide = "Divide"
#Ask the user the type of method they want to use (-,+,/,*) and give them the answers
print("What type of method do you want do calculate.")
print("Add, Sub, Multi, Divide?")
user = input("")
type(user)
if (user == multiplaction) :
	multi = int(input(""))
	print("One more number plz")
	multi2 = int(input(""))
	multianswer = multi * multi2
	print("The answer is:")
	print(multianswer)
elif (user == Subtraction) :
	sub = int(input(""))
	print("One more number plz")
	sub2 = int(input(""))
	subanswer = sub - sub2
	print("The answer is:")
	print(subanswer)
elif (user == Addition) :
	add = int(input(""))
	print("One more number plz")
	add2 = int(input(""))
	addanswer = add + add2
	print("The answer is:")
	print(addanswer) 
elif (user == Divide) :
	div = int(input(""))
	print("One more number plz")
	div2 = int(input(""))
	divanswer = div / div2
	print("The answer is:")
	print(divanswer)
else :
	print("Make sure that you enter EXACLTY what the word above said!")
	print("You must restart the program.")

