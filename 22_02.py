from collections import defaultdict
from collections import deque
from copy import deepcopy
import cProfile

class WinnerInfo:
    def __init__(self, winner, does_p1_win):
        self.winner = winner
        self.does_p1_win = does_p1_win

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

    winner = play_game(player1, player2).winner
    print(winner)
    ans = 0
    for i, card in enumerate(reversed(winner)):
        ans += (i+1)*card
    print(ans)


def play_game(player1, player2):
    seen_game = set()
    while player1 and player2:
        p1_deck, p2_deck = tuple(player1), tuple(player2)
        if (p1_deck, p2_deck) in seen_game:
            while player2:
                player1.append(player2.popleft())
            break
        seen_game.add((p1_deck, p2_deck))

        p1 = player1.popleft()
        p2 = player2.popleft()
        does_p1_win = p1 > p2
        if p1 <= len(player1) and p2 <= len(player2):
            does_p1_win =  subgame(player1, player2, p1, p2).does_p1_win
        if does_p1_win:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    return WinnerInfo(player1, True) if player1 else WinnerInfo(player2, False)


def subgame(player1, player2, p1_draw_num, p2_draw_num):
    cur_p1 = deepcopy(player1)
    cur_p2 = deepcopy(player2)

    this_player1 = deque()
    for i in range(p1_draw_num):
        this_player1.append(cur_p1.popleft())

    this_player2 = deque()
    for i in range(p2_draw_num):
        this_player2.append(cur_p2.popleft())

    return play_game(this_player1, this_player2)

if __name__ == '__main__':
	cProfile.run("main()")
