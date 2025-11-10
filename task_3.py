sentence = input("Enter a sentence: ")
words = sentence.split()

punctuation_marks = '.,?!...:;,-"()/'
result = []

for word in words:
    final_word = word.strip(punctuation_marks)
    result.append(final_word)

print(result)
