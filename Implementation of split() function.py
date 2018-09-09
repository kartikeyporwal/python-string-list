def split(sentence, splitby):
    length = len(sentence)
    splitted_list = []
    index = 0

    while index < length:
        if sentence[index] != splitby:
            word_start = index
            while index < length and sentence[index] != splitby:
                index += 1
                
            splitted_list.append(sentence[word_start:index])
        index += 1

    return splitted_list

print(split("How Are You?", " "))

print(split("Abra Ka Dabra", "a"))
