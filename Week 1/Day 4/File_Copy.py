source_file = "students.txt"

destination_file = "students_copy.txt"

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line)

print(f"Contents of '{source_file}' have been copied into '{destination_file}'")