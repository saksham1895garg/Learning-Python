# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount cannot be less than zero")
    else:
        break
while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("rate amount cannot be less than zero")
    else:
        break
while True:
    time = float(input("Enter the time amount: "))
    if time <= 0:
        print("time amount cannot be less than zero")
    else:
        break

total = principle * pow((1+(rate/100)), time)

print("Your total amount is: ", total)
