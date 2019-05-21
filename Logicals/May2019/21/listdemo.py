

if __name__ == '__main__':
    numbers = []

    N = int(input())

    for counter in range(N):
        command, *arguments = input().split()
        if(command != 'print'):
            eval('numbers.{0}{1}'.format(command, tuple(map(int, arguments))))
        else:
            print(numbers) 
