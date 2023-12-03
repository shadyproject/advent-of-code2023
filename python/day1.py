from aocd import get_data


def problem_one():
    input = get_data(day=1, year=2023)

    total = 0
    for line in input.split():
        numbers = [n for n in line.strip() if n.isdigit()]
        total += int(numbers[0] + numbers[-1])
    return total


def problem_two():
    input = get_data(day=1, year=2023)
    number_words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    total = 0
    for line in input.split():
        numbers = []
        for i in range(len(line)):
            n = line[i]
            if n.isdigit():
                numbers.append(n)
                continue
            for j in range(len(number_words)):
                num_word = number_words[j]
                end_range = i + len(num_word)
                curr_word = line[i:end_range]
                if curr_word == num_word:
                    numbers.append(str(j))
                    break
        line_sum = int(numbers[0] + numbers[-1])
        total += line_sum
    return total


if __name__ == "__main__":
    print(f"Answer for problem 1: {problem_one()}")
    print(f"Answer for problem 2: {problem_two()}")
