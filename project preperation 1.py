def mean(num):
    length=len(num)
    summ=sum(num)
    cal=summ/length
    return cal

def median(num):
    summ=sum(num)
    cal=summ/2
    return cal

def mode():
    for i in all_numbers:
        c=all_numbers.count(i)
        if c>1:
            
        
        
    

all_numbers=[]        
menu=int(input("1.mean\n2.median\n3.mode\nchoose from the menu:"))
print("please enter youre numbers\nonly 20 or less:")
if menu==1:
    for i in range (20):
        
        number=input("please enter number\nif youre done write stop:")
        if number=="stop":
            result=mean(all_numbers)
            print(result)
            break
        
            
        if number.isdigit():    
            all_numbers.append(float(number))
        
            
        else:
            print("error")
if menu==2:
    for i in range(20):
        number=input("please enter number\nif youre done write stop:")
        if number=="stop":
            result=median(all_numbers)
            print(result)
            break
        
            
        if number.isdigit():    
            all_numbers.append(float(number))
        
        else:
            print("error")

if menu ==3:
    for i in range(20):
        number=input("please enter number\nif youre done write stop:")
        if number=="stop":
    
    
    
        
        
            






















