import unittest
from main import get_parts

class TestSum(unittest.TestCase):
    def test_digit_next_to_no_symbols_is_not_part(self):
       in_str = "...353."
       # Expect false
       res = get_parts(in_str.split("\n"))
       self.assertEqual(len(res), 0)

    def test_digit_vertical_to_no_symbols_is_not_part(self):
       in_str = ".......\n..213..\n......."
       # Expect false
       res = get_parts(in_str.split("\n"))
       self.assertEqual(len(res), 0)

    def test_single_digit_next_to_symbol_is_part(self):
       in_str = "...3#..\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])
       in_str = "..#3...\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])

    def test_single_digit_vertical_to_symbol_is_part(self):
       in_str = ".......\n...3...\n...$..."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])
       in_str = "...$...\n...3...\n......."
        # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])

    def test_single_digit_diagonal_to_symbol_is_part(self):
       in_str = "...+...\n..4....\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["4"])
       in_str = ".......\n..4....\n...+..."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["4"])

    def test_multiple_digits_next_to_symbol_is_part(self):
       in_str = "..34#..\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["34"])
       in_str = "..#36..\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["36"])

    def test_multiple_digits_vertical_to_symbol_is_part(self):
       # Symbol below first digit
       in_str = ".......\n...32..\n...$..."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["32"])

       # Symbol above first digit 
       in_str = "...$...\n...342.\n......."
        # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["342"])

        # Symbol above second digit 
       in_str = "....$..\n...3223\n......."
        # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3223"])
       # Symbol below third digit
       in_str = ".......\n..132..\n....$.."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["132"])

    def test_multiple_digits_diagonal_to_symbol_is_part(self):
       # Symbol diagonal top right
       in_str = ".....%.\n.8390..\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["8390"])
       # Symbol diagonal top left
       in_str = "..@....\n...39..\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["39"])
       # Symbol diagonal bottom right
       in_str = ".......\n.8273..\n.....(."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["8273"])
       # Symbol diagonal bottom left
       in_str = "...!...\n....302\n......."
       # Expect true
       res = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["302"])

if __name__ == '__main__':
    unittest.main()