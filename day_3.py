"""Advent Of Code 2023 - Day 3"""


from utils import *


class Gear:
    def __init__(self, value: str) -> None:
        self.value = value


def solution_2(data: list[str]) -> None:
    result: int = 0
    gear: Gear = Gear("")
    adj_nums: list[Gear] = []

    data_pts: list[list[str]] = [list(row) for row in data]
    temp: list[list] = [[None for _ in row] for row in data_pts]
    adj: list[tuple[int, int]] = [(x, y) for x in range(-1, 2)
                                  for y in range(-1, 2) if (x, y) != (0, 0)]

    for i, row in enumerate(data_pts):
        for j, pt in enumerate(row):
            if pt.isdigit():
                gear.value += pt
                temp[i][j] = gear
            else:
                gear = Gear("")

    for i, row in enumerate(data_pts):
        for j, pt in enumerate(row):
            g: Gear
            adj_nums.clear()

            if pt == "*":
                for x, y in adj:
                    if (i + x) in range(len(data_pts)) and (j + y) in range(len(row)):
                        if temp[i + x][j + y] is not None:
                            g = temp[i + x][j + y]
                            if g not in adj_nums:
                                adj_nums.append(g)

            if len(adj_nums) == 2:
                result += int(adj_nums[0].value) * int(adj_nums[1].value)

    print(f"\nResult #2 : {result}")


def solution_1(data: list[str]) -> None:
    thing: str = ""
    result: int = 0
    keep: bool = False

    pts: list[list[str]] = [list(row) for row in data]
    adj: list[tuple[int, int]] = [(x, y) for x in range(-1, 2)
                                  for y in range(-1, 2) if (x, y) != (0, 0)]

    for i, row, in enumerate(pts):
        for j in range(len(row)):
            pt: str = row[j]

            if pt.isdigit():
                if any(
                    pts[i + x][j + y] != '.' and not pts[i + x][j + y].isdigit()
                    for x, y in adj
                    if (i + x) in range(len(pts)) and (j + y) in range(len(row))
                ):
                    keep = True
                thing += pt

            else:
                if keep and len(thing):
                    result += int(thing)
                keep = False
                thing = ""

    if keep and len(thing):
        result += int(thing)

    print(f"\nResult #1: {result}")


def main() -> None:
    data: list[str] = read_data(filename=__file__)

    solution_1(data)
    solution_2(data)


if __name__ == "__main__":
    main()
