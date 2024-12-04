import re


maze_list, maze_str = [], []
fwd_pattern = r'XMAS'
back_pattern = r'SAMX'
total = 0


def solve_part_one():
    global maze_list, maze_str, total

    with open('data\\day_four.txt') as file:
        for line in file:
            line_in = line.strip()
            maze_str.append(line_in)
            maze_list.append(list(line_in))

    total += search_horizontal(maze_str)
    total += search_vertical(maze_list)
    total += search_lr_diagonal(maze_list)
    total += search_rl_diagonal(maze_list)
    print(total)


def search_horizontal(maze):
    global fwd_pattern, back_pattern
    amt = 0

    for line in maze:
        amt += len(re.findall(fwd_pattern, line))
        amt += len(re.findall(back_pattern, line))

    return amt


def search_vertical(maze):
    global fwd_pattern, back_pattern
    amt = 0

    for i in range(len(maze[0])):
        col = ''.join(row[i] for row in maze)
        amt += len(re.findall(fwd_pattern, col))
        amt += len(re.findall(back_pattern, col))

    return amt


def search_lr_diagonal(maze):
    amt = 0
    for i in range(len(maze) - 3):
        for j in range(len(maze[0]) - 3):
            if maze[i][j] == 'X' and maze[i+1][j+1] == 'M' and maze[i+2][j+2] == 'A' and maze[i+3][j+3] == 'S':
                # print(f"LR Diagonal Match: XMAS at ({i}, {j})")
                amt += 1
            if maze[i][j] == 'S' and maze[i+1][j+1] == 'A' and maze[i+2][j+2] == 'M' and maze[i+3][j+3] == 'X':
                # print(f"LR Diagonal Match: SAMX at ({i}, {j})")
                amt += 1
    return amt


def search_rl_diagonal(maze):
    amt = 0
    for i in range(len(maze) - 3):
        for j in range(3, len(maze[0])):
            if maze[i][j] == 'X' and maze[i+1][j-1] == 'M' and maze[i+2][j-2] == 'A' and maze[i+3][j-3] == 'S':
                # print(f"RL Diagonal Match: XMAS at ({i}, {j})")
                amt += 1
            if maze[i][j] == 'S' and maze[i+1][j-1] == 'A' and maze[i+2][j-2] == 'M' and maze[i+3][j-3] == 'X':
                # print(f"RL Diagonal Match: SAMX at ({i}, {j})")
                amt += 1
    return amt


def solve_part_two():
    global maze_list
    total = 0

    for i in range(1, len(maze_list) - 1):
        for j in range(1, len(maze_list[0]) - 1):
            if maze_list[i][j] == 'A':
                lr_word = maze_list[i - 1][j - 1] + maze_list[i][j] + maze_list[i + 1][j + 1]
                rl_word = maze_list[i - 1][j + 1] + maze_list[i][j] + maze_list[i + 1][j - 1]
                if (lr_word == 'SAM' or lr_word == 'MAS') and (rl_word == 'SAM' or rl_word == 'MAS'):
                    total += 1

    print(total)
