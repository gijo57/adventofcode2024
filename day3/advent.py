import re

with open('input.txt') as f:
    memory = f.read()
    regex = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    valid_instructions = re.findall(regex, memory)

answer1, answer2 = 0, 0
enabled = True

for instruction in valid_instructions:
    factors = re.findall(r'\d+', instruction)

    if (factors):
        product = int(factors[0]) * int(factors[1])
        answer1 += product
    
    if (factors):
        if (enabled):
            product = int(factors[0]) * int(factors[1])
            answer2 += product
    else:
        enabled = True if len(instruction) == 4 else False

print(answer1, answer2)