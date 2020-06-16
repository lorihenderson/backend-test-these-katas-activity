import unittest
import katas

# pushing to dev branch
class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(8, 3), 11)

    def test_multiply(self):
        self.assertEqual(katas.multiply(6, 3), 18)

    def test_power(self):
        self.assertEqual(katas.power(5, 2), 25)

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(3), 1)


if __name__ == '__main__':
    unittest.main()
