import sys

symbol_dict = {}
number_dict = {}


def day3part2():
    sum = 0
    rows: list[str] = []

    for row in sys.stdin:
        rows.append(row)

    # Get symbols
    for rowIdx, row in enumerate(rows):
        for colIdx, c in enumerate(row):
            if c == "*":
                key = rowIdx
                if key not in symbol_dict:
                    symbol_dict[key] = {}
                symbol_dict[key][colIdx] = True

    # Get numbers
    for rowIdx, row in enumerate(rows):
        num = ""
        for colIdx, c in enumerate(row):
            if c.isnumeric():
                num += c
            else:
                if rowIdx not in number_dict:
                    number_dict[rowIdx] = {}
                if num != "":
                    number_dict[rowIdx][colIdx - len(num)] = int(num)
                num = ""

    for rowIdx in range(len(rows)):
        if rowIdx in symbol_dict:
            for colIdx in symbol_dict[rowIdx]:
                count = 0

                above = [0, 0]
                below = [0, 0]
                side = [0, 0]

                # Check above symbol
                if rowIdx > 0:
                    above = get_adjacent_numbers(rowIdx - 1, colIdx)
                    count += above[0]

                # Check below symbol
                if rowIdx < len(rows):
                    below = get_adjacent_numbers(rowIdx + 1, colIdx)
                    count += below[0]

                # Check Left and right
                side = get_adjacent_numbers(rowIdx, colIdx)
                count += side[0]

                above_adjacent = above[0] > 0
                below_adjacent = below[0] > 0
                side_adjacent = side[0] > 0

                if count == 2:
                    total = 1
                    if above_adjacent:
                        total *= above[1]
                    if below_adjacent:
                        total *= below[1]
                    if side_adjacent:
                        total *= side[1]

                    sum += total
    print(sum)


def get_adjacent_numbers(rowIdx: int, colIdx: int):
    count = 0
    total = 1

    for startIdx in number_dict[rowIdx]:
        num = number_dict[rowIdx][startIdx]
        endIdx = startIdx + len(str(num))

        if in_range(colIdx, startIdx, endIdx):
            count += 1
            total *= num

    return [count, total]


def in_range(colIdx: int, startIdx: int, endIdx: int):
    r = range(startIdx, endIdx)

    return colIdx in r or colIdx - 1 in r or colIdx + 1 in r
