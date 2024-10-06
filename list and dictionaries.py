
my2Dlist =[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(my2Dlist)

print("___________")
row=int(input("please select a row:"))
column=int(input("please select a column:"))
print(my2Dlist[row][column])
print("__________")

row1=int(input("which row would you like to choose:"))
display=my2Dlist[row1]
print(display)
new_value=int(input("write your value:"))
display.append(new_value)
print(display)

print("______________")
print(my2Dlist)
row=int(input("which row do you want to display?"))
print(my2Dlist[row])
column=int(input("which column do you want to display?"))
print(my2Dlist[row][column])
menu=input("do you want to change a value?")
if menu =="yes":
    new_value=int(input("write a new value"))
    my2Dlist[row][column]=new_value
    print("here is your row:",my2Dlist[row])
else:
    print("ok, nothing has changed..")
    print(my2Dlist[row])
print("______________")

my2DDictionary = {"Jhon":{"N":3056,"S":8463,"E":8441,"W":2694},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
#print(my2DDictionary["Jhon"])
#print(my2DDictionary["Jhon"]["N"])

name2=input("Anne,Fiona,Tom,John\nwrite a name:")
region=input("N,S,E,W\nwrite a region:")
region_value=input("give a region value:")
my2DDictionary[name2][region]=region_value
print(my2DDictionary[name2])

people_list=[]
for i in range (4):
    #name=[]
    people=[]
    name=input("enter a name:")
    #name.append(name1)
    people.append(name)
    #age=[]
    age=int(input("enter their age:"))
    people.append(age)
    shoe_size=float(input("enter their shoe size:"))
    people.append(shoe_size)
    people_list.append(people)
print(people_list)

namee=input("write a name for display:")
for i in people_list:
    if namee in i:
        print(i)

print("_____________")

for i in people_list:
    print(i[0],",",i[1])
    
print("________________")

name2=input("write the name that you want to delete:")
for i in people_list:
    if i[0]==name2:
        people_list.remove(i)
        print(people_list)
    #else:
        #print("this name is not in the list")
        #name2=input("write the name that you want to delete:")
        

        
    
    
    
    
    

    
        
        


    

























