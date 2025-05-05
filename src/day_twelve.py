def solve_part_one():
    garden_map = get_map()
    regions = get_regions(garden_map)
    total = 0

    # get perimeters
    for region in regions:
        area = len(region)
        perimeter = 0
        for r, c in region:
            plot = garden_map[r][c]

            # up
            if r == 0 or garden_map[r - 1][c] != plot:
                perimeter += 1

            # down
            if r == len(garden_map) - 1 or garden_map[r + 1][c] != plot:
                perimeter += 1

            # left
            if c == 0 or garden_map[r][c - 1] != plot:
                perimeter += 1

            # right
            if c == len(garden_map[0]) - 1 or garden_map[r][c + 1] != plot:
                perimeter += 1
        total += area * perimeter
    print(total)


def get_regions(garden_map):
    regions = []
    visited = set()
    row = len(garden_map[0])
    col = len(garden_map)

    for row in range(row):
        for col in range(col):
            point = (row, col)
            plot = garden_map[point[0]][point[1]]

            if point in visited:
                continue

            region = set()
            queue = [point]

            while queue:
                pos = queue.pop(0)
                if pos in visited:
                    continue
                visited.add(pos)
                region.add(pos)

                # up
                if pos[0] > 0 and garden_map[pos[0] - 1][pos[1]] == plot:
                    queue.append((pos[0] - 1, pos[1]))

                # down
                if pos[0] < len(garden_map) - 1 and garden_map[pos[0] + 1][pos[1]] == plot:
                    queue.append((pos[0] + 1, pos[1]))

                # left
                if pos[1] > 0 and garden_map[pos[0]][pos[1] - 1] == plot:
                    queue.append((pos[0], pos[1] - 1))

                # right
                if pos[1] < len(garden_map[0]) - 1 and garden_map[pos[0]][pos[1] + 1] == plot:
                    queue.append((pos[0], pos[1] + 1))
            regions.append(region)
    return regions


def get_map():
    garden_map = []
    with open('data\\day_twelve.txt') as file:
        for line in file:
            row = line.strip()
            garden_map.append(list(row))
    return garden_map


def solve_part_two():
    garden_map = get_map()
    regions = get_regions(garden_map)
    total = sum(get_sides(region) for region in regions)
    print(total)


def get_sides(region):
    region = set(region)
    corner_candidates = {}

    for row, col in region:
        for c_row, c_col in [(row - 0.5, col - 0.5), (row + 0.5, col - 0.5), (row + 0.5, col + 0.5), (row - 0.5, col + 0.5)]:
            corner_candidates.add((c_row, c_col))
    corners = 0
    for c_row, c_col in corner_candidates:
        config = [(sr, sc) in region for sr, sc in [(c_row - 0.5, c_col - 0.5), (c_row +
                                                                                 0.5, c_col - 0.5), (c_row + 0.5, c_col + 0.5), (c_row - 0.5, c_col + 0.5)]]
        number = sum(config)
        if number == 1 or number == 3:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
    return corners
