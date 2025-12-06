# Sample data structures
sample_list = [10, 20, 30, 40, 50, 60]
sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
sample_tuple = (100, 200, 300, 400, 500)
sample_set = {5, 10, 15, 20, 25}

# ===== ITERATING LISTS =====
print("--- ITERATING LISTS ---\n")

# 1. Basic iteration
print("1. Basic iteration:")
for item in sample_list:
    print(item, end=" ")
print("\n")

# 2. Iteration with index using enumerate()
print("2. With index (enumerate):")
for index, item in enumerate(sample_list):
    print(f"Index {index}: {item}")
print()

# 3. Iteration with custom start index
print("3. Enumerate with start index 1:")
for index, item in enumerate(sample_list, start=1):
    print(f"Item {index}: {item}")
print()

# 4. Iterate every 2nd element (step by 2)
print("4. Every 2nd element [::2]:")
for item in sample_list[::2]:
    print(item, end=" ")
print("\n")

# 5. Iterate every 3rd element
print("5. Every 3rd element [::3]:")
for item in sample_list[::3]:
    print(item, end=" ")
print("\n")

# 6. Reverse iteration
print("6. Reverse iteration [::-1]:")
for item in sample_list[::-1]:
    print(item, end=" ")
print("\n")


# 8. Iteration using range and length
print("8. Using range(len()):")
for i in range(len(sample_list)):
    print(f"sample_list[{i}] = {sample_list[i]}")
print()

# 9. Iterate specific range of indices
print("9. Specific range [1:4]:")
for item in sample_list[1:4]:
    print(item, end=" ")
print("\n")

# 10. While loop iteration
print("10. While loop:")
i = 0
while i < len(sample_list):
    print(sample_list[i], end=" ")
    i += 1
print("\n")

# ===== ITERATING DICTIONARIES =====
print("\n--- ITERATING DICTIONARIES ---\n")

# 11. Iterate keys (default)
print("11. Iterate keys (default):")
for key in sample_dict:
    print(key, end=" ")
print("\n")

# 12. Iterate keys explicitly
print("12. Iterate keys with .keys():")
for key in sample_dict.keys():
    print(key, end=" ")
print("\n")

# 13. Iterate values
print("13. Iterate values with .values():")
for value in sample_dict.values():
    print(value, end=" ")
print("\n")

# 14. Iterate key-value pairs
print("14. Iterate key-value pairs with .items():")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
print()

# 15. Iterate with enumeration
print("15. Dictionary with enumerate:")
for index, (key, value) in enumerate(sample_dict.items()):
    print(f"{index}. {key} = {value}")
print()

# ===== ITERATING TUPLES =====
print("\n--- ITERATING TUPLES ---\n")

# 16. Basic tuple iteration
print("16. Basic tuple iteration:")
for item in sample_tuple:
    print(item, end=" ")
print("\n")

# 17. Tuple with index
print("17. Tuple with index:")
for index, item in enumerate(sample_tuple):
    print(f"Index {index}: {item}")
print()

# 18. Every 2nd element in tuple
print("18. Every 2nd element [::2]:")
for item in sample_tuple[::2]:
    print(item, end=" ")
print("\n")

# 19. Unpacking tuple in loop
print("19. Unpacking tuples in list:")
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in tuple_list:
    print(f"Number: {num}, Letter: {letter}")
print()

# ===== ITERATING SETS =====
print("\n--- ITERATING SETS ---\n")

# 20. Basic set iteration (unordered)
print("20. Basic set iteration:")
for item in sample_set:
    print(item, end=" ")
print("\n")

# 21. Sorted set iteration
print("21. Sorted set iteration:")
for item in sorted(sample_set):
    print(item, end=" ")
print("\n")

# ===== ADVANCED ITERATION TECHNIQUES =====
print("\n--- ADVANCED TECHNIQUES ---\n")

# 22. List comprehension (creating new list while iterating)
print("22. List comprehension - squares:")
squares = [x**2 for x in sample_list]
print(squares)
print()

# 23. Zip - iterate multiple lists together
print("23. Zip - iterate two lists together:")
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for letter, number in zip(list1, list2):
    print(f"{letter}: {number}")
print()

# 24. Filter while iterating
print("24. Filter - only values > 30:")
for item in sample_list:
    if item > 30:
        print(item, end=" ")
print("\n")

# 25. Nested iteration
print("25. Nested iteration:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
print()