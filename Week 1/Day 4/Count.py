with open("students.txt", "r") as file:
    lines = file.readlines()
    count = len(lines)

print(f"Total number of students: {count}")