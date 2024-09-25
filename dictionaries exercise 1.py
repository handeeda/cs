book={}


menu=int(input("choose one\n1.write a sentence and count words\n2.write a word and count characters\n3.read from the text file:"))
if menu==1:
    text=input("Write a sentence:")
    texts=text.split()
    print(texts)
    #key_value=[]
    for i in texts:
        il=i.lower()
    
        if il in book:
            book[il]=book[il]+1
        else:
            book[il]=1
    print("word             count\n_________________________")
    for i,a in book.items():
        print(f"{i}                {a}")
    
elif menu==2:
    word=input("write a word:")
    wordl=list(word)
    for i in wordl:
        il=i.lower()
        if il in book:
            book[il]=book[il]+1
        else:
            book[il]=1
    print("character             count\n_________________________")
    for i,a in book.items():
        print(f"{i}                {a}")
    

elif menu==3:
    f=open("C:/Users/23HOzdemir.ACC/Desktop/book.txt","r")
    f_read=f.read()
    
    f_readl=list(f_read)
    print(f_readl)
    for i in f_readl:
        if i==" " or i== "\n":
            
            f_readl.remove(i)
    #print(f_readl)
    
        
        if i in book:
            book[i]=book[i]+1
        else:
            book[i]=1
    print("character             count\n_________________________")
    for i,a in book.items():
        print(f"{i}                {a}")
    


else:
    print("you didnt enter from the menu")
    print(menu)
    
    








