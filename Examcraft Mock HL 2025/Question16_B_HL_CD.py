#Question_16_B_HL
#Enter your name here: Hande Eda Ozdmeir

import random
print("Welcome to my shop")
total = 0
item_list = []
item_prices = []
stop=False

item_count=0
item_list=[]
total_item_price=[]


while "stop"==False:

    shopping_item=input("Please enter the item: ")
    item_list.append(shopping_item)
        
    item_price=int(input("Please enter the price of the item: "))
    total_item_price.append(item_price)
        
    total_answer=sum(total_item_price)
    print("The current total is €",total_answer)
    
    if shopping_item=="stop":
        

    
        







