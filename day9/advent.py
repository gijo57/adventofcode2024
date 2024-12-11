from copy import copy
import numpy as np

with open('input.txt') as f:
    memory = f.read()


def expand_memory(memory):
    expanded_memory = []
    id = 0
    for i in range(len(memory)):
        if (i % 2):
            expanded_memory.extend('.' * int(memory[i]))
        else:
            expanded_memory.extend([id] * int(memory[i]))
            id += 1
    return expanded_memory, id-1


def get_checksum(memory):
    checksum = 0
    index = 0

    while True:
        if (not memory):
            break
        first = memory[0]
        
        if (first != '.'):
            memory.pop(0)
            checksum += index * first
            index += 1
        else:
            last = memory.pop()
            if (last != '.'):
                memory[0] = last
        
    return checksum


def find_empty_space(memory, empty_indices, file_length, first_file_index):
    for i in empty_indices:
        if (i > first_file_index):
            return False, 0, 0
        potential_empty_space = memory[i:i+file_length]
        if (potential_empty_space.count('.') == len(potential_empty_space) and len(potential_empty_space) == file_length):
            return potential_empty_space.count('.') == len(potential_empty_space), i, i+file_length
    return False, 0, 0

            
def get_checksum_2(memory, last_id):
    checksum = 0
    current_file_id = last_id
    current_file = []
    current_file_indices = []
    count = 0
    end_index = -1

    while current_file_id > 0:
        last = memory[end_index]
        if (last == '.' or current_file_id < last):
            end_index -= 1
            continue
        empty_indices = np.where(np.array(memory) == '.')[0]
        if (last == current_file_id):
            current_file_indices.append(end_index + len(memory))
            current_file.append(last)
            end_index -= 1
        else:
            has_space, start, end = find_empty_space(memory, empty_indices, len(current_file), current_file_indices[-1])
            if (has_space):
                memory[start:end] = current_file
                for i in current_file_indices:
                    memory[i] = '.'
            current_file_indices = []
            current_file_id -= 1
            current_file = []
        count += 1
    for i, space in enumerate(memory):
        if (space != '.'):
            checksum += i * int(space)
    return checksum


expanded_memory, last_id = expand_memory(memory)
expanded_memory_2 = copy(expanded_memory)
answer1 = get_checksum(expanded_memory)
answer2 = get_checksum_2(expanded_memory_2, last_id)
print(answer1, answer2)