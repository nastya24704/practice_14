from typing import List, Tuple


def parse_int_list(input_line: str) -> List[int]:
    """
    Converts a space-separated string of integers into a list of integers.

    Args:
        input_line (str): The input string containing integers separated by spaces.

    Returns:
        List[int]: The list of integers parsed from the string.
    """
    return list(map(int, input_line.strip().split()))


def process_lists(
    lst1: List[int],
    lst2: List[int],
    start_idx: int,
    end_idx: int
) -> Tuple[List[int], List[int]]:
    """
    Moves a segment of lst1 (from start_idx to end_idx inclusive) in reverse order
    to lst2, and removes those elements from lst1.

    Args:
        lst1 (List[int]): The first list.
        lst2 (List[int]): The second list.
        start_idx (int): Starting index of the segment (0-based).
        end_idx (int): Ending index of the segment (0-based).

    Returns:
        Tuple[List[int], List[int]]: The updated lists after processing.
    """
    # Extract the segment
    segment = lst1[start_idx:end_idx + 1]
    # Remove the segment from lst1
    del lst1[start_idx:end_idx + 1]
    # Reverse the segment and extend lst2
    lst2.extend(segment[::-1])
    return lst1, lst2


def main() -> None:
    """
    Reads two input lines for lists of integers and two integers for range indices.
    Processes the lists as per the task description, then outputs both lists.
    """
    # Read input lists
    list1_input = input("Enter first list of integers: ")
    list2_input = input("Enter second list of integers: ")

    lst1 = parse_int_list(list1_input)
    lst2 = parse_int_list(list2_input)

    # Read start and end indices (assuming user enters valid integers)
    start_idx = int(input("Enter start index (0-based): "))
    end_idx = int(input("Enter end index (0-based): "))

    # Process lists
    lst1, lst2 = process_lists(lst1, lst2, start_idx, end_idx)

    # Output the results
    print("First list after processing:", lst1)
    print("Second list after processing:", lst2)


if __name__ == "__main__":
    main()
