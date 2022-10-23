from math import sqrt


def specialPythagoreanTriplet():
    for b in range(1000):
        for a in range(1, b):
            c = sqrt(a * a + b * b)
            if a + b + c == 1000:
                return round(a * b * c)

if __name__ == "__main__":
    print(specialPythagoreanTriplet())
