import math

# Addition (+ or +=) Used to increment a variable.
friends = 0
friends += 1
print(friends)

# Subtraction (- or -=) Used to decrement a variable.
friends = 0
friends -= 2
print(friends)

# Multiplication (* or *=): Used to multiply a variable.

friends = 5
friends *= 3
print(friends)

# Division (/ or /=) : Used to divide a variable, resulting in a float.

friends = 5
friends /= 2
print(friends)

# Exponentiation (** or **=) : Used to raise a variable to a power.

friends = 5
friends **= 2
print(friends)

# Modulus (%) : Gives the remainder of a division.

friends = 10
remainder = friends % 3
print(remainder)

# Maths
x = 3.14
y = -4
z =5

# result = round(x) #output =  3
# result = abs(y) # output = 4
# result = pow(z, 3) # output = 125
#result = max(x, y, z) # output = 5
#result = min(x, y, z) # output = -4
#result = math.sqrt(z) # output = 25 // Squaring function
#result = math.ceil(9.1) # output = 25 // round up function
result = math.floor(9.1) # output = 25 // round down function


print("Result: ", result)

print("Printing pi: ", math.pi)
print("Printing e: ", math.e)



radius = int(input("Enter the radius of circle: "))
circumference = 2 * math.pi * radius
print("Circumference: ", round(circumference, 2), "cm")