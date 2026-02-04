student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 84, 89]
max_scores=0
for scores in student_scores:
    if scores>max_scores:
        max_scores=scores

print(f"Highest score is {max_scores}")