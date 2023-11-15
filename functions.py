def number(a,b,c):
    
 if a>b and a>c:
    return a
 elif b>a and b>c:
    return b
 else:
    return c

def number2(a,b,c):
 if a>b:
    if a>c:
        return a
    else:
        return c
 else:
    if b>c:
        return b
    else:
        return c
    
def number3(a,b,c):
 maximum=a
 
 if maximum<b:    
     maximum=b
 if maximum<c:   
    maximum=c 
 
 return maximum
