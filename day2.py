import sys


def day2():
    sum = 0

    for index, line in enumerate(sys.stdin):
        inp = line.split(":")[1]

        sets = inp.split(";")
        is_line_possible = True

        for s in sets:
            color_cubes = s.split(",")

            for c in color_cubes:
                cubes = c.strip().split(" ")
                num = int(cubes[0])
                color = cubes[1]

                if not is_possible(num, color):
                    is_line_possible = False
                    break

        if is_line_possible:
            sum += index + 1

    print(sum)


def is_possible(num: int, color: str) -> bool:
    if color == "blue" and num > 14:
        return False
    if color == "red" and num > 12:
        return False
    if color == "green" and num > 13:
        return False

    return True
