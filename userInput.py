# # Input From User
#
# A function that prompts the user to enter data
#
#  Returns the enetered data

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
# or age = int(input(how old are you: "))
age = age + 1

print("Your name is: ", name)
print("Your age is: ", age)


# exercise 1, Calculate Area calc
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = length * width

print(area)

# Exercise 2 Shopping cart Program
item = input("What item you want to buy: ")
price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))
total = price * quantity

print("your total cart is: ", total)
