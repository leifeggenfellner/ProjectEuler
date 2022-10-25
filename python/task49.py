import math


def binarySearch(arr: list[int], target: int) -> int:
    L = 0
    R = len(arr) - 1

    while L <= R:
        m = math.floor((L + R) / 2)
        if arr[m] < target:
            L = m + 1
        elif arr[m] > target:
            R = m - 1
        else:
            return m

    return -1


def ifNotPrime(prime: list[int], x: int) -> bool:
    return (prime[int(x / 64)] & (1 << ((x >> 1) & 31)))


def makeComposite(prime: list[int], x: int) -> None:
    prime[int(x / 64)] |= (1 << ((x >> 1) & 31))


def bitwiseSieve(n: int) -> tuple[int]:
    prime = [0 for i in range(int(n / 64) + 1)]
    primes = [2]

    for i in range(3, n + 1, 2):
        if (i * i <= n):
            if (ifNotPrime(prime, i)):
                continue
            else:
                k = i << 1
                for j in range(i * i, n, k):
                    k = i << 1
                    makeComposite(prime, j)

    for i in range(3, n + 1, 2):
        if (ifNotPrime(prime, i)):
            continue
        else:
            primes.append(i)

    return primes


def isPermutation(m: int, n: int) -> bool:
    arr = [0 for _ in range(10)]

    temp = n
    while temp > 0:
        arr[temp % 10] += 1
        temp = int(temp / 10)

    temp = m
    while temp > 0:
        arr[temp % 10] -= 1
        temp = int(temp / 10)

    for i in range(10):
        if arr[i] != 0:
            return False

    return True


def findPrimePermutation() -> int:
    limit = 9999
    result = 0
    primes = bitwiseSieve(limit)
    primes = list(filter(lambda x: x > 1488, primes))

    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            k = primes[j] + (primes[j] - primes[i])
            if k <= limit and binarySearch(primes, k) >= 0:
                if isPermutation(primes[i], primes[j]) and isPermutation(primes[i], k):
                    result = int(str(primes[i]) + str(primes[j]) + str(k))
                    break
        if result > 0:
            break

    return result


def main() -> None:
    print(findPrimePermutation())


if __name__ == "__main__":
    main()
