def solve_part_one():
    size, empty = get_lists()

    storage = []

    for i in range(len(size)):
        for j in range(int(size[i])):
            storage.append(str(i))
        if i < len(empty):
            for k in range(int(empty[i])):
                storage.append('.')

    l_ptr = 0
    r_ptr = len(storage) - 1
    while l_ptr < r_ptr:
        if storage[l_ptr] == '.':
            if storage[r_ptr] != '.':
                storage[l_ptr], storage[r_ptr] = storage[r_ptr], storage[l_ptr]
            else:
                r_ptr -= 1
                continue
        else:
            l_ptr += 1
            continue

    checksum = 0
    for i in range(len(storage)):
        if storage[i] != '.':
            checksum += (i * int(storage[i]))
    print(checksum)


def get_lists():
    with open('data\\test.txt') as file:
        for line in file:
            input = line.strip()

    size = input[::2]
    empty = input[1::2]
    return size, empty


def solve_part_two():

    size, empty = get_lists()

    storage = []

    for i in range(len(size)):
        storage.extend([str(i)] * int(size[i]))
        if i < len(empty):
            storage.extend(['.'] * int(empty[i]))

    files = []
    i = 0
    while i < len(storage):
        if storage[i] != '.':
            start = i
            fid = storage[i]
            while i < len(storage) and storage[i] == fid:
                i += 1
            files.append((start, i - start, int(fid)))
        else:
            i += 1

    files.sort(key=lambda x: -x[2])

    for start, length, fid in files:
        free_space = get_free_space(storage)
        for free_start, free_len in free_space:
            if free_start >= start:
                break
            if free_len >= length:
                for i in range(length):
                    storage[free_start + i] = str(fid)
                    storage[start + i] = '.'
                break

    checksum = sum(i * int(ch) for i, ch in enumerate(storage) if ch != '.')
    print(checksum)


def get_free_space(disk):
    free_space = []
    i = 0
    while i < len(disk):
        if disk[i] == '.':
            start = i
            while i < len(disk) and disk[i] == '.':
                i += 1
            free_space.append((start, i - start))
        else:
            i += 1
    return free_space
