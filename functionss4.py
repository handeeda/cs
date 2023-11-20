
def slist(numbers):
    a=0
    for number in numbers:
      a=a+number   
    return a
list1=[8,2,3,0,7]
result=slist(list1)
print(result)

def slist(numbers):
    a=1
    for number in numbers:
      a=a*number   
    return a
list1=[8,2,3,-1,7]
result=slist(list1)
print(result)

def slist(words):
    length_string = len(words)
    
    for num in range (0,8,1):
       print(words[num])
       
       
       
list1=["1","2","3","4","a","b","c","d"]
slist(list1)

str1= "the quick Brow Fox"
upper=0
lower=0
for i in str1:
    
    if i.isupper():
        
        upper=upper+1
    else:
        
        lower=lower+1
        
print(upper)
print(lower)


def list1(numbers):
    list2=[]   
    for i in numbers:
        if i not in list2:
           list2.append(i)
        else:
            continue
    return list2

a=list1([1,2,3,3,3,3,4,5])
print(a)


def list1(numbers):
    list2=[]
    for i in numbers:
        if i%2==0:
            list2.append(i)
        else:
            continue
    return list2
a=list1([1,2,3,4,5,6,7,8,9])
print(a)
            








