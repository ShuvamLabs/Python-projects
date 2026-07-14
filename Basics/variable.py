# PYTHON VARIABLES AND DATA TYPES

# Integer (int)
# Stores whole numbers
age = 21
marks = 95
temperature = -10
print(age)
print(type(age))

# Float (float)
# Stores decimal numbers
height = 5.9
price = 199.99
pi = 3.14159
print(height)
print(type(height))

# String (str)
# Stores text (single, double, or triple quotes)
name = "Shuvam"
college = 'ABC College'
paragraph = """Python is an easy
and powerful programming language."""
print(name)
print(type(name))

# Boolean (bool)
# Stores only True or False
is_student = True
is_logged_in = False
print(is_student)
print(type(is_student))

# Complex Number (complex)
# Used in scientific and mathematical calculations
z = 4 + 3j
print(z)
print(type(z))

# TYPE CASTING
# Converting one data type into another


# String to Integer
num = "100"
num_int = int(num)

# Integer to Float
value = 25
value_float = float(value)
# Float to Integer (decimal part is removed)

pi = 3.14
pi_int = int(pi)
# Integer to String

roll = 101
roll_str = str(roll)
# Integer to Boolean

x = 5
bool_x = bool(x)      # True (any non-zero number)
# Zero to Boolean

y = 0
bool_y = bool(y)      # False

print(num_int, type(num_int))
print(value_float, type(value_float))
print(pi_int, type(pi_int))
print(roll_str, type(roll_str))
print(bool_x, type(bool_x))
print(bool_y, type(bool_y))

# TAKING USER INPUT
# input() always returns a STRING
name = input("Enter your name: ")
print(name)
print(type(name))

# Taking integer input
age = int(input("Enter your age: "))
print(age)
print(type(age))

# Taking float input
salary = float(input("Enter your salary: "))
print(salary)
print(type(salary))

# MULTIPLE VARIABLE ASSIGNMENT
a, b, c = 10, 20, 30
print(a, b, c)
# Assigning the same value to multiple variables
x = y = z = 100
print(x, y, z)

# VARIABLE NAMING RULES
student_name = "Rahul"      # Valid
_marks = 95                 # Valid
salary2 = 50000             # Valid
# Invalid variable names (Do NOT use)
# 2marks = 95
# first-name = "John"
# class = "Python"   # 'class' is a keyword

# CHECKING VARIABLE TYPE
number = 10
print(type(number))
text = "Python"
print(type(text))
decimal = 10.5
print(type(decimal))
flag = True
print(type(flag))

# DELETING A VARIABLE
temp = 500
print(temp)
del temp
# print(temp)    # This will raise NameError
