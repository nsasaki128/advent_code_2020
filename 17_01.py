def main():
    count = 8
    repeat = 6
    total = 2*(repeat+1) + count
    cube = [[["." for _ in range(total)] for _ in range(total)] for _ in range(total)]
    centerZ = total//2
    xyStart = centerZ - count//2

    for i in range(count):
        p = input()
        for j in range(len(p)):
            cube[xyStart + i][xyStart + j][centerZ] = p[j]

    for _ in range(repeat):
        cube = createNewCube(cube)

    ans = 0
    for plane in cube:
        for line in plane:
            for dot in line:
                if dot == "#":
                    ans += 1
    print(ans)

def createNewCube(prev):
    cube = [[["." for _ in range(len(prev))] for _ in range(len(prev))] for _ in range(len(prev))]

    for x in range(1, len(cube)-1):
        for y in range(1, len(cube[x])-1):
            for z in range(1, len(cube[x][y])-1):
                neighbors = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        for dz in range(-1, 2):
                            if dx == 0 and dy == 0 and dz == 0:
                                continue
                            neighbors += 1 if prev[x+dx][y+dy][z+dz] == "#" else 0
                if prev[x][y][z] == "." and neighbors == 3:
                    cube[x][y][z] = "#"
                if prev[x][y][z] == "#" and (neighbors == 3 or neighbors == 2):
                    cube[x][y][z] = "#"
    return cube


if __name__ == '__main__':
	main()
