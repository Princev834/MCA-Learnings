def second_largest(arr):
    if len(arr) < 2:
        return None

    unique_arr = list(set(arr))

    if len(unique_arr) < 2:
        return None 

    unique_arr.sort(reverse=True)  
    return unique_arr[1] 

numbers = [10, 20, 4, 45, 99, 99, 45]
print("List:", numbers)

result = second_largest(numbers)

if result is not None:
    print("Second largest element is:", result)
else:
    print("List does not have a second largest element")