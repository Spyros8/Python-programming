dim1_length = int(input("Enter dimension 1 length: "))
dim2_length = int(input("Enter dimension 2 length: "))
dim3_length = int(input("Enter dimension 3 length: "))
index = int(input("Enter index: "))

dim1_index = index // (dim2_length * dim3_length)

dim2_index = (index - (dim1_index * dim2_length * dim3_length)) // dim3_length

dim3_index = (index 
             - (dim1_index * dim2_length * dim3_length) 
             - (dim2_index * dim3_length))
             
print(f"({dim1_index}, {dim2_index}, {dim3_index})")
