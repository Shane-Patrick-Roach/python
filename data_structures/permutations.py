


nums = [1,2,3]

res = []


def getPerms(currentNums, currentPerm):
    if len(currentNums) == 0:
        res.append(currentPerm)
        return

    for i in range(len(currentNums)):
        num = currentNums[i]
        updatePerm = currentPerm + [num]
        updateNums = currentNums[:i] + currentNums[i + 1::]
        getPerms(updateNums, updatePerm)

getPerms(nums, [])

print(res)