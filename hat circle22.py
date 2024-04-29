import random
people=int(input("Hat Cirle\nwrite the amount of people"))
#list_of_people= [num for num in range(0, 7)]

all_lists=[]
a=0
while a<people+1:
    persons_hat=[]
    for i in range(1):
        
        
#for i in range (1,people+1):
        
        persons_hat.append(a)
        persons_hat.append(random.randint(0,1))
        a=a+1
    all_lists.append(persons_hat)
print("these are the people with their hat number\n",all_lists)


people_number=[]
hat_number=[]



