def main():
    count = 562
    mask = ""
    mem_dict = dict()

    for _ in range(count):
        cur = input().split()
        if cur[0] == "mask":
            mask = cur[2]
            continue
        mem_pos = int(cur[0][4:-1])
        cur_set = get_mem_pos_set(mem_pos, mask)
        for v in cur_set:
            mem_dict[v] = int(cur[2])

    print(sum(mem_dict.values()))

MASK_LEN = 36
def get_mem_pos_set(mem: int, mask: str) -> set:
    x_pos = set()
    for i in range(MASK_LEN):
        if mask[MASK_LEN-i-1] == "1":
            mem |= 1 << i
        if mask[MASK_LEN-i-1] == "X":
            x_pos.add(i)
    cur_set = {mem}
    for i in x_pos:
        next_set = set()
        for m in cur_set:
            next_set.add(m | (1<<i))
            next_set.add(m & ~(1<<i))
        cur_set = next_set
    return cur_set

if __name__ == '__main__':
	main()
