import random
name= input("welcome to the hangman game \n enter your name")
heart=4
points=0
hangman="--------------\n     0       |\n    /|\      |\n     |       |\n    / \      |\n"
hangman1="--------------\n     0       |\n    /|\      |\n     |       |\n    /        |\n"
hangman2="--------------\n     0       |\n    /|\      |\n     |       |\n             |\n"
hangman3="--------------\n     0       |\n    /|       |\n     |       |\n             |\n"
hangman4="--------------\n     0       |\n     |       |\n     |       |\n             |\n"
hangmanlist=[hangman1,hangman2,hangman3,hangman4]
print(hangman)
print(name,"you have ",heart,"hearts and",points,"points")
mode= input(name+" do you wanna play on hard mode or easy mode")
lword=["g","e","o","g","r","a","p","h","y"]
lword2=["g","e","o","g","r","a","p","h","y"]
lword3=["geography","computer"]
llword=["c","o","m","p","u","t","e","r"]
llword2=["c","o","m","p","u","t","e","r"]
ssword=["p","u","p","p","i","e","s"]
ssword2=["p","u","p","p","i","e","s"]
sword3=["puppies","money"]
sword=["m","o","n","e","y"]

h2=[]
lspace=["-"]*9
llspace=["-"]*8
ssspace=["-"]*7

geographylist=list("geography")
computerlist=list("computer")
puppieslist=list("puppies")
moneylist=list("money")
randomsword=random.choice(sword3)
randomlword=random.choice(lword3)
sspace=["-"]*len(randomsword)
#randomsword=random.choice(ssword,sword)
if randomlword == 'geography':
   
    randomlword=geographylist
else:
    
    randomlword=computerlist
a=0
if mode=="hard":
 
  while len(randomlword)> 0:
   if randomlword==geographylist:
      
    print(lspace)
    guess= input("make a guess")
    if guess not in randomlword:
       
       print(hangmanlist[a])
       a=a+1
       heart=heart-1
       print("you have",heart,"heart")
       print(lspace)
       input("make another guess")
    
       if heart==1:
           print("you lost")
           break
    if guess in randomlword:
       print(hangman)
       points=points+1
       print("you have",points,"point")
       print("you have",heart,"heart")
       for ch in range(len(randomlword)):
           if randomlword[ch] == guess:
              lspace[ch]=guess     
              lword2.remove(guess)
      
              print(guess,"deleted")
       
       
        #lspace.insert(c,guess)
       
       if lword2== []:
           print(randomlword)
           print("congrats you won!")
           break
   else:
    print(llspace)
    guess= input("make a guess")
    if guess not in randomlword:
       
       print(hangmanlist[a])
       a=a+1
       heart=heart-1
       print("you have",heart,"heart")
       print(llspace)
       input("make another guess")
    
       if heart==1:
           print("you lost")
           break
    if guess in randomlword:
       print(hangman)
       points=points+1
       print("you have",points,"point")
       print("you have",heart,"heart")
       for ch in range(len(randomlword)):
           if randomlword[ch] == guess:
              llspace[ch]=guess     
              llword2.remove(guess)
      
              print(guess,"deleted")
       
       
        #lspace.insert(c,guess)
       
       if llword2== []:
           print("congrats you won!")
           

if mode=="easy":
  if randomsword == 'money':
   sword2=list(randomsword)
   randomsword=moneylist
  else:
    
    randomsword=puppieslist
    sword2=list(puppieslist)
  a=0
  
  
  while len(randomsword)> 0:
      
          
    
 
       print(sspace)
       guess= input("make a guess")
       if guess not in randomsword:
       
        print(hangmanlist[a])
        a=a+1
        heart=heart-1
        print("you have",heart,"heart")
        print(sspace)
        input("make another guess")
    
        if heart==1:
           print("you lost")
           break
       if guess in randomsword:
        print(hangman)
        points=points+1
        print("you have",points,"point")
        print("you have",heart,"heart")
        for ch in range(len(randomsword)):
           if randomsword[ch] == guess:
              sspace[ch]=guess     
              sword2.remove(guess)
      
              print(guess,"deleted")
        print(sspace)
       
        #lspace.insert(c,guess)
       
       if sword2== []:
           print("congrats you won!")
           break








   