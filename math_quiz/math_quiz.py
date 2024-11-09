import random

def generate_random_number(min_value, max_value):
    """Generates a random integer between the given minimum and maximum values.

    Args:
        min_value (int): The minimum value for the random number.
        max_value (int): The maximum value for the random number.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """Generates a random arithmetic operator (+, -, *).

    Returns:
        str: A random operator.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """Creates a math problem string and calculates the correct answer.

    Args:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The arithmetic operator (+, -, *).

    Returns:
        tuple: A tuple containing the problem string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """Conducts a math quiz with a fixed number of questions.

    Prompts the user with math problems and evaluates their answers.
    Prints the final score at the end of the quiz.
    """
    total_questions = 10  # Adjust the number of questions as needed
    correct_answers = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems. Please provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 10)
        operator = generate_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            correct_answers += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {correct_answers}/{total_questions}")

if __name__ == "__main__":
    math_quiz()