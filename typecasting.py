# # TypeCasting
#
# The process of converting a variable from one data type to another
#
# str(), int(), float(), bool()

name = "Bro code"
noName = ""
age = 25
gpa = 3.2
is_student = True

gpa = int(gpa)
print(f"{name} is {gpa}")
print(type(gpa))

age = float(age)
print(f"{name} is {age}")
print(type(age))

# for boolean
print("is name is there: ", bool(name))
print("is name is there: ", bool(noName))
