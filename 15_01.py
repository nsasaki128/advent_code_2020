INIT = 0
def main():
    seeds = list(map(int, input().split(",")))
    count = 2020
    spoken_nums = dict()
    i = 0
    prev = 0
    for seed in seeds:
        spoken_nums[seed] = i
        prev = seed
        i += 1

    cur = 0

    while i < count:
        if prev not in spoken_nums:
            cur = INIT
        else:
            cur = i - spoken_nums[prev] - 1
        spoken_nums[prev] = i - 1
        prev = cur
        i += 1

    print(f"ans: {prev}")


if __name__ == '__main__':
	main()
