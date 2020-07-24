class BagOfOranges():
    def __init__(self, color, age, size):
        self.Color = color
        self.Age = age # In weeks
        self.Size = size # In Ounces

    def expired(self, e):
        self.Expired = e


org1 = BagOfOranges("light orange", 3, 8)
org2 = BagOfOranges("dark orange", 5, 12).expired("YES")
org3 = BagOfOranges("yellow", 1, 5)
print(org1.Age)