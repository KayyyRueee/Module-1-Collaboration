# Kay Hutchinson
# Did I Make It? (Title for app)
# This program determines if a student has made the dean's list or honor roll based on their GPA.


while True:
    student_name = input("Enter the student's last name: ")
    if student_name == "ZZZ":
        break
    student_gpa = float(input("Enter the student's grade: "))
    if student_gpa >= 3.5:
        print(f"{student_name} has made the dean's list.")
    elif student_gpa >= 3.25:
        print(f"{student_name} has made the honor roll.")
    else:
        print(f"{student_name} is not on the dean's list or honor roll.")

