num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
index = int(input("Enter index: "))

row_index = index // num_cols
col_index = index - (row_index * num_cols)
print(f"({row_index}, {col_index})")
