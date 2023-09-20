sports= ["basketball","football"]
msg= input("What is your favourite spor:")
sports.append(msg)
sports.sort()
print(sports)

subjects=["math","physic","art","pe","biology","business"]
msg= input("which subjects you dont like:")
subjects.remove(msg)
print(subjects)

colour=["blue","white","grey","red","black","orange","violet","green","yellow","pink"]
msg= int(input("Enter a number between 0 and 4:"))
if msg > 4:
  print("try again")
else:
  msg1= int(input("Enter a number between 5 and 9:"))
  if msg1<5 or msg1>9:
   print("try again")
  else:
   result= colour[msg:msg1]
   print(result)
   
numbers= ["365","894","937"]
print( numbers[0] +"\n"+number[1]+ "\n"+number[2])
msg= int(input("Enter a three digit number:"))
print(msg)
if msg=numbers:
 numbers.append(msg)
    



