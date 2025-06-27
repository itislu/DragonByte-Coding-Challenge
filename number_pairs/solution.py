import os
import sys
from typing import List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import runner


def solve(input: List[str]) -> List[str]:
    result = []
    for line in input[1:]:
        if len(line) == 0:
            continue
        distance = int(line)
        if calc_digit_sum(distance) % 9 != 0:
            result.append("None")
        else:
            result.append(" ".join(str(pair) for pair in find_digit_sum_pair(distance)))

    return result


def calc_digit_sum(num: int) -> int:
    return sum(int(c) for c in str(num))


def find_digit_sum_pair(distance: int) -> Tuple[int, int]:
    num = 1
    while True:
        if calc_digit_sum(num) == calc_digit_sum(num + distance):
            return (num, num + distance)
        num += 1


if __name__ == "__main__":
    runner.run(solve)
