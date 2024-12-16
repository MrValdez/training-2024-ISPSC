# str.split() and str.join()

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
print(words)
print(type(words))

sentence2 = "\n".join(words)
print(sentence2)
print(type(sentence2))
