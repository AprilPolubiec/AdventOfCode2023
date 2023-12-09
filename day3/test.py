import unittest
import os
from main import create_matrix, get_parts, get_sum

class TestSum(unittest.TestCase):
    def test_create_matrix(self):
       in_str = "...$...\n...342.\n......."
       # Expect false
       c_matrix = create_matrix(in_str.split("\n"))

       self.assertListEqual(c_matrix[0], [".", ".", ".", "$", ".", ".", "."])
       self.assertListEqual(c_matrix[1], [".", ".", ".", "342", "342", "342", "."])
       self.assertListEqual(c_matrix[2], [".", ".", ".", ".", ".", ".", "."])
    
    def test_digit_next_to_no_symbols_is_not_part(self):
       in_str = "...353."
       # Expect false
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(len(res), 0)

    def test_digit_vertical_to_no_symbols_is_not_part(self):
       in_str = ".......\n..213..\n......."
       # Expect false
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(len(res), 0)

    def test_single_digit_next_to_symbol_is_part(self):
       in_str = "...3#..\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])
       in_str = "..#3...\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])

    def test_single_digit_vertical_to_symbol_is_part(self):
       in_str = ".......\n...3...\n...$..."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])
       in_str = "...$...\n...3...\n......."
        # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3"])

    def test_single_digit_diagonal_to_symbol_is_part(self):
       in_str = "...+...\n..4....\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["4"])
       in_str = ".......\n..4....\n...+..."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["4"])

    def test_multiple_digits_next_to_symbol_is_part(self):
       in_str = "..34#..\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["34"])
       in_str = "..#36..\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["36"])

    def test_multiple_digits_vertical_to_symbol_is_part(self):
       # Symbol below first digit
       in_str = ".......\n...32..\n...$..."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["32"])

       # Symbol above first digit 
       in_str = "...$...\n...342.\n......."
        # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["342"])

        # Symbol above second digit 
       in_str = "....$..\n...3223\n......."
        # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["3223"])
       # Symbol below third digit
       in_str = ".......\n..132..\n....$.."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["132"])

    def test_example(self):
       ex = ["467..114..",
         "...*......",
         "..35..633.",
         "......#...",
         "617*......",
         ".....+.58.",
         "..592.....",
         "......755.",
         "...$.*....",
         ".664.598.."]
       (res, gears) = get_parts(ex)
       print(res)
       self.assertEqual(get_sum(res), 467835)
    def test_multiple_digits_diagonal_to_symbol_is_part(self):
       # Symbol diagonal top right
       in_str = ".....%.\n.8390..\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["8390"])
       # Symbol diagonal top left
       in_str = "..@....\n...39..\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["39"])
       # Symbol diagonal bottom right
       in_str = ".......\n.8273..\n.....(."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["8273"])
       # Symbol diagonal bottom left
       in_str = "...!...\n....302\n......."
       # Expect true
       (res, gears) = get_parts(in_str.split("\n"))
       self.assertEqual(res, ["302"])
   
    def test_get_parts_on_input_file(self):
      with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt"), "r") as f:
        lines = f.readlines()
      sum = get_parts(lines[:2])
      self.assertEqual(sum, ["411", "363", "134", "463", "775", "506"])

    def test_input_file(self):
      with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt"), "r") as f:
        lines = f.readlines()
      parts, gears = get_parts(lines)
      sum = get_sum(parts)
      self.assertEqual(sum, 536202)

if __name__ == '__main__':
    unittest.main()