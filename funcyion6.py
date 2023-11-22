import function5
num1=int(input("enter a number"))

function5.number(num1)

import random
num= int(input("pick a lower number"))
num1= int(input("pick a higher number"))

def lowandhigh(low,high):
   
     comp_num=random.randint(low,high)
     return comp_num
     
a=lowandhigh(num,num1)
print(a)
    
    
    

