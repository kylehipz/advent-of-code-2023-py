import sys


if __name__ == "__main__":
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }

    sum = 0

    for line in sys.stdin:
        start = ""
        end = ""
        found_first = False

        for index, c in enumerate(line):
            if c.isnumeric():
                if not found_first:
                    start = c
                    found_first = True
                end = c
            elif c.isalpha():
                for i in range(1, 6):
                    if index + i > len(line):
                        break
                    substr = line[index : index + i]

                    if substr in digit_map:
                        if not found_first:
                            start = digit_map[substr]
                            found_first = True
                        end = digit_map[substr]

        number = int(start + end)

        sum += number

    print(sum)
