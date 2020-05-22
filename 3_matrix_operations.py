print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical Univesity 
İstanbul, Turkey 

""")
import numpy as np

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print("A: \n", A)
print("B: \n", B)

print("--------------------------------- Element Wise Product: '*' ---------------------------------")

print("A*B= \n", A*B)

print("--------------------------------- Matrix Product: '@' ---------------------------------")

print("A x B = \n", A@B)

print("--------------------------------- Matrix Product: 'dot()' ---------------------------------")

print("A x B = \n", A.dot(B))
print("*********  OR  **********")
print("B x A = \n", B.dot(A))