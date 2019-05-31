import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


def wrap_v2(string, max_width):
    list_data = textwrap.wrap(string, max_width)
    return '\n'.join(list_data)


def main():
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

    result = wrap_v2(string, max_width)
    print(result)


if __name__ == '__main__':
    main()

