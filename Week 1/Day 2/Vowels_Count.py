def count_vowels(text):
    vowels = "aeiouAEIOU" 
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(string)}")