"""
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


f=open("book1.csv","w")

mybooklist={"0":{"book":"to kill a mockingbird","author":"harper lee","year released":"1960"},"1":{"book":"a brief history of time","author":"stephen hawking","year released":"1988"},"2":{"book":"the great gatsby","author":"f.scott fitzgerald","year released":"1922"},"3":{"book":"the man who mistook his wife for a hat","author":"oliver sacks","year released":"1985"},"4":{"book":"pride and prejudice","author":"jane austen","year released":"1813"}}
for i in mybooklist:
    f.write(i)
    for key,value in mybooklist[i].items():

        f.write(",")
        f.write(value)
    f.write("\n")
f.close()
"""
print("______________")





