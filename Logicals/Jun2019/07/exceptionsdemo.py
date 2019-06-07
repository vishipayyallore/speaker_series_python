loop = int(input())

for _ in range(loop):
    numbers = input().split()
    try:
        print(int(numbers[0]) / int(numbers[1]))
    except ZeroDivisionError as error:
        print('Error Code:', error)
