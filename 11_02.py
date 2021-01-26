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
        successor = seat_change(matrix, False)
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


def seat_change(matrix, debug):
    result = deepcopy(matrix)
    l = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    r = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    u = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    d = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    lu = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    ld = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    ru = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    rd = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # From Left to Right, Up to Down
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            if matrix[i][j] == ".":
                l[i][j] = l[i][j-1]
                u[i][j] = u[i-1][j]
                lu[i][j] = lu[i-1][j-1]
            if matrix[i][j] == "#":
                l[i][j] = True
                r[i][j] = True
                u[i][j] = True
                d[i][j] = True
                lu[i][j] = True
                ld[i][j] = True
                ru[i][j] = True
                rd[i][j] = True

    # From Right to Left, Down to Up
    for i in range(len(matrix)-2, 0, -1):
        for j in range(len(matrix[i])-2, 0, -1):
            if matrix[i][j] == ".":
                r[i][j] = r[i][j+1]
                d[i][j] = d[i+1][j]
                rd[i][j] = rd[i+1][j+1]

    # From Right to Left, Up to Down
    for i in range(1, len(matrix)-1):
        for j in range(len(matrix[i])-2, 0, -1):
            if matrix[i][j] == ".":
                ru[i][j] = ru[i-1][j+1]

    # From Left to Right, Down to Up
    for i in range(len(matrix)-2, 0, -1):
        for j in range(1, len(matrix[i])-1):
            if matrix[i][j] == ".":
                ld[i][j] = ld[i+1][j-1]

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            cur = matrix[i][j]
            count = 0
            if cur == "#":
                count += 1 if l[i][j-1] else 0
                count += 1 if r[i][j+1] else 0
                count += 1 if u[i-1][j] else 0
                count += 1 if d[i+1][j] else 0
                count += 1 if lu[i-1][j-1] else 0
                count += 1 if ld[i+1][j-1] else 0
                count += 1 if ru[i-1][j+1] else 0
                count += 1 if rd[i+1][j+1] else 0
                if count > 4:
                    result[i][j] = "L"
            if cur == "L":
                if l[i][j-1] or r[i][j+1] or u[i-1][j] or d[i+1][j]:
                    continue
                if lu[i-1][j-1] or ld[i+1][j-1] or ru[i-1][j+1] or rd[i+1][j+1]:
                    continue
                result[i][j] = "#"

    return result


def count_empty_seat(matrix):
    ans = 0
    for row in matrix:
        ans += row.count("#")
    return ans


if __name__ == '__main__':
	main()
