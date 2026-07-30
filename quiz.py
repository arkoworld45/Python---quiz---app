"""
Simple Quiz / Flashcard App
----------------------------
Concepts used: dictionaries, loops, functions, conditionals
"""

import random

# 1. Store questions and answers in a dictionary
# key = question, value = correct answer
quiz_data = {
    "What data type uses key-value pairs in Python?": "dictionary",
    "What keyword is used to define a function?": "def",
    "What symbol is used for a comment in Python?": "#",
    "What method adds an item to the end of a list?": "append",
    "What data type is immutable and defined with parentheses?": "tuple",
}


def run_quiz(data):
    score = 0
    total = len(data)

    # Turn dictionary items into a list so we can shuffle the order
    questions = list(data.items())
    random.shuffle(questions)

    for question, correct_answer in questions:
        print("\n" + question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was: {correct_answer}")

    show_results(score, total)


def show_results(score, total):
    percentage = (score / total) * 100
    print("\n--- Quiz Complete ---")
    print(f"Score: {score}/{total} ({percentage:.1f}%)")

    if percentage == 100:
        print("Perfect score! 🎉")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing — you'll get there!")


if __name__ == "__main__":
    print("Welcome to the Python Quiz!")
    run_quiz(quiz_data)
