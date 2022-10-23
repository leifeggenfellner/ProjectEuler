def smallestMultiple():
    keys = [i for i in range(2, 21)]
    values = [0 for _ in range(2, 21)]

    division = dict(zip(keys, values))

    number = 20

    while True:
        for key in division.keys():
            if number % key == 0:
                division[key] = 1

        if all(value == 1 for value in division.values()):
            return number
        else:
            number += 10
            division = dict.fromkeys(division, 0)

if __name__ == "__main__":
    print(smallestMultiple())
