if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        nums = [int(n) for line in f for n in line.split()]
    list1, list2 = sorted(nums[::2]), sorted(nums[1::2])
    print("Total distance:", sum(abs(a - b) for a, b in zip(list1, list2)))