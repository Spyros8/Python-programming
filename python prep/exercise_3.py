
dim1_length = int(input("Enter dimension 1 length: "))
dim2_length = int(input("Enter dimension 2 length: "))
dim3_length = int(input("Enter dimension 3 length: "))
dim1_index = int(input("Enter index for dimension 1: "))
dim2_index = int(input("Enter index for dimension 2: "))
dim3_index = int(input("Enter index for dimension 3: "))

index = (dim1_index * dim2_length * dim3_length 
        + dim2_index * dim3_length 
        + dim3_index)
print(index)
