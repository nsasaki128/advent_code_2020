from collections import defaultdict
def main():
    tile_len = 10
    count = 144
    tiles = list()
    edge_tile_names = dict()

    for i in range(count):
        name = int(input().split()[1][:-1])
        cur_tile = list()
        for _ in range(tile_len):
            tile = list(input())
            cur_tile.append(tile)
        tiles.append(cur_tile)

        le, re = list(), list()
        for j in range(tile_len):
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

        input()

    alone_edges = defaultdict(int)
    for vs in edge_tile_names.values():
        if len(vs) != 1:
            continue
        for v in vs:
            alone_edges[v] += 1

    ans = 1
    for k, v in alone_edges.items():
        if v == 4:
            print(k)
            ans *= k

    print(alone_edges)
    print(ans)


if __name__ == '__main__':
    main()

