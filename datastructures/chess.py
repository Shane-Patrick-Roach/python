

startingRowWhite = True
isWhite = True
n = 4

board= []

for i in range(n):

    boardRow = []

    isWhite = startingRowWhite

    for j in range(n):
        if isWhite:
            boardRow.append("W")
        else:
            boardRow.append("B")
        isWhite = not isWhite

    startingRowWhite = not startingRowWhite
    board.append(boardRow)


print(board)


list = [1,0,0,0,12,3,4,6,1,2,3]
list2 = list[::-1]

print(list2)