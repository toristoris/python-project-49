import random

MAX_TRIES = 3

RULES = (
    "Find the greatest common divisor of given numbers"
)


def get_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correct_answer = math.gcd(a, b) 

    question = f"{a} {b}"
    return question, correct_answer