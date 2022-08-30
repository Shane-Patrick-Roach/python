def coinChange(coins, amount):
    def findCoins(coins, amount, memo):
        if amount in memo:
            return memo.get(amount)
        if amount == 0:
            return []
        if amount < 0:
            return None

        shortestComb = None

        for coin in coins:

            remainder = amount - coin
            getCombination = findCoins(coins, remainder, memo)
            if getCombination is not None:
                getCombination.append(coin)

                if shortestComb is None or len(shortestComb) > len(getCombination):
                    shortestComb = getCombination

        memo[amount] = shortestComb
        print(shortestComb)

        return shortestComb

    smallestAmount = findCoins(coins, amount, {})

    if smallestAmount:
        return len(smallestAmount)
    else:
        return -1


coinChange([1,2,3], 6)
print(coinChange([1,2,3], 6))
