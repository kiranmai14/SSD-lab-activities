class Triangle(object):
    def __init__(self,b,h):
        self.base = b
        self.height = h
    def area(self):
        return (0.5)*self.base*self.height

class TriangleChild(Triangle):
    def __init__(self,b,s):
        super().__init__(b,s)
    def area(self):
        return self.base*self.height
    def getHeight(self):
        return self.height

tri = Triangle(2,3)
print(tri.area())

trichild = TriangleChild(2,3)
print(trichild.area())

print(trichild.getHeight())

