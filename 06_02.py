import copy
def main():
    count = 2178#15
    ans = 0
    cur = set()
    isFirst = True
    for _ in range(count):
        p = input()
        if len(p) == 0:
            ans += len(cur)
            isFirst = True
            continue

        person = set()
        for c in p:
            if c.isalpha():
                person.add(c)
        if isFirst:
            cur = person
            isFirst = False
        else:
            cur &= person
    ans += len(cur)
    print(ans)


if __name__ == '__main__':
	main()
