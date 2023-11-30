def Squares_of_a_Sorted_Array(nums):
    positiveSquares = []
    negativeSquares = []

    for num in nums:
        if num >= 0:
            positiveSquares.append(num ** 2)
        else:
            negativeSquares.append(num ** 2)

    negativeSquares.reverse()

    if len(negativeSquares) == 0: return positiveSquares
    if len(positiveSquares) == 0: return negativeSquares

    while 1:
        sortedSquares = []
        indexOfNegative = 0
        indexOfPositive = 0
        pos = positiveSquares[indexOfPositive]
        neg = negativeSquares[indexOfNegative]
        if pos == neg:
            indexOfPositive += 1
            indexOfNegative += 1
            sortedSquares.extend([pos, neg])

        elif pos < neg:
            sortedSquares.append(pos)
            indexOfPositive += 1

        else:
            sortedSquares.append(neg)
            indexOfNegative += 1

        if indexOfNegative == len(negativeSquares):
            if indexOfPositive <= len(positiveSquares):
                sortedSquares.extend(positiveSquares[indexOfPositive:])
                return sortedSquares
        if indexOfPositive == len(positiveSquares):
            if indexOfNegative <= len(negativeSquares):
                sortedSquares.extend(negativeSquares[indexOfNegative:])
                return sortedSquares


if __name__ == '__main__':
    print(Squares_of_a_Sorted_Array([-10000,-9999,-7,-5,0,0,10000]))
