words=["apple","banana","cherry"]

def return_first_letter(w):
    return w[0]
first_letter=list(map(return_first_letter,words))
print(first_letter)

def return_uppercase(w):
    upper= w.upper()
    
    return upper

uppercase=list(map(return_uppercase,words))
print(uppercase)

print("___________")
s=[" hello "," world "," phyton "]
def remove_space(s_list):
    return s_list.strip()

space=list(map(remove_space,s))
print(space)

print("___________")

celsius=[0,20,37,100]
def celsius_fahrenhiet(c):
    c=c*9/5
    c=c+32
    return c

f=list(map(celsius_fahrenhiet,celsius))
print(f)

    
