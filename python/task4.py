def largestPalindromeProduct() -> int:
    largestPalindrome = 0

    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if i > j:
                if str(i * j) == str(i * j)[::-1] and i * j > largestPalindrome:
                    largestPalindrome = i * j

    return largestPalindrome

if __name__ == "__main__":
    print(largestPalindromeProduct())
