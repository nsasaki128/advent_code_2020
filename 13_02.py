import sys
def main():
    input()
    ids = input().split(",")
    print(chinese_rem(ids))


def mod(a, m):
    return (a % m + m) % m


def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, q, p = ext_gcd(b, a%b)
    q -= a//b * p
    return d, p, q

def chinese_rem(ids):
    r, m = 0, 1
    for i, cur in enumerate(ids):
        if cur == "x":
            continue
        mi = int(cur)
        bi = mi - i
        d, p, q = ext_gcd(m, mi)

        if (bi - i - r) % d != 0:
            return 0, -1
        tmp = (bi - r) // d * p % (mi // d)
        r += m * tmp
        m *= mi // d

    return mod(r, m), m



if __name__ == '__main__':
	main()
