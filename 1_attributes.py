print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

print("The nd array as A: \n", a)

print("Dimension:", a.ndim)  # The numver of axes (dimensions) of the array

print("Shape: ", a.shape)   # The dimensions of the array

print("Size: ", a.size)   # Total number of elements in the array

print("Type: ", a.dtype)    # Type of the elements in the array

print("Item size: ", a.itemsize)    # The size in bytes of each element of the array

print("The data: ", a.data)     # Buffer containing actual elements of the array

######################
# EXAMPLE
######################

my_array = np.arange(15).reshape(3, 5)

print("My Array: \n", my_array)
print("The Shape of the array: ", my_array.shape)
print("The dimension of the array: ", my_array.ndim)
print("Name of the type of the array: ", my_array.dtype.name)
print("Item size of the array: ", my_array.itemsize)
print("Size of the array: ", my_array.size)
print("Type of this array: ", type(my_array))