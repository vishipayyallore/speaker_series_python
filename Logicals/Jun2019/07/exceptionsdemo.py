loop = int(input())

for _ in range(loop):
    try:
        num1, num2 = map(int, input().split())
        print(num1 // num2)
    except ZeroDivisionError as error:
        print('Error Code:', error)
    except ValueError as error:
        print('Error Code:', error)
