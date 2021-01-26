from collections import defaultdict
from collections import deque
tileLen = 10
squareLen = 12
count = squareLen*squareLen

def main():
    tiles = list()
    tilesDict = dict()
    edgeTileNames = dict()
    nameEdges = dict()

    for i in range(count):
        name = int(input().split()[1][:-1])
        curTile = list()
        for _ in range(tileLen):
            tile = list(input())
            curTile.append(tile)
        tiles.append(curTile)
        tilesDict[name] = curTile
        nameEdges[name] = set()

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
            nameEdges[name].add(e)

        input()

    aloneEdges = defaultdict(int)
    for k, vs in edgeTileNames.items():
        if len(vs) != 1:
            continue
        for v in vs:
            aloneEdges[v] += 1


    # Find left top
    lt = 0
    for k, v in aloneEdges.items():
        if v == 4:
            lt = k
            break

    fixSquare = fixTile(lt, edgeTileNames, tilesDict)

    #Create Tile
    ansTile = [["" for _ in range(squareLen*(tileLen-2))] for _ in range(squareLen*(tileLen-2))]
    totalSharp = 0
    for i in range(squareLen):
        for j in range(squareLen):
            curTile = fixSquare[i][j]
            for k in range(1, tileLen-1):
                for l in range(1, tileLen-1):
                    ansTile[i*(tileLen-2)+k-1][j*(tileLen-2)+l-1] = curTile[k][l]
                    totalSharp += 1 if curTile[k][l] == "#" else 0

    rotateNum = 8
    maxMonsNum = 0
    for n in range(rotateNum):
        monsNum = findMonsterNum(ansTile)
        maxMonsNum = max(maxMonsNum, monsNum)
        if n == 4:
            ansTile = flipTile(ansTile)
        else:
            ansTile = rotateTile(ansTile)
    print(totalSharp-maxMonsNum*15)


def rotateTile(tile):
    retTile = [["" for _ in range(len(tile[0]))] for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            retTile[i][j] = tile[len(tile)-1-j][i]
    return retTile

def flipTile(tile):
    retTile = [["" for _ in range(len(tile[0]))] for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            retTile[i][j] = tile[len(tile)-1-i][j]
    return retTile


def fixTile(lt, edgeTileNames, tilesDict):
    fixSquare = [[[["" for _ in range(tileLen)] for _ in range(tileLen)] for _ in range(squareLen)] for _ in range(squareLen)]
    rotateNum = 5
    seen = set()
    nextSquareQueue = deque()
    nextSquareQueue.append([0, 0, lt])
    posRestriction = dict()
    posRestriction[(0, 0)] = list()

    while nextSquareQueue:
        curI, curJ, curName = nextSquareQueue.popleft()
        curRestriction = posRestriction[(curI, curJ)]
        curSquare = tilesDict[curName]
        curRepeat = 0
        while True:
            le, re = list(), list()
            for j in range(tileLen):
                le.append(curSquare[j][0])
                re.append(curSquare[j][-1])
            t = "".join(curSquare[0])
            b = "".join(curSquare[-1])
            l = "".join(le)
            r = "".join(re)
            edges = list()
            edges.append(t)
            edges.append(b)
            edges.append(l)
            edges.append(r)
            isRightPos = True
            for direction, restriction in curRestriction:
                if edges[direction] != restriction:
                    isRightPos = False
            if curI == 0:
                if len(edgeTileNames[t]) != 1:
                    isRightPos = False
            if curJ == 0:
                if len(edgeTileNames[l]) != 1:
                    isRightPos = False
            if curI == squareLen-1:
                if len(edgeTileNames[b]) != 1:
                    isRightPos = False
            if curJ == squareLen-1:
                if len(edgeTileNames[r]) != 1:
                    isRightPos = False

            if isRightPos:
                fixSquare[curI][curJ] = curSquare
                seen.add(curName)
                if curI+1 != squareLen:
                    for v in edgeTileNames[b]:
                        if v in seen:
                            continue
                        if (curI+1, curJ) not in posRestriction:
                            nextSquareQueue.append([curI+1, curJ, v])
                            posRestriction[(curI+1, curJ)] = list()
                        posRestriction[(curI+1, curJ)].append([0, b])
                if curJ+1 != squareLen:
                    for v in edgeTileNames[r]:
                        if v in seen:
                            continue
                        if (curI, curJ+1) not in posRestriction:
                            nextSquareQueue.append([curI, curJ+1, v])
                            posRestriction[(curI, curJ+1)] = list()
                        posRestriction[(curI, curJ+1)].append([2, r])
                break
            curRepeat += 1
            if curRepeat == rotateNum:
                curSquare = flipTile(curSquare)
                continue
            curSquare = rotateTile(curSquare)

    return fixSquare


monster = [(0, 18), (1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11), (1, 12), (2, 13), (2, 16), (1, 17), (1, 18), (1,19)]
monsHeight = 20
monsWidth = 3
def findMonsterNum(tile):
    monsNum = 0
    for i in range(len(tile)-monsWidth):
        for j in range(len(tile)-monsHeight):
            monsNum += 1 if findMonster(tile, i, j) else 0
    return monsNum


def findMonster(tile, i, j):
    for di, dj in monster:
        if tile[i+di][j+dj] != "#":
            return False
    return True


if __name__ == '__main__':
	main()
