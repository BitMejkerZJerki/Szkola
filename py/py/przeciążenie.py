class Punkty:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt: ({self.x}, {self.y})"


    def __add__(self, other):
        self.new_x = self.x + other.x
        self.new_y = self.y + other.y
        newPunkt = {self.new_x + self.new_y}
        return f"Nowy punkt: ({newPunkt[0]},{newPunkt[1]})"

    def __sub__(self, other):
        self.new_x = self.x - other.x
        self.new_y = self.y - other.y
        newPunkt = {self.new_x - self.new_y}
        return f"Nowy punkt: ({newPunkt[0]},{newPunkt[1]})"


a = Punkty(3,6)
b = Punkty(5,6)
print(a)
print(b)


c = a+b
d = a-b

print(c)
print(d)