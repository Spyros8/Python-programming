last_number = int(input("Please enter an integer: "))

n = 2
while n <= last_number:
    divisor = 2
    is_prime_number = True

    while divisor < n:
        if n % divisor == 0:
            is_prime_number = False
            break
        else:
            divisor = divisor + 1

    if is_prime_number:
        print(n)
    
    n = n + 1
