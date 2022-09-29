
res = []
inputword = "()()"

def getPerms(word, currentStr):
    if len(currentStr) == len(inputword):
        res.append(currentStr)
        return

    for i in range(len(word)):
        newString = currentStr + word[i]
        newWord = word[:i] + word[i + 1::]

        getPerms(newWord, newString)

getPerms(inputword, "")

print(len(res))


