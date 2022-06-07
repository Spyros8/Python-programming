yr = int(input("Please enter year: "))

if yr%4 == 0 :
    print("{} is a leap year".format(yr))
else:
    print("{} is not a leap year".format(yr))