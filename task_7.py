def main() -> None:
    """
    Reads a list of integers from user input, calculates
    the sum of even and odd numbers, and prints the results.
    """
    elements = input("Enter integer numbers separated by spaces: ")
    numbers = [int(num) for num in elements.split()]

    sum_even = 0
    sum_odd = 0

    for number in numbers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number

    print(sum_even, sum_odd)


if __name__ == "__main__":
    main()
