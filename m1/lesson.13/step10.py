words = ["apple", "banana", "cherry", "orange", "data", "xyz"]

sorted_words = sorted(words)
print(sorted_words)

sorted_words_l = sorted(words, key=len)
print(sorted_words_l)

sorted_words_l = sorted(words, key=lambda x: len(x))
print(sorted_words_l)