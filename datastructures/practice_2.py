

# function isPalindromicSentence(s)

# input  = string
# output = boolean

# test cases
# uppercase values
# was it a car or a cat I saw
# sentence can have special character.      cat tac?

## Test 1: was it a car or a cat I saw
## Test 2: %??? is it ?.

# runtime o(n)
# space o(n)


def isPalindromicSentence(s):

    if len(s) == 0:
        return True

    filter_s = []  ### isit

    for char in range(len(s)):
        if s[char].isAlpha():
            filter_s.append(s[char].toLower())

    return isPalindrome(''.join(filter_s))


