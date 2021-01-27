from collections import deque
def main():
    card_num = 25
    player1 = deque()
    player2 = deque()

    input()
    for _ in range(card_num):
        player1.append(int(input()))
    input()

    input()
    for _ in range(card_num):
        player2.append(int(input()))

    while player1 and player2:
        p1 = player1.popleft()
        p2 = player2.popleft()
        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    winner = player1 if player1 else player2
    ans = 0
    for i, card in enumerate(reversed(winner)):
        ans += (i+1)*card
    print(ans)



if __name__ == '__main__':
	main()
