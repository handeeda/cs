my2DDictionary =[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(my2DDictionary)

print("___________")
row=int(input("please select a row:"))
column=int(input("please select a column:"))
print(my2DDictionary[row][column])
print("__________")

row1=int(input("which row would you like to choose:"))
display=my2DDictionary[row1]
print(display)
new_value=int(input("write your value:"))