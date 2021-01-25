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
        curSet = getMemPosSet(memPos, mask)
        for v in curSet:
            memDict[v] = int(cur[2])

    print(sum(memDict.values()))

maskLen = 36
def getMemPosSet(mem: int, mask: str) -> set:
    xPos = set()
    for i in range(maskLen):
        if mask[maskLen-i-1] == "1":
            mem |= 1 << i
        if mask[maskLen-i-1] == "X":
            xPos.add(i)
    curSet = {mem}
    for i in xPos:
        nextSet = set()
        for m in curSet:
            nextSet.add(m | (1<<i))
            nextSet.add(m & ~(1<<i))
        curSet = nextSet
    return curSet

if __name__ == '__main__':
	main()
