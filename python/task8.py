def largestProductInSeries(seriesFile) -> int:
    with open(seriesFile, "r") as series:
        data = series.read().replace("\n", "")

    largest = 0

    for i in range(len(data) - 13):
        total = 1
        for j in range(i, i + 13):
            total *= int(data[j])

        if total > largest:
            largest = total

    return largest

print(largestProductInSeries("./inc/task8.txt"))
