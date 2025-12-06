# Sample data structures
sample_list = [10, 20, 30, 40, 50, 60]
sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
sample_tuple = (100, 200, 300, 400, 500)
sample_set = {5, 10, 15, 20, 25}


print("\n" + "="*60)
print("FUNCTIONS - ALL CONCEPTS")
print("="*60 + "\n")

# ===== BASIC FUNCTIONS =====
print("--- BASIC FUNCTIONS ---\n")

# 1. Simple function with no parameters, no return
def greet():
    print("Hello, World!")

print("1. No parameters, no return:")
greet()
print()

# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

print("2. With parameters:")
greet_person("Alice")
print()

# 3. Function with return value
def add(a, b):
    return a + b

print("3. With return value:")
result = add(5, 3)
print(f"5 + 3 = {result}")
print()

# 4. Function with multiple return values (returns tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)

print("4. Multiple return values:")
minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")
print()

# 5. Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print("5. Default parameters:")
print(f"power(3) = {power(3)}")  # Uses default exponent=2
print(f"power(3, 3) = {power(3, 3)}")  # Override default
print()

# ===== PARAMETER TYPES =====
print("--- PARAMETER TYPES ---\n")

# 6. Positional arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

print("6. Positional arguments:")
describe_pet("dog", "Buddy")
print()

# 7. Keyword arguments
print("7. Keyword arguments:")
describe_pet(name="Whiskers", animal="cat")
print()

# 8. *args - Variable positional arguments
def sum_all(*args):
    return sum(args)

print("8. *args (variable positional):")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print()

# 9. **kwargs - Variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("9. **kwargs (variable keyword):")
print_info(name="Bob", age=30, city="NYC")
print()

# 10. Mixed parameters (*args and **kwargs)
def mixed_function(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print("10. Mixed parameters:")
mixed_function("Must have", 1, 2, 3, key1="value1", key2="value2")
print()

# ===== RETURN VALUES =====
print("--- RETURN VALUES ---\n")

# 11. Return None (implicit)
def no_return():
    x = 5 + 5

print("11. No return (implicit None):")
result = no_return()
print(f"Result: {result}")
print()

# 12. Return None (explicit)
def explicit_none():
    return None

print("12. Explicit None return:")
result = explicit_none()
print(f"Result: {result}")
print()

# 13. Early return (conditional)
def check_positive(number):
    if number <= 0:
        return "Not positive"
    return "Positive"

print("13. Early return:")
print(f"check_positive(5) = {check_positive(5)}")
print(f"check_positive(-3) = {check_positive(-3)}")
print()

# 14. Return different types
def flexible_return(mode):
    if mode == "int":
        return 42
    elif mode == "str":
        return "Hello"
    elif mode == "list":
        return [1, 2, 3]
    elif mode == "dict":
        return {"key": "value"}
    else:
        return None

print("14. Return different types:")
print(f"flexible_return('int') = {flexible_return('int')}")
print(f"flexible_return('list') = {flexible_return('list')}")
print()

# 15. Return function (functions are first-class objects)
def get_operation(op):
    def add(a, b):
        return a + b
    def multiply(a, b):
        return a * b
    
    if op == "add":
        return add
    else:
        return multiply

print("15. Return a function:")
operation = get_operation("add")
print(f"operation(3, 4) = {operation(3, 4)}")
print()

# ===== ADVANCED CONCEPTS =====
print("--- ADVANCED CONCEPTS ---\n")

# 16. Lambda function (anonymous function)
print("16. Lambda function:")
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")
add_lambda = lambda a, b: a + b
print(f"add_lambda(3, 7) = {add_lambda(3, 7)}")
print()

# 17. Function with mutable default argument (CAREFUL!)
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print("17. Mutable default (safe way):")
print(f"add_to_list('a') = {add_to_list('a')}")
print(f"add_to_list('b') = {add_to_list('b')}")
print()

# 18. Function as parameter (callback)
def apply_operation(func, x, y):
    return func(x, y)

print("18. Function as parameter:")
print(f"apply_operation(add, 10, 5) = {apply_operation(add, 10, 5)}")
print(f"apply_operation(lambda a, b: a * b, 10, 5) = {apply_operation(lambda a, b: a * b, 10, 5)}")
print()

# 19. Nested functions (closure)
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print("19. Nested functions (closure):")
add_5 = outer_function(5)
print(f"add_5(10) = {add_5(10)}")
print()

import time
# 20. Decorator function
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()          # start time
        result = func(*args, **kwargs)
        end = time.time()            # end time
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def say_hello():
    print("Hello!")

print("20. Decorator:")
say_hello()
print()

# 21. Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("21. Recursive function:")
print(f"factorial(5) = {factorial(5)}")
print()

# 22. Type hints (Python 3.5+)
#type hint is just for humans and IDEs
#to enforce tpyes you'll need to use libraries
def typed_function(name: str, age: int) -> str:
    return f"{name} is {age} years old"

print("22. Type hints:")
print(typed_function("Charlie", 25))
print()


# 23. Positional-only parameters (Python 3.8+)
def pos_only(a, b, /):
    return a + b

print("23. Positional-only (/):")
print(f"pos_only(3, 5) = {pos_only(3, 5)}")
# pos_only(a=3, b=5) would raise an error
print()

# 24. Keyword-only parameters
def keyword_only(*, name, age):
    return f"{name} is {age}"

print("24. Keyword-only (*):")
print(keyword_only(name="Diana", age=28))
# keyword_only("Diana", 28) would raise an error
print()

# 25. Docstrings
def documented_function(x, y):
    """
    This function adds two numbers.
    
    Parameters:
    x (int/float): First number
    y (int/float): Second number
    
    Returns:
    int/float: Sum of x and y
    """
    return x + y

print("25. Docstrings:")
print(documented_function(3, 4))
print(f"Docstring: {documented_function.__doc__}")
print()
