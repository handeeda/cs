countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti",
"Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
"Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
"Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco",
"Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan",
"Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe" ]
name= "countries of africa"
print(name)
score=0
heart=3
while len(countries) >0:
 msg="number of countries to guess:"
 print(msg)
 print(len(countries))
 print("score is:",score)
 print("number of hearts are:",heart)
 country= input("enter the name of country:")
 if country in countries:
     print("good guess")
     score=score+1
     countries.remove(country)
 else:
  print("invalid guess")
  heart=heart-1
  print(heart)
 if heart==0:
     print(end)
     break
     
     
 
 





