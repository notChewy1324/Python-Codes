class BagOfOranges():
    def __init__(self, color, age, size):
        self.Color = color
        self.Age = age # In weeks
        self.Size = size # In Ounces

    def expired(self, e):
        self.Expired = e


# Oranges
org1 = BagOfOranges("light orange", 3, 8)
org2 = BagOfOranges("dark orange", 5, 12)
org2.expired("YES")
org3 = BagOfOranges("yellow", 1, 5)

# Display Values
print(org3.Color)
print(org2.Color)
print(org1.Color)