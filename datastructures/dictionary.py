from collections import defaultdict

res = defaultdict(str)



def getAsciCount(str):

    count = [0] * 26

    for s in str:
        count[ord(s) - ord("a")] += 1

    res[tuple(count)] = "Wow"


getAsciCount("asdas")
getAsciCount("asdaasasds")

print(res.keys())



