from collections import defaultdict
from collections import deque
TILE_LEN = 10
SQUARE_LEN = 12
COUNT = SQUARE_LEN*SQUARE_LEN

def main():
    tiles = list()
    tiles_dict = dict()
    edge_tile_names = dict()
    name_edges = dict()

    for i in range(COUNT):
        name = int(input().split()[1][:-1])
        cur_tile = list()
        for _ in range(TILE_LEN):
            tile = list(input())
            cur_tile.append(tile)
        tiles.append(cur_tile)
        tiles_dict[name] = cur_tile
        name_edges[name] = set()

        le, re = list(), list()
        for j in range(TILE_LEN):
            le.append(cur_tile[j][0])
            re.append(cur_tile[j][-1])
        t = "".join(cur_tile[0])
        b = "".join(cur_tile[-1])
        l = "".join(le)
        r = "".join(re)
        rt = "".join(reversed(cur_tile[0]))
        rb = "".join(reversed(cur_tile[-1]))
        rl = "".join(reversed(le))
        rr = "".join(reversed(re))
        cur_edges = list()
        cur_edges.append(t)
        cur_edges.append(b)
        cur_edges.append(l)
        cur_edges.append(r)
        cur_edges.append(rt)
        cur_edges.append(rb)
        cur_edges.append(rl)
        cur_edges.append(rr)
        for e in cur_edges:
            if e not in edge_tile_names:
                edge_tile_names[e] = set()
            edge_tile_names[e].add(name)
            name_edges[name].add(e)

        input()

    alone_edges = defaultdict(int)
    for k, vs in edge_tile_names.items():
        if len(vs) != 1:
            continue
        for v in vs:
            alone_edges[v] += 1


    # _find left top
    lt = 0
    for k, v in alone_edges.items():
        if v == 4:
            lt = k
            break

    fix_square = fix_tile(lt, edge_tile_names, tiles_dict)

    #_create _tile
    ans_tile = [["" for _ in range(SQUARE_LEN*(TILE_LEN-2))] for _ in range(SQUARE_LEN*(TILE_LEN-2))]
    total_sharp = 0
    for i in range(SQUARE_LEN):
        for j in range(SQUARE_LEN):
            cur_tile = fix_square[i][j]
            for k in range(1, TILE_LEN-1):
                for l in range(1, TILE_LEN-1):
                    ans_tile[i*(TILE_LEN-2)+k-1][j*(TILE_LEN-2)+l-1] = cur_tile[k][l]
                    total_sharp += 1 if cur_tile[k][l] == "#" else 0

    rotate_num = 8
    max_mons_num = 0
    for n in range(rotate_num):
        mons_num = find_monster_num(ans_tile)
        max_mons_num = max(max_mons_num, mons_num)
        if n == 4:
            ans_tile = flip_tile(ans_tile)
        else:
            ans_tile = rotate_tile(ans_tile)
    print(total_sharp-max_mons_num*15)


def rotate_tile(tile):
    ret_tile = [["" for _ in range(len(tile[0]))] for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            ret_tile[i][j] = tile[len(tile)-1-j][i]
    return ret_tile

def flip_tile(tile):
    ret_tile = [["" for _ in range(len(tile[0]))] for _ in range(len(tile))]
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            ret_tile[i][j] = tile[len(tile)-1-i][j]
    return ret_tile


def fix_tile(lt, edge_tile_names, tiles_dict):
    fix_square = [[[["" for _ in range(TILE_LEN)] for _ in range(TILE_LEN)] for _ in range(SQUARE_LEN)] for _ in range(SQUARE_LEN)]
    rotate_num = 5
    seen = set()
    next_square_queue = deque()
    next_square_queue.append([0, 0, lt])
    pos_restriction = dict()
    pos_restriction[(0, 0)] = list()

    while next_square_queue:
        cur_i, cur_j, cur_name = next_square_queue.popleft()
        cur_restriction = pos_restriction[(cur_i, cur_j)]
        cur_square = tiles_dict[cur_name]
        cur_repeat = 0
        while True:
            le, re = list(), list()
            for j in range(TILE_LEN):
                le.append(cur_square[j][0])
                re.append(cur_square[j][-1])
            t = "".join(cur_square[0])
            b = "".join(cur_square[-1])
            l = "".join(le)
            r = "".join(re)
            edges = list()
            edges.append(t)
            edges.append(b)
            edges.append(l)
            edges.append(r)
            is_right_pos = True
            for direction, restriction in cur_restriction:
                if edges[direction] != restriction:
                    is_right_pos = False
            if cur_i == 0:
                if len(edge_tile_names[t]) != 1:
                    is_right_pos = False
            if cur_j == 0:
                if len(edge_tile_names[l]) != 1:
                    is_right_pos = False
            if cur_i == SQUARE_LEN-1:
                if len(edge_tile_names[b]) != 1:
                    is_right_pos = False
            if cur_j == SQUARE_LEN-1:
                if len(edge_tile_names[r]) != 1:
                    is_right_pos = False

            if is_right_pos:
                fix_square[cur_i][cur_j] = cur_square
                seen.add(cur_name)
                if cur_i+1 != SQUARE_LEN:
                    for v in edge_tile_names[b]:
                        if v in seen:
                            continue
                        if (cur_i+1, cur_j) not in pos_restriction:
                            next_square_queue.append([cur_i+1, cur_j, v])
                            pos_restriction[(cur_i+1, cur_j)] = list()
                        pos_restriction[(cur_i+1, cur_j)].append([0, b])
                if cur_j+1 != SQUARE_LEN:
                    for v in edge_tile_names[r]:
                        if v in seen:
                            continue
                        if (cur_i, cur_j+1) not in pos_restriction:
                            next_square_queue.append([cur_i, cur_j+1, v])
                            pos_restriction[(cur_i, cur_j+1)] = list()
                        pos_restriction[(cur_i, cur_j+1)].append([2, r])
                break
            cur_repeat += 1
            if cur_repeat == rotate_num:
                cur_square = flip_tile(cur_square)
                continue
            cur_square = rotate_tile(cur_square)

    return fix_square


MONSTER = [(0, 18), (1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11), (1, 12), (2, 13), (2, 16), (1, 17), (1, 18), (1,19)]
MONS_HEIGHT = 20
MONS_WIDTH = 3
def find_monster_num(tile):
    mons_num = 0
    for i in range(len(tile)-MONS_WIDTH):
        for j in range(len(tile)-MONS_HEIGHT):
            mons_num += 1 if find_monster(tile, i, j) else 0
    return mons_num


def find_monster(tile, i, j):
    for di, dj in MONSTER:
        if tile[i+di][j+dj] != "#":
            return False
    return True


if __name__ == '__main__':
	main()
