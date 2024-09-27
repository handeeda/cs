menu=("1.create a new file\n2. display the file\n3.add a new item to the file")
print(menu)
selection=input("select:")
a=1
while a==1:
    if selection=="1":
        name=input("create a file name:")
        item=input("write an item ")
        f=open(name+".txt","w")
        f.write(item)
        f.close()
        print(menu)
        selection=input("select:")


    elif selection=="2":
        fn=open("C:/Users/23HOzdemir.ACC/Desktop/"+name+".txt","r")
        readd=fn.read()
        print(readd)
        fn.close()
        selection=input("select:")

    elif selection=="3":
    
        item1=input("write an item:")
        fn= open("C:/Users/23HOzdemir.ACC/Desktop/"+name+".txt","a")
        fn.write(item1)
        fn.close()
        selection=input("select:")

    elif menu=="stop":
        break


    else:
        print("error please enter again")
        selection=input("select:")

print("____________________")
