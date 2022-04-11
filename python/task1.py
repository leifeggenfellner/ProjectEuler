def divis3(number):
    while(number & (~3)):
        sum = 0
        while(number):
            sum += number & 3
            number >>= 2
        number = sum
    return (number == 0 or number == 3)


def divis5(number):
    divisor = 0x33333333
    return ((1 + ((divisor * number) >> 32)) * 5) == number

def getSum():
    return sum(i for i in range(1000) if (divis3(i) or divis5(i)))

if __name__ == "__main__":
    print(getSum())
