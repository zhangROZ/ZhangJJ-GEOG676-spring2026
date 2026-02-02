import math

textfile = r"D:\Spring2026_Courses\GEOG676\ZhangJJ-GEOG676-spring2026\lab_3\shape.txt"

with open (textfile,"r") as f:
    data = f.readlines()
print(data)

class Shape():
    def __init__(self):
        pass
    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return math.pi * self.r ** 2
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return self.h * self.b * 0.5

shape_list = []
for shapes in data:
    tmp = shapes.strip().split(",")
    shape_type = tmp[0]
    
    if shape_type == 'Rectangle':
        l = float(tmp[1])
        w = float(tmp[2])
        myobj = Rectangle(l, w)
    elif shape_type == 'Circle':
        r = float(tmp[1])
        myobj = Circle(r)
    elif shape_type == 'Triangle':
        b = float(tmp[1])
        h = float(tmp[2])
        myobj = Triangle(b, h)
    else:
        continue
    
    shape_list.append(myobj)

for i in shape_list:
    area = round(i.getArea(),2)
    print(f'{type(i).__name__}\'s area is {area}')