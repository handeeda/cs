word=input("write a word:")
prefix="un"
def add_un(word2,a):
    new_word=a+word2
    return(new_word)
function=add_un(word,prefix)
print(function)

print("_____________")

word=input("write a word:")
prefix="s"
def add_un(word2,a):
    new_word=word2+a
    return(new_word)
function=add_un(word,prefix)
print(function)

print("_____________")

import math


print("_____________")




menu=int(input("1.area of circle\n2.perimeter of circle\n3.area of rectangle\n4.perimeter of rectangle:"))
if menu==1:
    diameter=float(input("enter the diameter of the circle:"))
    def circle_area(d):
        answer=math.pi*d
        return (answer)
    function=circle_area(diameter)
    print("the area of a circle of diameter",diameter,"is",function)

if menu==2:
    diameter=float(input("enter the diameter of the circle:"))
    def circle_perimeter(d):
        answer=2*math.pi*d
        return (answer)
    function=circle_perimeter(diameter)
    print("the area of a circle of perimeter",diameter,"is",function)
    
if menu==3:
    height=float(input("enter the height:"))
    width=float(input("enter the width:"))
    def rectangle_area(h,w):
        answer=h*w
        return(answer)
    function=rectangle_area(height,width)
    print("the area of of the rectangle is",function)
    
if menu==4:
    height=float(input("enter the height:"))
    width=float(input("enter the width:"))
    def rectangle_perimeter(h,w):
        hw=h*w
        answer=2*hw
        
        return(answer)
    function=rectangle_perimeter(height,width)
    print("the -perimeter of of the rectangle is",function)
    
    
    
    
    
    




    