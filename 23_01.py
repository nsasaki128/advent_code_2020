def main():
    repeat = 100

    cur = input()
    cur_array = list(map(int, cur))
    for _ in range(repeat):
        pick = cur_array[0]
        skips = cur_array[1:4]
        destination = next_destination(pick)
        while destination in skips:
            destination = next_destination(destination)
        next_top_pos = cur_array.index(destination)
        next_array = cur_array[4:next_top_pos+1]+skips
        if next_top_pos != len(cur_array)-1:
            next_array += cur_array[next_top_pos+1:]
        next_array += [pick]
        cur_array = next_array

    print(cur_array)
    pick_pos = cur_array.index(1)
    ans_array = []
    if pick_pos != len(cur_array)-1:
        ans_array = cur_array[pick_pos+1:]
    ans_array += cur_array[:pick_pos]
    print(ans_array)
    print("".join(list(map(str, ans_array))))


def next_destination(p):
    return p-1 if p != 1 else 9


if __name__ == '__main__':
	main()
