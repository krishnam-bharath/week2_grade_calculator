# Week 2 - Student Grade Calculator

def calculate_grade(marks):
    """Returns grade and message based on marks."""
    if 90 <= marks <= 100:
        return "A", "Excellent! Outstanding performance! 🌟"
    elif 80 <= marks < 90:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks < 80:
        return "C", "Good job! You can do even better! 🙂"
    elif 60 <= marks < 70:
        return "D", "Work harder! You can improve! 💪"
    else:
        return "F", "Don't worry! Keep practicing and you'll improve! ❤️"


# MAIN PROGRAM
print("📘 Student Grade Calculator\n")

student_name = input("Enter student name: ")

# MARKS INPUT VALIDATION USING WHILE LOOP
while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid input. Marks must be between 0 and 100.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", student_name.upper(), ":")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
