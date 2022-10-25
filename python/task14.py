def bin_add(*bin_nums: str) -> str:
    return bin(sum(int(x, 2) for x in bin_nums))[2:]


def longest_collatz_sequence(number: int) -> int:
    longest_chain = 0
    number_with_longest_chain = 0
    sequence = None

    cache = [-1 for _ in range(number + 1)]
    cache[1] = 1

    for i in range(2, number + 1):
        sequence = i
        k = 0
        while sequence != 1 and sequence >= i:
            k += 1
            if sequence & 1:
                starting_num = bin(sequence)[2:]
                n_bin = bin(sequence)[2:] + "1"
                sequence = int(bin_add(starting_num, n_bin), 2)
            else:
                sequence >>= 1

        cache[i] = k + cache[sequence]

        if cache[i] > longest_chain:
            longest_chain = cache[i]
            number_with_longest_chain = i

    return number_with_longest_chain


def main() -> None:
    number = 1000000
    print(longest_collatz_sequence(number))


if __name__ == "__main__":
    main()
