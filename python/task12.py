import math


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


def get_divisors(n: int, primeList: list[int]) -> int:
    number_of_divisors = 1
    exponent = None
    remainder = n

    for prime in primeList:
        if prime * prime > n:
            return number_of_divisors * 2
        exponent = 1
        while (remainder % prime == 0):
            exponent += 1
            remainder /= prime
        number_of_divisors *= exponent

        if remainder == 1:
            return number_of_divisors

    return number_of_divisors


def main() -> int:
    number = 1
    i = 2
    count = 0
    Dn1 = 2
    Dn = 2
    primeList = bitwiseSieve(1000)

    while count < 500:
        if i & 1 == 0:
            Dn = get_divisors(i + 1, primeList)
            count = Dn * Dn1
        else:
            Dn1 = get_divisors(int((i + 1) / 2), primeList)
            count = Dn * Dn1
        i += 1

    number = int(i * (i - 1) / 2)
    print(number)


if __name__ == "__main__":
    main()
