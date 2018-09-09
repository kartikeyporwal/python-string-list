def rev_word(sentence):
    return " ".join(word[::-1] for word in sentence.split())

print(rev_word(" Hello World"))
