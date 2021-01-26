def main():
    count = 623
    op, val = list(), list()
    change_instructions = list()
    for i in range(count):
        cur_op, cur_val = input().split()
        op.append(cur_op)
        val.append(int(cur_val))
        if cur_op != "acc":
            change_instructions.append(i)

    seen = [False for _ in range(count)]
    acc_num = 0
    pos = 0
    cur_change = change_instructions.pop()
    while True:
        if pos >= count:
            break
        # _fault initialize
        if seen[pos]:
            seen = [False for _ in range(count)]
            acc_num = 0
            pos = 0
            cur_change = change_instructions.pop()

        seen[pos] = True
        if op[pos] == "acc":
            acc_num += val[pos]
            pos += 1
            continue
        if op[pos] == "jmp":
            # work as nop
            if pos == cur_change:
                pos += 1
                continue
            pos += val[pos]
            continue

        if op[pos] == "nop":
            # work as jmp
            if pos == cur_change:
                pos += val[pos]
                continue
            pos += 1
    print(acc_num)


if __name__ == '__main__':
	main()
