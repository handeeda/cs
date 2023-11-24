
      
import random

print ("i am thinking of a number between 1 and 10")
num1= int(input("guess the number"))

def function1(num):
        num2= random.randint(1,10)
        while num2:
         if num1!=num2:
          print(int(input("guess again")))
         else:
          print("thats right!!")
          
function1(num1)

    

import random

print ("i am thinking of a number between 1 and 10")
num1= int(input("guess the number"))
randomvalue=random.randint(1,10)
print(randomvalue)
def function1(num,num1):
        
        if num1>num:
          return -1#(int(input("too high")))
          
        elif num1<num:
          return 1#(int(input("too low")))
          
        else:
            return 0#("correct guess")
          
a=function1(num1,randomvalue)
while a!= 0:
    if a==-1:
        print("too low")
        num1=int(input("guess the number"))
    else:
        print("too high")
        num1=int(input("guess the number"))
    a=function1(num1,randomvalue)

import random
choice=(int(input("1. addition\n 2. subtraction\n enter 1 or 2:")))
add=1
sub=2
def function1(add,sub,choice):
    randomvalue=random.randint(5,20)
    randomvalue1=random.randint(5,20)
    print(randomvalue,randomvalue1)
    if choice ==add:
        user=int(input("add them together"))
        total1=randomvalue+randomvalue1
        if total1==user:
            print("correct")
        else:
            print(int(input("try again")))
                  
    else:
        user1=int(input("subtract them"))
        total2= randomvalue-randomvalue1
        if total2==user1:
            print("correct")
        else:
            print(int(input("try again")))
function1(add,sub,choice)        

    
    
    
    
    
    
    
    
    
    

