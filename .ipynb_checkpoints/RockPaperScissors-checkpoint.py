import random


print("Welcome to Rock Paper Sicssors! ")

user_choice = input("Please make a selection (rock, paper, or scissors): ")

possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)

print(f"\n Your selection was {user_choice},  Your opponent's selection was {computer_choice}")


while  user_choice == computer_choice: #turn into a while loop
    print(f"Both players chose {user_choice}, tie game")
    user_choice = input("Please make a selection (rock, paper, or scissors): ")
    computer_choice = random.choice(possible_choices)
    if user_choice != computer_choice:
        break
#Make it so if its a tie both players choose again
if user_choice == "paper":    #tun into an if statement
    if computer_choice  == "rock":
        print("Paper covers Rock! You Win!")
    else:
        print("Scissors cuts paper, you lose")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You Win!")
    else:
        print("Paper covers rock, you lose")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper, you win")
    else:
        print("Rock smashes scissors, you lose")



    




