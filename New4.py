class Circle:
    PI=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.PI*self.radius*self.radius
    def circumference(self):
        return 2*Circle.PI*self.radius
    #def show(self):
        #print("radius is", self.radius)
C1=Circle(7.2)
print("area is = ",C1.area())
print("circumference is", C1.circumference())
#C1.area()
#C1.circumference()
