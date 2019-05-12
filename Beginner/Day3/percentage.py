import math

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
query_name = input()

current_marks = student_marks[query_name]
average = (sum(current_marks) / len(current_marks)) * 1.00
print("{0:.2f}".format(average))


