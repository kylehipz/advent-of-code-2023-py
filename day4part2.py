import sys


def day4part2():
    total = 0
    cards: list[str] = []
    card_count = {}

    for index, line in enumerate(sys.stdin):
        cards.append(line)
        card_count[index] = 1

    for index, card in enumerate(cards):
        count = 0
        inp = card.split(":")[1]

        numbers = inp.split("|")
        winning = numbers[0].strip().split()
        card = numbers[1].strip().split()

        for num in card:
            if num in winning:
                count += 1

        for i in range(index + 1, index + count + 1):
            if i in card_count:
                card_count[i] += card_count[index]

    for k in card_count:
        total += card_count[k]

    print(total)
