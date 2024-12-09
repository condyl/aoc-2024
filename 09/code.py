import sys
from collections import defaultdict

def read_input(file_path):
    with open(file_path) as file:
        return [int(x) for x in file.read().strip()]

def process_memory(line):
    memory = []
    memory_dict = dict()
    free_space = defaultdict(list)
    position = 0

    for index, value in enumerate(line):
        for _ in range(value):
            if index % 2 == 0:
                memory.append(index // 2)
            else:
                memory.append('.')
        if index % 2 == 0:
            memory_dict[position] = (index // 2, value)
        else:
            if value > 0:
                free_space[value].append(position)
        position = value + position

    return memory, memory_dict, free_space

def part1(memory):
    index = 0
    while index < len(memory):
        if memory[index] == '.':
            memory[index] = memory[-1]
            memory = memory[:-1]
            while memory and memory[-1] == '.':
                memory = memory[:-1]
        index += 1

    return sum(i * value for i, value in enumerate(memory))

def part2(memory_dict, free_space):
    positions = list(memory_dict.keys())[::-1]
    for position in positions:
        identifier, length = memory_dict[position]
        free_spaces = sorted(free_space.keys(), reverse=True)
        new_positions = {min(free_space[space]): space for space in free_spaces if length <= space and free_space[space]}
        if new_positions:
            new_position = min(new_positions)
            if new_position < position:
                space = new_positions[new_position]
                free_space[space].remove(new_position)
                memory_dict.pop(position)
                memory_dict[new_position] = (identifier, length)
                if space - length > 0:
                    free_space[space - length].append(new_position + length)

    return sum(identifier * (position + i) for position, (identifier, value) in memory_dict.items() for i in range(value))

if __name__ == "__main__":
    line = read_input('./input.txt')
    memory, memory_dict, free_space = process_memory(line)

    print('part1', part1(memory))
    print('part2', part2(memory_dict, free_space))
