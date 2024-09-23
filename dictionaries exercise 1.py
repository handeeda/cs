book={}
text=input("Write a sentence:")
texts=text.split()
print(texts)
check=True
for i in texts:
    if i in book:
        i.lower()
        book[i]=book[i]+1
    else:
        book[i]=1
print(book)


