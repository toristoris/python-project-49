import random

MAX_TRIES = 3

RULES = (
    "What is the result of the expression?"
)


def get_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        correct_answer = a + b
    elif operation == "-":
        correct_answer = a - b
    elif operation == "*":
        correct_answer = a * b

    question = f"{a} {operation} {b}"
    return question, correct_answer
