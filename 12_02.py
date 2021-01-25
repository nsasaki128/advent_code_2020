def main():
    count = 780
    position = [0, 0]
    direction = [10, 1]
    for _ in range(count):
        cur = input()
        action, value = cur[0], int(cur[1:])
        position, direction = move(position, direction, action, value)

    print(position)
    print(abs(position[0]) + abs(position[1]))


def move(position, direction, action, value):
    if value == 0:
        return position, direction
    if action == "L":
        if value == 90:
            direction = [-direction[1], direction[0]]
        if value == 180:
            direction = [-direction[0], -direction[1]]
        if value == 270:
            direction = [direction[1], -direction[0]]
    if action == "R":
        if value == 90:
            direction = [direction[1], -direction[0]]
        if value == 180:
            direction = [-direction[0], -direction[1]]
        if value == 270:
            direction = [-direction[1], direction[0]]

    if action == "F":
        position = [position[0] + value * direction[0], position[1] + value * direction[1]]

    if action == "N":
        direction[1] += value
    if action == "S":
        direction[1] -= value
    if action == "E":
        direction[0] += value
    if action == "W":
        direction[0] -= value

    return position, direction


if __name__ == '__main__':
	main()
