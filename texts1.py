print("welcome to the binary numbers program \n please choose from the menu")
menu=input("\n\nbinary to decimal\ndecimal to binary\nadd two binary numbers")




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
    list2=[]
    decimal=int(input("write a decimal number"))
    list1=[]
    list1.append(decimal)
    i=decimal
    while i>0:
        
        list2.append(i%2)
        i=i//2
        
    print(list2)    
        
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
        
        print(result)
        num=num-1
        if result==a or result==b:
            list2.append(1)
            
        elif result==c:
            list2.append(0)
        elif result==2:
            carry=carry+1
            list2.append(0)
            
    print(list2)       
     
      
      
      
      
      
      
      
      
      
      
        
        