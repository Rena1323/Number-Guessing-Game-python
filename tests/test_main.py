from number_guessing_game_python import MAX_NUMBER, MIN_NUMBER, generate_secret_number


def test_generate_secret_number():
    number = generate_secret_number()

    assert MIN_NUMBER <= number <= MAX_NUMBER
