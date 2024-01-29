import functions
print("welcome to the binary numbers program \n please choose from the menu")
menu=input("\n\nbinary to decimal\ndecimal to binary\nadd two binary numbers\nbinary to hexidecimal\nhexidecimal to binary")

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
    hexinum=input("write a hexidecimal number")
    
    listedhexinum=list(hexinum)
    inthexinum=int(hexinum)
   
    num=0
    
    list2=[]
    while inthexinum>0:
        remainder=listedhexinum[num]%2
        ans=listedhexinum[num]//2
        list2.append(remainder)
        list2.append(ans)
        num=num+1
    print(list2)         
        
        
         
    
      
      
      
      
      
      
      
      
      
      
        
        