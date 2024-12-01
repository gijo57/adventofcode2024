from bisect import insort

with open('input.txt') as f:
    rows = f.read().split('\n')
    list1, list2, = [], []

for row in rows:
    num1, num2 = row.split('   ')
    insort(list1, int(num1))
    insort(list2, int(num2))

total_distance = 0
similarity_score = 0

for i in range(len(list1)):
    item1, item2 = list1[i], list2[i]
    diff = abs(item1 - item2)
    total_distance += diff
    row_score = item1 * list2.count(item1)
    similarity_score += row_score

answer1 = total_distance
answer2 = similarity_score
print(answer1, answer2)
