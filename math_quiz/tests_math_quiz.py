import unittest
from math_quiz import generate_random_number, generate_random_operator, create_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        """Tests if random numbers are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        """Tests if random operators are valid."""
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
            random_operator = generate_random_operator()
            self.assertIn(random_operator, valid_operators)

    def test_create_math_problem(self):
        """Tests if math problems are created correctly and answers are calculated accurately."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24),
            (0, 5, '+', '0 + 5', 5),
            (10, 0, '-', '10 - 0', 10),
            (1, 1, '*', '1 * 1', 1),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()