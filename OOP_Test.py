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


first = dog("Jackson", 3, 45)
second = dog("Gracie", 3, 5)

print(first.dog_name(), second.dog_name())