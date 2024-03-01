menu= input("choose a gate\nAND\nNAND\nNOT\nOR\nNOR\nXOR\nXNOR")
if menu =="and":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 2 inputs write p:")
    
    if choose =="tt":
        print("A    B    AB\n0    0    0\n0    1    0\n1    0    0\n1    1    1")
    elif choose=="p":
        input1=int(input("write the first input:"))
        input2=int(input("write the second:")) 
        
   
        print(AND_gate(input1,input2))

if menu=="not":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 1 input write p:")
    if choose =="tt":
        print("A    A-\n0    1\n1    0")
    elif choose=="p":
        input1=int(input("write the input:"))
        
        print(NOT_gate(input1))
if menu=="or":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 2 inputs write p:")
    if choose =="tt":
        print("A    B    A+B\n0    0    0\n0    1    1\n1    0    1\n1    1    1")
    elif choose=="p":
        input1=int(input("write the first input:"))
        input2=int(input("write the second:"))     
        
   
        print(OR_gate(input1,input2))
        
if menu=="nor":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 2 inputs write p:")
    if choose =="tt":
        print("A    B    A+B-\n0    0    1\n0    1    0\n1    0    0\n1    1    0")
    elif choose=="p":
        input1=int(input("write the first input:"))
        input2=int(input("write the second:"))     
        
   
        print(NOR_gate(input1,input2))        
        
if menu=="xnor":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 2 inputs write p:")
    if choose =="tt":
        print("A    B    A+oB-\n0    0    1\n0    1    0\n1    0    0\n1    1    1")
    elif choose=="p":
        input1=int(input("write the first input:"))
        input2=int(input("write the second:"))     
        
   
        print(XNOR_gate(input1,input2))
        
        
        
if menu=="xor":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 2 inputs write p:")
    if choose =="tt":
        print("A    B    A+oB-\n0    0    0\n0    1    1\n1    0    1\n1    1    0")
    elif choose=="p":
        input1=int(input("write the first input:"))
        input2=int(input("write the second:"))     
        
   
        print(XNOR_gate(input1,input2))
        
        
        
if menu=="nand":
    choose=input("if you wanna see the truth table write tt\nif you wanna provide 2 inputs write p:")
    if choose =="tt":
        print("A    B    AB-\n0    0    1\n0    1    1\n1    0    1\n1    1    0")
    elif choose=="p":
        input1=int(input("write the first input:"))
        input2=int(input("write the second:"))     
        
   
        print(NAND_gate(input1,input2))           
        
        
        
        
        
        