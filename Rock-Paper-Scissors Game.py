import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        user_choice = user_choice.lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You Win!"
    else:
        return "Computer Wins!"
    
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result.startswith("You"):
            user_score += 1
        elif result.startswith("computer"):
            computer_score += 1
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    print(f"\nFinal score: You - {user_score}, computer - {computer_score}")
    
play_game()                             
            