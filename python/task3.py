from math import sqrt


def largestPrimeFactor(number) -> int:
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        divisor += 1
        if divisor ** 2 > number:
            if number > 1: factors.append(number)
            break

    return int(max(factors))


print(largestPrimeFactor(600851475143))
