from brain_games.cli import welcome_user  # импортируем приветствие
import prompt  # библиотека для ввода/вывода
from typing import Callable


def game_engine(
    rules: str, max_tries: int, func_question: Callable, check_answer: Callable
):
    name = welcome_user()
    print(rules)
    count_tries = 0

    while count_tries < max_tries:
        number = func_question()
        correct_answer = "yes" if number % 2 == 0 else "no"
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ").lower().strip()
        check = check_answer(user_answer, correct_answer)

        if check:
            print("Correct!")
            count_tries += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")
