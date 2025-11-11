def sort_string(user_str: str) -> str:
    """
    Sort characters in a string in ascending order.

    Args:
        user_string (str): The input string to be sorted

    Returns:
        str: A new string with characters sorted in ascending order

    """
    elements = list(user_str)
    elements.sort()
    sorted_elements = ''.join(elements)
    return sorted_elements


def main():
    """
    Main function to get user input and display sorted string.
    """
    user_str = input("Enter the string: ")
    sorted_str = sort_string(user_str)
    print("Sorted string:", sorted_str)


if __name__ == "__main__":
    main()
