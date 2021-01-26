import copy
def main():
    count = 2178#15
    ans = 0
    cur = set()
    is_first = True
    for _ in range(count):
        p = input()
        if len(p) == 0:
            ans += len(cur)
            is_first = True
            continue

        person = set()
        for c in p:
            if c.isalpha():
                person.add(c)
        if is_first:
            cur = person
            is_first = False
        else:
            cur &= person
    ans += len(cur)
    print(ans)


if __name__ == '__main__':
	main()
