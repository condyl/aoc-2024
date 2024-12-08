import itertools

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    equations = []
    for line in lines:
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((test_value, numbers))
    return equations

def evaluate_expression(expression):
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = int(tokens[i + 1])
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        i += 2
    return result

def evaluate_equation(test_value, numbers):
    operators = ['+', '*']
    for ops in itertools.product(operators, repeat=len(numbers)-1):
        expression = str(numbers[0])
        for num, op in zip(numbers[1:], ops):
            expression += f' {op} {num}'
        if evaluate_expression(expression) == test_value:
            return True
    return False

def evaluate_expression_with_concat(expression):
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = int(tokens[i + 1])
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result) + str(num))
        i += 2
    return result

def evaluate_equation_with_concat(test_value, numbers):
    operators = ['+', '*', '||']
    for ops in itertools.product(operators, repeat=len(numbers)-1):
        expression = str(numbers[0])
        for num, op in zip(numbers[1:], ops):
            expression += f' {op} {num}'
        if evaluate_expression_with_concat(expression) == test_value:
            return True
    return False

def part1():
    equations = parse_input('./input.txt')
    total_calibration_result = 0
    for test_value, numbers in equations:
        if evaluate_equation(test_value, numbers):
            total_calibration_result += test_value
    return total_calibration_result

def part2():
    equations = parse_input('./input.txt')
    total_calibration_result = 0
    for test_value, numbers in equations:
        if evaluate_equation_with_concat(test_value, numbers):
            total_calibration_result += test_value
    return total_calibration_result

if __name__ == "__main__":
    print(part1())
    print(part2())
