import unittest


def multiply(a, b):
    return a * b


class TestMultiplyFunction(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -5), 15)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply(3, -5), -15)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_with_one(self):
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(5, 1), 5)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000000, 1000000), 1000000000000)

if __name__ == '__main__':
    unittest.main()