takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00
all_price_list=[]
total=[]

users_name=input("whats youre name?")
print("Welcome to the takeaway delivery service.")
print("Here's our menu.")

for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
def get_bill_total(k,b):    
    for i in takeaway_menu:
        price_of_food=[]
        price_of_food.append(i)
        index_i=takeaway_menu.index(i)
        price_of_food.append(takeaway_prices[index_i])
        k.append(price_of_food)
    print(k)

    
    
    for i in k:
        for a in order:
            if i[0]==takeaway_menu[a-1]:
                b.append(i[1])
get_bill_total(all_price_list,total)

total=sum(total)
total=total+delivery_fee
if total<=free_delivery_price:
    print("the total cost with the delivery fee is",total)
else:
    total=total-delivery_fee
    print("your delivery is free!!\nthe total cost is",total)
        
print("Thank you your order",users_name,", is as follows")
for item in order:
    print(takeaway_menu[item-1])    


    


            
            
    
    
    
    














