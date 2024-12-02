def is_safe_report(report):
    levels = list(map(int, report.split()))
    increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    levels = list(map(int, report.split()))
    if is_safe_report(report):
        return True
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if is_safe_report(' '.join(map(str, modified_report))):
            return True
    return False

def count_safe_reports():
    with open("./input.txt", 'r') as file:
        reports = file.readlines()
    safe_reports = [report for report in reports if is_safe_with_dampener(report)]
    return len(safe_reports)

if __name__ == "__main__":
    print(f"Number of safe reports: {count_safe_reports()}")
