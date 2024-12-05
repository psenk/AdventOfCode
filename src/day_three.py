import re

mult_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"
content = ""


def solve_part_one():
    global content

    total = 0
    pattern_result = None

    with open('data\\day_three.txt') as file:
        for line in file:
            content += line.strip()

    pattern_result = re.finditer(mult_pattern, content)

    for i in pattern_result:
        val = re.findall(r'\d+', str(i))
        total += int(val[2]) * int(val[3])

    print(total)
    print()


def solve_part_two():
    global content
    multiply = True
    total = 0

    combined_pattern = f'{do_pattern}|{dont_pattern}|{mult_pattern}'
    matches = re.finditer(combined_pattern, content)

    for match in matches:
        if match.group(0) == 'do()':
            multiply = True
        elif match.group(0) == "don't()":
            multiply = False
        elif match.groups() and multiply:
            x, y = map(int, match.groups())
            total += x * y

    print(total)
