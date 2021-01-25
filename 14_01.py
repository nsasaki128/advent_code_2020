def main():
    count = 562
    mask = ""
    memDict = dict()

    for _ in range(count):
        cur = input().split()
        if cur[0] == "mask":
            mask = cur[2]
            continue
        memPos = int(cur[0][4:-1])
        memDict[memPos] = updateMem(int(cur[2]), mask)

    print(sum(memDict.values()))

maskLen = 36
def updateMem(mem: int, mask: str) -> int:
    for i in range(maskLen):
        if mask[maskLen-i-1] == "1":
            mem |= 1 << i
        if mask[maskLen-i-1] == "0":
            mem &= ~(1 << i)
    return mem


if __name__ == '__main__':
	main()
