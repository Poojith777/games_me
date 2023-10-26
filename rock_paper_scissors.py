import random

user_points = 0
comp_points = 0 

options = ["rock", "paper" ,"scissors"]

while True:
    user_turn = input("Please play Rock/Paper/Scissors or enter q to quit ").lower()
    if user_turn == "q":
        break
    
    if user_turn not in options:
        continue
    
    random_num = random.randint(0,2)    
    #rock = 0 ,paper = 1,scissor = 2 
    comp_pick = options[random_num]
    print("Computers Picked", comp_pick +".")

    if user_turn =="rock" and comp_pick == "scissors" :
        print ("You win!")
        user_points += 1 
        
    elif user_turn =="paper" and comp_pick == "rock" :
        print ("You win!")
        user_points += 1
         
    elif user_turn =="scissors" and comp_pick == "paper" :
        print ("You win!")
        user_points += 1         
    elif user_turn == comp_pick :
        print("it's Tied!")    
        user_points += 1 
        comp_points += 1
    else :
        print("Computer won") 
        comp_points += 1

print("You won",user_points,"times.")
print("Computer won",comp_points,"times.")    
print("Good  Game 🤝 ")    