def main():
    count = 374
    ans = 0

    for _ in range(count):
        p = tokenize(input())
        a = calc(p, 0)[0]
        ans += a
    print(ans)


def calc(tok, num):
    cur = 0
    op = "+"
    i = num
    while i < len(tok):
        if tok[i] == "*" or tok[i] == "+":
            op = tok[i]
        elif tok[i] == "(":
            res, nextI = calc(tok, i+1)
            cur = operation(op, cur, res)
            i = nextI
        elif tok[i] == ")":
            return cur, i
        elif tok[i].isdigit():
            cur = operation(op, cur, int(tok[i]))
        i += 1

    return cur, i


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
