def PascalsII(rowIndex):
    result = [[1]]

    for i in range (rowIndex):
        temp = [0] + result[-1] + [0]
        row = []

        for j in range (len(result[-1]) + 1):
            row.append(temp[j] + temp[j+1])

        result.append(row)

    return result[rowIndex]

print(PascalsII(5))

