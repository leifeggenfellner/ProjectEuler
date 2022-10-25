def get_matrix() -> list[list[int]]:
    with open('./inc/task67.txt', 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        data = [x.split(' ') for x in data]
        data = [list(map(int, i)) for i in data]

    columns = len(data[-1])

    for row in data:
        while len(row) < columns:
            row.append(0)

    return data


def max_sum_path() -> int:
    inputTriangle = get_matrix()
    lines = len(inputTriangle)

    for i in range(lines - 2, -1, -1):
        for j in range(i + 1):
            inputTriangle[i][j] += max(inputTriangle[i + 1]
                                       [j], inputTriangle[i + 1][j + 1])
    return inputTriangle[0][0]


def main() -> None:
    print(max_sum_path())


if __name__ == '__main__':
    main()
