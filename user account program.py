user_ID=[]
not_finished=False
password_line=False
menu=int(input("1)create a new user ID:\n2)change password:\n3)display all user IDs:\n4)quit:"))

while not not_finished:
    
    if menu==1:
        ID=int(input("write a new ID:"))
        y=False
        while not y:
            person=[]
            if ID in user_ID:
                print("the ID is already in the list")
                ID=int(input("write a new ID:"))
            else:
                person.append(ID)
                
                password=input("enter a password with at least 8 characters:")
                while not password_line:
                    password_len=len(password)
                    if password_len<8:
                        print("youre password is too short..")
                        password=input("enter a password with at least 8 characters:")
                    else:
                        print("youre password is valid!!")
                        password_line=True
        
                if password_len>=8:
                    person.append(password)
                    #print(person)
                    print("youre new ID has been created")
                    user_ID.append(person)
                    print(user_ID)
                    y=True
                    #print(user_ID)
                    menu=int(input("1)create a new user ID:\n2)change password:\n3)display all user IDs:\n4)quit:"))            
            

    if menu==2:
        #ID=int(input("write your ID:"))
        
        y=False
        password_loop=False
        #while menu==2:
        
            #a=0
        while not y:
            ID=int(input("write your ID:"))
            for i in user_ID:
                if ID in i:
                    while not password_loop:
                        password=input("enter a password with at least 8 characters:")
                        password_len=len(password)
                        if password_len<8:
                        
                            print("youre password is too short..")
                            #password=input("enter a password with at least 8 characters:")
        
                        else:
                        
                            for p in i:
                                if p==ID:
                                    index=i.index(p)
                                    del i[index+1]
                                    i.insert(index+1,password)
                                    print(user_ID)
                                    print("your password has been changed!!")
                            menu=int(input("1)create a new user ID:\n2)change password:\n3)display all user IDs:\n4)quit:"))            
                            y=True
                        #else:
                            #print("youre password is invalid..")
                            #password=input("enter a password with at least 8 characters:")
            
        
            if not y:
                print("this ID doesnt exist..")
                
            
            

        




    