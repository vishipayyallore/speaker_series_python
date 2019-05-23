n = int(input())
integer_list = map(int, input().split())

output = hash(tuple(integer_list))
print(output)
