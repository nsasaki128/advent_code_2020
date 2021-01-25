def main():
    count = 200
    nums = []
    for i in range(count):
        nums.append(int(input()))
    total_sum = 2020
    prev_set = set()
    for i in range(count):
        if nums[i] in prev_set:
            print(nums[i]*(total_sum-nums[i]))
            break
        prev_set.add(total_sum-nums[i])

if __name__ == '__main__':
	main()
