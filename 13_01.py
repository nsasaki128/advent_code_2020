import sys
def main():
    t = int(input())
    ids = input().split(",")

    ansTime = sys.maxsize
    ansId = 0

    for cur in ids:
        if not cur.isnumeric():
            continue
        i = int(cur)
        curAnsTime = i * ( ( (t//i) + 1) ) if t%i != 0 else t

        if curAnsTime < ansTime:
            ansTime = curAnsTime
            ansId = i

    print(f"time: {ansTime}")
    print(f"id: {ansId}")
    print(f"ans: {(ansTime - t) * ansId}")



if __name__ == '__main__':
	main()
