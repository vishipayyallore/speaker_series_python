
def create_matrix():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # with filter
    output = [[i, j, k] for i in range(
        x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
    print(output)

    # without filter
    output = [[i, j, k] for i in range(x + 1)
            for j in range(y + 1) for k in range(z + 1)]
    for item in output:
        print(item)


def main():
    create_matrix()


if __name__ == "__main__":
    main()