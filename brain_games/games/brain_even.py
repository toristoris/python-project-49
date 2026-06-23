import prompt
import random
from brain_games.cli import welcome_user  # импортируем приветствие

MAX_TRIES = 3

RULES = 'Answer "yes" if the number is even, otherwise answer "no".' # знакомим с правилами

def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer == correct_answer

def get_question():
    question = random.randint(1, 100)
    return question



    

    


    

