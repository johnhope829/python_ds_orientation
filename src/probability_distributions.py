import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rng = np.random.default_rng()

poisson = rng.poisson(5, 10000)
binomial = rng.binomial(10,0.5,10000)
uniform = rng.uniform(0,1,10000)

fig, axes = plt.subplots(2,2, constrained_layout=True)
fig.delaxes(axes[1,1])

# poisson plot
plt.subplot(2,2,1)
plt.hist(poisson, 15, density=True, color='green', edgecolor='black')
plt.title('Poisson')

# binomial plot
plt.subplot(2,2,2)
plt.hist(binomial, 10, density=True, color='green', edgecolor='black')
plt.title('Binomial')

# uniform plot
plt.subplot(2,2,3)
plt.hist(uniform, 10, density=True, color='green', edgecolor='black')
plt.title('Uniform')

plt.suptitle('Probability Distributions')
plt.show()