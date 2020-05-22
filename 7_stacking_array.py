print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")

import numpy as np

rg = np.random.default_rng(1)

A = np.floor(10*rg.random((3, 3)))
print("A: \n", A)

B = np.floor(10*rg.random((3, 3)))
print("\nB: \n", B)

C = np.vstack((A, B))
print("\nVertical stacking with np.vtstack: \n", C)

D = np.hstack((A, B))
print("\nHorizontal stacking with np.hstack: \n", D)

print("\nSame result can be handled with 'column_stack'")

E = np.column_stack((A, B))
print("\nStacking with 'column_stack': \n", E)

print("--------------------- Another Example -------------------")

G = np.array([4., 2.])
H = np.array([3., 8.])
print("\nG: ", G)
print("\nH: ", H)

J = np.column_stack((G, H))
print("\nStacked G and H: \n", J)

K = np.vstack((G, H))
print("\nStacking G and H with 'vstack': \n", K)

S = np.hstack((G, H))
print("\nStacking G and H with 'hstack': \n", S)

from numpy import newaxis
print("\nG: ", G,"\nShape: ",G.shape)

E = G[:, newaxis]
print("\nAdding a new axis to G: \n", E,"\nShape: ", E.shape)

