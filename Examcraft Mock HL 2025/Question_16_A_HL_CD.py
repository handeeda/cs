#Question_16_A_HL
#Enter your name here: Hande Eda Ozdemir

s = 0
vowel_count=0
digit_count=0
letter_count=0
words_count=0

vowels=["a","e","o","u","i"]

sentence = input("Please enter a sentence: ")

sentence=sentence.lower()
sentence_list=list(sentence)

for i in sentence_list:
    
    if i=="s":
        s=s+1
        
for i in sentence_list:
    if i in vowels:
        vowel_count=vowel_count+1
        
for i in sentence_list:
    if i.isdigit():
        digit_count=digit_count+1

    else:
        if i==" ":
            continue
        
        else:
            letter_count=letter_count+1
        

sentence_splitted=sentence.split()
for i in sentence_splitted:
    words_count=words_count+1


     
    
        
# print("the number of s's was: ",s)
# print("your lower case sentence is: ",sentence)
# print("the number of vowels was: ",vowel_count)

# print("the number of letter was: ",letter_count)
# print("the number of digits was: ",digit_count)

print("The number of words was: ",words_count)

