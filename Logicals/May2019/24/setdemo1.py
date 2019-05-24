def average(array):
    filtered_data = set(array)
    return sum(filtered_data)/len(filtered_data)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)