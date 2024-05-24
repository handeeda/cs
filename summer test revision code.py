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


msg=("***Welcome***\nplease choose an option below \n1. enter sales data\n2. view total sales to date\n3. view maximum sale value of any staff member\n4. view minimum sale of any staff member\n5. view average sale value of any staff member\nif you are finished please write'done'or'DONE'")
print(msg)
menu=input("write your option:")
a=0
while a==0:
    while menu!="done" and menu!="DONE":
    
    
        if menu=="1":
            name=input("enter the name of the sales person:")
            name_sales_person.append(name)
            print(name_sales_person)
            value=float(input("enter the value of the sale"))
            while value!= float(value) and value!= int(value):
                print("this is not a number")
                value=float(input("enter the value of the sale"))
            
            value_of_sale.append(value)
            print(value_of_sale)
            print(msg)
            menu=input("write your option:")
        
        elif menu=="2":
            summ=sum(value_of_sale)
            print("your value of the total sales is",summ)
            print(msg)
            menu=input("write your option:")
        
        elif menu=="3":
            name2=input("which person?:")
            name_sales_person2=name_sales_person.copy()
            value_of_sale2=value_of_sale.copy()
            all_value1=[]
            if name2 in name_sales_person2:
            
                while name2 in name_sales_person2:
                    #for name2 in name_sales_person:
                
                    persons_index=name_sales_person2.index(name2)
                    value1=value_of_sale2[persons_index]
                    name_sales_person2.remove(name2)
                    value_of_sale2.remove(value1)
                    all_value1.append(value1)
                    #if name2 in name_sales_person:
                
                max_value=max(all_value1)
                print(name2,"'s maximum value is",max_value)
                menu=input("write your option:")
    
                
            
            else:
                print(name2,"is not in list")
                print(msg)
                menu=input("write your option:")
    
        elif menu=="4":
            name2=input("which person?:")
            value_of_sale3=value_of_sale.copy()
            name_sales_person3=name_sales_person.copy()
            all_value1=[]
            if name2 in name_sales_person3:
                while name2 in name_sales_person3:
                
                    persons_index=name_sales_person3.index(name2)
                    value1=value_of_sale3[persons_index]
                    name_sales_person3.remove(name2)
                    value_of_sale3.remove(value1)
                    all_value1.append(value1)
                min_value=min(all_value1)
                print(name2,"'s minimum value is",min_value)
                menu=input("write your option:")
    
                
            
            else:
                print(name2,"is not in list")
                print(msg)
                menu=input("write your option:")
            
        elif menu=="5":
            name2=input("which person?:")
            value_of_sale4=value_of_sale.copy()
            name_sales_person4=name_sales_person.copy()
            all_value1=[]
            if name2 in name_sales_person4:
                while name2 in name_sales_person4:
                
                    persons_index=name_sales_person4.index(name2)
                    value1=value_of_sale4[persons_index]
                    name_sales_person4.remove(name2)
                    value_of_sale4.remove(value1)
                    all_value1.append(value1)
                
                len_all_value1=len(all_value1)
                sum_all_value1=sum(all_value1)
                sum_all_value1=sum_all_value1/len_all_value1
                sum_all_value1=round(sum_all_value1,2)
                print(name2,"'s value of their avergae sales is",sum_all_value1)
                print(msg)
                menu=input("write your option")
    
                
            
            else:
                print(name2,"is not in list")
                print(msg)
                menu=input("write your option:")
    
    
        else:
            print(menu,"is not an option")
            print(msg)
            menu=input("write your option:")
   
    break         
   
        
       
    
    
    

    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    