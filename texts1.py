#import functions
print("welcome to the binary numbers program \n please choose from the menu")
menu=input("\n\nbinary to decimal\ndecimal to binary\nadd two binary numbers\nhexidecimal to binary\nbinary to hexidecimal\nhexidecimal to decimal\ndecimal to hexidecimal")

def db(decimal):
    list2=[]
    i=decimal
    while i>0:
        
        list2.append(i%2)
        i=i//2
    list2.reverse()
    return list2




if menu=="bd":
     binary=int(input("write a binary number"))
     strbinary= str(binary)
     listedbinary=list(strbinary)
     lenoflist=len(listedbinary)
     x=lenoflist
     x=x-1
     powerbase=2
     list1=[]
     ppower=0
     
     for i in listedbinary:
         if i =="1":
          ppower=ppower+pow(powerbase,x)
         x=x-1
          
     print(ppower)

if menu=="db":
    
    decimal=int(input("write a decimal number"))
    result=functions.db(decimal)
    
   
        
    print(result)    
        
if menu=="bb":
    b1=int(input("write a binary number"))
    b2=int(input("write another binary number"))
    strb1=str(b1)
    strb2=str(b2)
    listedb1=list(strb1)
    listedb2=list(strb2)
    
    a=1+0
    b=0+1
    c=0+0
    d=1+1
    carry=0
    list2=[]
    num=-1
    for i in listedb1:
        
        result=int(listedb1[num])+int(listedb2[num])+carry
        if result ==0:
            carry=0
            list2.append(0)
        elif result==1:
            carry=0
            list2.append(1)
        
        elif result==2:
            carry=1
            list2.append(0)
            list2.append(1)
        elif result==3:
            carry=1
            list2.append(1)
            list2.append(1)
        num=num-1
    print(list2)       

if menu=="hb":
    
    
    A=10
    B=11
    C=12
    D=13
    E=14
    list3=["A","B","C","D","E"]
    print(list3)
    hexinum=input("write a hexidecimal number")
    print(list3)
    listedhexinum=list(hexinum)
    list4=[]
    list2=[]
    num=0
    for i in listedhexinum:
        if i in list3:
            if i =="A":
             list2.append(10)  
            if i =="B":
              list2.append(11)
            if i =="C":
                list2.append(12)
            if i =="D":
                list2.append(13)
            if i =="E":
                list2.append(14)
            if i =="F":
                list2.append(15)
        else:
            list2.append(int(i))
    print(list2)
    #strhexinum=str(listedhexinum)    
    #inthexinum=int(strhexinum)
    list5=[]
    for i in list2:
        print('-------------------')
        print(i)
        print('-------------------')
        while i>0:
            remainder=i%2
            ans=i//2
            list4.append(remainder)
            #list4.append(ans)
            i=ans
        if len(list4)<4:
            list4.append(0)
            
        print(list4)         
        
    
        list5.append(list4)
        list4=[]
    print(list5)
         
if menu== "bh":
     binarynum=input("enter the binry number")
     #strbinarynum=str(binarynum)
     list3=[]
    
     listedbinarynum=list(binarynum)
     #print(listedbinarynum)
     len1=len(listedbinarynum)
     listedbinarynum.reverse()
     while len1%4 !=0:
        
         listedbinarynum.append(0)
         len1=len(listedbinarynum)
     #print(len1)
     listedbinarynum.reverse()
     
     i=-1
     k=-5
     while k >= (len1+1)*-1:
         
     
     
         lenoflist=listedbinarynum[i:k:-1]
         x=lenoflist
     
         print(x)
         powerbase=2
         power=0
         list1=[]
         result=0
     
         for a in x:
             
             
                 a=int(a)
                 result+=pow(powerbase,power)*a
             
                 power=power+1    
         list3.append(result)    
         #print(list1)
         i=i-4
         k=k-4
         if result==10:
             list3.append("A")
         elif result==11:
             list3.append("B")
         elif result==12:
             list3.append("C")
         elif result==13:
             list3.append("D")
         elif result==14:
             list3.append("E")
         elif result==15:
             list3.append("F")    
      
     print(list3)
      
if menu=="hd":
    hnum=input("enter a hexidecimal number")
    listedhnum=list(hnum)
    print(listedhnum)
    powerbase=16
    power=0
    result=0
    list2=[]
    list3=[]
    for i in listedhnum:
        if i =="A":
            list2.append(10)
        elif i =="B":
            list2.append(11)
        elif i =="C":
            list2.append(12)    
        elif i =="D":
            list2.append(13)
        elif i =="E":
            list2.append(14)
        elif i =="F":
            list2.append(15)
        else:
            list2.append(int(i))
    list2.reverse()          
    for i in list2:
                   
        result+=pow(powerbase,power)*i
        power=power+1      
          
    print(result)
    
if menu =="dh":   
    dnum=int(input("enter a decimal number"))
    list2=[]
    
    
    while dnum>0:
        remainder=dnum%16
        dnum=dnum//16
        list2.append(remainder)
        
            
    print(list2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
        
        