from itertools import product

def concat_numbers(equation, equation_result):
    concatenated_number = equation_result
    if ('||' in equation):
        concat_index = equation.index('||')
        concatenated_number = str(equation[concat_index-1]) + str(equation[concat_index+1])
        equation[concat_index-1:concat_index+2] = [concatenated_number]
    return equation, int(concatenated_number)


with open('example.txt') as f:
    rows = f.read().split('\n')

    valid_results = []
    valid_results_2 = []
    for row in rows:
        parts = row.split(':')
        result = int(parts[0])
        numbers = [num for num in parts[1].strip().split(' ')]
        perms = list(product(['*','+', '||'], repeat=len(numbers)-1))

        for p in perms:
            equation = [item for sublist in zip(numbers[:-1], p) for item in sublist] + [numbers[-1]]
            equation_result = int(equation[0])
            current_operator = equation[1]

            for i, item in enumerate(equation[2:]):
                if (equation_result > result):
                    break
                if (item == '+' or item == '*' or item == '||'):
                    current_operator = item
                else:
                    if (current_operator == '+'):
                        equation_result += int(item)
                    if (current_operator == '*'):
                        equation_result *= int(item)
                    if (current_operator == '||'):
                        equation, equation_result = concat_numbers(equation, equation_result)
                    equation = [equation_result, *equation[i+3:]]
            if (result == equation_result):
                if ('||' not in p):
                    valid_results.append(result)
                valid_results_2.append(result)
    
    answer1, answer2 = sum(set(valid_results)), sum(set(valid_results_2))
    print(answer1, answer2)