from collections import deque
def main():
    joltages = list()
    joltages.append(0)
    count = 111
    max_joltage = 0
    for _ in range(count):
        cur = int(input())
        max_joltage = max(max_joltage, cur)
        joltages.append(cur)

    joltages.append(max_joltage+3)
    joltages.sort()
    diffs = [0, 0, 0, 0]
    for i in range(count+1):
        diff = joltages[i+1] - joltages[i]
        # This case never happened
        if diff > 3:
            continue
        diffs[diff] += 1

    print(joltages)
    print(diffs)
    print(diffs[1]*diffs[3])


if __name__ == '__main__':
	main()
