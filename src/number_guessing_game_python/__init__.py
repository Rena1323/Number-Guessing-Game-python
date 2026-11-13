from random import randint
from textwrap import dedent


def choose_difficulty() -> int:
    while True:
        difficulty_choice = input("Enter your Choice: ")
        if difficulty_choice == "1":
            max_attempts = 10
            selected_level = "easy"
            break
        elif difficulty_choice == "2":
            max_attempts = 5
            selected_level = "medium"
            break
        elif difficulty_choice == "3":
            max_attempts = 3
            selected_level = "hard"
            break
        else:
            print("\nPlease select level (type '1', '2' or '3' and press Enter)")

    print(
        f"\nGreat! You have selected the {selected_level} difficulty level.\nLet's start the game!"
    )
    return max_attempts


def generate_secret_number() -> int:
    return randint(1, 100)


def ask_to_play_again() -> bool:
    replay_answer = input(
        "\nDo you want to play again? ('yes' or 'no' and press Enter): "
    )
    while True:
        if replay_answer == "yes":
            return True
        elif replay_answer == "no":
            return False
        else:
            replay_answer = input("Please, type 'yes' or 'no': ")
            continue


def get_valid_guess() -> int:
    while True:
        raw_guess = input("\nEnter your guess (1-100): ")

        try:
            guess = int(raw_guess)
        except ValueError:
            print("Please enter a whole number")
            continue
        if 1 <= guess <= 100:
            return guess

        print("Your guess must be between 1 and 100.")


def main():
    print(
        dedent("""
            +------------------------------------------+
            | Welcome to the Number Guessing Game!     |
            | I'm thinking of a number from 1 to 100.  |
            | You have some chances to guess correctly.|
            +------------------------------------------+
            """)
    )

    print(
        dedent("""
            Please select the difficulty level:
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)""")
    )

    attempts_used = 0
    max_attempts = choose_difficulty()
    secret_number = generate_secret_number()

    while True:
        if attempts_used >= max_attempts:
            play_again = ask_to_play_again()
            if play_again:
                attempts_used = 0
                secret_number = generate_secret_number()
                continue
            else:
                print(
                    "\nYou have decided to end the game. Thanks for playing and good luck!"
                )
                break
        else:
            guess = get_valid_guess()
            attempts_used += 1
            if guess > secret_number:
                print(f"Incorrect! The number is less than {guess}")
            elif guess < secret_number:
                print(f"Incorrect! The number is greater than {guess}")
            else:
                print(
                    f"\nCongratulations! You guessed the correct number in {attempts_used} attempts."
                )
                play_again = ask_to_play_again()
                if play_again:
                    attempts_used = 0
                    secret_number = generate_secret_number()
                    continue
                else:
                    print("\nThanks for playing and good luck!")
                    break


if __name__ == "__main__":
    main()
