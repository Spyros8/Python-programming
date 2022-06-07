initial_rows = int(input("Enter an integer: "))
row_count = 1
updated_rows = 0

while row_count <= (initial_rows):
    print('*' + '*'*(updated_rows))
    updated_rows = updated_rows + 2
    row_count = row_count + 1