"""
string=input("write a string")
vowels=["a","e","o","u","i"]
listed=list(string)
for letter in string:
 if letter in vowels:
    counted=listed.count(vowels)
    print(counted)
 else:
    print("there is no vowel")

a=input("write")

b=a[::-1]
print(b)
"""
name=input("write your name")
a=name.isupper()
if a==name:
    print(a)
else:
    print("there is no uer string")



string=input("enter something")
a=string[::-1]
print(a)

a=int(input("enter something"))
listed=list(a)
b=0
if b==0:
    deleted= del listed[1 ]
    print(deleted)








