def read_and_split_file(filename):
    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            for i, number in enumerate(numbers):
                if i % 2 == 0:
                    list1.append(int(number))
                else:
                    list2.append(int(number))
    
    return list1, list2

if __name__ == "__main__":
    list1, list2 = read_and_split_file('./input.txt')
    list1.sort()
    list2.sort()

    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    print("Total distance:", total_distance)