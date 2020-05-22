print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")
import numpy as np

# First way

a = np.array([1, 2, 3])
print("With array command: \n", a)

# Second way
b = np.array([[1, 2], [3, 4]], dtype=complex)
print("Complex elements: \n", b)


# Array with zeros
c = np.zeros((3, 4), dtype='int')
print("Array with integer zeros: \n", c)

d = np.zeros((3, 4), dtype='float')
print("Array with float zeros: \n", d)


# 3 dimensional array with ones

e = np.ones((2, 3, 4), dtype='int')
print("3 dimensional array: \n", e)
print("Dimension of this array: ", e.ndim)
print("Shape of this 3 dimensional array: ", e.shape)


# Third way to create numpy array

f = np.arange(10, 30, 5, dtype = 'float')
print("Array with arange function: ", f)

# Creating an empty array

g = np.empty((2, 3), dtype='float', order='F')
print("An empty array with the shape 2, 3\n: ", g)

# with linspace

h = np.linspace(0, 2, 9)
print("Array with linspace: ", h)
print("The shape of linspaced array: ", h.shape)

from numpy import pi
j = np.linspace(0, 2*pi, 100)
k = np.sin(j)
print(k)


l = np.arange(0, 12).reshape(4, 3)
print("The array: ", l)
s = np.array(l<10)
print("The elemets of the l<10: \n", s)