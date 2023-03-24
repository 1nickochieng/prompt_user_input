import random

exit = False
user_points = 0
computer_points = 0


while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper or scissors: ")
    computer_input = random.choice(options)
    
    if user_input == "exit":
        print("Game ended")
        exit = True
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer imput is rock")
            print("It is a tie")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer imput is paper")
            print("Computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer imput is scissors")
            print("You win")
            user_points += 1
            
    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer imput is rock")
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer imput is paper")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer imput is scissors")
            print("Computer wins")
            computer_points += 1
            
        
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer imput is rock")
            print("Computer wins!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer imput is paper")
            print("You win!")
            user_points =+ 1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer imput is scissors")
            print("It's a tie")
            
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Inavlid input!")
            