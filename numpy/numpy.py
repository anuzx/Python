import numpy as np

array = np.array([1,2,3,4,5])

#basic operations
print("Array: " , array)
print("Mean:" , np.mean(array))
print("Sum:", np.sum(array))

#create 2D array (matrix)

matrix = np.array[[1,2,3],[4,5,6]]

#matrix operations

print("Matrix:\n" , matrix)
print("Transpose:\n" , np.transpose(matrix))
print("element wise addition:\n" , matrix+10) #10 will be added in each element of matrix
