import unittest
import glob
import os

from main import get_max_pulls, is_valid_game, get_sum


class TestSum(unittest.TestCase):
    def __create_test_file(self, filename: str, contents: [str]):
        f = open(f"test_{filename}.txt", "w")
        f.write("\n".join(contents))
        f.close()
        return f
    def __clean_test_files(self):
        for file in glob.glob("test_*.txt"):
            os.remove(file)

    def test_get_max_pulls_all_colors(self):
       res = get_max_pulls("7 red, 1 green, 4 blue; 13 red, 11 blue; 6 red, 2 blue; 9 blue, 9 red; 4 blue, 11 red; 15 red, 1 green, 3 blue")
       self.assertEqual(3, len(res.keys()))
       self.assertEqual(15, res["red"])
       self.assertEqual(1, res["green"])
       self.assertEqual(11, res["blue"])

    def test_get_max_pulls_some_colors(self):
       res = get_max_pulls("4 blue; 2 red; 4 blue, 6 red")
       self.assertEqual(2, len(res.keys()))
       self.assertEqual(6, res["red"])
       self.assertEqual(4, res["blue"])

    def test_is_valid_game(self):
       res = is_valid_game("4 blue; 2 red; 4 blue, 6 red")
       self.assertTrue(res)

       res = is_valid_game("7 red, 1 green, 4 blue; 13 red, 11 blue; 6 red, 2 blue; 9 blue, 9 red; 4 blue, 11 red; 15 red, 1 green, 3 blue")
       self.assertFalse(res)

    def test_get_sum(self):
       games = ["Game 1: 4 blue; 1 green, 2 red; 4 blue, 1 green, 6 red",
                "Game 2: 7 red, 1 green, 4 blue; 13 red, 11 blue; 6 red, 2 blue; 9 blue, 9 red; 4 blue, 11 red; 15 red, 1 green, 3 blue",
                "Game 3: 1 blue, 10 green; 4 green, 8 blue; 3 blue, 14 green, 1 red",
                "Game 4: 1 green, 2 blue; 1 blue, 4 green; 8 red, 3 blue, 3 green; 8 red, 2 green, 1 blue; 7 green, 3 blue, 2 red; 1 red, 1 green, 3 blue",
                "Game 5: 3 red, 7 blue, 4 green; 12 blue, 16 red, 4 green; 9 red, 2 green; 1 blue, 1 green, 1 red",
                "Game 6: 15 blue; 15 red, 14 blue, 2 green; 8 red, 2 blue, 2 green; 2 green, 11 blue, 1 red"]
       f = self.__create_test_file("get_sum", games)
       
       res = get_sum(f.name)
       self.assertEqual(res, 5)
       self.__clean_test_files()

if __name__ == '__main__':
    unittest.main()