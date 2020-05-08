import random


# setting up a function that decorates all my statements
def decoration_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()

# setting up a function that checks if user wrote an integer
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


# setting up a function that checks what item did user chose
def item_check():
    global users_choice

    users_choice = input ("Please chose rock (r), paper (p) or scissors (s): ")
    if users_choice == "rock" or users_choice == "r" or users_choice == "Rock" or users_choice == "ROCK" or users_choice == "R":
        users_choice = "rock"
    elif users_choice == "paper" or users_choice == "Paper" or users_choice == "PAPER" or users_choice == "p" or users_choice == "P":
        users_choice = "paper"
    elif users_choice == "scissors" or users_choice == "Scissors" or users_choice == "SCISSORS" or users_choice == "s" or users_choice == "S":
        users_choice = "scissors"
    else:
        print("Sorry, I don't understand")
        item_check()
    return users_choice


# setting up a winning system
def winning_system():
    global rounds_allowed
    global computers_choice
    global users_choice


# creating a list of tokens
tokens = ["rock", "paper", "scissors"]

# initializing variables
rounds_allowed = int_check("How many rounds do you want to play? ", 2)
computers_choice = random.choice(tokens)
users_choice = item_check()

print(users_choice)
winning_system()
