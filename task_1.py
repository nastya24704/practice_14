def elements() -> list:
    """
    Reads 10 integers entered by the user in a single line, separated by spaces or commas.

    Returns:
        list: A list of 10 integers.
    """
    while True:
        numbers = input("Enter 10 integers numbers separated by spaces: ").split()
        if len(numbers) != 10:
            print("Please enter exactly 10 numbers.")
            continue
        try:
            first_list = [int(figure) for figure in numbers]
            return first_list
        except ValueError:
            print("Invalid input detected. Please try again.")


def new_elements(components: list) -> list:
    """
    Creates a new list of 8 elements, each being the sum of the elements
    that are immediately before and after each current element in the original list.

    Args:
        components (list): The original list of 10 integers.

    Returns:
        list: A list of 8 elements, each being the sum of neighbors in the original list.
    """
    new_list = []
    for i in range(1, 9):
        sum_value = components[i - 1] + components[i+1]
        new_list.append(sum_value)
    return new_list


def main() -> None:
    """
    Main function of the program: reads numbers and displays the result.
    """
    components = elements()
    result = new_elements(components)
    print("New list:", result)


if __name__ == "__main__":
    main()
