import random

print("Welcome to my rock, paper, scissors game!!!")
def rps_game():
    computer_choice = random.choice(['r', 'p', 's'])
    user_choice = str(input("Type 'r' for rock, 'p' for paper, and 's' for scissors: "))
    if user_choice != computer_choice:
        if (user_choice == "p" and computer_choice == "s") or (user_choice == "r" and computer_choice == "p") or (user_choice == "s" and computer_choice == "r"):
            print(f"You lost! The computer played {computer_choice}")
        else:
            print(f"Yayy! You won. The computer played {computer_choice}")
        
    else:
        print(f"This is a draw! You both played {computer_choice}. Now play again: ")
        rps_game()

rps_game()
    