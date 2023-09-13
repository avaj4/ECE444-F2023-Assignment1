import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_reversed_int(self):
        self.assertEqual(Utils.reversed(12345), 54321)

    def test_reversed_string(self):
        # Reversing a string should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.reversed("12345")

    def test_reversed_float(self):
        # Reversing a float should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.reversed(12.345)

    def test_formatter_int(self):
        binary, octal = Utils.formatter(42)
        self.assertEqual(binary, '101010')
        self.assertEqual(octal, '0o52')

    def test_formatter_string(self):
        # Formatting a string should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.formatter("42")

    def test_formatter_float(self):
        # Formatting a float should raise a TypeError
        with self.assertRaises(TypeError):
            Utils.formatter(42.0)

if __name__ == "__main__":
    unittest.main()
