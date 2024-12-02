if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        l = [int(x) for line in f for x in line.split()]
    print("Total similarity:", sum(x * l[1::2].count(x) for x in sorted(l[::2])))