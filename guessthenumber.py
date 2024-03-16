import random

def guess_number(x):
    random_num = random.randint(1, x)
    user_num = 0
    while user_num != random_num:
        user_num = int(input(f"Guess a number from 1 to {x}: "))
        
        ####
        # This loop in the code will prompt the user to choose enter an int from 0 to x
        # No negative numbers and no numbers greater than x
        while user_num < 0 or user_num > x:
            print ( f" Please enter a valid guess between 1 and {x}. " )
            user_num = int(input(f"Guess a number from 1 to {x}: "))
        else: 
            break 
        ####
        
        if user_num < random_num:
            print("Not quite there yet. Number is low. Enter again: ")
        elif user_num > random_num:
            print("Hmm!. Number is high. Enter again: ")
    print(f"Yayy! You guessed right, the number is {random_num}")

guess_number(3)


    
