#%%


#%%


unit = input("is this temperature in Celsius or Fahrenheit? (F or C): ")
temp = float(input("Enter the temperature: "))

if unit == "F":
    temp = round((9 * temp / 5) + 32, 1)
    print("Temp: ", temp)
elif unit == "C":
    temp = round((9*temp)/5+32, 1)
    print("Temperature in Celsius: ", temp)
else:
    print(f"{unit} is an invalid unit of temperature")