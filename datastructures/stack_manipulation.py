import random


def getPermutations(nums, building, perms):
    if len(nums) == 0:
        perms.append(building)
        return

    for i in range(len(nums)):
        newArr = nums[:i] + nums[i + 1:]
        newPerm = building + [nums[i]]
        getPermutations(newArr, newPerm, perms)


def perms(nums):
    permutations = []
    getPermutations(nums, [], permutations)
    return permutations


class Shuffler():

    def __init__(self, listOfNums):
        self.listOfNums = listOfNums
        self.currentShuffledList = listOfNums

    def shuffle(self):
        permutations = []
        getPermutations(self.listOfNums, [], permutations)

        randomSelector = random.choice(permutations)
        self.currentShuffledList = randomSelector
        return randomSelector

    def reset(self):
        self.currentShuffledList = self.listOfNums



shuffle = Shuffler([1,2,3])


print(shuffle.shuffle())
print(shuffle.shuffle())







# nums = [1, 2, 3]
# perms = perms(nums)
# print(perms)
#
# nums = [1,2,3,5,6]
#
# print(nums[1:])
# newArr = nums[:1] + nums[3:]
#
# print(newArr)
# print(nums)
