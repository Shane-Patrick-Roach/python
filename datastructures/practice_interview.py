# tacocat  -  tacocat
# cat

# input string
# output boolean

# 1st approach - input word and reversing word
## then check if its equivalent  runtime o(n) space o(n)

# two pointer approach o(n) runtime o(n) space

## Tacocat



def isPalindrome(s):


    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1

    return True
