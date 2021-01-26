import copy
def main():
    count = 839
    total = 1024
    empty_seats = set([i for i in range(total)])
    for _ in range(count):
        cur = get_count(input())
        if cur in empty_seats:
            empty_seats.remove(cur)
    for val in empty_seats:
        if val-1 not in empty_seats and val+1 not in empty_seats:
            print(val)
            break

def get_count(seat: str) -> int:
    row_num = 7
    col_num = 10
    row = 0
    col = 0
    for i in range(row_num):
        if seat[i] == "B":
            row += 1 << (6 - i)
    for j in range(row_num, col_num):
        if seat[j] == "R":
            col += 1 << (9 - j)
    return 8*row + col

if __name__ == '__main__':
	main()
