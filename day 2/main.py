def get_data_from_file():
    data = []

    with open("input.txt", "r") as file:
        lines = file.readlines()

        for report in lines:
            report_array = list(map(int, report.split(" ")))
            data.append(report_array)

    return data


def get_array_safety_state(array: list[int]) -> bool:
    differences = [array[i + 1] - array[i] for i in range(len(array) - 1)]

    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    return all_increasing or all_decreasing


def part_one():
    result = get_data_from_file()

    safe_count = sum(1 for value in result if get_array_safety_state(value))

    print(f"Number of safe reports: {safe_count}")


def is_safe_with_dampener(report):
    if get_array_safety_state(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if get_array_safety_state(modified_report):
            return True
    return False


def part_two():
    result = get_data_from_file()
    safe_count = sum(1 for report in result if is_safe_with_dampener(report))
    print(f"Number of safe reports: {safe_count}")


if __name__ == '__main__':
    part_one()
    part_two()