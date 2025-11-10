def elements() -> list:
    """
    Reads a list of integers from user input until valid data is entered.
    
    Returns:
        list: A list of integers entered by the user.
    """
    while True:
        first_list = input("Enter integers separated by spaces: ").split()
        try:
            return [int(figure) for figure in first_list]
        except ValueError:
            print("Invalid input. Please enter only integers.")


def new_list(components: list) -> list:
    """
    Checks if the list contains exactly one '3'.
    If so, returns a new list with all '3's removed.
    
    Args:
        components (list): The original list of integers.
    
    Returns:
        list: The new list without '3' if exactly one '3' was present.
        None: If the list does not contain exactly one '3'.
    """
    if components.count(3) != 1:
        return None
    return [component for component in components if component != 3]


def main() -> None:
    """
    Main function: reads input, processes the list, and outputs the result.
    """
    numbers = elements()
    result = new_list(numbers)
    if result is None:
        print("The list must contain exactly one '3'.")
    else:
        print("New list:", result)


if __name__ == "__main__":
    main()
