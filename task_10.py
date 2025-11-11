def get_list() -> list:
    """
    Get a list of integers from user input.

    Returns:
        list: A list of integers entered by the user
    """
    while True:
        user_input = input("Enter the numbers for the list separated by spaces: ")
        try:
            numbers_list = list(map(int, user_input.split()))
            return numbers_list
        except ValueError:
            print("Input error.")


def get_range() -> tuple:
    """
    Get a range of two integers from user input.

    Returns:
        tuple: A tuple containing (range_min, range_max)
    """
    while True:
        user_input = input("Enter two numbers - space separated range: ")
        numbers = user_input.split()
        if len(numbers) != 2:
            print("Please enter exactly two numbers.")
            continue
        try:
            range_min, range_max = map(int, numbers)
            return range_min, range_max
        except ValueError:
            print("Input error.")


def operation(list_1: list, list_2: list, range_min: int, range_max: int) -> tuple:
    """
    Transfer elements from list_1 to list_2 within specified range.

    Args:
        list_1 (list): Source list to remove elements from
        list_2 (list): Target list to add elements to
        range_min (int): Start index of the range (inclusive, 1-based indexing)
        range_max (int): End index of the range (inclusive, 1-based indexing)

    Returns:
        tuple: A tuple containing (modified_list_1, modified_list_2)

    """
    carry_digit = []

    for num in range(range_min - 1, range_max + 1):
        carry_digit.append(list_1[num])

    for el in carry_digit:
        list_1.remove(el)

    list_2.extend(carry_digit[::-1])
    return list_1, list_2


def main() -> None:
    """
    Main function to coordinate the element transfer process.

    Returns:
        None
    """
    list_1 = get_list()
    list_2 = get_list()

    range_min, range_max = get_range()

    modified_list_1, modified_list_2 = operation(
        list_1, list_2, range_min, range_max)

    print("First list:", modified_list_1)
    print("Second list:", modified_list_2)


if __name__ == "__main__":
    main()
