def solve_part_one():
    # 3 tokens to push A
    # 1 token to push B
    # x = right
    # y = forward
    # find least amount of tokens to win prize
    # it is possible to NOT win a prize

    inputs = get_inputs()
    claw_machines = get_machines(inputs)

    total = 0
    for prize, button in claw_machines.items():
        ax, ay = button[0]
        bx, by = button[1]
        x_prize, y_prize = prize
        min_cost = None

        for a_presses in range(101):
            rem_x = x_prize - (a_presses * ax)
            rem_y = y_prize - (a_presses * ay)

            if bx == 0 or by == 0:
                continue

            if rem_x % bx == 0 and rem_y % by == 0:
                b_x = rem_x // bx
                b_y = rem_y // by

                if b_x == b_y and 0 <= b_x <= 100:
                    print(f'a_presses: {a_presses}, b_presses: {b_x}')
                    cost = (3 * a_presses) + b_x
                    if min_cost is None or cost < min_cost:
                        min_cost = cost
        if min_cost is not None:
            total += min_cost
    print(total)


def get_machines(inputs, val=0):
    claw_machines = {}
    for i in range(0, len(inputs), 3):
        button_a = inputs[i].replace(',', '').split()
        button_b = inputs[i + 1].replace(',', '').split()
        prize = inputs[i + 2].replace(',', '').split()
        claw_machines[(int(prize[1][2:]) + val, int(prize[2][2:]) + val)] = [
            (int(button_a[2][2:]), int(button_a[3][2:])), (int(button_b[2][2:]), int(button_b[3][2:]))]

    return claw_machines


def get_inputs():
    inputs = []
    with open('data\\day_thirteen.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                inputs.append(line)
    return inputs


def solve_part_two():
    inputs = get_inputs()
    claw_machines = get_machines(inputs, val=10000000000000)

    total = 0
    for prize, button in claw_machines.items():
        ax, ay = button[0]
        bx, by = button[1]
        x_prize, y_prize = prize

        cost = solve_machine(ax, ay, bx, by, x_prize, y_prize)
        if cost is not None:
            total += cost
    print(total)


# extended euclidean algorithm
# diophantine equations
def solve_machine(ax, ay, bx, by, x_prize, y_prize):
    # equation: ax * a + bx * b = x_prize
    g, x, y = extended_gcd(ax, bx)

    if x_prize % g != 0:
        return None

    scale = x_prize // g
    a0 = x * scale
    b0 = y * scale

    coef_t = (bx * ay - ax * by) // g
    rhs = y_prize - (a0 * ay + b0 * by)

    if coef_t == 0:
        if rhs != 0:
            return None
        t = 0
    elif rhs % coef_t != 0:
        return None
    else:
        t = rhs // coef_t

    a = a0 + (bx // g) * t
    b = b0 - (ax // g) * t

    if a < 0 or b < 0:
        return None

    return 3 * a + 1 * b


def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)
