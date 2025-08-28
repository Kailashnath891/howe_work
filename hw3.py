# 1. What is the output of print(2 ** 3 ** 2)?
# Output: 512
print(2 ** 3 ** 2)  # 2 ** (3 ** 2) = 2 ** 9 = 512

# 2. What is the output of print(2 * 3 ** 3 * 4)?
# Output: 216
print(2 * 3 ** 3 * 4)  # 3 ** 3 = 27, 2 * 27 = 54, 54 * 4 = 216

# 3. What is the output of print(10 - 4 * 2)?
# Output: 2
print(10 - 4 * 2)  # 4 * 2 = 8; 10 - 8 = 2

# 4. What is the output of the expression print(-18 // 4)?
# Output: -5
print(-18 // 4)  # -18 / 4 = -4.5, floor division rounds down to -5

# 5. What is the output of print(2 % 6)?
# Output: 2
print(2 % 6)  # Remainder when 2 is divided by 6 is 2

# 6. What is the output of the following code?
# x = 100 
# y = 50 
# Output: 50
x = 100 
y = 50 
print(x and y)  # Both are non-zero, "and" returns y

# 7. What is the value of the following Python Expression print(36 / 4)?
# Output: 9.0
print(36 / 4)  # 36 divided by 4 = 9.0

# 8. What is the output of the following code?
# var1 = 1 
# var2 = 2 
# var3 = "3" 
# Output: TypeError
# print(var1 + var2 + var3)  # Error, can't add int and str

# 9. What is the output of the following code?
# p, q, r = 10, 20, 30
# Output: 10 20 30
p, q, r = 10, 20, 30
print(p, q, r)

# 10. What is the output of the following code?
# valueOne = 5 ** 2 
# valueTwo = 5 ** 3 
# Output: 25
#         125
valueOne = 5 ** 2 
valueTwo = 5 ** 3 
print(valueOne)
print(valueTwo)

# 11. What is the output of the following code?
# var = "James" * 2 * 3 
# Output: JamesJamesJamesJamesJamesJames
var = "James" * 2 * 3  # (2*3=6), "James" * 6
print(var)

# 12. What is the output of the following?
# x = 36 / 4 * (3 + 2) * 4 + 2 
# Output: 182.0
x = 36 / 4 * (3 + 2) * 4 + 2  # 36/4=9, (3+2)=5, 9*5=45, 45*4=180, 180+2=182
print(x)

# 13. What is the data type of print(type(10))?
# Output: <class 'int'>
print(type(10))

# 14. Creating an int variable, float variable, string variable and assign the values to the above three variable names.
int_var = 25
float_var = 12.5
string_var = "Python"
print("Int value:", int_var)
print("Float value:", float_var)
print("String value:", string_var)

# 15. Create Integer number
# Roll number is: 33 
# <class 'int'> 
# 25 
# <class 'int'>
roll_number = 33
print("Roll number is:", roll_number)
print(type(roll_number))
another_integer = 25
print(another_integer)
print(type(another_integer))
