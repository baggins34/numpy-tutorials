print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")

import numpy as np

rg = np.random.default_rng(1)

A = np.floor(10*rg.random((2, 12)))
print("A: \n", A)
print("\nShape of A: ", A.shape)

print("-----------------  Split matrix A into 3 --------------------")

B = np.array(np.hsplit(A, 3))
print("\nB: \n", B)
print("\nShape of A: {}, and Shape of B: {}".format(A.shape, B.shape))

print("\n--------------------------  Split after 3rd and 4th column -----------------")

C = np.hsplit(A, (3, 4))
print("\nC: \n", C)