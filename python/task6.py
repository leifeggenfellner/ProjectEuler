def sumSquareDifference() -> int:
    sumOfSquares = sum(num ** 2 for num in range(1, 101))
    squareOfSum = sum(i for i in range(1, 101)) ** 2

    return abs(sumOfSquares - squareOfSum)

print(sumSquareDifference())
