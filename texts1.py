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
      
      
      
      
      
      
      
      
      
      
      
        
        