from collections import defaultdict
from functools import cmp_to_key
from math import floor
from copy import deepcopy

with open('input.txt') as f:
    parts = f.read().split('\n\n')
    rules = [[int(page) for page in rule.split('|')] for rule in parts[0].split('\n')]
    updates = [[int(page) for page in update.split(',')] for update in parts[1].split('\n')]
    rules_dict = defaultdict(list)

for rule in rules:
    before, after = rule
    rules_dict[before].append(after)


def comparator(x, y):
    if y in rules_dict[x]:
        return -1

    if x in rules_dict[y]:
        return 1

    return 0


answer1, answer2 = 0, 0
for update in updates:
    original = deepcopy(update)
    is_correctly_ordered = False
    for i, page in enumerate(update):
        previous_pages = update[:i]
        incorrect_order_pages = list(set(previous_pages).intersection(rules_dict[page]))
        is_correctly_ordered = len(incorrect_order_pages) == 0
        if (not is_correctly_ordered):
            update = sorted(update, key = cmp_to_key(comparator))
            break
    if (update == original):
        answer1 += update[floor(len(update)/2)]
    else:
        answer2 += update[floor(len(update)/2)]
print(answer1, answer2)