import sys
def main():
    t = int(input())
    ids = input().split(",")

    ans_time = sys.maxsize
    ans_id = 0

    for cur in ids:
        if not cur.isnumeric():
            continue
        i = int(cur)
        cur_ans_time = i * ( ( (t//i) + 1) ) if t%i != 0 else t

        if cur_ans_time < ans_time:
            ans_time = cur_ans_time
            ans_id = i

    print(f"time: {ans_time}")
    print(f"id: {ans_id}")
    print(f"ans: {(ans_time - t) * ans_id}")



if __name__ == '__main__':
	main()
