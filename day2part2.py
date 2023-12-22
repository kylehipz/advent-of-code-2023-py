import sys


def day2part2():
    sum = 0

    for line in sys.stdin:
        inp = line.split(":")[1]

        sets = inp.split(";")

        max_blue = 0
        max_red = 0
        max_green = 0

        for s in sets:
            color_cubes = s.split(",")

            for c in color_cubes:
                cubes = c.strip().split(" ")
                num = int(cubes[0])
                color = cubes[1]

                if color == "blue":
                    max_blue = max(max_blue, num)
                elif color == "red":
                    max_red = max(max_red, num)
                else:
                    max_green = max(max_green, num)

        power = max_blue * max_red * max_green
        sum += power

    print(sum)
