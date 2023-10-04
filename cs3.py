a = int(input("enter the first number:"))
b = int(input("enter the second number:"))

if a>b:
    print (b)
    print(a)
elif b>a:
    print(a)
    print(b)
else:
    print("they are the same numbers")
    
a= int(input("enter a number under 20:"))
if a>=20:
    print("too high")
else:
    print("thank you")
    
number= int (input("enter a number between 10 and 20:"))
if number>10 and number<20:
    print("thank you")
else:
    print("incorrect")
    
colour= input("what is your favourite colour:")
a="red"
b="RED"
if colour== a or colour==b:
    print("i like red too")
else:
    print("i dont like" ,colour, "i like red")
   
weather= input("is it rainy outside:")
weather=weather.lower()
a="yes"
c="no"
if weather==c:
   print ("enjoy your day")
elif weather==a:
    weather2= input("is it windy:")
    if weather2==c:
     print("take an umbrella")
    else:
     print("its too windy for an umbrella")

age= int(input("what is your age:"))
if age>=18:
    print ("you can vote")
elif age==17:
    print("you can drive a car")
elif age ==16:
    print("you can buy a lottery ticket")
else:
    print ("you can do trick or treat")

number= int(input("enter a number:"))
if number<10:
    print("too low")
elif number>10 and number<20:
    print("correct")
else:
    print("too high")

number= int(input("enter 1,2 or 3:"))
if number==1:
    print("thank you")
elif number==2:
    print("well done")
elif number==3:
    print("correct")
else:
    print("error message")

name= input("write your name:")
for a in range (3):
 print(name)

name= input("write your name:")
number= int(input("enter a number:"))
for a in range (number):
    print(name)















