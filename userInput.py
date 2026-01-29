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