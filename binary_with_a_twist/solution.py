import os
import sys
from functools import cache
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import runner


def solve(input: List[str]) -> List[str]:
    result = []
    for i, line in enumerate(input[1:]):
        if len(line) == 0:
            continue
        n = int(line)
        if n == 2:
            result.append("-1")
            continue

        # print(f"doing #{i + 1}: {n}")
        base = 3
        while not is_only_01(n, base):
            base += 1
        result.append(str(base))

    return result


@cache
def is_only_01(n: int, base: int) -> bool:
    if n == 0:
        return True
    if n % base > 1:
        return False
    return is_only_01(n // base, base)


if __name__ == "__main__":
    runner.run(solve)
