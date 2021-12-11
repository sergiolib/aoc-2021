# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3.9.7 64-bit
#     language: python
#     name: python3
# ---

# # Challenge 1: calculate score of the **first** bingo board to win

lines = open("input.txt", "r").read().split("\n")

numbers = list(map(int, lines[0].split(",")))


def is_bingo_line(line):
    n = len(line)
    if n == 0:
        return False
    return True


boards = []
board = []
for line in lines[2:]:
    if is_bingo_line(line):
        board.append(list(map(int, line.split())))
    else:
        boards.append(board)
        board = []
        continue


# +
class Bingo:
    def __init__(self, boards):
        self.boards = boards
        self.numbers = list()
        self.bingo = [False for _ in range(len(boards))]
        self.bingo_order = []

    def add_number(self, number):
        self.numbers.append(number)
        is_bingo = self.check_bingo()
        return is_bingo

    def check_bingo(self):
        any_bingo = False
        for i, board in enumerate(self.boards):
            is_bingo = False
            for row in board:
                is_bingo = self.check_line(row)
                if is_bingo:
                    self.add_maybe_to_bingo_order(i)
                    break
            if not is_bingo:
                for ic in range(5):
                    col = [r[ic] for r in board]
                    is_bingo = self.check_line(col)
                    if is_bingo:
                        self.add_maybe_to_bingo_order(i)
                        break
            self.bingo[i] = is_bingo
            if not any_bingo and is_bingo:
                any_bingo = True
        return any_bingo

    def add_maybe_to_bingo_order(self, board_n):
        if board_n in self.bingo_order:
            return
        self.bingo_order.append(board_n)

    def check_line(self, line):
        for number in line:
            if number not in self.numbers:
                return False
        return True

    def score(self, board_n):
        if not self.bingo[board_n]:
            raise Exception("Algorithm wrong")
        board = self.boards[board_n]
        # Sum of unmarked numbers
        unmarked_sum = 0
        for row in board:
            for elem in row:
                if elem not in self.numbers:
                    unmarked_sum += elem
        return unmarked_sum * self.numbers[-1]

b = Bingo(boards)
for n in numbers:
    is_bingo = b.add_number(n)
    if any(b.bingo):
        break
print(b.score(b.bingo_order[0]))


# -

# # Challenge 2: calculate score of the **last** bingo board to win

# +
class Bingo:
    def __init__(self, boards):
        self.boards = boards
        self.numbers = list()
        self.bingo = [False for _ in range(len(boards))]
        self.bingo_order = []

    def add_number(self, number):
        self.numbers.append(number)
        is_bingo = self.check_bingo()
        return is_bingo

    def check_bingo(self):
        any_bingo = False
        for i, board in enumerate(self.boards):
            is_bingo = False
            for row in board:
                is_bingo = self.check_line(row)
                if is_bingo:
                    self.add_maybe_to_bingo_order(i)
                    break
            if not is_bingo:
                for ic in range(5):
                    col = [r[ic] for r in board]
                    is_bingo = self.check_line(col)
                    if is_bingo:
                        self.add_maybe_to_bingo_order(i)
                        break
            self.bingo[i] = is_bingo
            if not any_bingo and is_bingo:
                any_bingo = True
        return any_bingo

    def add_maybe_to_bingo_order(self, board_n):
        if board_n in self.bingo_order:
            return
        self.bingo_order.append(board_n)

    def check_line(self, line):
        for number in line:
            if number not in self.numbers:
                return False
        return True

    def score(self, board_n):
        if not self.bingo[board_n]:
            raise Exception("Algorithm wrong")
        board = self.boards[board_n]
        # Sum of unmarked numbers
        unmarked_sum = 0
        for row in board:
            for elem in row:
                if elem not in self.numbers:
                    unmarked_sum += elem
        return unmarked_sum * self.numbers[-1]

b = Bingo(boards)
for n in numbers:
    is_bingo = b.add_number(n)
    if all(b.bingo):
        break
print(b.score(b.bingo_order[-1]))
# -


