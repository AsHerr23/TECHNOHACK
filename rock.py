import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n==== Rock, Paper, Scissors Game ====")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '4':
            print("\nGame Over. Goodbye!")
            break
        elif user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        user_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}[user_choice]
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nGame Over. Goodbye!")
            break

if __name__ == "__main__":
    play_game()
