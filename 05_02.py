import copy
def main():
    count = 839
    total = 1024
    empty_seats = set([i for i in range(total)])
    for _ in range(count):
        cur = getCount(input())
        if cur in empty_seats:
            empty_seats.remove(cur)
    for val in empty_seats:
        if val-1 not in empty_seats and val+1 not in empty_seats:
            print(val)
            break

def getCount(seat: str) -> int:
    rowNum = 7
    colNum = 10
    row = 0
    col = 0
    for i in range(rowNum):
        if seat[i] == "B":
            row += 1 << (6 - i)
    for j in range(rowNum, colNum):
        if seat[j] == "R":
            col += 1 << (9 - j)
    return 8*row + col

if __name__ == '__main__':
	main()
