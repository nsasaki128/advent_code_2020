def main():
    count = 623
    op, val = list(), list()
    changeInstructions = list()
    for i in range(count):
        curOp, curVal = input().split()
        op.append(curOp)
        val.append(int(curVal))
        if curOp != "acc":
            changeInstructions.append(i)

    seen = [False for _ in range(count)]
    accNum = 0
    pos = 0
    curChange = changeInstructions.pop()
    while True:
        if pos >= count:
            break
        # Fault initialize
        if seen[pos]:
            seen = [False for _ in range(count)]
            accNum = 0
            pos = 0
            curChange = changeInstructions.pop()

        seen[pos] = True
        if op[pos] == "acc":
            accNum += val[pos]
            pos += 1
            continue
        if op[pos] == "jmp":
            # work as nop
            if pos == curChange:
                pos += 1
                continue
            pos += val[pos]
            continue

        if op[pos] == "nop":
            # work as jmp
            if pos == curChange:
                pos += val[pos]
                continue
            pos += 1
    print(accNum)


if __name__ == '__main__':
	main()
