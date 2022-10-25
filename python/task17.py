def one_to_ten() -> int:
    return 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4


def ten_to_nineteen() -> int:
    return 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8


def twenty_to_ninety_nine() -> int:
    return 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8*(one_to_ten())


def hundred_to_ninehundred_ninety_nine() -> int:
    return 100*one_to_ten() + 9 * \
        (one_to_ten() + ten_to_nineteen() + twenty_to_ninety_nine()) + 7*9 + 891*10


def main() -> None:
    print(one_to_ten() + ten_to_nineteen() + twenty_to_ninety_nine() +
          hundred_to_ninehundred_ninety_nine() + 11)


if __name__ == "__main__":
    main()
