import unittest
from guessing_game import check_guess


class TestGuessingGame(unittest.TestCase):

    def test_even_number(self):
        result = check_guess(501, 500)
        self.assertEqual(result, "Please enter an odd number.")

    def test_too_low(self):
        result = check_guess(501, 499)
        self.assertEqual(result, "Too low!")

    def test_correct_guess(self):
        result = check_guess(501, 501)
        self.assertEqual(result, "Correct! You guessed the number!")


if __name__ == "__main__":
    unittest.main()