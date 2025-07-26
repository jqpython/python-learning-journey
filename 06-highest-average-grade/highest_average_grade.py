def highest_average_grade (students):
    if not students:
        return None

    max_avg = -1
    top_student = None

    for student in students:
        grades = student["Grades"]
        print(grades)
        names =student["name"]
        print(names)
        average = sum(grades)/ len(grades)
        if average > max_avg:
            max_avg = average
            top_student = student["name"]

    return top_student

students = [{"name": "Alice", "Grades": [90, 85, 95]},{"name": "Bob", "Grades": [80, 85, 90]},{"name": "Charlie", "Grades": [70, 75, 80]}]

print(highest_average_grade(students))
