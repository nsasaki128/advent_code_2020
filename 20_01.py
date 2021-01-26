from collections import defaultdict
def main():
    tileLen = 10
    count = 144
    tiles = list()
    edgeTileNames = dict()

    for i in range(count):
        name = int(input().split()[1][:-1])
        curTile = list()
        for _ in range(tileLen):
            tile = list(input())
            curTile.append(tile)
        tiles.append(curTile)

        le, re = list(), list()
        for j in range(tileLen):
            le.append(curTile[j][0])
            re.append(curTile[j][-1])
        t = "".join(curTile[0])
        b = "".join(curTile[-1])
        l = "".join(le)
        r = "".join(re)
        rt = "".join(reversed(curTile[0]))
        rb = "".join(reversed(curTile[-1]))
        rl = "".join(reversed(le))
        rr = "".join(reversed(re))
        curEdges = list()
        curEdges.append(t)
        curEdges.append(b)
        curEdges.append(l)
        curEdges.append(r)
        curEdges.append(rt)
        curEdges.append(rb)
        curEdges.append(rl)
        curEdges.append(rr)
        for e in curEdges:
            if e not in edgeTileNames:
                edgeTileNames[e] = set()
            edgeTileNames[e].add(name)

        input()

    aloneEdges = defaultdict(int)
    for vs in edgeTileNames.values():
        if len(vs) != 1:
            continue
        for v in vs:
            aloneEdges[v] += 1

    ans = 1
    for k, v in aloneEdges.items():
        if v == 4:
            print(k)
            ans *= k

    print(aloneEdges)
    print(ans)


if __name__ == '__main__':
	main()
