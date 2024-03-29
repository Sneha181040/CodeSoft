import random

def get_user_choice():

    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():

    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):

    print("\nYour choice:" ,user_choice)
    print("Computer's choice:" ,computer_choice)
    print("\nResult:",result)

def play_game():

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()

        if 'win' in result.lower():
            user_score += 1
        elif 'lose' in result.lower():
            computer_score += 1

        print("Score = You:",user_score, "\nComputer:", computer_score)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
