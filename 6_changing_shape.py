print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")

import numpy as np

rg = np.random.default_rng(1)

A = np.floor(10*rg.random((3, 4)))
print("A: \n", A)
print("\nShape of A: ", A.shape)

print("\nFirst Flatten the matrix A with ravel()")
print("Flattened A with ravel(): \n", A.ravel())

print("\nNow reshape A with reshape()")
print("Reshaped A with reshape(): \n", A.reshape(2, 6))

print("\nWe can have the transpose of A with: 'T'")
print("Shape of A is: {}\nShape of the transpose is: {}".format(A.shape, A.T.shape))
print("Transpose of A: \n", A.T)

print("-------------------------------Modifying with resize()-------------------------------")
A.resize((2, 6))
print("Resized A: \n", A)