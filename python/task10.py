def ifNotPrime(prime: list[int], x: int) -> bool:
    return (prime[int(x / 64)] & (1 << ((x >> 1) & 31)))


def makeComposite(prime: list[int], x: int) -> None:
    prime[int(x / 64)] |= (1 << ((x >> 1) & 31))


def bitWiseSieve(n: int) -> tuple[int]:
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


def main() -> None:
    n = 2000000
    primes = bitWiseSieve(n)
    print(sum(primes))


if __name__ == "__main__":
    main()
