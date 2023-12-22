import sys


def day4():
    sum = 0

    for line in sys.stdin:
        count = 0
        inp = line.split(":")[1]

        numbers = inp.split("|")
        winning = numbers[0].strip().split()
        card = numbers[1].strip().split()

        for num in card:
            if num in winning:
                count += 1

        value = 0

        if count > 0:
            value = 1 << count - 1

        sum += value

    print(sum)
