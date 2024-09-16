f=open("C:/Users/23HOzdemir.ACC/Downloads/exercise.csv","r")
line=f.readline()
print(line)

all_numbers=[]
length=0

numbers=[]
start=0
a=1
b=0
firstpass=True
for line in f:
    
    line=list(line)
    line.remove("\n")
    len_of_line=len(line)
    #for a in range (len_of_line):
        #numbers.append(a)
    #print(numbers)    
    for i in line:
        if i.isdigit() or i==".":
            #i=int(i)
            length=length+1
            
            #numa.append(i)
            #all_numbers.append(numa)
            #continue
        elif i ==",":
            numa=[]
            if firstpass==True:
                b=0
                firstpass=False
            else:
                b=b+1
            numa.append(line[start:length+b])#look at here
            #look at here
            start=length+1
            #if bh in numa:
                #numa.remove(",")
            all_numbers.append(numa)
            print(numa,"this is num",a)
            a=a+1
#print(all_numbers)
            
            
            
            
            