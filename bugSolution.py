def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 3.0

my_list = [1, 2, 3, 4, 'a']
average = calculate_average(my_list)
print(f"The average is: {average}") # Output: 2.5