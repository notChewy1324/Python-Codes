# OOP in Python

class dog():

    def __init__(self, name, age, hrs):
        self.name = name
        self.age = age
        self.hrs = hrs

    def dog_name(self):
        return self.name

    def dog_age(self):
        return self.age

    def dog_toyTime(self):
        return self.hrs

dog1 = input("Whats your first dogs name?: ")
dog2 = input("Whats your second dogs name?: ")

dog1Age = input("Whats your first dogs age?: ")
dog1Age = int(dog1Age)
dog2Age = input("Whats your second dogs age?: ")
dog2Age = int(dog1Age)

dog1hrs = input("Whats your first dogs play time?: ")
dog1hrs = int(dog1hrs)
dog2hrs = input("Whats your second dogs play time?: ")
dog2hrs = int(dog2hrs)

firstDog = dog(dog1, dog1Age, dog1hrs)
secondDog = dog(dog2, dog2Age, dog2hrs)

# Change methods for different outputs
print(firstDog.dog_name, secondDog.dog_name())