f=open("C:/Users/23HOzdemir.ACC/Downloads/exercise.csv","r")
line=f.readline()
print(line)

all_numbers=[]
length=0
numa=[]
numbers=[]
start=0



for line in f:
    
    line=list(line)
    len_of_line=len(line)
    for a in range (len_of_line):
        numbers.append(a)
    print(numbers)    
    for i in line:
        if i.isdigit():
            i=int(i)
            length=length+1
            
            #numa.append(i)
            #all_numbers.append(numa)
            #continue
        elif i ==",":
            
            
            #else:
            #for i in line:
            numa.append(line[start:length])
            start=length+1
            print(numa,"this is num 1")
print(all_numbers)
            