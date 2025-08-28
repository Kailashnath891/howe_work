# 1. Calculate the multiplication and sum of two numbers.
a = 10
b = 5
sum_result = a + b
product_result = a * b
print("Sum:", sum_result)
print("Product:", product_result)

# 2. Create a string made of the first, middle and last character of "Quality".
word = "Quality"
first_char = word
middle_char = word[len(word)//2]
last_char = word[-1]
new_string = first_char + middle_char + last_char
print(new_string)  # Output: 'Qit'

# Note: The expected output "Quality Thought" suggests joining full words, but if you want just the first, middle, last characters, the code above does that.

# 3. Print: "One half of 100 is 50." Use a variable for 50.
half = 50
print("One half of 100 is", half)

# 4. Calculate and explain myTotal = 4 + 2 * 8 - 6.
myTotal = 4 + 2 * 8 - 6
print(myTotal)  # Output: 14
# Explanation: Multiplication has higher precedence, so 2 * 8 = 16. Then 4 + 16 - 6 = 14.

# 5. Floor division example: myTotal = 7 // 5.
myTotal = 7 // 5
print(myTotal)  # Output: 1
# Floor division gives the quotient without remainder.

# 6. Use parentheses in myTotal = (8 + 2) * 10.
myTotal = (8 + 2) * 10
print(myTotal)  # Output: 100
# Parentheses change the order of operations.

# 7. Without parentheses: myTotal = 8 + 2 * 10.
myTotal = 8 + 2 * 10
print(myTotal)  # Output: 28
# Multiplication happens before addition.

# 8. Division with and without parentheses.
myTotal = 8 + 10 / 2
print(myTotal)  # Output: 13.0

myTotal = (8 + 10) / 2
print(myTotal)  # Output: 9.0

# 9. Using variables with arithmetic expressions.
numberOne = 16
numberTwo = 4

answer = numberOne + numberTwo
print(answer)  # Output: 20

answer = numberOne + numberTwo + 20
print(answer)  # Output: 40

answer = 10 * numberOne + (numberTwo + 20)
print(answer)  # Output: 180

answer = numberOne + 20 + numberTwo - 10
print(answer)  # Output: 30

# 10. Concatenate strings.
FirstName = "Quality"
SecondName = "Thought"
print("Full Name is:", FirstName + " " + SecondName)
# Output: Full Name is: Quality Thought
