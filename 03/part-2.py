def extract_and_multiply(data):
    data = "\n".join(data)
    execute = True
    total_sum = 0
    while data:
        if data.startswith("do()"):
            data = data[3:]
            execute = True
            continue
        elif data.startswith("don't()"):
            data = data[6:]
            execute = False
            continue
        elif data.startswith("mul("):
            if ")" in data:
                args = data[4:].split(")", 1)[0]
                if args.count(",") == 1:
                    x, y = args.split(",")
                    if x.isdigit() and y.isdigit():
                        if execute:
                            total_sum += int(x) * int(y)
                            data = data[4:].split(")", 1)[1]
                            continue
        data = data[1:]

    return total_sum

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.readlines()
    result = extract_and_multiply(data)
    print(result)