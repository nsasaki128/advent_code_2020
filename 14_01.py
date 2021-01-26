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
        mem_dict[mem_pos] = update_mem(int(cur[2]), mask)

    print(sum(mem_dict.values()))

MASK_LEN = 36
def update_mem(mem: int, mask: str) -> int:
    for i in range(MASK_LEN):
        if mask[MASK_LEN-i-1] == "1":
            mem |= 1 << i
        if mask[MASK_LEN-i-1] == "0":
            mem &= ~(1 << i)
    return mem


if __name__ == '__main__':
	main()
