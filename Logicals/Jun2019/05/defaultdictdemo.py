from collections import defaultdict

source = defaultdict(list)

inputs = list(map(int, input().split()))

for counter in range(inputs[0]):
    source['first'].append(input())

print(source)