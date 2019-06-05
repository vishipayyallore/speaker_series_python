from collections import defaultdict

source = defaultdict(list)

inputs = list(map(int, input().split()))

for counter in range(inputs[0]):
    source['first'].append(input())

for counter in range(inputs[1]):
    source['second'].append(input())

for item in source['second']:
    print(item)