def can_construct(word, word_bank):
    if word == '':
        return True

    for prefix in word_bank:
        if prefix in word and word.index(prefix) == 0:
            length_prefix = len(prefix)
            new_word = word[length_prefix:]
            if can_construct(new_word, word_bank):
                return True

    return False


word_bank1 = ["h", "e", "l", "o"]
word1 = "hello"

word_bank2 = ["bo","rd","ate", "b", "ska", "sk", "boar"]
word2 = "skateboard"

#
print(can_construct(word2, word_bank2))
