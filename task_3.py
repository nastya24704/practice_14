def main() -> None:
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    punctuation_marks = '.,?!...:;,-"()/'
    result = []

    for word in words:
        final_word = word.strip(punctuation_marks)
        result.append(final_word)
    return result
    
if __name__ == "__main__":
    res = main()
    print(res)
