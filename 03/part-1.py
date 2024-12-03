import re

def extract_and_multiply(line):
    # Regular expression to find valid mul instructions
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, line)
    
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    
    return total

def main():
    total_sum = 0
    with open('./input.txt', 'r') as file:
        for line in file:
            total_sum += extract_and_multiply(line)
    
    print(f"Total sum of all valid multiplications: {total_sum}")

if __name__ == "__main__":
    main()