
#Read integer function

def read_integer():
#Note make it clearer by defining variable end outputting the int type of the variable
    return int(input("Please enter an integer: "))    

    
#Abstracting divisibility statement
def is_divisible_by(number, divisor):
    return number % divisor == 0
    
       
#check if its a prime number function
def is_prime_number(number):
    if number <= 1:
        return False
        
        
    divisor = 2

    while divisor < number:
        if is_divisible_by(number, divisor):
            return False
        else:
            divisor += divisor
    return True
         

n = read_integer()

if is_prime_number(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")