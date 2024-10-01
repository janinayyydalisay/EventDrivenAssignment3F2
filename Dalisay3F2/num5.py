students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]

highest_score = 0
highest_scorer = []

for student in students_scores:
    if student[1] > highest_score:
        highest_score = student[1]
        highest_scorer = []  # Reset the list if a higher score is found
        highest_scorer.append(student[0])

print("Student with the highest score:", highest_scorer[0], "Score:", highest_score)
