#1
from functools import reduce

def multiply(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

# Example:
list = [2, 3, 4, 5]
result = multiply(list)
print(result)

#2
def upper_lower(s):
    u_count = sum(1 for char in s if char.isupper())
    l_count = sum(1 for char in s if char.islower())
    return u_count, l_count

# Example:
s = "Gauhar"
upper, lower = upper_lower(s)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

#3
def is_palindrome(s):
    reverse = s[::-1]
    return s == reverse

# Example:
s = "level"
if is_palindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")

#4
import time
import math

def s(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

# Example:
n = 25100
delay_ms = 2123
output = s(n, delay_ms)
print(f"Square root of {n} after {delay_ms} milliseconds is {output}")

#5
def true(t):
    return all(t)

# Example:
t = (True, False, False, True)
result = true(t)
print(f"All elements are True: {result}")