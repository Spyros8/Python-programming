n = int(input("Please enter a number: "))
x = 0
while x <= n:
    if abs(x*x - n) < 0.00001:
        print(x)
        break

    x = x + 0.0001

print("Exiting program...")