# Python Recap: Data Types

# 1. Integer (int) - Whole numbers
my_int = 42
print(f"Integer: {my_int}, Type: {type(my_int)}")

# 2. Float (float) - Decimal numbers
my_float = 3.14
print(f"Float: {my_float}, Type: {type(my_float)}")

# 3. String (str) - Text data
my_string = "Hello, Python!"
print(f"String: {my_string}, Type: {type(my_string)}")

# 4. Boolean (bool) - True or False
my_bool = True
print(f"Boolean: {my_bool}, Type: {type(my_bool)}")

# 5. List (list) - Ordered, mutable collection
my_list = [1, 2, 3, "four", 5.0]
print(f"List: {my_list}, Type: {type(my_list)}")

# 6. Tuple (tuple) - Ordered, immutable collection
my_tuple = (10, 20, 30, "forty")
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")

# 7. Set (set) - Unordered collection of unique items
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set}, Type: {type(my_set)}")

# 8. Dictionary (dict) - Key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Dictionary: {my_dict}, Type: {type(my_dict)}")

# 9. NoneType (None) - Represents absence of value
# Don't use mutable data as default function arguments
my_none = None
print(f"NoneType: {my_none}, Type: {type(my_none)}")

# 10. Complex (complex) - Complex numbers
my_complex = 3 + 4j
print(f"Complex: {my_complex}, Type: {type(my_complex)}")

# 11. Bytes (bytes) - Immutable sequence of bytes
my_bytes = b"Hello"
print(f"Bytes: {my_bytes}, Type: {type(my_bytes)}")

# 12. Bytearray (bytearray) - Mutable sequence of bytes
my_bytearray = bytearray(b"Hello")
print(f"Bytearray: {my_bytearray}, Type: {type(my_bytearray)}")

# 13. Frozenset (frozenset) - Immutable set
my_frozenset = frozenset([1, 2, 3, 4])
print(f"Frozenset: {my_frozenset}, Type: {type(my_frozenset)}")

# 14. Range (range) - Sequence of numbers
my_range = range(5)
print(f"Range: {my_range}, Type: {type(my_range)}")
print(f"Range as list: {list(my_range)}")