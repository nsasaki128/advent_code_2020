def main():
    count = 8
    repeat = 6
    total = 2*(repeat+1) + count
    cube = [[[[0 for _ in range(total)] for _ in range(total)] for _ in range(total)] for _ in range(total)]
    centerZW = total//2
    xyStart = centerZW - count//2

    for i in range(count):
        p = input()
        for j in range(len(p)):
            cube[xyStart + i][xyStart + j][centerZW][centerZW] = 1 if p[j] == "#" else 0

    for _ in range(repeat):
        print(countCube(cube))
        cube = createNewCube(cube)

    print(countCube(cube))

def createNewCube(prev):
    cube = [[[[0 for _ in range(len(prev))] for _ in range(len(prev))] for _ in range(len(prev))] for _ in range(len(prev))]

    for x in range(1, len(cube)-1):
        for y in range(1, len(cube[x])-1):
            for z in range(1, len(cube[x][y])-1):
                for w in range(1, len(cube[x][y][z])-1):
                    neighbors = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                for dw in range(-1, 2):
                                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                        continue
                                    neighbors += prev[x+dx][y+dy][z+dz][w+dw]
                    if prev[x][y][z][w] == 0 and neighbors == 3:
                        cube[x][y][z][w] = 1
                    if prev[x][y][z][w] == 1 and (neighbors == 3 or neighbors == 2):
                        cube[x][y][z][w] = 1
    return cube

def countCube(cube):
    ans = 0
    for world in cube:
        for plane in world:
            for line in plane:
                for dot in line:
                    ans += dot
    return ans

if __name__ == '__main__':
	main()
