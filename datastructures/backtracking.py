

arr = [1,2,3]

total = []

def subsets(nums):

    res = []
    res.append([])

    def backtrack(numsbacktrack):
        if numsbacktrack == None:
            return
        if numsbacktrack not in res:
            res.append(numsbacktrack)

        for i in range(len(numsbacktrack)):

            n = numsbacktrack.pop(0)

            backtrack(numsbacktrack)

            numsbacktrack.append(n)

    backtrack(nums)
    return res

res = subsets(arr)

print(res)



