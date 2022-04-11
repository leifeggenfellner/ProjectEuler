def getNthPrimeNumber(N) -> int:
    totalPrimeNumbers = 0
    sizeFactor = 2
    size = (N * sizeFactor)

    while totalPrimeNumbers < N:
        primeNumbers = getPrimeNumbers(size)
        totalPrimeNumbers = sum(primeNumbers[2:])
        sizeFactor += 1
        size = (N * sizeFactor)

    nthPrimeNumber = countPrimeNumbers(primeNumbers, N)
    return nthPrimeNumber

def getPrimeNumbers(size) -> list[int]:
    primeNumbers = bytearray([1]*size)

    for i in range(2, size):
        if primeNumbers[i] == 1:
            for j in range(i, size):
                if i * j < size:
                    primeNumbers[i*j] = 0
                else:
                    break
    
    return primeNumbers

def countPrimeNumbers(primeNumbers, N) -> int:
    count = 0

    for i in range(2, len(primeNumbers)):
        count += primeNumbers[i]
        if count == N:
            return i

if __name__ == "__main__":
    print(getNthPrimeNumber(10001))
