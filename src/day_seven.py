import itertools


def solve_part_one():
    calibration = []
    answers = set()

    with open('data\\day_seven.txt') as file:

        # extracting input data
        for line in file:

            new_line = line.strip().split(':')

            key = int(new_line[0])
            value = [int(x) for x in new_line[1].split()]

            calibration.append((key, value))

    # solving problem
    operators = ['*', '+']
    for k, v in calibration:
        # print(f'key: {k} ----- value: {v}')
        combinations = itertools.product(operators, repeat=len(v) - 1)

        for combo in combinations:
            if custom_eval(v, combo) == k:
                answers.add(k)

    print(f'answer: {sum(answers)}')


def solve_part_two():
    calibration = []
    answers = []

    with open('data\\day_seven.txt') as file:

        # extracting input data
        for line in file:

            new_line = line.strip().split(':')

            key = int(new_line[0])
            value = [int(x) for x in new_line[1].split()]

            calibration.append((key, value))

    # solving problem
    operators = ['*', '+', '||']
    for k, v in calibration:
        # print(f'key: {k} ----- value: {v}')
        combinations = itertools.product(operators, repeat=len(v) - 1)

        for combo in combinations:
            if custom_eval(v, combo) == k:
                answers.append(k)
                break

    print(f'answer: {sum(answers)}')


# evaluate expression left to right
# ignores operator precedence
def custom_eval(numbers, ops):
    result = numbers[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += numbers[i + 1]
        elif ops[i] == '*':
            result *= numbers[i + 1]
        elif ops[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result
