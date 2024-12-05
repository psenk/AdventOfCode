rules: dict = {}
updates: list = []
incorrect_updates = []


def solve_part_one():
    global rules, updates
    get_inputs()
    total = 0

    for update in updates:
        if are_rules_followed(update):
            total += update[(len(update) - 1) // 2]

    print(total)


def are_rules_followed(update):
    # print(f'Update: {update}')
    global rules, incorrect_updates

    for y, x_list in rules.items():
        for x in x_list:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    incorrect_updates.append(update)
                    return False
    return True


def get_inputs():
    global rules, updates

    trigger = False
    with open('data\\day_five.txt') as file:
        for line in file:
            if line == '\n':
                trigger = True
                continue
            if not trigger:
                rule = line.strip().split('|')
                # key: this page has to be after value: all these pages
                if int(rule[1]) not in rules:
                    rules[int(rule[1])] = [int(rule[0])]
                else:
                    rules[int(rule[1])].append(int(rule[0]))
            else:
                line_in = line.strip().split(',')
                line_in = [int(num) for num in line_in]
                updates.append(line_in)


def solve_part_two():
    global incorrect_updates
    total = 0

    for i in range(len(incorrect_updates)):
        incorrect_updates[i] = sort_update(incorrect_updates[i])

    for update in incorrect_updates:
        total += update[(len(update) - 1) // 2]
    print(total)


def sort_update(update):
    global rules
    weights = {page: 0 for page in update}
    for y, x_list in rules.items():
        for x in x_list:
            if x in update and y in update:
                weights[y] += 1

    return sorted(update, key=lambda x: weights[x])
