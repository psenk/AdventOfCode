def solve_part_one():
    t_map = create_map()

    # find starting points
    starts = get_trail_starts(t_map)

    total = 0
    for start in starts:
        total += scan(t_map, start)
    print(total)


def get_trail_starts(t_map):
    starts = []
    for i in range(len(t_map)):
        for j in range(len(t_map[0])):
            if t_map[i][j] == 0:
                starts.append((i, j))
    return starts


def create_map():
    t_map = []
    with open('data\\day_ten.txt') as file:
        for line in file:
            t_map.append(list(map(int, line.strip())))
    return t_map


def scan(t_map, point):
    count = 0
    stack = [point]
    visited = set()
    while stack:
        pos = stack.pop(0)
        if pos in visited:
            continue
        else:
            visited.add(pos)
        val = t_map[pos[0]][pos[1]]
        if val == 9:
            count += 1
            continue
        # up
        if pos[0] > 0 and t_map[pos[0] - 1][pos[1]] == val + 1:
            stack.append((pos[0] - 1, pos[1]))
        # down
        if pos[0] < len(t_map) - 1 and t_map[pos[0] + 1][pos[1]] == val + 1:
            stack.append((pos[0] + 1, pos[1]))
        # left
        if pos[1] > 0 and t_map[pos[0]][pos[1] - 1] == val + 1:
            stack.append((pos[0], pos[1] - 1))
        # right
        if pos[1] < len(t_map[0]) - 1 and t_map[pos[0]][pos[1] + 1] == val + 1:
            stack.append((pos[0], pos[1] + 1))
    return count


def solve_part_two():
    t_map = create_map()
    starts = get_trail_starts(t_map)

    total = 0
    for start in starts:
        total += get_ratings(t_map, start)
    print(total)


def get_ratings(t_map, point):
    count = 0
    stack = [point]
    while stack:
        pos = stack.pop(0)
        val = t_map[pos[0]][pos[1]]

        if val == 9:
            count += 1
            continue

        # up
        if pos[0] > 0 and t_map[pos[0] - 1][pos[1]] == val + 1:
            stack.append((pos[0] - 1, pos[1]))
        # down
        if pos[0] < len(t_map) - 1 and t_map[pos[0] + 1][pos[1]] == val + 1:
            stack.append((pos[0] + 1, pos[1]))
        # left
        if pos[1] > 0 and t_map[pos[0]][pos[1] - 1] == val + 1:
            stack.append((pos[0], pos[1] - 1))
        # right
        if pos[1] < len(t_map[0]) - 1 and t_map[pos[0]][pos[1] + 1] == val + 1:
            stack.append((pos[0], pos[1] + 1))
    return count
