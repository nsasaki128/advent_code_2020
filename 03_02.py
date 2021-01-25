import math
def main():
    count = 323
    anss = [0, 0, 0, 0, 0]
    moves = [1, 3, 5, 7]
    matrix = list()
    for i in range(count):
        matrix.append(input())
    for i in range(count):
        for pos, move in enumerate(moves):
            if matrix[i][(i*move)%len(matrix[i])] == "#":
                anss[pos] += 1
    pos = 0
    for i in range(0, count, 2):
        if matrix[i][pos%len(matrix[i])] == "#":
            anss[-1] += 1
        pos += 1
    print(anss)
    print(math.prod(anss))


if __name__ == '__main__':
	main()
