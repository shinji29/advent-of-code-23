"""Advent Of Code 2023 - Day 2"""


from utils import *


def solution_2(data: list[str]) -> None:
    result: int = 0

    for game in data:
        w: str = game[game.find(':') + 2:]
        x: list[str] = w.split("; ")
        sub_games: list[list[str]] = [z.split(", ") for z in x]

        min_r: int = 0
        min_g: int = 0
        min_b: int = 0

        for sub_game in sub_games:
            count: dict[str, int] = {}

            for sub_set in sub_game:
                key: str
                value: str

                value, key = sub_set.split(" ")
                count[key] = int(value)

            min_r = max(min_r, count["red"] if "red" in count else 0)
            min_g = max(min_g, count["green"] if "green" in count else 0)
            min_b = max(min_b, count["blue"] if "blue" in count else 0)

        result += int(min_r) * int(min_g) * int(min_b)

    print(f"\nResult #2 : {result}")


def solution_1(data: list[str]) -> None:
    result: int = 0

    for i, games in enumerate(data):
        x: str = games[games.find(':') + 2:]
        y: list[str] = [i for i in x.split("; ")]
        z: list[list[str]] = [j.split(", ") for j in y]

        flag: bool = True
        for game in z:
            count: dict[str, int] = {}

            for sub_game in game:
                value: str
                key: str

                value, key = (sub_game.strip().split(" "))
                count[key] = int(value)

            if "red" in count and count["red"] > 12:
                flag = False
                break
            if "green" in count and count["green"] > 13:
                flag = False
                break
            if "blue" in count and count["blue"] > 14:
                flag = False
                break

        if flag:
            result += i + 1

    print(f"\nResult #1 : {result}")


def main() -> None:
    data: list[str] = read_data(filename=__file__)
    solution_1(data)
    solution_2(data)


if __name__ == "__main__":
    main()
