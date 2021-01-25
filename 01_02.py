def main():
    count = 200
    nums = []
    for i in range(count):
        nums.append(int(input()))
    ans = 0
    prev_set = set()
    for i in range(count):
        for j in range(i, count):
            for k in range(j, count):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i]*nums[j]*nums[k])
                    break


if __name__ == '__main__':
	main()
