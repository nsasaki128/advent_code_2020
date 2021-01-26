def main():
    count = 1000
    ans = 0
    for i in range(count):
        num, char, password = input().split()
        min_num, max_num = map(int, num.split("-"))
        if min_num <= password.count(char[0]) <= max_num:
            ans += 1
    print(ans)


if __name__ == '__main__':
	main()
