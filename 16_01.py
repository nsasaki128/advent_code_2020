def main():
    count = 267
    validRange = list()
    nearbyProcess = False
    myProcess = False
    invalidSeats = list()
    classes = list()

    for _ in range(count):
        p = input()
        if nearbyProcess:
            seats = list(map(int, p.split(",")))
            for seat in seats:
                invalid = True
                for l, r in validRange:
                    if l <= seat <= r:
                        invalid = False
                        break
                if invalid:
                    invalidSeats.append(seat)
            continue

        if p == "":
            continue

        if p.startswith("nearby tickets"):
            nearbyProcess = True
            myProcess = False
            continue
        if p.startswith("your ticket"):
            myProcess = True
            continue

        if myProcess:
            continue

        rules = p.split(":")[1].split()
        validRange.append(extractRule(rules[0]))
        validRange.append(extractRule(rules[2]))


    print(validRange)
    print(invalidSeats)
    print(sum(invalidSeats))

def extractRule(rule: str) -> (int, int):
    lr = rule.split("-")
    return (int(lr[0]), int(lr[1]))

if __name__ == '__main__':
	main()
