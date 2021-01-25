def main():
    count = 323
    ans = 0
    matrix = list()
    for i in range(count):
        matrix.append(input())
    for i in range(count):
        if matrix[i][(i*3)%len(matrix[i])] == "#":
            ans += 1
    print(ans)


if __name__ == '__main__':
	main()
