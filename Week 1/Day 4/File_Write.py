with open("students.txt", "w") as file:
    n = int(input("Enter how many students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        file.write(name + "\n")

print("Student names have been stored in 'students.txt'")