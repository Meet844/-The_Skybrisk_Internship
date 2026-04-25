# List Example
numbers = [1, 2, 3, 4, 5]

# Sum of squares using list comprehension
squares = [x*x for x in numbers]
print("Squares:", squares)

# Filtering even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# Dictionary Example
student = {"name": "Meet", "age": 21}
print("Student:", student)

# Function Example
def add(a, b):
    return a + b

print("Addition using function:", add(5, 3))

# Data Cleaning (Remove duplicates)
data = [1, 2, 2, 3, 4, 4, 5]
clean_data = list(set(data))
print("Clean Data:", clean_data)