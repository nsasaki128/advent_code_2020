from collections import defaultdict
def main():
    count = 553
    days = 100
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

    cur_blacks = set()
    for pos, v in color_tile.items():
        if v%2 == 1:
            cur_blacks.add(pos)

    adjacent = [(-2, 0), (-1, -1), (-1, 1), (2, 0), (1, 1), (1, -1)]
    for _ in range(days):
        next_blacks = set()
        for x, y in cur_blacks:
            # Check black tile
            black_num = 0
            for dx, dy in adjacent:
                if (x+dx, y+dy) in cur_blacks:
                    black_num += 1
            if black_num == 1 or black_num == 2:
                next_blacks.add((x, y))
            # Chwck adjacent white tile
            for dx, dy in adjacent:
                white_black_num = 0
                # Eliminate black
                if (x+dx, y+dy) in cur_blacks:
                    continue
                # Eliminate already checked tile
                if (x+dx, y+dy) in next_blacks:
                    continue
                for dx2, dy2 in adjacent:
                    if (x+dx+dx2, y+dy+dy2) in cur_blacks:
                        white_black_num += 1
                if white_black_num == 2:
                    next_blacks.add((x+dx, y+dy))
        cur_blacks = next_blacks

    print(len(cur_blacks))


if __name__ == '__main__':
	main()

