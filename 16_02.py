import copy
def main():
    count = 267
    valid_range = list()
    nearby_process = False
    my_process = False
    check_pos = set()
    nearby_seats = list()
    my_seats = list()

    for _ in range(count):
        p = input()
        if nearby_process:
            seats = list(map(int, p.split(",")))
            nearby_seats.append(seats)
            continue

        if p == "":
            continue

        if p.startswith("nearby tickets"):
            nearby_process = True
            my_process = False
            continue
        if p.startswith("your ticket"):
            my_process = True
            continue

        if my_process:
            my_seats = list(map(int, p.split(",")))
            continue

        valid_range.append(extract_rule(p))


    # Ignore invalid seats
    invalid_seats = set()
    for row in range(len(nearby_seats)):
        for col in range(len(nearby_seats[row])):
            invalid = True
            seat = nearby_seats[row][col]
            for l1, r1, l2, r2, info in valid_range:
                if l1 <= seat <= r1 or l2 <= seat <= r2:
                    invalid = False
                    break
            if invalid:
                invalid_seats.add((row, col))

    # Collect possible combination
    possible_combination = [{} for _ in range(len(nearby_seats[0]))]
    col = 0
    while col < len(nearby_seats[0]):
        for l1, r1, l2, r2, info in valid_range:
            invalid = False
            for row in range(len(nearby_seats)):
                if (row, col) in invalid_seats:
                    continue
                seat = nearby_seats[row][col]
                if not(l1 <= seat <= r1 or l2<= seat <= r2):
                    invalid = True
                    break

            if not invalid:
                possible_combination[col]["id"] = col
                if "info" not in possible_combination[col]:
                    possible_combination[col]["info"] = list()
                possible_combination[col]["info"].append(info)
        col += 1

    # Guess
    possible_combination.sort(key=lambda x: len(x["info"]))
    is_solved, seat_cols = solve(0, possible_combination, dict())

    # Multiple departure seat num
    ans = 1
    for k, v in seat_cols.items():
        if k.startswith("departure"):
            ans *= my_seats[v]
    print(ans)

def solve(num, possible_combination, ans):
    if num == len(possible_combination):
        return True, ans
    cur = possible_combination[num]
    cur_ans = copy.deepcopy(ans)
    for name in cur["info"]:
        # Already used
        if name in ans:
            continue
        # Consider as use
        cur_ans[name] = cur["id"]
        is_solved, possible_ans = solve(num+1, possible_combination, cur_ans)
        if is_solved:
            return True, possible_ans
        cur_ans.pop(name)
    # Try all possible combination but it can't be solved
    return False, _none

def extract_rule(p: str) -> (int, int, int, int, str):
    rule_info = p.split(":")
    rules = rule_info[1].split()
    lr1 = rules[0].split("-")
    lr2 = rules[2].split("-")
    return (int(lr1[0]), int(lr1[1]), int(lr2[0]), int(lr2[1]), rule_info[0])

if __name__ == '__main__':
	main()
