import time
from random import randint
from textwrap import dedent

MIN_NUMBER = 1
MAX_NUMBER = 100


def choose_difficulty() -> int:
    while True:
        difficulty_choice = input("Enter your Choice: ").strip()
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
    return randint(MIN_NUMBER, MAX_NUMBER)


def ask_to_play_again() -> bool:
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False

        print("Please, type 'yes' or 'no'.")


def get_valid_guess() -> int:
    while True:
        raw_guess = input(f"\nEnter your guess ({MIN_NUMBER}-{MAX_NUMBER}): ")

        try:
            guess = int(raw_guess)
        except ValueError:
            print("Please enter a whole number")
            continue
        if MIN_NUMBER <= guess <= MAX_NUMBER:
            return guess

        print(f"Your guess must be between {MIN_NUMBER} and {MAX_NUMBER}.")


def display_game_time(start_time: float) -> None:
    elapsed_time = time.perf_counter() - start_time
    print(f"Game time: {elapsed_time:.2f} sec.")


def play_round(max_attempts: int):
    start_time = time.perf_counter()
    secret_number = generate_secret_number()

    for attempts_used in range(1, max_attempts + 1):
        guess = get_valid_guess()

        if guess > secret_number:
            print(f"Incorrect! The number is less than {guess}")

        elif guess < secret_number:
            print(f"Incorrect! The number is greater than {guess}")

        else:
            print(
                f"\nCongratulations! You guessed the correct number in {attempts_used} attempts."
            )
            display_game_time(start_time)
    print(f"\nGame over! The number was {secret_number}.")
    display_game_time(start_time)


def main():
    print(
        dedent(f"""
            Welcome to the Number Guessing Game!
            I'm thinking of a number from {MIN_NUMBER} to {MAX_NUMBER}.
            You have some chances to guess correctly.
            """)
    )

    print(
        dedent("""
            Please select the difficulty level:
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)""")
    )

    max_attempts = choose_difficulty()

    while True:
        play_round(max_attempts)

        if not ask_to_play_again():
            print("\nThanks for playing and good luck!")
            break


if __name__ == "__main__":
    main()
