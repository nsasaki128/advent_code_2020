import copy
def main():
    count = 839
    ans = 0
    for _ in range(count):
        cur = get_count(input())
        ans = max(ans, cur)
    print(ans)

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
