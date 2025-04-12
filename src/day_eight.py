import itertools


def solve_part_one():

    graph = make_graph()

    nodes = get_nodes(graph)

    antinodes = get_antinodes(graph, nodes)
    print(antinodes)


def get_nodes(graph):
    nodes = {}
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            point = graph[i][j]
            if point != '.':
                if point not in nodes.keys():
                    nodes[point] = [(j, i)]
                else:
                    nodes[point].append((j, i))
    return nodes


def make_graph():
    graph = []
    with open('data\\day_eight.txt') as file:
        for line in file:
            graph.append(list(line.strip()))
    return graph


def get_antinodes(graph, nodes):
    antinodes = set()
    for k in nodes.keys():
        key_product = itertools.product(nodes[k], repeat=2)
        for v in key_product:
            line = list(v)
            point_1 = line[0]
            point_2 = line[1]
            if point_1 != point_2:
                offset_1 = (point_1[0] - point_2[0], point_1[1] - point_2[1])
                offset_2 = (point_2[0] - point_1[0], point_2[1] - point_1[1])
                # print(f'offset_1: {offset_1}, offset_1: {offset_2}')
                antinode_1 = (point_1[0] + offset_1[0],
                              point_1[1] + offset_1[1])
                antinode_2 = (point_2[0] + offset_2[0],
                              point_2[1] + offset_2[1])
                # print(f'antinode_1: {antinode_1}, antinode_2: {antinode_2}')
                if 0 <= antinode_1[0] < len(graph[0]) and 0 <= antinode_1[1] < len(graph):
                    # print(f'antinode_1: {antinode_1}')
                    antinodes.add(antinode_1)
                if 0 <= antinode_2[0] < len(graph[0]) and 0 <= antinode_2[1] < len(graph):
                    # print(f'antinode_2: {antinode_2}')
                    antinodes.add(antinode_2)
    return len(antinodes)


def get_antinodes_two(graph, nodes):
    antinodes = set()
    for k in nodes.keys():
        if len(nodes[k]) > 1:
            for n in nodes[k]:
                antinodes.add(n)

        key_product = itertools.product(nodes[k], repeat=2)
        for v in key_product:
            line = list(v)
            point_1 = line[0]
            point_2 = line[1]
            if point_1 != point_2:
                offset_1 = (point_1[0] - point_2[0], point_1[1] - point_2[1])
                offset_2 = (point_2[0] - point_1[0], point_2[1] - point_1[1])
                # print(f'offset_1: {offset_1}, offset_1: {offset_2}')

                antinode_1 = (point_1[0] + offset_1[0], point_1[1] + offset_1[1])
                while 0 <= antinode_1[0] < len(graph[0]) and 0 <= antinode_1[1] < len(graph):
                    antinodes.add(antinode_1)
                    antinode_1 = (antinode_1[0] + offset_1[0], antinode_1[1] + offset_1[1])
                    
                antinode_2 = (point_2[0] + offset_2[0], point_2[1] + offset_2[1])
                while 0 <= antinode_2[0] < len(graph[0]) and 0 <= antinode_2[1] < len(graph):
                    antinodes.add(antinode_2)
                    antinode_2 = (antinode_2[0] + offset_2[0], antinode_2[1] + offset_2[1])

                # print(f'antinode_1: {antinode_1}, antinode_2: {antinode_2}')

    return len(antinodes)


def solve_part_two():

    graph = make_graph()

    nodes = get_nodes(graph)
    antinodes = get_antinodes_two(graph, nodes)
    print(antinodes)
