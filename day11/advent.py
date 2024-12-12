with open('example.txt') as f:
    stones = [int(stone) for stone in f.read().split(' ')]
    print(stones)


def count_stones(stones):
    stone_count = 0
    for stone in stones:
        if (stone == 0):
            stone_count += 1
        if (stone == 1):
            stone = 2024