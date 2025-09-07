with open("students.txt", "r") as file:
    print("Student Names:")
    for line in file:
        print(line.strip())