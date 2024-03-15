import random

def guess_number(x):
    random_num = random.randint(1, x)
    user_num = 0
    while user_num != random_num:
        user_num = int(input(f"Guess a number from 1 to {x}: "))
        if user_num < random_num:
            print("Not quite there yet. Number is low. Enter again: ")
        elif user_num > random_num:
            print("Hmm!. Number is high. Enter again: ")
    print(f"Yayy! You guessed right, the number is {random_num}")



    