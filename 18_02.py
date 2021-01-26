node_num = "num"
class Node:
    def __init__(self, node_type, val, l, r):
        self.node_type = node_type
        self.val = val
        self.l = l
        self.r = r

    def calc(self):
        if self.node_type == node_num:
            return self.val
        if self.node_type == "*":
            return self.l.calc() * self.r.calc()
        if self.node_type == "+":
            return self.l.calc() + self.r.calc()
        return 0

    def debug_print(self, ch):
        if self.kind == node_num:
            print(f"{ch}└ type: {self.node_type}, val: {self.val}")
        else:
            print(f"{ch}├ type: {self.node_type}, val: {self.val}")
        if self.l:
            if self.r:
                print(f"{ch}├ _left")
                self.l.debug_print(ch+"|")
            else:
                print(f"{ch}└ _left")
                self.l.debug_print(ch+" ")
        if self.r:
            print(f"{ch}└ _right")
            self.r.debug_print(ch+" ")


def main():
    count = 374
    ans = 0

    for _ in range(count):
        p = tokenize(input())
        n, _ = mul(p, 0)
        # n.debug_print("")
        ans += n.calc()
    print(ans)


def add(tok, pos):
    l, i = primary(tok, pos)
    while i < len(tok):
        if tok[i] == "+":
            r, next_i = primary(tok, i+1)
            l = Node("+", l.val+r.val, l, r)
            i = next_i
        else:
            return l, i
    return l, i


def mul(tok, pos):
    l, i = add(tok, pos)
    while i < len(tok):
        if tok[i] == "*":
            r, next_i = add(tok, i+1)
            l = Node("*", l.val*r.val, l, r)
            i = next_i
        else:
            return l, i
    return l, i


def primary(tok, pos):
    i = pos
    while i < len(tok):
        if tok[i].isdigit():
            return Node(node_num, int(tok[i]), None, None), i+1
        if tok[i] == "(":
            n, next_i = mul(tok, i+1)
            if tok[next_i] != ")":
                print("error")
            return n, next_i+1
        i += 1
    return None, len(tok)


def tokenize(p):
    ans = list()
    for i in range(len(p)):
        if p[i] == " ":
            continue
        if p[i].isdigit() and ans and ans[-1].isdigit():
                ans[-1] += p[i]
                continue
        ans.append(p[i])

    return ans


def operation(op, l, r):
    if op == "+":
        return l + r
    if op == "*":
        return l * r


if __name__ == '__main__':
	main()
