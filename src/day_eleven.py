def get_input():
    with open('data\\day_eleven.txt') as file:
        return list(map(int, file.readline().split()))


def solve_part_one():
    stones = get_input()

    print(loop_stones(stones, 25))
    """
    rules:
    1. stone = 0: replace with 1
    2. stone has even # digits: replace w/ 2 stones, cut digits in half, no leading 0s
    3. else: multiply num by 2024
    """


def loop_stones(stones, amt):
    memo = {}

    def count_stones(stone, depth):
        key = (stone, depth)
        if key in memo:
            return memo[key]
    
        if depth == 0:
            memo[key] = 1
            return 1

        if stone == 0:
            result = count_stones(1, depth - 1)
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                result = count_stones(left, depth - 1) + count_stones(right, depth - 1)
            else:
                result = count_stones(stone * 2024, depth - 1)

        memo[key] = result
        return result

    return sum(count_stones(stone, amt) for stone in stones)


def solve_part_two():
    stones = get_input()

    print(loop_stones(stones, 75))
