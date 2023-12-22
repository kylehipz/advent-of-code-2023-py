import sys

symbol_dict = {}
number_dict = {}


def day3():
    sum = 0
    rows: list[str] = []

    for row in sys.stdin:
        rows.append(row)

    # Get symbols
    for rowIdx, row in enumerate(rows):
        for colIdx, c in enumerate(row):
            if not c.isalnum() and c != "." and c != "\n":
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
                # Check above symbol
                if rowIdx > 0:
                    sum += get_adjacent_numbers(rowIdx - 1, colIdx)

                # Check below symbol
                if rowIdx < len(rows):
                    sum += get_adjacent_numbers(rowIdx + 1, colIdx)

                # Check Left and right
                sum += get_adjacent_numbers(rowIdx, colIdx)
    print(sum)


def get_adjacent_numbers(rowIdx: int, colIdx: int) -> int:
    total = 0

    for startIdx in number_dict[rowIdx]:
        num = number_dict[rowIdx][startIdx]
        endIdx = startIdx + len(str(num))

        if in_range(colIdx, startIdx, endIdx):
            total += num

    return total


def in_range(colIdx: int, startIdx: int, endIdx: int):
    r = range(startIdx, endIdx)

    return colIdx in r or colIdx - 1 in r or colIdx + 1 in r
