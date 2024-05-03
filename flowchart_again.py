import random
colours_list=["pink","blue","white","yellow","green","black","orange"]
random_colours_list=[]
right_place=0
wrong_place=0
print(colours_list)

    
for i in range(4):
    a=random.choice(colours_list)
    random_colours_list.append(a)
    print(random_colours_list)
while right_place!=4:
    
    
    users_colour=input("select from the list")
    users_colour=users_colour.split()
    correct_colours_right_place=[]
    

    for i in range(4):
        if users_colour[i]==random_colours_list[i]:
            correct_colours_right_place.append(users_colour[i])
            right_place=right_place+1
    
    correct_colours_wrong_place=[]        
    b=0
    for i in users_colour:
        if i != random_colours_list[b]:
            
            correct_colours_wrong_place.append(i)
            wrong_place=wrong_place+1
                
    wrong_place=wrong_place-right_place
    print("correct colour correct place:",right_place,"\ncorrect colour wrong place:",wrong_place)

    
                
















