import random

upper_bound = input("Type a Number: ")

if upper_bound.isdigit():
    upper_bound = int(upper_bound)
    
    if upper_bound <= 0:
        print('Enter a number larger than Zero in the next attempt.')
        quit()
else:
    print('Please input a number next time.')  
    quit()      
        
random_number = random.randint(0,upper_bound)
guesses = 0
#print(random_number)

while True:
    guesses += 1
    user_guess = input("Make a guess of the number generated:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print('Please input a number next time.')  
        continue
    
    if user_guess == random_number :
        print("You Guessed it Correct!!")
        break    
    elif user_guess > random_number:
            print("You Guessed a bit higher number")
    else:
            print("You Guessed a bit Lower number")   
        
print("You Guessed it in ",guesses,"guesses")
#basically "," is eqv to  writing "+ str()"           
