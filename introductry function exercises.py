"""
fnum=int(input("write a number"))
snum=int(input("write the second number"))
def ag(a,b):
    total=a+b
    return total
print(ag(fnum,snum))

word=input("write a word:")
addword="un"
def newword(a,b):
    listeda=list(a)
    listedb=list(b)
    
    listeda.reverse()
    listeda.append(listedb)
    listeda.reverse()
    strlisteda=str(listeda)
    return strlisteda
print(newword(word,addword))

word=input("write a word and ill check if its palindrome or not:")

def palindrome_checker(a):
    listeda=list(a)
    listedb=list(a)
    listedb.reverse()
    
    if listeda==listedb:
        return True
    else:
        return False
        
print(palindrome_checker(word))

num=int(input("write numbers"))
even=0
odd=0
def count(a,ab,ac):
    stra=str(a)
    listeda=list(stra)
    for i in listeda:
        i=int(i)
        if i%2==0:
            ab=ab+1
        else:
            ac=ac+1
    return ab , ac
c=count(num,even,odd)
print(c)
def totals(a,b):
    c=count(num,even,odd)
    total=a+b
    return total
print(totals(c[0],c[1]))

"""
sentence=input("write a sentence:")
list1=[]
def sentence_to_decimal(a,b):
    
    listeda=list(a)
   
    for i in listeda:
        chrofa=ord(i)
        b.append(chrofa)
    return b
#print(sentence_to_decimal(sentence,list1))

sd=sentence_to_decimal(sentence,list1)
list1=[]

list3=[]
def decimal_to_binary(i):
    #b=sentence_to_decimal(sentence,list1)
    #sentence_to_decimal(sentence,list1)
    #listeda=list(a)
    #print(listeda)
    #for i in listeda:
    c=[]    
    while i !=0:
        i=i//2
        d=i%2
        c.append(d)
    c.reverse()
    return c
for i in sd:
    list3.append(decimal_to_binary(i))
print(list3)

for i in list3:
    lenofi=len(i)
    if lenofi <=7:
        i.reverse()
        i.append(0)
        i.reverse()
    if lenofi>7 and lenofi<=11:
        i.reverse()
        i[:6].append(0)
        i[:6].append(1)
        i.reverse()
            
    





















































