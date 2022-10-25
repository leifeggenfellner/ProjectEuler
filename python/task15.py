from math import factorial


def calculate_paths(n: int, k: int) -> int:
    return factorial(n + k) // (factorial(n) * factorial(k))


def main() -> None:
    n = m = 20
    print(calculate_paths(n, m))


if __name__ == '__main__':
    main()
