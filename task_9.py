def get_input() -> list:
    """
    Reads multiple lines of input from the user until an empty line is entered.

    Returns:
        list: A list containing all input lines.
    """
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)
    return lines


def clean_word(word: str) -> str:
    """
    Removes all non-letter characters from a word.

    Args:
        word (str): The original word possibly containing punctuation.

    Returns:
        str: The cleaned word containing only alphabetic characters.
    """
    return ''.join(element for element in word if element.isalpha())


def count_and_sort_words(lines: list) -> list:
    """
    Counts the frequency of each word and sorts the words primarily by
    decreasing frequency, secondarily by their appearance order in the text.

    Args:
        lines (list): List of input lines.

    Returns:
        list: Sorted list of words according to the specified criteria.
    """
    word_counts = {}
    order = []
    for line in lines:
        for raw_word in line.split():

            cleaned_word = clean_word(raw_word).lower()

            if not cleaned_word:
                continue


            if cleaned_word not in word_counts:
                word_counts[cleaned_word] = 0
                order.append(cleaned_word)


            word_counts[cleaned_word] += 1

    sorted_words = sorted(
        set(order),
        key=lambda w: (-word_counts[w], order.index(w))
    )

    return sorted_words


def main() -> None:
    """
    Main function to execute the input reading, processing, and output.
    """
    lines = get_input()
    sorted_word_list = count_and_sort_words(lines)
    for word in sorted_word_list:
        print(word.lower())


if __name__ == '__main__':
    main()
