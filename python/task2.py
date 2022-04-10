def sumEvenFibonacci(num1, num2, limit) -> list[int]:
    fibonacciNumbers = [num1, num2]
    while (fibonacciNumbers[-1] + fibonacciNumbers[-2]) < limit:
        fibonacciNumbers.append(fibonacciNumbers[-1] + fibonacciNumbers[-2])

    evenFibonacciNumbers = list(filter(
        lambda num: not(num & 1), fibonacciNumbers))

    return sum(number for number in evenFibonacciNumbers)


print(sumEvenFibonacci(1, 2, 4000000))
