import copy
def main():
    count = 1068
    base_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    cur_set = copy.deepcopy(base_set)
    ans = 0
    is_valid = True

    for i in range(count):
        cur_input = input()
        if len(cur_input) == 0:
            if (len(cur_set) == 0 and is_valid):
                ans += 1
            is_valid = True
            cur_set = copy.deepcopy(base_set)
            continue
        cur_inputs = cur_input.split()
        for cur in cur_inputs:
            param = cur[0:3]
            if param not in cur_set:
                continue
            cur_set.remove(param)
            if not is_valid_param(param, cur[4:]):
                is_valid = False
                continue
    if (len(cur_set) == 0 and is_valid):
       ans += 1

    print(ans)

def is_valid_param(key: str, val:str):
    eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if key == "byr":
        return 1920 <= int(val) <= 2002
    if key == "iyr":
        return 2010 <= int(val) <= 2020
    if key == "eyr":
        return 2020 <= int(val) <= 2030
    if key == "hgt":
        unit = val[-2:]
        if not(unit == "cm" or unit == "in"):
            return False
        height = int(val[:-2])
        if unit == "cm":
            return 150 <= height <= 193
        return 59 <= height <= 76
    if key == "hcl":
        head = val[0]
        tail = val[1:]
        if not(head == "#" and len(tail) == 6):
            return False
        for char in tail:
            if char.isdigit():
                continue
            if char not in {"a", "b", "c", "d", "e", "f"}:
                return False
        return True
    if key == "ecl":
        return val in eye_colors
    if key == "pid":
        return len(val) == 9 and val.isdigit() and val[0] != "-"
    return False

if __name__ == '__main__':
	main()
