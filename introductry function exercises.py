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
"""
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
    listeda=list(a)
    for i in listeda:
        if i==2%
            ab=ab+1
        else:
            ac=ac+1
    return ab and ac
print(count(num,even,odd))

    







