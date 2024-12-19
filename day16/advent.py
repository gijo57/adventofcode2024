from itertools import count
import numpy as np
import heapq

with open('input.txt') as f:
    storage = np.array([[x for x in list(row.strip())] for row in f.readlines()])
    start = [int(y) for x in np.where(storage == 'S') for y in x]
    end = [y for x in np.where(storage == 'E') for y in x]
    turn_left = np.array([[0, 1], [-1, 0]])
    turn_right = np.array([[0, -1], [1, 0]])
    direction = [1, 0]
    limit = len(storage)-1


def get_neighbors(current):
    return [[sum(x) for x in zip(current, direction)], [sum(x) for x in zip(current, np.dot(direction, turn_left))], [sum(x) for x in zip(current, np.dot(direction, turn_right))], [sum(x) for x in zip(current, np.dot(np.dot(direction, turn_right), turn_right))]]


tiebreaker = count()
shortest_path = 0
nodes = []
visited = []
nodes.append([0, next(tiebreaker), [start, start]])
while nodes:
    node = heapq.heappop(nodes)
    prev = node[2][1]
    pos = node[2][0]

    visited.append(pos)
    current_direction = [pos[0]-prev[0], pos[1]-prev[1]]
    if (current_direction[0] == 0 and current_direction[1] == 0):
        current_direction = direction

    if (pos == end):
        shortest_path = node[0]
        break
    neighbors = get_neighbors(pos)
    for neighbor in neighbors:
        neighbor_node = [int(neighbor[0]), int(neighbor[1])]
        if (neighbor_node[0] < 0 or neighbor_node[0] > limit or neighbor_node[1] < 0 or neighbor_node[1] > limit):
            continue
        if (neighbor_node in visited or storage[neighbor_node[0]][neighbor_node[1]] == '#'):
            continue
        dist = node[0]
        if (neighbor_node == [sum(x) for x in zip(pos, current_direction)]):
            dist += 1
        else:
            dist += 1001
        heapq.heappush(nodes, [dist, next(tiebreaker), [neighbor_node, pos]])

answer1 = shortest_path
print(answer1)