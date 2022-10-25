def power_digit_sum(number: int, power: int) -> int:
    return sum(int(x) for x in str(number ** power))


def main() -> None:
    print(power_digit_sum(2, 1000))


if __name__ == '__main__':
    main()
