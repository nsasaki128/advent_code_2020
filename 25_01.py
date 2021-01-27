def main():
    s = 7
    card = int(input())
    door = int(input())
    key = 20201227

    card_loop = get_loop(s, key, card)
    door_loop = get_loop(s, key, door)
    print(f"card_loop: {card_loop}")
    print(f"door_loop: {door_loop}")

    ans_card = 1
    for _ in range(door_loop):
        ans_card *= card
        ans_card %= key
    print(ans_card)
    ans_door = 1
    for _ in range(card_loop):
        ans_door *= door
        ans_door %= key
    print(ans_door)


def get_loop(s, key, dest):
    loop = 0
    start = 1
    while start != dest:
        loop += 1
        start *= s
        start %= key
    return loop

if __name__ == '__main__':
	main()

