price1 = 3.14159
price2 = -987123.65
price3 = 123223.34


# .2f === two decimals

print(f"Price1 is {price1:.2f}")
print(f"Price2 is {price2:.2f}")
print(f"Price2 is {price2:.2f}")

# :10 is for space before and :010 is do this all number will pe 0 padded

print(f"Price1 is {price1:10}")
print(f"Price2 is {price2:10}")
print(f"Price2 is {price2:10}")

# :<10 for space after
print(f"Price1 is {price1:<10}")
print(f"Price2 is {price2:<10}")
print(f"Price2 is {price2:<10}")

# :^10 this will center the number
print(f"Price1 is {price1:^10}")
print(f"Price2 is {price2:^10}")
print(f"Price2 is {price2:^10}")

# :+ for print sign of number
print(f"Price1 is {price1:+}")
print(f"Price2 is {price2:+}")
print(f"Price2 is {price2:+}")
#, for print commas btw number
print(f"Price1 is {price1:,}")
print(f"Price2 is {price2:,}")
print(f"Price2 is {price2:,}")



