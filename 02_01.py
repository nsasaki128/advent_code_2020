def main():
    count = 1000
    ans = 0
    for i in range(count):
        num, char, password = input().split()
        minNum, maxNum = map(int, num.split("-"))
        if minNum <= password.count(char[0]) <= maxNum:
            ans += 1
    print(ans)


if __name__ == '__main__':
	main()
