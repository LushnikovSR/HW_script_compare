def sort_list_imperative(numbers):
    for mini in range(len(numbers) - 1):
        for i in range(mini+1, len(numbers)):
            if numbers[i] < numbers[mini]:
                temp = numbers[i]
                numbers[i] = numbers[mini]
                numbers[mini] = temp
    return numbers


def sort_list_declarative(numbers):
    return sorted(numbers)


if __name__ == '__main__':
    test_list = [15, 12, 9, 5, 2, 3, 20, 27, 32, 4]
    print("imperative: ", end=' ')
    print(sort_list_imperative(test_list))
    print("declarative:", end=' ')
    print(sort_list_declarative(test_list))
