print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")

import numpy as np

A = np.arange(12)**2
print("A: ", A)

B = np.array([1, 1, 3, 8, 5])
print("\nB: ", B)

print("B indexes in A as A[B]: ", A[B])

C = np.array([[3, 4], [9, 7]])
print("\nC: \n", C)

print("\nC indexes in A as A[C]: \n", A[C])

print("\n-------------------------- Another Examples --------------------------")

time = np.linspace(20, 145, 5)
print("\nTime: ", time)

data = np.sin((np.arange(20))).reshape(5, 4)
print("\nData: \n", data)

print("\nWe can find the indexes of the max elements.")

ind = data.argmax(axis=0)
print("\nIndices of Max values: ", ind)

time_max = time[ind]
print(time_max)

