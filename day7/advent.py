from itertools import product

with open('example.txt') as f:
    rows = f.read().split('\n')

    valid_results = []
    for row in rows:
        parts = row.split(':')
        result = int(parts[0])
        numbers = [num for num in parts[1].strip().split(' ')]
        perms = list(product(['*','+'], repeat=len(numbers)-1))

        for p in perms:
            equation = [item for sublist in zip(numbers[:-1], p) for item in sublist] + [numbers[-1]]
            equation_result = int(equation[0])
            current_operator = equation[1]

            for item in equation[2:]:
                if (item == '+' or item == '*' or item == '||'):
                    current_operator = item
                else:
                    if (current_operator == '+'):
                        equation_result += int(item)
                    if (current_operator == '*'):
                        equation_result *= int(item)
            if (result == equation_result):
                valid_results.append(result)
    answer1 = sum(set(valid_results))
    print(answer1)