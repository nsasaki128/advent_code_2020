CUP_NUM = 1_000_000
class LinkedList:

    def __init__(self, val, nextnode=None):
        self.val = val
        self.nextnode = nextnode

    def printVals(self):
        tmp = self.nextnode
        print(self.val, end=",")
        while tmp.val != self.val:
            print(tmp.val, end=",")
            tmp = tmp.nextnode
        print()

def main():
    repeat = 10_000_000

    cur_array = list(map(int, input()))
    cur_array += [i for i in range(10, CUP_NUM+1)]
    node_dict = dict()

    head = LinkedList(cur_array[0], None)
    node_dict[cur_array[0]] = head
    cur, prev = None, head
    for i in range(1, len(cur_array)):
        cur = LinkedList(cur_array[i])
        node_dict[cur_array[i]] = cur

        prev.nextnode = cur
        prev = cur
    cur.nextnode = head
    node_1 = node_dict[1]
    cur = head

    for j in range(repeat):
        if j % CUP_NUM == 0:
            print(j)
            print()
        move = cur
        skips = set()
        for _ in range(3):
            move = move.nextnode
            skips.add(move.val)

        destination = next_destination(cur.val)
        while destination in skips:
            destination = next_destination(destination)

        dest = node_dict[destination]

        tmp = cur.nextnode
        cur.nextnode = move.nextnode
        move.nextnode = dest.nextnode
        dest.nextnode = tmp

        cur = cur.nextnode

    print(node_1.nextnode.val)
    print(node_1.nextnode.nextnode.val)
    print("ans")
    print(node_1.nextnode.val*node_1.nextnode.nextnode.val)


def next_destination(p):
    return p-1 if p != 1 else CUP_NUM


if __name__ == '__main__':
	main()
