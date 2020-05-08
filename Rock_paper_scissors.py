import random


# setting a function that checks if user wrote an integer
def int_check(question, low=None):
    global error
    if low is not None:
        error = ("Please write an integer more than "
                 + str(low-1))
    elif low is None:
        error = ("Please write an integer")

    while True:
        try:
            print()
            response = int(input(question))
            if low is not None and response < low:
                print(error)
                continue
            return response
        except ValueError:
            print(error)
            continue


def winning_system():
    global rounds_allowed
    global computers_choice


# creating a list of tokens
tokens = ["rock", "paper", "scissors"]

# initializing variables
rounds_allowed = int_check("How many rounds do you want to play? ", 2)
computers_choice = random.choice(tokens)
winning_system()
