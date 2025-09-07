def is_palindrome(value):
    s = str(value)
    return s == s[::-1]

S = input("Enter a string or number: ")

if is_palindrome(S):
    print(f"{S} is a palindrome.")
else:
    print(f"{S} is not a palindrome.")
