import random

MAX_TRIES = 3

RULES = (
    'Answer "yes" if the number is even, otherwise answer "no".'  # знакомим с правилами
)

def get_question():
    number = random.randint(1, 100)
    question = number
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
