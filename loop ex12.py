
total=0
name= input("enter a name ")
print(name,"has been invited")
total=total+1
msg= input("wanna invite somebody else")
while msg=="y":
        name2= input("enter the name")
        print(name2,"has invited")
        total=total+1
        msg= input("wanna invite somebody else")
if msg=="n":
    print(total)
 
compnum=50
count=0
guess= int(input("enter your guess"))
a=True
while a :
    if guess<compnum:
     print ("too low")
     guess= int(input("enter your other guess"))
     count=count+1
    elif guess>compnum:
     print("too high")
     guess= int(input("enter your other guess"))
     count=count+1
    else:
     a=False
print("congrats it took you" ,count, "times to guess")

nmb=int(input("enter a number between 10 and 20 "))
a=True
while a:
    if nmb<10:
        print("too low")
        nmb=int(input("enter a number between 10 and 20 "))
    elif nmb>20:
        print("too high")
        nmb=int(input("enter a number between 10 and 20 "))
    else:
        a=False
print("thank you")

num=10
print("there are ",num,"green bottles hanging on the wall",num,"green bottles hanging on the wall, and if 1 green bottle should accidentaly fall")
num2=int(input("how many green bottles will be hanging on the wall"))
num=num-1
a=True
while a:
    if num2==num:
     print("there are ",num,"green bottles hanging on the wall",num,"green bottles hanging on the wall, and if 1 green bottle should accidentaly fall")
     num2=int(input("how many green bottles will be hanging on the wall"))
     num=num-1
     if num==0:
         a=False
         print("there are no more green bottles on the wall")
        
    elif num2!=num:
        num2=int(input("try again"))
   
        a=False
        print("there are no more green bottles on the wall")
        


 

    
    
    




    
    
        
 
 





