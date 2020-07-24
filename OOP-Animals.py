class Dogs():
    def __init__(self, b, s, c, w):
        self.Breed = b
        self.Size = s
        self.Color = c
        self.Weight = w # In pounds

    def SleepTime(self, t):
        self.sleepTime = t # In hrs
    
    def Bark(self):
        print("BARK!")
    
    def Eat(self):
        print("EATING")

# Dogs
Jackson = Dogs("Poodle", "small", "white", 15)
Jackson.SleepTime(8)

Gracie = Dogs("Shih Tzu", "medium", "black", 12)

# Display the dogs information
print(Jackson.Size)