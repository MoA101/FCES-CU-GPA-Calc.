grade_point_map = {
    'A+': 4.0,
    'A': 3.7,
    'B+': 3.4,
    'B': 3.0,
    'C+': 2.7,
}

credit_hours_per_course = 3

num_courses = int(input("Enter the number of courses: "))

total_points = 0
total_credits = num_courses * credit_hours_per_course

for i in range(num_courses):
    print(f"\nCourse {i + 1}:")
    letter_grade = input("Enter your letter grade for this course (A+, A, B+, B, C+): ").strip().upper()
    
    if letter_grade in grade_point_map:
        grade_points = grade_point_map[letter_grade]
    else:
        print("Invalid grade entered. Assuming 0.0 grade points.")
        grade_points = 0.0
    
    total_points += grade_points * credit_hours_per_course

if total_credits > 0:
    gpa = total_points / total_credits
else:
    gpa = 0

print(f"\nYour GPA is: {gpa:.2f}")

     