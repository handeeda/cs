user_ID=[]
a=0
s=0
menu=int(input("1)create a new user ID:\n2)change password:\n3)display all user IDs:\n4)quit:"))
while s==0:
    if menu==1:
        ID=int(input("write a new ID:"))
    #while menu==1:
        #ID=int(input("write a new ID:"))
    
    #while menu==1:
        for i in range(1):
            person=[]
            if ID in user_ID:
                print("the ID is already in the list")
                ID=int(input("write a new ID:"))
            else:
                person.append(ID)
                password=input("enter a password with at least 8 characters:")
                password_len=len(password)
        
                if password_len<8:
                    print("youre password is too short..")
                    password=input("enter a password with at least 8 characters:")
        
                elif password_len>=8:
                    person.append(password)
                    #print(person)
                    print("youre new ID has been created")
                    user_ID.append(person)
                #print(user_ID)
                    menu=int(input("1)create a new user ID:\n2)change password:\n3)display all user IDs:\n4)quit:"))            
            
                else:
                    print("youre password is invalid..")
                    password=input("enter a password with at least 8 characters:")

    if menu==2:
    #ID=int(input("write your ID:"))
        ID=int(input("write your ID:"))
    #while menu==2:
        
        #a=0
        for i in user_ID:
            for p in i:
                if ID in i:
                    password=input("enter a password with at least 8 characters:")
                    if password_len<8:
                       print("youre password is too short..")
                       password=input("enter a password with at least 8 characters:")
        
                    elif password_len>=8:
                        for p in i:
                            if p==ID:
                                index=i.index(p)
                                del i[index+1]
                                i.insert(index+1,password)
                                print(user_ID)
                                print("your password has been changed!!")
                        menu=int(input("1)create a new user ID:\n2)change password:\n3)display all user IDs:\n4)quit:"))            
            
                    else:
                        print("youre password is invalid..")
                        password=input("enter a password with at least 8 characters:")
            
        
                else:
                    #a=a+1
                    print("this ID doesnt exist..")
                    ID=int(input("write your ID:"))
            
            

        




    