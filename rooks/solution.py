import os
import sys
from typing import Dict, Iterator, List, NamedTuple, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import runner


class Rook(NamedTuple):
    pos: Tuple[int, int]
    is_white: bool


def solve(input: List[str]) -> List[str]:
    result = []
    it = iter(input[1:])
    done = 0

    while True:
        line = next(it, None)
        if line is None:
            break
        if len(line) == 0:
            continue

        board_len, rook_amount = (int(n) for n in line.split())
        board: Dict[Tuple[int, int], str] = {}  # 2D array would use too much memory
        whites, blacks = parse_rooks(rook_amount, board, it)
        count = 0

        for white in whites:
            for white_move in get_moves(white, board, board_len):
                replaced = move_rook(white.pos, white_move, board)

                for black in blacks:
                    if black.pos == white_move:
                        continue
                    count += sum(1 for _ in get_moves(black, board, board_len))

                move_rook(white_move, white.pos, board, replaced)

        result.append(str(count))
        done += 1
        print(f"done: {done}")

    return result


def move_rook(
    fr: Tuple[int, int],
    to: Tuple[int, int],
    board: Dict[Tuple[int, int], str],
    restore: str = "",
) -> str:
    replaced = board.get(to, "")
    board[to] = board.get(fr, "")
    if restore == "":
        board.pop(fr, None)
    else:
        board[fr] = restore
    return replaced


def get_moves(
    rook: Rook, board: Dict[Tuple[int, int], str], board_len: int
) -> Iterator[Tuple[int, int]]:
    x, y = rook.pos
    color = "W" if rook.is_white else "B"
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        while 0 <= new_x < board_len and 0 <= new_y < board_len:
            if (new_x, new_y) not in board:  # Empty square
                yield (new_x, new_y)
            else:  # Hit a piece
                existing_color = board[(new_x, new_y)]
                if existing_color != color:
                    yield (new_x, new_y)
                break
            new_x += dx
            new_y += dy


def parse_rooks(
    rook_amount: int, board: Dict[Tuple[int, int], str], it: Iterator[str]
) -> Tuple[List[Rook], List[Rook]]:
    whites, blacks = [], []

    for _ in range(rook_amount):
        line = next(it)
        words = line.split()
        x, y = int(words[0]), int(words[1])
        is_white = words[2] == "W"
        rook = Rook(pos=(x, y), is_white=is_white)
        if is_white:
            whites.append(rook)
        else:
            blacks.append(rook)
        board[(x, y)] = "W" if is_white else "B"

    return whites, blacks


if __name__ == "__main__":
    runner.run(solve)
