def main():
    count = 623
    op, val = list(), list()
    for _ in range(count):
        curOp, curVal = input().split()
        op.append(curOp)
        val.append(int(curVal))
    seen = [False for _ in range(count)]
    accNum = 0
    pos = 0

    while True:
        if seen[pos]:
            break
        seen[pos] = True
        if op[pos] == "jmp":
            pos += val[pos]
            continue
        if op[pos] == "acc":
            accNum += val[pos]
        # both acc and nop increase position
        pos += 1

    print(accNum)


if __name__ == '__main__':
	main()
