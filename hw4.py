# 1. Python swapping means interchanging the values of two variables.
# Example: if x=10 and y=5, after swapping x=5 and y=10.

# 2. Numbers in Python data types:
# int: integers without decimal, e.g., 3, 855
# float: decimal numbers, e.g., 2.564728
# complex: numbers with real and imaginary parts, e.g., 2 + 3j, 6j

# 3. Output of the code:
x = 6
y = 2
print(x ** y)  # 6 raised to power 2 = 36
print(x // y)  # floor division: 6 // 2 = 3

# 4. Bitwise operators with a=4 (100 binary), b=11 (1011 binary):
a = 4
b = 11
print(a | b)   # bitwise OR: 100 | 1011 = 1111 (decimal 15)
print(a >> 2)  # right shift a by 2 bits: 100 >> 2 = 1 (decimal 1)

# 5. Output of the assignment operator:
# y = 10
# x = y += 2  # This is a syntax error in Python; can't assign from augmented assignment

# 6. Output of print(2 * 3 ** 3 * 4):
print(2 * 3 ** 3 * 4)  # 3**3=27, 2*27=54, 54*4=216

# 7. Output of print(10 - 4 * 2)
print(10 - 4 * 2)  # 4*2=8, 10-8=2

# 8. Output of print(-18 // 4)
print(-18 // 4)  # -18/4 = -4.5 floor division rounds down to -5

# 9. Output of the following Python code with condition:
x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)  # 10**2=100, not >100, so condition False, nothing printed

# 10. Output of print(x and y)
x = 100
y = 50
print(x and y)  # both non-zero, 'and' returns y -> 50

# 11. Output of type(range(5))
print(type(range(5)))  # <class 'range'>

# 12. Data type of print(type(10))
print(type(10))  # <class 'int'>
