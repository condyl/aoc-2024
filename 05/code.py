def part1():
    with open('./input.txt') as f:
        lines = f.read().strip().split('\n')
    
    rules = {}
    i = 0
    while '|' in lines[i]:
        x, y = map(int, lines[i].split('|'))
        if x not in rules:
            rules[x] = []
        rules[x].append(y)
        i += 1
    
    updates = []
    for line in lines[i:]:
        if line:
            updates.append(list(map(int, line.split(','))))
    
    def is_correct_order(update):
        for x in rules:
            if x in update:
                for y in rules[x]:
                    if y in update and update.index(x) > update.index(y):
                        return False
        return True
    
    correct_updates = [update for update in updates if is_correct_order(update)]
    
    middle_sum = 0
    for update in correct_updates:
        middle_index = len(update) // 2
        middle_sum += update[middle_index]
    
    return middle_sum

def part2():
    with open('./input.txt') as f:
        lines = f.read().strip().split('\n')
    
    rules = {}
    i = 0
    while '|' in lines[i]:
        x, y = map(int, lines[i].split('|'))
        if x not in rules:
            rules[x] = []
        rules[x].append(y)
        i += 1
    
    updates = []
    for line in lines[i:]:
        if line:
            updates.append(list(map(int, line.split(','))))
    
    def is_correct_order(update):
        for x in rules:
            if x in update:
                for y in rules[x]:
                    if y in update and update.index(x) > update.index(y):
                        return False
        return True
    
    def reorder_update(update):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for x in update:
            in_degree[x] = 0
        for x in rules:
            if x in update:
                for y in rules[x]:
                    if y in update:
                        graph[x].append(y)
                        in_degree[y] += 1
        
        queue = deque([x for x in update if in_degree[x] == 0])
        sorted_update = []
        while queue:
            node = queue.popleft()
            sorted_update.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted_update
    
    incorrect_updates = [update for update in updates if not is_correct_order(update)]
    
    middle_sum = 0
    for update in incorrect_updates:
        sorted_update = reorder_update(update)
        middle_index = len(sorted_update) // 2
        middle_sum += sorted_update[middle_index]
    
    return middle_sum

if __name__ == "__main__":
    print(part1())
    print(part2())
