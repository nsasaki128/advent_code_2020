from collections import defaultdict
def main():
    count = 553
    color_tile = defaultdict(int)

    for _ in range(count):
        x, y = 0, 0
        tile_info = input()
        i = 0
        while i < len(tile_info):
            if tile_info[i] == "e":
                x += 2
                i += 1
                continue
            elif tile_info[i] == "w":
                x -= 2
                i += 1
                continue
            elif i == len(tile_info) - 1:
                i += 1
                continue

            if tile_info[i] == "s" and tile_info[i+1] == "w":
                x -= 1
                y -= 1
            if tile_info[i] == "s" and tile_info[i+1] == "e":
                x += 1
                y -= 1
            if tile_info[i] == "n" and tile_info[i+1] == "w":
                x -= 1
                y += 1
            if tile_info[i] == "n" and tile_info[i+1] == "e":
                x += 1
                y += 1
            i += 2
        color_tile[(x, y)] += 1

    ans = 0
    for v in color_tile.values():
        ans += 1 if v%2 == 1 else 0

    print(ans)


if __name__ == '__main__':
	main()

