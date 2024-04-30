import random
people=int(input("Hat Cirle\nwrite the amount of people"))
for i in range(7):
     while i<7:
        
#for i in range (1,people+1):
        persons_hat=[]
        persons_hat.append(i)
        persons_hat.append(random.randint(0,1))
print("these are the people with their hat number\n",persons_hat)


