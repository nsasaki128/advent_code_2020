from collections import deque
def main():
    keep = 25
    count = 1000
    nums = deque()
    ans = 0
    find = False
    for i in range(count):
        cur = int(input())
        if i < keep:
            nums.append(cur)
            continue
        if i > keep:
            nums.popleft()
        if not find_num(nums, cur) and not find:
            ans = cur
            find = True
        nums.append(cur)

    print(ans)


def find_num(nums, target) -> bool:
    possible = set()
    for num in nums:
        if num in possible:
            return True
        possible.add(target-num)
    return False

if __name__ == '__main__':
	main()
