import copy
def main():
    count = 839
    ans = 0
    for _ in range(count):
        cur = getCount(input())
        ans = max(ans, cur)
    print(ans)

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
