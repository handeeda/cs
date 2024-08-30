def swap1(n):
            i=0
            c=1
            x=n(i)
            n.insert(c,x)
            i=i+1
            c=c+1
            

numbers_list=input("please enter the numbers:")
numbers_list=list(numbers_list)
print("this is your list:",numbers_list)
numbers_list1=numbers_list

for i in  range(len(numbers_list)-1):
    if numbers_list[i]<numbers_list[i+1]:
        temp=numbers_list[i]
        numbers_list[i]=numbers_list[i+1]
        numbers_list[i+1]=temp
        
        numbers_list[i],numbers_list[i+1]=numbers_list[i+1],numbers_list[i]
        
#while numbers_list1!=numbers_list:
    #a=0
    #if numbers_list1[a]!=numbers_list[a]:
        #swap1(numbers_list1)
        #print(numbers.list1)
#print("done:)")

        
        
            