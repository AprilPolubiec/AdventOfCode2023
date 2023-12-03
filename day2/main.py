import re

CONFIG = { "red": 12, "green": 13, "blue": 14 }
GAME_ID_START_IDX = len("game") + 1

def get_games(filename: str):
    games = []
    with open(filename, "r") as f:
        games = f.readlines()
    return games

def get_max_pulls(game):
    maxes = {}
    # Find each number
    matches = re.findall("(\d+\sred|\d+\sblue|\d+\sgreen)", game)
    for m in matches:
        [count, color] = m.split(" ")
        count = int(count)
        if maxes.get(color) == None:
            maxes[color] = count
        elif maxes[color] < count:
            maxes[color] = count
    return maxes

def is_valid_game(game):
    max_pulls = get_max_pulls(game)
    for color in max_pulls:
        if max_pulls[color] > CONFIG[color]:
            return False
    return True


def get_sum(filename):
    sum = 0
    games = get_games(filename)
    for game in games:
        game_id_end_idx = game.find(":")
        game_id = int(game[GAME_ID_START_IDX:game_id_end_idx])
        is_valid = is_valid_game(game[game_id_end_idx + 1:])
        if is_valid:
            sum += game_id
            
    return sum

if __name__ == '__main__':
    res = get_sum("input.txt")
    print(res)