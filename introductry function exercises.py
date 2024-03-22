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
"""
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

#for i in list3:
    stri=str(i)
    listedi=list(stri)
    lenofi=len(listedi)
    if lenofi <=7:
        listedi.reverse()
        listedi.append(0)
        listedi.reverse()
    if lenofi>7 and lenofi<=11:
        listedi.insert(5,0)
        listedi.insert(5,1)
        listedi.reverse()
        listedi.append(0)
        listedi.append(1)
        listedi.append(1)
        listedi.reverse()
    if lenofi>11 and lenofi<=16:
        listedi.insert(10,0)
        listedi.insert(10,1)
        listedi.insert(4,0)
        listedi.insert(4,1)
        listedi.reverse()
        listedi.append(0)
        listedi.append(1)
        listedi.append(1)
        listedi.append(1)
        listedi.reverse()
    if lenofi>16:
        listedi.insert(15,0)
        listedi.insert(15,1)
        listedi.insert(9,0)
        listedi.insert(9,1)
        listedi.insert(3,0)
        listedi.insert(3,1)
        listedi.reverse()
        listedi.append(0)
        listedi.append(1)
        listedi.append(1)
        listedi.append(1)
        listedi.append(1)
        listedi.reverse()
print(list3)            
 """   

def utf_to_binary(listt):
    #for i in listt:
        listedi=list(listt)
        lenofi=len(listedi)
        print(lenofi)
        if lenofi <=8:
            listedi.remove(listedi[0])
        elif lenofi>8 and lenofi<=16:
            output = listedi[:2] +listedi[12:16]
            del listedi[:2]
            #listedi.remove(listedi[0])
            #listedi.remove(listedi[1])
            #listedi.remove(listedi[2])
            del listedi[4:5]
            #listedi.remove(listedi[7])
            #listedi.remove(listedi[8])
            
        if lenofi>16 and lenofi<=24:
            output = listedi[4:7] +listedi[12:16]
            #listedi.remove(listedi[0])
            #listedi.remove(listedi[1])
            #listedi.remove(listedi[2])
            #listedi.remove(listedi[3])
            del listedi[3:4]
            #listedi.remove(listedi[7])
            #listedi.remove(listedi[8])
            listedi.remove(listedi[15])
            listedi.remove(listedi[16])
        if lenofi>24:
            listedi.remove(listedi[0])
            listedi.remove(listedi[1])
            listedi.remove(listedi[2])
            listedi.remove(listedi[3])
            listedi.remove(listedi[4])
            listedi.remove(listedi[7])
            listedi.remove(listedi[8])
            listedi.remove(listedi[15])
            listedi.remove(listedi[16])
            listedi.remove(listedi[23])
            listedi.remove(listedi[24])
        return listedi
print(utf_to_binary(sentence))        
        
1100100001010101


















































