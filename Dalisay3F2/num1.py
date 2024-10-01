students = ['John', 'Maria', 'David', 'Samantha']
selected_student = []

while True:
    try:
        index = int(input("Enter an index (0-3): "))
        if 0 <= index < len(students):
            selected_student.append(students[index])
            print("Student at index", index, ":", selected_student[0])
            break
        else:
            print("Invalid index. Please enter an integer between 0 and 3.")
    except ValueError:
        print("Please enter a valid integer.")
