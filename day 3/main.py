import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"


def get_data_from_file():
    with open("input.txt", "r") as file:
        content = file.read()

    return content


def multiply_data(first: int, second: int, enabled: bool):
    return first * second if enabled else 0


def process_instructions(content: str):
    enabled = True
    total_sum = 0

    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", content)

    for instruction in instructions:
        instruction = instruction.strip()
        if re.match(do_pattern, instruction):
            enabled = True
        elif re.match(dont_pattern, instruction):
            enabled = False
        elif re.match(mul_pattern, instruction):
            match = re.search(mul_pattern, instruction)
            if match:
                first = int(match.group(1))
                second = int(match.group(2))
                total_sum += multiply_data(first, second, enabled)

    return total_sum


def main():
    content = get_data_from_file()
    result = process_instructions(content)
    print(result)


if __name__ == '__main__':
    main()
