class Apple():
    def __init__(self, c, w, s, m):
        self.color = c
        self.weight = w # In Ounces
        self.size = s # In Inches
        self.mold = m # 0 for no mold & 1 for mold

    def cost(self, s):
        if s >= 10:
            return 100
        else:
            return 5
    

# Change methods for different outputs
apple1 = Apple("red", 12, 15, 0)
apple2 = Apple("blue", 3, 5, 1)
print(apple2.cost(1))