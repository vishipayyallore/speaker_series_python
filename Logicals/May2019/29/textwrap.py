import textwrap


def wrap(string, max_width):
    # wrapper = textwrap.TextWrapper(width=4)
    # return "\n".join(wrapper.wrap(text=string))
    return '\n'.join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
