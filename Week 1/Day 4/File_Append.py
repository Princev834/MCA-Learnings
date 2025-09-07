with open("students.txt", "a") as file:
    n = int(input("Enter how many new students to add: "))
    for i in range(n):
        name = input(f"Enter name of new student {i+1}: ")
        file.write(name + "\n")

print("New student names have been added to 'students.txt'")