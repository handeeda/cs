"""
nums=input("write 5 numbers:")
nums=nums.split()
#print(type(nums))
while len(nums)<5 or len(nums)>5:
    nums=input("numbers are less or greater than 5\nwrite 5 numbers:")
    print(nums)
    nums=nums.split()
    #print(type(nums))
    
for i in range(len(nums)):
    nums[i]=int(nums[i])
print(nums)

a=0
for i in nums:
    i=i+1
    nums[a]=i
    a=a+1
print(nums)


hours=[12,7,9,9,6,8,2]
milk=0.5
milk_cost=1.35
all_a=[]

for h in hours:
    a=0
        
    a=h*milk
    a=a*milk_cost
    all_a.append(a)

all_a=sum(all_a)

all_a=round(all_a,1)
print(all_a)


day=1
rainfall_cm_list=[]
while day!=8:
    print("write the daily rainfall cm for day",day)
    rainfall_cm=float(input("write here:"))
    rainfall_cm_list.append(rainfall_cm)
    day=day+1
total=sum(rainfall_cm_list)
print("the total rainfall cm is",total)

len_rainfall=len(rainfall_cm_list)
average=total/len_rainfall
average=round(average,2)
print("the average of rainfall cm is",average)


for i in rainfall_cm_list:
    if i>3.5:
        exceeded_amount=i-3.5
        exceeded_amount=round(exceeded_amount,2)
        print("the exceeded amount for",i,"is",exceeded_amount)
    else:
        continue
    
"""    
    
    
name_sales_person=[]
value_of_sale=[]
print("***Welcome***\nplease choose an option below:")
menu=int(input("\n1. enter sales data\n2. view total sales to date\n3. view maximum sale value of any staff member\n4. view minimum sale of any staff member\n5. view average sale value of any staff member\nif you are finished please write'done'or'DONE'")),

while menu!="done" or menu!="DONE":
    if menu=="1":
        name=input("enter the name of the sales person:")
        value=float(input("enter the value of the sale"))
    
        #num_of_people=int(input("enter the number of people:"))
    
    

    
    
    
    
    
    