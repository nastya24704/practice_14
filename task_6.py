def divisors(number: int) -> list:
    """
    Return a sorted list of all divisors of the given number.

    :param number: The integer for which to find the divisors.
    :return: Sorted list of the number's divisors.
    """
    result = []
    for num in range(1, int(number ** 0.5) + 1):
        if number % num == 0:
            result.append(num)
            if num != number // num:
                result.append(number // num)
    result.sort()
    return result


def main():
    """
    Main function to get user input and display the divisors.
    """
    number = int(input("Enter an integer number: "))
    print(divisors(number))


if __name__ == "__main__":
    main()
