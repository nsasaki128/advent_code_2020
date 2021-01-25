import copy
def main():
    count = 1068
    base_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    cur_set = copy.deepcopy(base_set)
    ans = 0

    for i in range(count):
        cur_input = input()
        if len(cur_input) == 0:
            if (len(cur_set) == 0):
                ans += 1
            cur_set = copy.deepcopy(base_set)
            continue
        cur_inputs = cur_input.split()
        for cur in cur_inputs:
            if cur[0:3] in cur_set:
                cur_set.remove(cur[0:3])

    if (len(cur_set) == 0):
        ans += 1
    print(ans)


if __name__ == '__main__':
	main()
