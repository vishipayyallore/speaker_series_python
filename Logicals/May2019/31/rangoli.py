alphabets = 'abcdefghijklmnopqrstuvwxyz'

def print_rangoli(size):
    # your code goes here
    pass


if __name__ == '__main__':
    # n = int(input())
    # print_rangoli(n)
    n = 5
    current_data = alphabets[0:n]
    print(current_data, current_data[::-1])
    print('-'.join(alphabets[n-1]))

#size 3
"""
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""