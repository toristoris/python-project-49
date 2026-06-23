from brain_games.cli import welcome_user  # импортируем приветствие
import prompt  # библиотека для ввода/вывода
from typing import Callable 

def game_engine(rules: str, max_tries: int, func_question = Callable):
    name = welcome_user() #выводим приветствие
    print (f"Game rules: {rules}") #выводим правила
    count_tries = 0