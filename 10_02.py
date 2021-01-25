from collections import deque
def main():
    joltages = list()
    joltages.append(0)
    count = 111
    maxJoltage = 0
    for _ in range(count):
        cur = int(input())
        maxJoltage = max(maxJoltage, cur)
        joltages.append(cur)

    joltages.append(maxJoltage+3)
    joltages.sort()

    # approaches[0, 1] is just dummy for avoiding if statement
    approaches = [0 for _ in range(maxJoltage+6)]
    approaches[2] = 1
    for i in range(count+1):
        cur = joltages[i+1] + 2
        approaches[cur] = sum(approaches[cur-3:cur])

    print(approaches)
    print(approaches[-1])


if __name__ == '__main__':
	main()
