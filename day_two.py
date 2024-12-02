
def solve_part_one():

    count = 0

    with open('data\\day_two.txt') as file:

        for line in file:
            level = [int(num) for num in line.split()]

            if is_sorted(level) and is_adjacent(level):
                count += 1

        print(f'{count}\n')


def is_sorted(list_in):
    return list_in == sorted(list_in) or list_in == sorted(list_in, reverse=True)


def is_adjacent(list_in):

    for i in range(len(list_in) - 1):

        val = abs(list_in[i] - list_in[i + 1])
        if val > 3 or val < 1:
            return False
    return True


def solve_part_two():
    count = 0

    with open('data\\day_two.txt') as file:

        for line in file:
            level = [int(num) for num in line.split()]

            if is_adjacent_dampener(level):
                count += 1

        print(count)


def is_adjacent_dampener(list_in):

    for i in range(len(list_in)):
        modified_list = list_in[:i] + list_in[i + 1:]  # Remove one element
        if is_sorted(modified_list) and is_adjacent(modified_list):
            return True
    return False
