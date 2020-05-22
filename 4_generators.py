print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")
import numpy as np

rg = np.random.default_rng(1)

A = np.ones((3, 4), dtype='int')
print("A: \n", A)

B = rg.random((3, 4))
print("\nB: \n", B)

A *= 4
print("\nMultiplying the elements of A with 4: \n", A)

B += A
print("\nAdding A to B: \n", B)


print("---------------------------------------------")
print("Max of A: ", A.max())
print("Min of A: ", A.min())
print("Sum of A: ", A.sum())


print("---------------------------------------------")
print("Max of B: ", B.max())
print("Min of B: ", B.min())
print("Sum of B: ", B.sum())
