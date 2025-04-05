student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

# total create the above "sum" function ourselves

total_score = 0

for score in student_scores:
    total_score += score

print(total_score)

print(range(1, 10))

# to create max function

max_num = 0

for num in student_scores:
    if num > max_num:
        max_num = num
print(max_num)
