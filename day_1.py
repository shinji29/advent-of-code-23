"""Advent Of Code 2023 - Day 1"""


from utils import read_data


digit_map: dict[str, int] = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}


def solution_2(data: list[str]) -> None:
    result: int = 0
    for line in data:
        left: int = -1
        right: int = -1

        scan: str = ""
        digit: int = -1

        for l in line:
            if l.isdigit():
                digit = int(l)
            else:
                scan += l
                for key, value in digit_map.items():
                    if scan.endswith(key):
                        digit = value

            if digit != -1:
                if left == -1:
                    left = digit
                    right = digit
                else:
                    right = digit

        result += left * 10 + right

    print(f"\nResult : {result}")


def solution_1(data: list[str]) -> None:
    result: int = 0
    for line in data:
        left: int = -1
        right: int = -1

        for l in line:
            if l.isdigit():
                if left == -1:
                    left = int(l)
                    right = int(l)
                else:
                    right = int(l)

        result += left * 10 + right

    print(f"\nResult : {result}")


def main() -> None:
    data: list[str] = read_data(filename=__file__)
    solution_1(data)
    solution_2(data)


if __name__ == "__main__":
    main()
