def mean(num):
    length=len(num)
    summ=sum(num)
    cal=summ/length
    return cal

def median(num):
    summ=sum(num)
    cal=summ/2
    return cal

def mode(num):
    for i in num:
        c=num.count(i)
        if c>1:
            cal=c
            return cal
        
def frequency(num):
    f=float(input("write a frequency:"))
    length=len(num)
    cal=f/length
    return cal

def top5(num):
    list1=[]
    num.sort()
    num.reverse()
    for i in num:
        list1.append(i)
        if len(list1)==5:
            return list1
    
    
    

def last5(num):
    list1=[]
    num.sort()
    for i in num:
        list1.append(i)
        if len(list1)==5:
            return list1
    
    
def text(def1):
    f=open("C:/Users/23HOzdemir.ACC/Desktop/numbers.txt",'r')
    
    for line in f:
        
        for i in line:
            if i==" ":
               continue 
            else:
                a=int(i)
                text_num.append(a)
            
            
            
        
        result=def1(text_num)
        return result
    f.close()


def inputt(deff):
    for i in range(20):
        number=input("please enter youre numbers\nonly 20 or less\nenter number\nif youre done write stop:")
        if number=="stop":
            resultt=deff(all_numbers)
            return resultt
            break
        if number.isdigit():    
            all_numbers.append(float(number))
        
        else:
            print("error")
            
        
        
    

all_numbers=[]
text_num=[]
msg=("for this menu numbers have already been chosen")
menu=int(input("1.mean\n2.median\n3.mode\n4.frequency\n5.top 5 numbers\n6.last 5 numbers\nchoose from the menu:"))

if menu==1:
    print(msg)
    r=text(mean)
    print(r)
if menu==2:
    print(msg)
    r=text(median)
    print(r)
           
if menu ==3:
    print(msg)
    r=text(mode)
    print(r)
        
       
if menu==4:
    r=inputt(frequency)
    print(r)

if menu==5:
    for i in range(20):
        number=input("please enter youre numbers\nonly 20 or less\nenter number\nif youre done write stop:")
        if number=="stop":
            result=top5(all_numbers)
            print(result)
            break
        if number.isdigit():    
            all_numbers.append(float(number))
        
        else:
            print("error")
            
if menu==6:
    for i in range(20):
        number=input("please enter youre numbers\nonly 20 or less\nenter number\nif youre done write stop:")
        if number=="stop":
            result=last5(all_numbers)
            print(result)
            break
        if number.isdigit():    
            all_numbers.append(float(number))
        
        else:
            print("error")
            
    


    
    
            

    

        
    
    
    
        
        
            






















