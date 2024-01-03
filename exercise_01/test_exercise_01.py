import unittest
from .exercise_01 import formatNumber

class TestFormatNumberFunction(unittest.TestCase):

    def test_default_formatting(self):
        self.assertEqual(formatNumber(1528.7213), "1,528.72")

    def test_english_formatting_rounding_enable(self):
        self.assertEqual(formatNumber(65428.9768, format_digit="en", decimal_places=3, rounding=True), "65,428.977")
        
    def test_english_formatting_rounding_disable(self):
        self.assertEqual(formatNumber(65428.9768, format_digit="en", decimal_places=2, rounding=False), "65,428.97")

    def test_french_formatting_enable(self):
        self.assertEqual(formatNumber(1673728.368, format_digit="fr", decimal_places=2, rounding=True), "1.673.728,37")
        
    def test_french_formatting_disable(self):
        self.assertEqual(formatNumber(1673728.368, format_digit="fr", decimal_places=2, rounding=False), "1.673.728,36")

if __name__ == '__main__':
    unittest.main()
