"""
if obj in front, turn 90 right
else step forward
count distinct positions visited
"""

# row, col
start_pos = [0, 0]
floor = []


def solve_part_one():
    global start_pos, floor

    with open('data\\day_six.txt') as file:
        row_count = 0
        for line in file:
            if '^' in line:
                start_pos[0] = row_count
                for i in range(len(line)):
                    if line[i] == '^':
                        start_pos[1] = i
            line_in = line.strip()
            floor.append(list(line_in))
            row_count += 1

    # print(f'Starting position: {start_pos}')
    # print(f'Floor height: {len(floor)}, floor length: {len(floor[0])}')
    print(len(traverse(floor, start_pos)))


def traverse(floor, pos):
    visited = set()
    visited.add(tuple(pos))  # couldn't use lists because they aren't hashable
    dir = 1

    # step one, get next position
    while True:
        next_pos = pos[:]
        match dir:
            case 1:  # North
                next_pos[0] -= 1
            case 2:  # East
                next_pos[1] += 1
            case 3:  # South
                next_pos[0] += 1
            case 4:  # West
                next_pos[1] -= 1

        # is next position out of bounds
        if not (0 <= next_pos[0] < len(floor) and 0 <= next_pos[1] < len(floor[0])):
            break  # loop break condition

        # is next position blocked
        if floor[next_pos[0]][next_pos[1]] == '#':
            dir = (dir % 4) + 1
        else:  # clear to move
            pos = next_pos
            visited.add(tuple(pos))

    return visited


def solve_part_two():
    global start_pos, floor
    total = 0

    path = traverse(floor, start_pos)

    for row, col in path:
        if (row, col) == tuple(start_pos):  # skip starting point
            continue
        floor[row][col] = '#'
        if find_loops(floor, start_pos):
            total += 1
        floor[row][col] = '.'

    print(total)


def find_loops(floor, pos):
    visited = set()
    dir = 1
    visited.add((tuple(pos), dir))  # using vector to find a true loop

    # step one, get next position
    while True:
        next_pos = pos[:]
        match dir:
            case 1:  # North
                next_pos[0] -= 1
            case 2:  # East
                next_pos[1] += 1
            case 3:  # South
                next_pos[0] += 1
            case 4:  # West
                next_pos[1] -= 1

        # is this a loop?
        if (tuple(next_pos), dir) in visited:
            return 1  # loop found

        # is next position out of bounds
        if not (0 <= next_pos[0] < len(floor) and 0 <= next_pos[1] < len(floor[0])):
            return 0  # loop break condition

        # is next position blocked
        if floor[next_pos[0]][next_pos[1]] == '#':
            dir = (dir % 4) + 1
        else:  # clear to move
            pos = next_pos
            visited.add((tuple(pos), dir))
