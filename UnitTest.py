def add(a, b):
    return a + b


import unittest

# The function we're testing
def add(a, b):
    return a + b

# Test case class
class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 = 5

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)  # Test if -2 + -3 = -5

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)  # Test if 2 + -3 = -1

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)  # Test if 0 + 5 = 5

if __name__ == '__main__':
    unittest.main()
    
