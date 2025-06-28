import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import runner


def solve(input: List[str]) -> List[str]:
    result = []

    for line in input[1:]:
        if len(line) == 0:
            continue

        distance = int(line)
        if distance % 9 != 0:
            result.append("NONE")
        else:
            n = distance // 9
            result.append(f"{n} {n * 10}")

    return result


if __name__ == "__main__":
    runner.run(solve)
