class circle():
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return (self.radius**2)*(22)/(7)
    
    def perimeter(self):
        return 2*self.radius*((22)/(7))

a = int(raw_input('entewr radius: '))
new_circle = circle(a)
print("%.4f"% new_circle.area())
print("%.4f"% new_circle.perimeter())
