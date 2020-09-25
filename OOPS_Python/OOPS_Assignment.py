'''
Create Two classes , parentClass and childclass named Area and Area2 respectively.
In parentclass , define a method area1 and in that method Implement Area of
rectangle(length * breadth) , In ChildClass Area2 , construct a constructor
def init(self, length ,breadth, height): , define override method that is area1
and implement the area of triangle(0.5 * length *breadth ) , and also implement
a method volume to print volume of rectangle(length * breadth * heigth). and
At last create an object and pass the values for Area2 and call area1() and
volume() methods and print the result.
'''
class Area1:
    def areal(self,length,breadth):
        self.length  = length
        self.breadth = breadth
        return self.length * self.breadth
        
class Area2(Area1):
    def __init__(self,length,breadth,height):
        self.length  = length
        self.breadth = breadth
        self.height  = height
    def area1(self):
        return 0.5 * self.length * self.breadth
    def volume(self):
        return self.length * self.breadth * self.height
a = Area2(5,10,15)
print(a.area1())
print(a.volume())
