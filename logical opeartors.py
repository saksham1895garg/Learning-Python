# logical operators = evalute multiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the conditons(not False, not True)

temp = 40
is_raining = True

if temp > 35 or temp <0 or is_raining:
    print('''Temperature is too high {"or" condition}''')
else:
    print("Temperature is ok")

if temp > 35 and is_raining:
    print("Temperature is not ok, this is for and condition")
else:
    print("Temperature is ok")
if temp > 35 and not is_raining:
    print("Temperature is not ok, this is for not condition")
else:
    print("Temperature is ok")