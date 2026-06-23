import random  # библиотека для рандома
import prompt  # библиотека для ввода/вывода
from brain_games.cli import welcome_user  # импортируем приветствие


def is_even(number):  # проверяет, является ли число чётным
    return number % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer


def main():  # используем уже готовое приветствие
    name = welcome_user()
    print(
        'Answer "yes" if the number is even, otherwise answer "no".'
    )  # знакомим с правилами

    rounds_to_win = 3

    for _ in range(rounds_to_win):
        number, correct_answer = generate_question()
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
