weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds: (K or L)")


if unit == "K":
    weight = weight *2.205
    unit = "Lbs."
    valid = True
    print(f"Your weight is {round(weight, 1)}, {unit}")
elif unit == "Pounds":
    weight = weight / 2.205
    unit = "Kgs."
    valid = True
    print(f"Your weight is {round(weight, 1)}, {unit}")
else:
    print("unit is not valid")

