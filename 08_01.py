def main():
    count = 623
    op, val = list(), list()
    for _ in range(count):
        cur_op, cur_val = input().split()
        op.append(cur_op)
        val.append(int(cur_val))
    seen = [False for _ in range(count)]
    acc_num = 0
    pos = 0

    while True:
        if seen[pos]:
            break
        seen[pos] = True
        if op[pos] == "jmp":
            pos += val[pos]
            continue
        if op[pos] == "acc":
            acc_num += val[pos]
        # both acc and nop increase position
        pos += 1

    print(acc_num)


if __name__ == '__main__':
	main()
