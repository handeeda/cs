f=open("C:/Users/23HOzdemir.ACC/Downloads/exercise.csv","r")
line=f.readline()
print(line)

all_numbers=[]
length=0
num=[]
numbers=[]
start=0
a=1
b=0
firstpass=True
for line in f:
    
    line=list(line)

    line.remove("\n")
    len_of_line=len(line)
    for i in line:
        
        if i.isdigit() and ".":
            b=b+1
    
        
        elif i==",":
            print(b)
            while b-1>=0:
                b-1
                num.append(line[b])
            print(num)
            
        #numbers.append(line[start,b+1])
        #start=start+b
        
        
#1,2,3,4,5,6,7,        
        