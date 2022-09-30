def count_construct(word, word_bank, memo= {}):
    if word in memo:
        return memo[word]
    if word == "":
        return 1

    total_count = 0

    for prefix in word_bank:
        if prefix in word and word.index(prefix) == 0:
            new_word = word[len(prefix):]
            count = count_construct(new_word, word_bank, memo)
            total_count += count

    memo[word] = total_count
    return memo[word]


word1 = "abcdef"
word_bank1 = ["ab", "abc", "cd", "def", "abcd"]

word_bank2 = ["bo", "rd", "ate", "b", "ska", "sk", "boar"]
word2 = "skateboard"

#
print(count_construct(word1, word_bank1))