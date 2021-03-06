from copy import deepcopy
def main():
    count = 90
    matrix = list()
    for i in range(count):
        cur = list("."+input()+".")
        if i == 0:
            matrix.append(list("."*len(cur)))
        matrix.append(cur)
    matrix.append(list("."*len(matrix[0])))
    repeat = 0

    while True:
        repeat += 1
        successor = seat_change(matrix)
        if is_same(matrix, successor):
            break
        matrix = successor

    print(repeat)
    print(count_empty_seat(matrix))

def is_same(before, after):
    for i in range(1, len(before)-1):
        for j in range(1, len(before[i])-1):
            if after[i][j] != before[i][j]:
                return False
    return True


def seat_change(matrix):
    result = deepcopy(matrix)
    adj = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]]

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            cur = matrix[i][j]
            if cur == "#":
                count = 0
                for n in adj:
                    if matrix[i+n[0]][j+n[1]] == "#":
                        count += 1
                if count >= 4:
                    result[i][j] = "L"
            if cur == "L":
                is_adj_empty = True
                for n in adj:
                    if matrix[i+n[0]][j+n[1]] == "#":
                        is_adj_empty = False
                        continue
                if is_adj_empty:
                    result[i][j] = "#"

    return result


def count_empty_seat(matrix):
    ans = 0
    for row in matrix:
        ans += row.count("#")
    return ans


if __name__ == '__main__':
	main()
