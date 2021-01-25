init = 0
def main():
    seeds = list(map(int, input().split(",")))
    count = 30000000
    spokenNums = dict()
    i = 0
    prev = 0
    for seed in seeds:
        spokenNums[seed] = i
        prev = seed
        i += 1

    cur = 0

    while i < count:
        if prev not in spokenNums:
            cur = init
        else:
            cur = i - spokenNums[prev] - 1
        spokenNums[prev] = i - 1
        prev = cur
        i += 1

    print(f"ans: {prev}")


if __name__ == '__main__':
	main()
