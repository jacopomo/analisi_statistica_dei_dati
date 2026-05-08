'''
Script that generates a plot to visualize how to combine p-values, 
'''
import numpy as np
import matplotlib.pyplot as plt
from asd import utils

p = 0.05
p1 = np.linspace(0.001, 1, 1000)
p2 = np.linspace(0, 1, 1000)
y = p / p1
mask = y <= 1
# Generate plot
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

ax.plot(p1[mask], y[mask], color="C0", linewidth=1)
ax.plot([1, 1], [0, 1], color="black", ls="--", lw=1.0)
ax.plot([0, 1], [1, 1], color="black", ls="--", lw=1.0)
ax.text(0.25, 0.30, r'$\alpha / p_1$', color="C0", ha='center', va='bottom')

ax.set_xlabel('$p_1$')
ax.set_ylabel(r'$p_2$')
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 1.1)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(['0', '0.5', '1'])
ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(['0', '0.5', '1'])

ax.grid(alpha=0.3)

ax.set_title('Combination of p-values')
plt.savefig("images/p_value_comb.pgf", bbox_inches='tight')
plt.close()
