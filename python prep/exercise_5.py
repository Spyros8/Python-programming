int_1 = int(input("Please enter the first integer: "))
int_2 = int(input("Please enter the second integer: "))
int_3 = int(input("Please enter the third integer: "))
if int_1 > int_2 & int_1 > int_3:
    print(int_1)
elif int_2 > int_1 & int_2 > int_3:
    print(int_2)
else:
    print(int_3)	