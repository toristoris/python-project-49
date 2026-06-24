from brain_games.cli import welcome_user  # импортируем приветствие
import prompt  # библиотека для ввода/вывода
from typing import Callable


def game_engine(
    rules: str, max_tries: int, func_question: Callable
):
    name = welcome_user()
    print(rules)
    count_tries = 0

    while count_tries < max_tries:
        question, correct_answer = func_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").lower().strip()
        
        if user_answer == str(correct_answer):  # проверка прямо здесь
            print("Correct!")
            count_tries += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")
