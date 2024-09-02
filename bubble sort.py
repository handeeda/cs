

numbers_list=input("please enter the numbers:")
numbers_list=list(numbers_list)
print("this is your list:",numbers_list)

menu=int(input("1.bubble sort\n2.linear search\n3.binary search:"))

if menu == 1:
    while numbers_list[0]>numbers_list[1]:
        for i in  range(len(numbers_list)-1):
            if numbers_list[i]>numbers_list[i+1]:
                temp=numbers_list[i]
                numbers_list[i]=numbers_list[i+1]
                numbers_list[i+1]=temp
                print(numbers_list)
        
   
if menu==2:
    target_value=int(input("write your target value:"))
    def linear_search(numl):
        
        #target_value=int(input("write your target value:"))
        for i in range(len(numl)):
            num=int(numl[i])
            if num==target_value:
            
                print("we found youre target value in your list!!\nnumber is:",target_value)
                return 1
        
        
                
        print("your target value is not in the list")
    linear_search(numbers_list)        
                









        
        
            