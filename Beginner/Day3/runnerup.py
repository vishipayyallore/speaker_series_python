
def find_runnerup():
    n = int(input())
    numbers = input()

    numbers_list = list(map(int, numbers.split()))
    numbers_list = list(dict.fromkeys(sorted(numbers_list)))
    print(numbers_list)
    print(numbers_list[-2])


def main():
    find_runnerup()


if __name__ == "__main__":
    main()

# numbers_list = list(map(int, numbers.split()))
# numbers_list = [int(i) for i in numbers.split()] 
# print(numbers_list)
# print(sorted(numbers_list))

