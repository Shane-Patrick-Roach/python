for i in range(1):
    print(i)


def rotate(matrix):
    l = 0
    r = len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            topLeft = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topLeft
        l += 1
        r -= 1

    return matrix


testMatrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate(testMatrix))