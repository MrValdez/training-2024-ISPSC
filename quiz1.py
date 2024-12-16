# quiz1.py
#  Make a program that outputs the sentence without the vowels

sentence = "The quick brown fox jumps over the lazy dog"

#sentence = "Th qck brwn fx jmps vr th lzy dg"

sentence = sentence.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")

sentence = sentence.replace("a", "")  \
                   .replace("e", "")  \
                   .replace("i", "")  \
                   .replace("o", "")  \
                   .replace("u", "") 

sentence = (sentence.replace("a", "")
                   .replace("e", "")
                   .replace("i", "")
                   .replace("o", "")
                   .replace("u", "")) 

sentence = (
    sentence.replace("a", "")
    .replace("e", "")
    .replace("i", "")
    .replace("o", "")
    .replace("u", "")
) 

print(sentence)