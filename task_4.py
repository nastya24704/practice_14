def main() -> None:
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    punctuation_marks = '.,?!...:;,-"()/'
    result = []

    for word in words:
        final_word = word.strip(punctuation_marks)
        if final_word not in result:
            result.append(final_word)
    print(result)

if __name__ == "__main__":
    main()
