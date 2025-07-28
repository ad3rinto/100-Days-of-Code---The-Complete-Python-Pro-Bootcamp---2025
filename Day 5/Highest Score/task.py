student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(max(student_scores))
# print(min(student_scores))
#
# total = 0
# for each_score in student_scores:
#     total += each_score
# print(total)


min_score = 120
for score in student_scores:
    if score < min_score:
        min_score = score
print(min_score) 