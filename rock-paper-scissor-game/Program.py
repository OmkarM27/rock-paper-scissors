import random

choices = ["rock" , "paper" , "scissors"]
user_win = 0
computer_win = 0

while True:
    user_choice = input("Enter rock , paper or scissors(or 'exit' to quit) : ").lower()
  
    if user_choice == 'exit' :
        print("Thanks for playing")
        break
    
    
    if user_choice not in choices:
        print("invalud input. Try again")
        continue
    
    
    computer_choice = random.choice(choices)
    
    print(f"computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("its a TIE")
    elif ((user_choice == "rock" and computer_choice == "scissors") or 
              (user_choice == "scissors" and computer_choice == "paper") or
              (user_choice == "paper" and computer_choice == "rock")):
        print("You win")  
        user_win +=1  
        
    else:
        print("You lose")
        computer_win +=1