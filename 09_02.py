from collections import deque
def main():
    keep = 25
    count = 1000
    nums = deque()
    allNums = list()
    ans = 0
    find = False
    for i in range(count):
        cur = int(input())
        allNums.append(cur)
        if i < keep:
            nums.append(cur)
            continue
        if i > keep:
            nums.popleft()
        if not findNum(nums, cur) and not find:
            ans = cur
            find = True
        nums.append(cur)

    print("Q1: answer:")
    print(ans)
    print()
    print("Q2: answer:")
    print(findNumSum(allNums, ans))


def findNum(nums, target) -> bool:
    possible = set()
    for num in nums:
        if num in possible:
            return True
        possible.add(target-num)
    return False

def findNumSum(nums, target) -> int:
    head, tail = 0, 0
    cur = nums[0]
    while head <= tail:
        if cur == target:
            return min(nums[head:tail+1]) + max(nums[head:tail+1])
        if cur < target and tail < len(nums):
            tail += 1
            cur += nums[tail]
        else:
            if head < len(nums):
                cur -= nums[head]
            head += 1

    return 0


if __name__ == '__main__':
	main()
