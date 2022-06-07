""" Debugging exercise.

This version fixes the code, but has also been rewritten to be more concise and intuitive.

Author: Josiah Wang
"""

num = int(input("Enter an integer: "))

# check whether the number is even
is_num_even = (num % 2 == 0)

total = 0
current_num = 1

# go through numbers from 1 to num
while current_num <= num:
    # check whether current number is even
    is_current_num_even = (current_num % 2 == 0)

    # add current number to total
    # if both num and current_num have the same evenness
    if is_num_even == is_current_num_even:
        total = total + current_num

    current_num = current_num + 1

print(total)
