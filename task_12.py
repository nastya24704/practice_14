holes_letters = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']


def count_letters(word: str) -> int:
    '''
    Counts the number of letters in a word that have holes.

    Args:
        word (str): The word to analyze.

    Returns:
        int: The number of letters with holes.
    '''
    count = 0
    for letter in word:
        if letter in holes_letters:
            count += 1
    return count


def count_words(words: list) -> tuple:
    '''
    Analyzes a list of words: counts total letters with/without holes
    and identifies words with two or more letters with holes.

    Args:
        words (list of str): The list of words to analyze.

    Returns:
        tuple: (total number of letters with holes,
                total number of letters without holes,
                list of words with at least two letters with holes)
    '''
    
    letters_with_holes = 0
    letters_without_holes = 0
    words_with_holes_more_2 = []

    for word in words:
        count_holes = count_letters(word)
        if count_holes >= 1:
            letters_with_holes += count_holes
            letters_without_holes += len(word) - count_holes
        else:
            letters_without_holes += len(word)

        if count_holes >= 2:
            words_with_holes_more_2.append(word)

    return letters_with_holes, letters_without_holes, words_with_holes_more_2


def main():
    '''
    Main function to receive user input, process the words, and display statistics.
    '''
    sentence = input("Enter a string: ").strip().lower()
    words = sentence.split()

    letters_with_holes, letters_without_holes, words_with_holes_more_2 = count_words(words)

    print("Number of letters with holes:", letters_with_holes)
    print("Number of letters without holes:", letters_without_holes)
    print("Words with two or more letters with holes:", *words_with_holes_more_2)


if __name__ == "__main__":
    main()
