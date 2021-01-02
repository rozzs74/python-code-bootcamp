# def angryProfessor(required_in_class, students):
#     i = 0
#     not_late = []
#     for j in range(0, required_in_class):
#         student = students[j]
#         if student <= 0:
#             not_late.append(student)
#         i += 1
#         if i == required_in_class:
#             print(not_late)
#             return "NO" if len(not_late) == required_in_class else "YES"

# https://www.hackerrank.com/challenges/angry-professor/problem
def angryProfessor(required_in_class, students):
    i = 0
    for student in students:
        if student < 1:
            i += 1
    return "YES" if i < required_in_class else "NO"

a = angryProfessor(3, [-1, -3, 4, 2])
# a = angryProfessor(4, [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67])
# a = angryProfessor(4, [-1, -1, 0, 0, 1, 1])
print(a)
# 4 3
# -1 -3 4 2

# 10
# 10 4
# -93 -86 49 -62 -90 -63 40 72 11 67