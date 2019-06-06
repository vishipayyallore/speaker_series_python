from collections import defaultdict

source = defaultdict(list)
outputs = defaultdict(list)

inputs = list(map(int, input().split()))

for counter in range(inputs[0]):
    source['first'].append(input())

for counter in range(inputs[1]):
    source['second'].append(input())

for item in source['second']:
    outputs[item].append(-1)

for item in outputs.items():
    for i in range(len(item)):
        print(item[i])

