
def main() -> None:
    with open('./inc/task13.txt', 'r') as f:
        data = f.readlines()

    print(str(sum(int(num) for num in data))[:10])


if __name__ == "__main__":
    main()
