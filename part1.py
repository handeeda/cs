
print("this program will find the greatest number")
a= int(input("enter a number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print(a,"is the greatest number")
elif b>a and b>c:
    print(b,"is the greatest number")
else:
    print(c,"is the greatest number")
    

if a>b:
    if a>c:
        print(a,"is the greatest number")
    else:
        print(c,"is the greatest number")
else:
    if b>c:
        print(b,"is the greatest number")
    else:
        print(c,"is the greatest number")

print("this program will find the greatest number")
a= int(input("enter a number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
maximum=a
if maximum<b:
    maximum=b
if maximum<c:
    maximum=c
print(maximum,"is the greatest number")



