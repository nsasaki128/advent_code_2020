nodeNum = "num"
class Node:
    def __init__(self, nodeType, val, l, r):
        self.nodeType = nodeType
        self.val = val
        self.l = l
        self.r = r

    def calc(self):
        if self.nodeType == nodeNum:
            return self.val
        if self.nodeType == "*":
            return self.l.calc() * self.r.calc()
        if self.nodeType == "+":
            return self.l.calc() + self.r.calc()
        return 0

    def debugPrint(self, ch):
        if self.kind == nodeNum:
            print(f"{ch}└ type: {self.nodeType}, val: {self.val}")
        else:
            print(f"{ch}├ type: {self.nodeType}, val: {self.val}")
        if self.l:
            if self.r:
                print(f"{ch}├ Left")
                self.l.debugPrint(ch+"|")
            else:
                print(f"{ch}└ Left")
                self.l.debugPrint(ch+" ")
        if self.r:
            print(f"{ch}└ Right")
            self.r.debugPrint(ch+" ")


def main():
    count = 374
    ans = 0

    for _ in range(count):
        p = tokenize(input())
        n, _ = mul(p, 0)
        # n.debugPrint("")
        ans += n.calc()
    print(ans)


def add(tok, pos):
    l, i = primary(tok, pos)
    while i < len(tok):
        if tok[i] == "+":
            r, nextI = primary(tok, i+1)
            l = Node("+", l.val+r.val, l, r)
            i = nextI
        else:
            return l, i
    return l, i


def mul(tok, pos):
    l, i = add(tok, pos)
    while i < len(tok):
        if tok[i] == "*":
            r, nextI = add(tok, i+1)
            l = Node("*", l.val*r.val, l, r)
            i = nextI
        else:
            return l, i
    return l, i


def primary(tok, pos):
    i = pos
    while i < len(tok):
        if tok[i].isdigit():
            return Node(nodeNum, int(tok[i]), None, None), i+1
        if tok[i] == "(":
            n, nextI = mul(tok, i+1)
            if tok[nextI] != ")":
                print("error")
            return n, nextI+1
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
