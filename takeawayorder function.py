def get_bill_total(tm,apl,o,tp):
    for i in tm:
            price_of_food=[]
            price_of_food.append(i)
            index_i=tm.index(i)
            price_of_food.append(tp[index_i])
            apl.append(price_of_food)
    print(apl)

#list_of_total=[]
    count=1
    for i in apl:
    #for a in i:
        a=i[0]
    
        
        aindex=i.index(a)
        aindex=aindex+count
        count=count+1
        if aindex in o:
            total.append(i[1])
        