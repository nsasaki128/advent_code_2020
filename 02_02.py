def main():
    count = 1000
    ans = 0
    for i in range(count):
        num, char, password = input().split()
        left, right = map(int, num.split("-"))
        isLeft, isRight = password[left-1] == char[0], password[right-1] == char[0]

        if isLeft ^ isRight:
            ans += 1
    print(ans)


if __name__ == '__main__':
	main()
