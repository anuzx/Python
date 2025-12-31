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



#linspace -> divides a range into equal intervals ; eg: np.linspace(0,10,5)-> start from 0 end at 10 and 5 element array

#arange -> generates values with a fixed step size ; eg: np.arange(0,10,2)->[0,2,4,6,8]

