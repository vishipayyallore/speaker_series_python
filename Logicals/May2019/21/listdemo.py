
numbers = []


def perform_action(data):
    if(data[0] == 'insert'):
        numbers.insert(int(data[1]), int(data[2]))
    elif(data[0] == 'insert'):
        numbers.append(int(data[1]))
    elif(data[0] == 'remove'):
        numbers.remove(int(data[1]))


if __name__ == '__main__':
    N = int(input())

    for counter in range(N):
        data = input()
