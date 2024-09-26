menu=("1.create a new file\n2. display the file\n3.add a new item to the file")
print(menu)
selection=int(input("select:"))


f=open("Numbers.txt","w")
f.write("1,2,3,4,5")
f.close()

fn=open("Names.txt","w")
fn.write("bob\nrob\njosh\ntate\n")
fn.close()

fn=open("C:/Users/23HOzdemir.ACC/Desktop/Names.txt","r")
readd=fn.read()
print(readd)
fn.close()

name=input("write a name:")
fn= open("C:/Users/23HOzdemir.ACC/Desktop/Names.txt","a")
fn.write(name)
fn.close()

fn=open("C:/Users/23HOzdemir.ACC/Desktop/Names.txt","r")
ready=fn.read()
print(ready)




