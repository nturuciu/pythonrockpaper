import random

USER_WINS = 0
COMPUTER_WINS = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit:").lower()
    if user_input == "q":
        break

    if user_input not in [
        "rock",
        "paper",
        "scissors",
    ]:  # Check if the input is not one of the valid options
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        USER_WINS += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        USER_WINS += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won")
        USER_WINS += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You Lost!")
        COMPUTER_WINS += 1

print("You Won", USER_WINS, "times.")
print("The computer won", COMPUTER_WINS, "times.")

print("Goodbye!")
