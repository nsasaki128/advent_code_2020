def main():
    count = 267
    valid_range = list()
    nearby_process = False
    my_process = False
    invalid_seats = list()
    classes = list()

    for _ in range(count):
        p = input()
        if nearby_process:
            seats = list(map(int, p.split(",")))
            for seat in seats:
                invalid = True
                for l, r in valid_range:
                    if l <= seat <= r:
                        invalid = False
                        break
                if invalid:
                    invalid_seats.append(seat)
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
            continue

        rules = p.split(":")[1].split()
        valid_range.append(extract_rule(rules[0]))
        valid_range.append(extract_rule(rules[2]))


    print(valid_range)
    print(invalid_seats)
    print(sum(invalid_seats))

def extract_rule(rule: str) -> (int, int):
    lr = rule.split("-")
    return (int(lr[0]), int(lr[1]))

if __name__ == '__main__':
	main()
