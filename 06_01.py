import copy
def main():
    count = 2178
    ans = 0
    cur = set()
    for _ in range(count):
        p = input()
        if len(p) == 0:
            ans += len(cur)
            cur = set()
            continue
        for c in p:
            if c.isalpha():
                cur.add(c)
    ans += len(cur)
    print(ans)


if __name__ == '__main__':
	main()
