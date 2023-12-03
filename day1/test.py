import unittest
import glob
import os

from main import get_sum, get_first_and_last_digit, has_num_string


class TestSum(unittest.TestCase):
    def __create_test_file(self, filename: str, contents: [str]):
        f = open(f"test_{filename}.txt", "w")
        f.write("\n".join(contents))
        f.close()
        return f
    def __clean_test_files(self):
        for file in glob.glob("test_*.txt"):
            os.remove(file)

    def test_has_num_string(self):
        res = has_num_string("six")
        self.assertEqual(res, "six")
        res = has_num_string("esix")
        self.assertEqual(res, "six")
        res = has_num_string("sixe")
        self.assertEqual(res, "six")

    def test_get_first_and_last(self):
        res = get_first_and_last_digit("six5eht")
        self.assertListEqual(res, [6, 5])
        res = get_first_and_last_digit("soeightwo39ktl132")
        self.assertListEqual(res, [8, 2])
        res = get_first_and_last_digit("ntxmgvkm9")
        self.assertListEqual(res, [9, 9])

    def test_single_digit(self):
        """
        Tests getting sum when strings have one integer
        """
        data = ["sibfjblhsjr3", "sx5eht", "treb7uchet"]
        f = self.__create_test_file("single_digit", data)
        result = get_sum(f.name)
        self.__clean_test_files()
        self.assertEqual(result, 165)

    def test_two_digit(self):
        """
        Tests getting sum when strings have two integers
        """
        data = ["hcpjssql4kjhbcqzkvr2fiebpllzqbkhg", "4thegctxgdmbm1"]
        f = self.__create_test_file("double_digit", data)
        result = get_sum(f.name)
        self.__clean_test_files()
        self.assertEqual(result, 83)

    def test_digits_and_strings(self):
        """
        Tests getting sum when strings have integers and strings
        """
        data = ["sixbfjblhsjr3", "soeightwo39ktl132", "9oneonetwofiveseven42", "6twotwo18eightthreeeight"]
        f = self.__create_test_file("digits_and_strings", data)
        # 63 + 82 + 92 + 68
        result = get_sum(f.name)
        self.__clean_test_files()
        self.assertEqual(result, 305)

if __name__ == '__main__':
    unittest.main()