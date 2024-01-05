numbers = [10, 5, 8, 20, 3, 15, 7, 1, 25]

# Find the three highest numbers
highest_numbers = sorted(numbers, reverse=True)[:3]

# Find the lowest number
lowest_number = min(numbers)

print("Three Highest Numbers:", highest_numbers)
print("Lowest Number:", lowest_number)
