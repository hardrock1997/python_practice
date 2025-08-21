# ==============================
# Basic Data Types in Python
# ==============================

x = "Hello"
print(type(x))   # str (string)

y = 3
print(type(y))   # int (integer)

z = 4.5
print(type(z))   # float (floating point number)

a = 'c'
print(type(a))   # str (Python has no char type, single char is also a string)

b = True
print(type(b))   # bool (boolean type)

# Python is dynamically typed (variable type can change at runtime)
b = 3
print(type(b))   # int now


# ==============================
# Type Conversions
# ==============================

# User input is always taken as a string
# x = input()
# print(x, type(x))

# Explicit conversion
# x_int = int(x)   # converts string to integer
# print(type(x_int))

# y = int(input())  # directly converting input into int
# print(y, type(y))

# Convert int -> str
# y_string = str(y)
# print(y_string, type(y_string))

# Convert int -> float
# y_float = float(y)
# print(y_float)

# Falsy values in Python: "", {}, [], 0
# Truthy values: any non-empty string, list, dict, non-zero numbers
# print(bool([]), bool({}), bool(0), bool(""))     # all False
# print(bool("True"), bool("False"))               # both True


# ==============================
# Operators
# ==============================

x = "hello"
y = x
print(x, y)

# Integers, strings, bool, float → immutable objects

# Arithmetic Operators
# x = int(input())
# y = int(input())
# add = x + y
# prod = x * y
# int_div = x // y   # floor division
# div = x / y        # normal division (float result)
# diff = x - y
# rem = x % y
# exp = x ** y       # exponentiation

# print(add, prod, div, diff, int_div, type(div), type(int_div), rem, exp)

# Comparison Operators
x = 5
y = 2
print(x > y, x <= y, x == y)

s1 = "yash mundra"
s2 = "yash"
print(s1 == s2, s1 != s2, s1 < s2, s1 > s2)   # lexicographical comparison


# ==============================
# Conditional Statements
# ==============================

# Greatest of three numbers
# x = int(input())
# y = int(input())
# z = int(input())
# if x > y and x > z:
#     print("x", x)
# elif y > x and y > z:
#     print("y", y)
# else:
#     print("z", z)


# ==============================
# Loops
# ==============================

# Print even numbers till n
# n = int(input())

# for i in range(n):
#     if i % 2 == 0:
#         print(i)

# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 2
# while i <= n:
#     print(i)
#     i += 2


# ==============================
# Printing Patterns
# ==============================

# Print square of n*n stars
# n = int(input())
# j = 1
# while j <= n:
#     s = ""
#     i = 1
#     while i <= n:
#         if i < n:
#             s = s + "* "
#         else:
#             s = s + "*"
#         i += 1
#     print(s)
#     j += 1

# Print rectangle of n*m stars
# n = int(input())
# m = int(input())
# i = 1
# while i <= n:
#     s = ""
#     j = 1
#     while j <= m:
#         if j < m:
#             s += "* "
#         else:
#             s += "*"
#         j += 1
#     print(s)
#     i += 1


# ==============================
# Strings
# ==============================

s = "yash"
print(s * 3, len(s * 3))    # repeat string * 3

s = "yash"
print(s[-4], s[0], s[0:4])  # indexing and slicing

s = "yashMundra"
print(s[1:6:2])  # slice with step (from index 1 to 5, step = 2)

# find() and index()
s = "Yash"
print(s.find("as"), s.index("as"))   # both return starting index of substring

# Membership operators
s = "yash_mundra"
print("_" in s)
print("t" not in s)

# Strings are immutable
s = "Yash"
# s[3] = "XX"   ❌ Not allowed
# Instead, create a new string
s = "yash_mundra"
s = s[:4] + "___" + s[5:]
print(s)


# ==============================
# Identity & Equality
# ==============================

a = 10
print(id(a))   # memory location

# Immutable objects (strings) may point to same memory
s = "hello"
s1 = "hello"

# Mutable objects (lists) get different memory locations
a = [1, 2, 3]
b = [1, 2, 3]

print(s is s1)   # True (same memory ref for strings)
print(a is b)   # False (different memory for lists)

print(s == s1)  # True (content same)
print(a == b)   # True (content same, but memory different)
