counts={}#create a dictionary
counts2=dict({})#create a dictionary
print(counts)
print(counts2)
#to add a key value pair
counts["games"]=24
print(counts)
counts["players"]=200
print(counts)
#to find the number of items in a dictionary
print(len(counts))
#to check if a key is in a dictionary

if "players" in counts: #boolean check
    print("players found")
if "managers" not in counts: #returns true or false
    print("managers not found")
#to print a value
print(counts["games"]) # returns games value - error if no key
print(counts)
print(counts.get("games")) # returns games value - returns none if no key
print(counts)
print(count.pop("games")) # returns games value - -removes items from list
print(counts)
