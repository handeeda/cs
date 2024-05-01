
import random
#people=int(input("Hat Cirle\nwrite the amount of people\nit must be even"))
#list_of_people= [num for num in range(0, 7)]

all_lists=[]
a=1
while a<people+1:
    persons_hat=[]
    for i in range(1):
        
        
#for i in range (1,people+1):
        
        persons_hat.append(a)
        #persons_hat.append(random.randint(0,1))
        a=a+1
    all_lists.append(persons_hat)
print("these are the people with their hat number\n",all_lists)


people_number=[]
hat_number=[]

for list1 in all_lists:
    people_number.append(list1[0])
    hat_number.append(list1[1])
print("people numbers are",people_number)
print("hat numbers are",hat_number)
len_hat_number=len(hat_number)


num=len_hat_number/2
num=int(num)
number_match=0
for i in range (num):
    if hat_number[i]== hat_number[num+i]:
        number_match+=1

number_match=number_match*2
print("the amount of people who sees the same number with their hat number is",number_match)
"""
#list_zero=[]
#list_zero[:len_hat_number+1]=0
#while hat_number!=list_zero:
    lists=[]
    
    
    lists.append(hat_number[index])
    lists.append(hat_number[num])
    hat_number[a]=0
    num=num+1
    a=a+1
print(lists)
        
[0,0,0,0,0,0]        
"""












