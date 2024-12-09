def read_input(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == "": continue
            grid.append(line.strip())
    return grid

def part1():
    antinodes = set()
    grid = read_input('./input.txt')

    N = len(grid)
    M = len(grid[0])

    nodes = {}

    for i in range(N):
        for j in range(M):
            if grid[i][j] != ".":
                if grid[i][j] in nodes:
                    nodes[grid[i][j]].append((i,j))
                else:
                    nodes[grid[i][j]] = [(i,j)]

    def antinode(pr1, pr2):
        x1, y1 = pr1
        x2, y2 = pr2
        newx = x2 + (x2 - x1)
        newy = y2 + (y2 - y1)
        if newx >= 0 and newx < N and newy >= 0 and newy < M:
            antinodes.add((newx,newy))
                    
    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]
                antinode(node1, node2)
                antinode(node2, node1)

    return len(antinodes)

def part2():
    antinodes = set()
    grid = read_input('./input.txt')

    N = len(grid)
    M = len(grid[0])

    nodes = {}

    for i in range(N):
        for j in range(M):
            if grid[i][j] != ".":
                if grid[i][j] in nodes:
                    nodes[grid[i][j]].append((i,j))
                else:
                    nodes[grid[i][j]] = [(i,j)]

    def antinode(pr1, pr2):
        x1, y1 = pr1
        x2, y2 = pr2
        antinodes.add((x2,y2))
        newx = x2 + (x2 - x1)
        newy = y2 + (y2 - y1)
        while newx >= 0 and newx < N and newy >= 0 and newy < M:
            antinodes.add((newx,newy))
            newx += (x2 - x1)
            newy += (y2 - y1)
                    
    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]
                antinode(node1, node2)
                antinode(node2, node1)

    return len(antinodes)

if __name__ == "__main__":
    print(part1())
    print(part2())