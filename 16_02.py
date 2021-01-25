import copy
def main():
    count = 267
    validRange = list()
    nearbyProcess = False
    myProcess = False
    checkPos = set()
    nearbySeats = list()
    mySeats = list()

    for _ in range(count):
        p = input()
        if nearbyProcess:
            seats = list(map(int, p.split(",")))
            nearbySeats.append(seats)
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
            mySeats = list(map(int, p.split(",")))
            continue

        validRange.append(extractRule(p))


    # Ignore invalid seats
    invalidSeats = set()
    for row in range(len(nearbySeats)):
        for col in range(len(nearbySeats[row])):
            invalid = True
            seat = nearbySeats[row][col]
            for l1, r1, l2, r2, info in validRange:
                if l1 <= seat <= r1 or l2 <= seat <= r2:
                    invalid = False
                    break
            if invalid:
                invalidSeats.add((row, col))

    # Collect possible combination
    possibleCombination = [{} for _ in range(len(nearbySeats[0]))]
    col = 0
    while col < len(nearbySeats[0]):
        for l1, r1, l2, r2, info in validRange:
            invalid = False
            for row in range(len(nearbySeats)):
                if (row, col) in invalidSeats:
                    continue
                seat = nearbySeats[row][col]
                if not(l1 <= seat <= r1 or l2<= seat <= r2):
                    invalid = True
                    break

            if not invalid:
                possibleCombination[col]["id"] = col
                if "info" not in possibleCombination[col]:
                    possibleCombination[col]["info"] = list()
                possibleCombination[col]["info"].append(info)
        col += 1

    # Guess
    possibleCombination.sort(key=lambda x: len(x["info"]))
    isSolved, seatCols = solve(0, possibleCombination, dict())

    # multiple departure seat num
    ans = 1
    for k, v in seatCols.items():
        if k.startswith("departure"):
            ans *= mySeats[v]
    print(ans)

def solve(num, possibleCombination, ans):
    if num == len(possibleCombination):
        return True, ans
    cur = possibleCombination[num]
    curAns = copy.deepcopy(ans)
    for name in cur["info"]:
        # Already used
        if name in ans:
            continue
        # Consider as use
        curAns[name] = cur["id"]
        isSolved, possibleAns = solve(num+1, possibleCombination, curAns)
        if isSolved:
            return True, possibleAns
        curAns.pop(name)
    # Try all possible combination but it can't be solved
    return False, None

def extractRule(p: str) -> (int, int, int, int, str):
    ruleInfo = p.split(":")
    rules = ruleInfo[1].split()
    lr1 = rules[0].split("-")
    lr2 = rules[2].split("-")
    return (int(lr1[0]), int(lr1[1]), int(lr2[0]), int(lr2[1]), ruleInfo[0])

if __name__ == '__main__':
	main()
