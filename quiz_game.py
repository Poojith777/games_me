print("Welcome to The Basic Quiz ")

playing = input("Do You want to Play ? ")

if playing.lower() != "yes":
    quit()

print("Let's get Started ")
score = 0
answer = input("What is the full form of TV?  ")
if answer.lower() == "television":
      print('Correct!')
      score += 1
else:
     print("Incorrect ")   
#2 
answer = input("What's the capital of Assam?  ")
if answer.lower() == "dispur":
      print('Correct!')
      score += 1
else:
     print("Incorrect ") 
#3
answer = input("What's the name of India's Longest River?  ")
if answer.lower() == "ganga":
      print('Correct!')
      score += 1
else:
     print("Incorrect ")      
#4
answer = input("What's the most populated Country in the World?  ")
if answer.lower() == "india":
      print('Correct!')
      score += 1
else:
     print("Incorrect ")      
#5  
answer = input("World's Most Used Social media App from 2020-Present?  ")
if answer.lower() == "instagram":
      print('Correct!')
      score += 1
else:
     print("Incorrect ") 
  
print("Your Score is " + str(score))
print("Your Acuracy is " + str((score / 5)*100) + "%.")   