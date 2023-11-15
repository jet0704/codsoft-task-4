import random

score = 0
choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Please choose your option (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        continue

    computer_choice = random.choice(choices)

    print("You chose", user_choice)
    print("The computer chose", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        score += 1
    else:
        print("You lose!")
        score -= 1

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Final score:", score)