def user_list():
    """
    Prompts the user to input a list of values separated by spaces.
    Continues prompting until the user enters valid input.

    Returns:
        list: A list of integers provided by the user.
    """
    while True:
        user_input = input("Enter list values separated by spaces: ")
        try:
            return list(map(int, user_input.split()))
        except ValueError:
            print("Input error: please enter valid integers separated by spaces.")


def user_command():
    """
    Prompts the user to input a command in the format of a direction ('L' or 'R')
    followed by a number indicating the shift amount.
    Continues prompting until a valid command is entered.

    Returns:
        tuple: A tuple containing:
            - direction (str): 'L' or 'R'
            - shift (int): The number of positions to shift.
    """
    while True:
        command = input("Enter a command ('L' or 'R') followed by the shift number: ").strip()
        if len(command) < 2:
            print("Invalid command: too short.")
            continue

        direction = command[0]
        shift_str = command[1:]

        if direction not in ('L', 'R'):
            print("Command must start with 'L' or 'R'. Please try again.")
            continue
        if not shift_str.isdigit():
            print("Shift value must be a number. Please try again.")
            continue
        shift = int(shift_str)
        return direction, shift


def list_shift(lst, direction, shift):
    """
    Shifts the list left or right by a specified number of positions.

    Args:
        lst (list): The list to be shifted.
        direction (str): 'L' for left shift, 'R' for right shift.
        shift (int): The number of positions to shift.

    Returns:
        list: The shifted list.
    """
    num = len(lst)
    if num == 0:
        return lst
    shift %= num
    if direction == 'L':
        return lst[shift:] + lst[:shift]
    else:
        return lst[-shift:] + lst[:-shift]


def main():
    """
    Main function to execute the list shifting based on user input.
    """
    lst = user_list()
    direction, shift = user_command()
    final_list = list_shift(lst, direction, shift)
    print("Result:", final_list)


if __name__ == "__main__":
    main()
