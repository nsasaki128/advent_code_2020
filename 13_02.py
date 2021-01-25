import sys
def main():
    input()
    ids = input().split(",")
    print(chineseRem(ids))


def mod(a, m):
    return (a % m + m) % m


def extGcd(a, b):
    if b == 0:
        return a, 1, 0
    d, q, p = extGcd(b, a%b)
    q -= a//b * p
    return d, p, q

def chineseRem(ids):
    r, m = 0, 1
    for i, cur in enumerate(ids):
        if cur == "x":
            continue
        mi = int(cur)
        bi = mi - i
        d, p, q = extGcd(m, mi)

        if (bi - i - r) % d != 0:
            return 0, -1
        tmp = (bi - r) // d * p % (mi // d)
        r += m * tmp
        m *= mi // d

    return mod(r, m), m



if __name__ == '__main__':
	main()
