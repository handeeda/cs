 def AND_gate (a,b):
            if a==1 and b==1:
                return 1
            else:
                return 0

def NOT_gate (a):
            if a==1:
                return 0
            else:
                return 1
def OR_gate (a,b):
            if a==0 and b==0:
                return 0
            else:
                return 1            
            
def NOR_gate (a,b):
            if a==0 and b==0:
                return 1
            else:
                return 0            
            
def XNOR_gate (a,b):
            if a==0 and b==0:
                return 1
            elif a==1 and b==1:
                return 1
            else:
                return 0            
            
def XOR_gate (a,b):
            if a==0 and b==0:
                return 0
            elif a==1 and b==1:
                return 0
            else:
                return 1            
            
            
def NAND_gate (a,b):
            if a==1 and b==1:
                return 0
            else:
                return 1            
            
            
def half_adder(a,b):
    summ=XOR_gate(a,b)
    carry=AND_gate(a,b)
    return(summ,carry)
h=half_adder(a,b)

def full_adder (a,b,carry_in):
    h(a,b)
    h(carry_in,summ)
    d=OR_gate(carry,carry)
    return(summ,d)
f=full_adder(a,b,carry_in)

















            
            
            
            