import sys

sum = 0

for line in sys.stdin:
    start = ""
    end = ""
    found_first = False

    for c in line:
        if c.isnumeric():
            if not found_first:
                start = c
                found_first = True
            end = c

    number = int(start + end)

    sum += number

print(sum)
