print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")

import numpy as np

C = np.array([[[0,  1,  2], [10, 12, 13]],
              [[100, 101, 102], [110, 112, 113]]])
print("C: \n", C)

print("\nShape of C: ", C.shape)
print("\nFirst of C: \n", C[0, ...])
print("\nSecond of C: \n", C[1, ...])
print("\nLast parts of C: \n", C[..., 2])

print("\nEach element of C: \n")
for i in C.flat:
    print(i)
