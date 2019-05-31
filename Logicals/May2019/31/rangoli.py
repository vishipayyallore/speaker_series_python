alphabets = 'abcdefghijklmnopqrstuvwxyz'

def print_rangoli(size):
    # your code goes here
    pass


if __name__ == '__main__':
    # n = int(input())
    # print_rangoli(n)
    n = 5
    current_data = alphabets[0:n]
    print(current_data)
    print('-'.join(alphabets[n-1]))
