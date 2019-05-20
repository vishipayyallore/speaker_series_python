students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

print(students)

second_lowest = sorted(list(set([marks for name, marks in students])))[1]
print(second_lowest)

print('\n'.join([a for a,b in sorted(students) if b == second_lowest]))

"""
students.sort(key = lambda x: x[1])
print(students)

filtered_name = [x for x in students if x[1] == students[1][1]]
filtered_name.sort(key = lambda x: x[0])

for student in filtered_name:
    print(student[0])
"""

# for name in students:
#    print(name)
# print(students[1][1])


"""
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])


    second_lowest = sorted(list(set([marks for name, marks in students])))[1]

    print('\n'.join([a for a,b in sorted(students) if b == second_lowest]))
    
    students.sort(key = lambda item: item[1])

    filtered_name = [item for item in students if item[1] == students[1][1]]
    filtered_name.sort(key = lambda x: x[0])
    for student in filtered_name:
        print(student[0])
"""
