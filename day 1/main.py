def get_data_from_file():
    first_list = []
    second_list = []

    with open("input.txt", "r") as file:
        line = file.readlines()

        for i in line:
            alpha, beta = i.split("   ")
            first_list.append(int(alpha))
            second_list.append(int(beta))

    first_list.sort()
    second_list.sort()

    return first_list, second_list


def part_one():
    first_list, second_list = get_data_from_file()

    count = len(first_list)

    difference_list = [abs(first_list[i] - second_list[i]) for i in range(count)]

    difference_sum = sum(difference_list)

    print(difference_sum)


def part_two():
    first_list, second_list = get_data_from_file()

    similarity_dict = [second_list.count(i) * i for i in first_list]

    similarity_score = sum(similarity_dict)

    print(similarity_score)


if __name__ == '__main__':
    part_one()  # Answer: 1258579
    part_two()  # Answer: 23981443
