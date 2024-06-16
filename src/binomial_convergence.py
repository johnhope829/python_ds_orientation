import matplotlib.pyplot as plt
import numpy as np
import os

rng = np.random.default_rng()
binomial1 = rng.binomial(1,0.5,1000)
binomial2 = rng.binomial(10,0.5,1000)
binomial3 = rng.binomial(100,0.5,1000)
binomial4 = rng.binomial(1000,0.5,1000)
binomial5 = rng.binomial(10000,0.5,1000)
binomial6 = rng.binomial(100000,0.5,1000)

fig, axes = plt.subplots(3,2, constrained_layout=True)

plt.subplot(3,2,1)
plt.hist(binomial1, 10, density=True, color='green', edgecolor='black')
plt.title('n = 1')

plt.subplot(3,2,2)
plt.hist(binomial2, 10, density=True, color='green', edgecolor='black')
plt.title('n = 10')

plt.subplot(3,2,3)
plt.hist(binomial3, 10, density=True, color='green', edgecolor='black')
plt.title('n = 100')

plt.subplot(3,2,4)
plt.hist(binomial4, 10, density=True, color='green', edgecolor='black')
plt.title('n = 1,000')

plt.subplot(3,2,5)
plt.hist(binomial5, 10, density=True, color='green', edgecolor='black')
plt.title('n = 10,000') 

plt.subplot(3,2,6)
plt.hist(binomial6, 10, density=True, color='green', edgecolor='black')
plt.title('n = 100,000')

plt.savefig('figures/binomial_distributions')
