
left_list, right_list = [], []


def solve_part_one():

    answer = 0

    with open('data\\day_one.txt') as file:

        for line in file:
            item = line.split()
            left_list.append(int(item[0]))
            right_list.append(int(item[1]))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        answer += abs(right_list[i] - left_list[i])

    print(answer)
    print()


def solve_part_two():

    map = {num: 0 for num in left_list}
    answer = 0

    for num in right_list:
        if num in map:
            map[num] += 1

    for key, val in map.items():
        if val != 0:
            answer += key * val

    print(answer)
