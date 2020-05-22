print("""

İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 

""")

import numpy as np
import matplotlib.pyplot as plt

rg = np.random.default_rng(1)

mu, sigma = 2, 0.5

print("mean: {}, and variance: {}".format(mu, sigma**2))


print("\n------------------ Draw random samples from a normal (Gaussian) distribution with np.normal----------")

v = rg.normal(mu, sigma, 10000)
print("\nv: \n", v)
print("\nShape of v: ", v.shape)

print("\n-------------------- Plotting ------------------------------------")


(n, bins) = np.histogram(v, bins=50, density=True)
plt.plot(0.5*(bins[1:]+bins[:-1]), n, color='red')
plt.hist(v, bins=50, density=1, color='blue')
plt.title("The Histogram")
plt.show()